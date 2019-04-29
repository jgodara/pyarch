import requests
from cliff.command import Command
from cliff.lister import Lister


class ListArtifacts(Lister):
    """Lists all available artifacts"""

    command_name = "ls"

    def take_action(self, parsed_args):
        # TODO Add yaml support
        artifacts = requests.get(
            f"https://raw.githubusercontent.com/jgodara/pyarch/dist/catalogs/stable/_index/artifacts"
        ).json()

        return (
            ("id", "name"),
            ((artifact_line["id"], artifact_line["name"])
             for artifact_line in artifacts)
        )
