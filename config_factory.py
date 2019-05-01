import yaml
import constants


class ConfigFactory:
    __instance = None

    @staticmethod
    def get_instance():
        if ConfigFactory.__instance is None:
            ConfigFactory.__instance = ConfigFactory()

        return ConfigFactory.__instance

    def __init__(self):
        with open(constants.REPOS_CONFIG_FILE) as repos_cfg:
            try:
                self._config = yaml.safe_load(repos_cfg)
                print(self._config)
            except yaml.YAMLError as err:
                print(err)
                exit(1)

    def get_repos(self):
        return self._config["repositories"]

    def get_repo(self, repo_name):
        for repo in self.get_repos():
            if repo["name"] == repo_name:
                return repo

        return None
