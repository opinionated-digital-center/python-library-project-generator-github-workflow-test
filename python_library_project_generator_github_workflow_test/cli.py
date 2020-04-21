"""Console script for python_library_project_generator_github_workflow_test."""
import sys

import cleo

from . import __version__


class HelloCommand(cleo.Command):
    """
    First Command

    hello
    """

    def handle(self):
        self.line(
            "Replace this message by putting your code into "
            "python_library_project_generator_github_workflow_test.cli.main)"
        )
        self.line("See cleo documentation at https://cleo.readthedocs.io/en/latest/")


class Application(cleo.Application):
    def __init__(self):
        super().__init__("ODC Python boilerplate GitLab", __version__)

        self.add(HelloCommand())


def main(args=None):
    return Application().run()


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
