import os
from typing import List, Optional

import click
import yaml
from click import Command
from pydantic import BaseModel, Field
from rich.console import Console

from cli.models import TaskParameters
from cli.status_indicator import StatusIndicator
from cli.task_runner import TaskRunner
from cli.util import is_git_repo, get_git_root

COMMAND_FILE_PATH = ".pilot-commands.yaml"


class PilotCommand(BaseModel):
    """Implementation of 'pilot run' command."""

    name: str = Field(..., description="Name of the command", pattern="^[a-z0-9-]+$")
    description: str = Field(..., description="Description of the command")
    params: TaskParameters = Field(..., description="CLI parameters for the command")

    def callback(self, *args, **kwargs):
        console = Console()

        # Overwrite parameters
        self.params.output = kwargs.get("output", self.params.output)
        self.params.model = kwargs.get("model", self.params.model)
        self.params.verbose = kwargs.get("verbose", self.params.verbose)
        self.params.debug = kwargs.get("debug", self.params.debug)
        self.params.spinner = kwargs.get("spinner", self.params.spinner)
        self.params.sync = kwargs.get("sync", self.params.sync)
        self.params.wait = kwargs.get("wait", self.params.wait)

        if self.params.sync:
            # Get current branch from git
            current_branch = os.popen("git rev-parse --abbrev-ref HEAD").read().strip()
            if current_branch not in ["master", "main"]:
                self.params.branch = current_branch
        status_indicator = StatusIndicator(
            spinner=self.params.spinner,
            display_log_messages=self.params.verbose,
            console=console,
        )
        runner = TaskRunner(status_indicator)
        runner.run_task(self.params)
        status_indicator.stop()

    def to_click_command(self) -> Command:
        cmd = Command(self.name, callback=self.callback, help=self.description)

        cmd.params.append(
            click.Option(
                ["--output", "-o"],
                help="💾 Overwrite the output file path.",
                default=self.params.output,
                show_default=True,
            )
        )
        cmd.params.append(
            click.Option(
                ["--model", "-m"],
                help="🧠 Overwrite the model to use.",
                default=self.params.model,
                show_default=True,
            )
        )
        cmd.params.append(
            click.Option(
                ["--verbose"],
                help="🔊 Print more status messages.",
                is_flag=True,
                default=self.params.verbose,
            )
        )
        cmd.params.append(
            click.Option(
                ["--debug"],
                help="🐞 Run in debug mode.",
                is_flag=True,
                default=self.params.debug,
            )
        )
        cmd.params.append(
            click.Option(
                ["--spinner/--no-spinner"],
                help="🔄 Display a loading indicator.",
                is_flag=True,
                default=self.params.spinner,
            )
        )
        cmd.params.append(
            click.Option(
                ["--sync/--no-sync"],
                help="🔄 Sync local repository state with Arcane Engine changes.",
                is_flag=True,
                default=self.params.sync,
            )
        )
        cmd.params.append(
            click.Option(
                ["--wait/--no-wait"],
                help="⏳ Wait for the task to complete.",
                is_flag=True,
                default=self.params.wait,
            )
        )
        return cmd


def find_pilot_commands_file() -> Optional[str]:
    """Discover the location of the .pilot-commands.yaml file.

    The file is searched for in the following order:
    1. The root of the current Git repository
    2. The home directory

    :return: The absolute path to the file, or None if not found.
    """
    # Check if the current directory is part of a Git repository
    if is_git_repo():
        git_root = get_git_root()
        if git_root:
            git_repo_file_path = os.path.join(git_root, ".pilot-commands.yaml")
            if os.path.isfile(git_repo_file_path):
                return os.path.abspath(git_repo_file_path)
    return None


class CommandIndex:
    """
    A class to manage the index of commands stored in a YAML file.
    """

    def __init__(self, file_path: str = None):
        """
        Initialize the CommandIndex with the given file path.

        :param file_path: Path to the YAML file containing commands.
        """
        self.file_path = file_path
        if not self.file_path:
            self.file_path = find_pilot_commands_file()
        self.commands = self._load_commands() if self.file_path else []

    def _load_commands(self) -> List[PilotCommand]:
        """
        Load commands from the YAML file.

        :return: A list of Command instances.
        """
        try:
            with open(self.file_path, "r") as file:
                data = yaml.safe_load(file)
                return [PilotCommand(**cmd) for cmd in data.get("commands", [])]
        except FileNotFoundError:
            return []

    def save_commands(self) -> None:
        """
        Save the current list of commands to the YAML file.
        """
        with open(self.file_path, "w") as file:
            yaml.dump(
                {"commands": [cmd.model_dump(exclude_none=True) for cmd in self.commands]},
                file,
            )

    def add_command(self, new_command: PilotCommand) -> None:
        """
        Add a new command to the list and save it.

        :param new_command: The Command instance to add.

        :raises ValueError: If a command with the same name already exists.
        """
        for cmd in self.commands:
            if cmd.name == new_command.name:
                raise ValueError(f"Command with name '{new_command.name}' already exists")
        new_command.params.branch = None
        new_command.params.pr_number = None
        if new_command.params.file:
            new_command.params.prompt = None
        self.commands.append(new_command)
        self.save_commands()

    def get_commands(self) -> List[PilotCommand]:
        """
        Get the list of commands.

        :return: A list of Command instances.
        """
        return self.commands

    def get_command(self, command_name) -> Optional[PilotCommand]:
        """
        Get a command by name.

        :param command_name:
        :return:
        """
        for cmd in self.commands:
            if cmd.name == command_name:
                return cmd
        return None

    def remove_command(self, command_name) -> None:
        """
        Remove a command by name.

        :param command_name:
        """
        self.commands = [cmd for cmd in self.commands if cmd.name != command_name]
        self.save_commands()
