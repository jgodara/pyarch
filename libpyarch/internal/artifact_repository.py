import abc
from typing import List

from libpyarch.internal.artifact import Artifact


class ArtifactRepository:

    @abc.abstractmethod
    def path_of(self, artifact: Artifact) -> str: pass

    @abc.abstractmethod
    def get_url(self) -> str: pass

    @abc.abstractmethod
    def find(self, artifact: Artifact) -> Artifact: pass

    @abc.abstractmethod
    def find_versions(self, artifact: Artifact) -> List[Artifact]: pass
