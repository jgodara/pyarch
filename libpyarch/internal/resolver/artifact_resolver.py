import abc
from typing import List

from libpyarch.internal.artifact import Artifact
from libpyarch.internal.artifact_repository import ArtifactRepository


class ArtifactResolver:

    @abc.abstractmethod
    def resolve_artifact(self,
                         local_repository: ArtifactRepository,
                         remote_repositories: List[ArtifactRepository],
                         artifact: Artifact):
        pass


class DefaultArtifactResolver(ArtifactResolver):

    def resolve_artifact(self,
                         local_repository: ArtifactRepository,
                         remote_repositories: List[ArtifactRepository],
                         artifact: Artifact) -> Artifact:
        pass


class ArtifactResolverError(Exception):

    def __init__(self, error):
        super().__init__(error)
