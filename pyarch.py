import sys
from commands.artifacts import ListArtifacts

from cliff.app import App
from cliff.commandmanager import CommandManager


class PyarchClient(App):

    def __init__(self):
        super().__init__(
            description="PyArch desktop client",
            version="0.1-Beta",
            command_manager=CommandManager("pyarch"),
            deferred_help=True
        )

    def initialize_app(self, argv):
        commands = [ListArtifacts]
        for command in commands:
            self.command_manager.add_command(command.command_name, command)


def main(argv=sys.argv[1:]):
    admin_app = PyarchClient()
    return admin_app.run(argv)


if __name__ == "__main__":
    sys.exit(main(argv=sys.argv[1:]))
