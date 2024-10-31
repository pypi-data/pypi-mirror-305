import os
import subprocess

import click
import inquirer
import jinja2
from arcane.engine import ArcaneEngine
from rich.console import Console
from rich.padding import Padding
from rich.prompt import Prompt

from cli.task_handler import TaskHandler
from cli.util import is_git_repo, get_git_root

MAX_RECURSION_LEVEL = 3


def select(prompt: str, choices: list[str]):
    """Prompt the user to select one of the choices."""
    questions = [
        inquirer.List(
            "choices",
            message=prompt,
            choices=choices,
        ),
    ]
    response = inquirer.prompt(questions)
    if not response:
        raise click.Abort()
    return response["choices"]


def sh(shell_command, status):
    """Run a shell command and return the output"""
    status.start()
    if isinstance(shell_command, str):
        shell_command = shell_command.split()

    status.update_spinner_message(f"Running shell command: {' '.join(shell_command)}")
    subprocess_params = dict(
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=os.environ.copy()
    )
    result = subprocess.run(shell_command, **subprocess_params)
    if result.stderr:
        status.fail()
        status.stop()
        console = Console()
        console.print(Padding(result.stderr, (1, 1)))
    else:
        status.stop()
        status.log_message(f"Run shell command `{' '.join(shell_command)}`")
    result = (result.stdout + result.stderr).strip()
    return result


def read_env_var(variable, default=None):
    """Get the value of an environment variable, with a default value."""
    if variable not in os.environ and default is None:
        # Ask for Variable input with click
        prompt = variable.lower().replace("_", " ")
        first_letter_capitalized = prompt[0].upper() + prompt[1:]
        os.environ[variable] = Prompt.ask("> " + first_letter_capitalized)
    return os.environ.get(variable, default)


def wrap_function_with_status(func, status):
    def wrapper(*args, **kwargs):
        kwargs["status"] = status
        return func(*args, **kwargs)

    return wrapper


class PromptTemplate:

    def __init__(
        self, template_file_path, repo, model, status, recursion_level=0, home=None, **kwargs
    ):
        self.template_file_path = template_file_path
        self.repo = repo
        self.model = model
        self.status = status
        self.variables = kwargs
        self.recursion_level = recursion_level
        self.home = home
        if not self.home:
            self.home = self.determine_template_home()

    def determine_template_home(self):
        if is_git_repo():
            # If the template is in a git repo, use the root of the git repo as the home directory
            return get_git_root()
        # Otherwise, use the current working
        return os.getcwd()

    def get_template_file_path(self):
        """
        The template file path is relative. If it exists relative to the current working directory
        AND the current working directory is a sub-dir of self.home, the assemble a path that
        is relative to self.home.
        Otherwise, return the template file path as is.
        """
        full_template_path = os.path.join(os.getcwd(), self.template_file_path)
        current_template_path = os.path.dirname(full_template_path)
        if current_template_path.startswith(self.home) and os.path.exists(full_template_path):
            # Templates relative to the cwd have priority
            return os.path.relpath(full_template_path, self.home)
        return self.template_file_path

    def render(self):

        def subtask(prompt, status, **kwargs):
            # Treat prompt as a file path and read the content if the file exists
            # The file name will be relative to the current jinja template
            full_template_path = os.path.join(os.getcwd(), self.template_file_path)
            current_template_path = os.path.dirname(full_template_path)
            potential_file_path = os.path.join(current_template_path, prompt)
            status.start()
            if os.path.exists(potential_file_path):

                if self.recursion_level >= MAX_RECURSION_LEVEL:
                    status.update_spinner_message(
                        f"Abort loading {prompt}. Maximum recursion level reached."
                    )
                    status.fail()
                    return ""
                sub_template = PromptTemplate(
                    potential_file_path,
                    self.repo,
                    self.model,
                    status,
                    self.recursion_level - 1,
                    **kwargs,
                )
                prompt = sub_template.render()

            try:
                status.update_spinner_message("Creating sub-task ...")
                engine = ArcaneEngine()
                task = engine.create_task(self.repo, prompt, log=False, gpt_model=self.model)
                task_handler = TaskHandler(task, status)
                return task_handler.wait_for_result(log_messages=False, print_result=False)
            except Exception as e:
                raise click.ClickException(f"Error creating sub-task: {e}")
            finally:
                status.stop()

        env = jinja2.Environment(loader=jinja2.FileSystemLoader(self.home))
        env.globals.update(env=read_env_var)
        env.globals.update(select=select)
        env.globals.update(subtask=wrap_function_with_status(subtask, self.status))
        env.globals.update(sh=wrap_function_with_status(sh, self.status))
        template = env.get_template(self.get_template_file_path())
        return template.render(self.variables)
