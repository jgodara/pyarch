import os
import sys
from commands.artifacts import GetArtifact
from config_factory import ConfigFactory
import requests
from cliff.app import App
from cliff.commandmanager import CommandManager

import constants


class PyarchClient(App):

    def __init__(self):
        super().__init__(
            description="PyArch desktop client",
            version="0.1-Beta",
            command_manager=CommandManager("pyarch"),
            deferred_help=True
        )

    def prepare_to_run_command(self, cmd):
        # Check for config
        if not os.path.exists(constants.REPOS_CONFIG_FILE):
            print(f"{constants.REPOS_CONFIG_FILE} not found.")

            if not os.path.exists(constants.WORK_DIR):
                os.makedirs(constants.WORK_DIR)

            with open(constants.REPOS_CONFIG_FILE, "wb") as conf_file:
                remote_file = requests.get(constants.DEFAULT_CONFIG_URL)
                conf_file.write(remote_file.content)

                print("Generated default config")

        _ = ConfigFactory.get_instance()

    def initialize_app(self, argv):
        commands = [GetArtifact]
        for command in commands:
            self.command_manager.add_command(command.command_name, command)


def main(argv=sys.argv[1:]):
    admin_app = PyarchClient()
    return admin_app.run(argv)


if __name__ == "__main__":
    sys.exit(main(argv=sys.argv[1:]))
