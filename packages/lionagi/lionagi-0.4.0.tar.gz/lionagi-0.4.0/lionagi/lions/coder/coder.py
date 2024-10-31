import asyncio
from pathlib import Path

from lionagi import logging as _logging
from lionagi.core import Session
from lionagi.libs import ParseUtil

from .base_prompts import CODER_PROMPTS
from .util import (
    install_missing_dependencies,
    save_code_file,
    set_up_interpreter,
)


class Coder:

    def __init__(
        self,
        prompts: dict = None,
        session: Session = None,
        session_kwargs: dict = None,
        required_libraries: list = None,
        work_dir: Path | str = None,
    ) -> None:

        self.prompts = prompts or CODER_PROMPTS
        self.session = session or self._create_session(session_kwargs)
        self.required_libraries = required_libraries or ["lionagi"]
        self.work_dir = work_dir or Path.cwd() / "coder" / "code_files"

    def _create_session(self, session_kwargs: dict = None) -> Session:
        session_kwargs = session_kwargs or {}
        return Session(system=self.prompts["system"], **session_kwargs)


class Coder:
    def __init__(
        self,
        prompts=None,
        session=None,
        session_kwargs=None,
        required_libraries=None,
        work_dir=None,
    ):
        print("Initializing Coder...")
        self.prompts = prompts or CODER_PROMPTS
        self.session = session or self._create_session(session_kwargs)
        self.required_libraries = required_libraries or ["lionagi"]
        self.work_dir = work_dir or Path.cwd() / "coder" / "code_files"
        print("Coder initialized.")

    def _create_session(self, session_kwargs=None):
        print("Creating session...")
        session_kwargs = session_kwargs or {}
        session = Session(system=self.prompts["system"], **session_kwargs)
        print("Session created.")
        return session

    async def _plan_code(self, context):
        print("Planning code...")
        plans = await self.session.chat(
            self.prompts["plan_code"], context=context
        )
        print("Code planning completed.")
        return plans

    async def _write_code(self, context=None):
        print("Writing code...")
        code = await self.session.chat(
            self.prompts["write_code"], context=context
        )
        print("Code writing completed.")
        return ParseUtil.extract_code_blocks(code)

    async def _review_code(self, context=None):
        print("Reviewing code...")
        code = await self.session.chat(
            self.prompts["review_code"], context=context
        )
        print("Code review completed.")
        return code

    async def _modify_code(self, context=None):
        print("Modifying code...")
        code = await self.session.chat(
            self.prompts["modify_code"], context=context
        )
        print("Code modification completed.")
        return code

    async def _debug_code(self, context=None):
        print("Debugging code...")
        code = await self.session.chat(
            self.prompts["debug_code"], context=context
        )
        print("Code debugging completed.")
        return code

    def _handle_execution_error(self, execution, required_libraries=None):
        print("Handling execution error...")
        if execution.error and execution.error.name == "ModuleNotFoundError":
            print(
                "ModuleNotFoundError detected. Installing missing dependencies..."
            )
            install_missing_dependencies(required_libraries)
            print("Dependencies installed. Retrying execution.")
            return "try again"
        elif execution.error:
            print(f"Execution error: {execution.error}")
            return execution.error

    def execute_code(self, code, **kwargs):
        print("Executing code...")
        interpreter = set_up_interpreter()
        with interpreter as sandbox:
            print("Running code in sandbox...")
            execution = sandbox.notebook.exec_cell(code, **kwargs)
            error = self._handle_execution_error(
                execution, required_libraries=kwargs.get("required_libraries")
            )
            if error == "try again":
                print("Retrying code execution...")
                execution = sandbox.notebook.exec_cell(code, **kwargs)
            print("Code execution completed.")
            return execution

    def _save_code_file(self, code, **kwargs):
        print("Saving code...")
        save_code_file(code, self.work_dir, **kwargs)
        print("Code saved.")

    @staticmethod
    def _load_code_file(file_path):
        print("Loading code...")
        try:
            with open(file_path) as file:
                print("Code loaded.")
                return file.read()
        except FileNotFoundError:
            _logging.error(f"File not found: {file_path}")
            return None


async def main():
    print("Starting main function...")
    coder = Coder()

    code_prompt = """
    write a pure python function that takes a list of integers and returns the sum of all the integers in the list. write a couple tests as well
    """

    print(f"Code prompt: {code_prompt}")

    print("Planning code...")
    code_plan = await coder._plan_code(context=code_prompt)
    print("Code plan generated.")

    print("Writing code...")
    code = await coder._write_code()
    print("Code written.")

    print("Executing code...")
    execution_result = coder.execute_code(code)
    print("Code execution completed.")

    from IPython.display import Markdown

    print("Displaying code plan...")
    Markdown(code_plan)

    print("Displaying generated code...")
    print(code)

    print("Displaying execution result...")
    print(execution_result)

    print("Main function completed.")


if __name__ == "__main__":
    print("Running script...")
    asyncio.run(main())
    print("Script execution completed.")
