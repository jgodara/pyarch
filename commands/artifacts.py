import os
import requests
import yaml
import tarfile
from cliff.command import Command

import constants
from config_factory import ConfigFactory


class GetArtifact(Command):
    command_name = "get"

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)

        parser.add_argument(
            "artifact", help="Name of the artifact to download")

        parser.add_argument(
            "--repo", "-r", help="Name of repo to download artifact from")
        return parser

    def take_action(self, parsed_args):
        repo_name = parsed_args.repo if parsed_args.repo else constants.DEFAULT_REPO_NAME
        artifact_name = parsed_args.artifact
        repo = ConfigFactory.get_instance().get_repo(repo_name)

        repo_url, catalog_name = repo["url"], repo["catalog"]
        artifact_url = f"{repo_url}/catalogs/{catalog_name}/{artifact_name}.tar.gz"

        artifact = requests.get(artifact_url)
        with open(f"{os.getcwd()}/{artifact_name}", "wb") as artifact_archive:
            artifact_archive.write(artifact.content)

        artifact_file = tarfile.open(f"{os.getcwd()}/{artifact_name}", "r:gz")
        try:
            artifact_file.extractall()
        finally:
            artifact_file.close()
