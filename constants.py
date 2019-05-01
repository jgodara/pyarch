from pathlib import Path


WORK_DIR = f"{Path.home()}/.pyarch"
REPOS_CONFIG_FILE = f"{WORK_DIR}/repositories.yaml"

DEFAULT_REMOTE_URL = "https://raw.githubusercontent.com/jgodara/pyarch/dist"
DEFAULT_CONFIG_URL = f"{DEFAULT_REMOTE_URL}/default_config.yaml"
DEFAULT_REPO_NAME = "PyArch-Central"
