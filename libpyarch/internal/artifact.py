import abc

from libpyarch.internal.artifact_repository import ArtifactRepository


class Artifact:

    @abc.abstractmethod
    def get_group_id(self) -> str: pass

    @abc.abstractmethod
    def set_group_id(self, group_id: str): pass

    @abc.abstractmethod
    def get_artifact_id(self) -> str: pass

    @abc.abstractmethod
    def set_artifact_id(self, artifact_id: str): pass

    @abc.abstractmethod
    def get_version(self) -> str: pass

    @abc.abstractmethod
    def set_version(self, version: str): pass

    @abc.abstractmethod
    def get_repository(self): pass

    @abc.abstractmethod
    def set_repository(self, remote_repository: ArtifactRepository): pass

    @abc.abstractmethod
    def get_download_url(self) -> str: pass

    @abc.abstractmethod
    def set_download_url(self, download_url: str): pass

    @abc.abstractmethod
    def get_file(self): pass

    @abc.abstractmethod
    def set_file(self, file): pass
