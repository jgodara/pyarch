import abc
from typing import List

from libpyarch.internal.artifact import Artifact
from libpyarch.internal.artifact_repository import ArtifactRepository
from libpyarch.internal.resolver.artifact_resolver import ArtifactResolverError, ArtifactResolver, DefaultArtifactResolver
from pyarch_commons.downloader.error import DownloadError


class Downloader:
    __artifact_resolver: ArtifactResolver = None

    @abc.abstractmethod
    def download(self,
                 group_id: str,
                 artifact_id: str,
                 version: str,
                 local_repository: ArtifactRepository,
                 remote_repositories: List[ArtifactRepository]):
        pass


class DefaultDownload(Downloader):
    __artifact_resolver = DefaultArtifactResolver()

    def download(self,
                 group_id: str,
                 artifact_id: str,
                 version: str,
                 local_repository: ArtifactRepository,
                 remote_repositories: List[ArtifactRepository]):

        repositories = list(remote_repositories)
        if local_repository:
            repositories.append(local_repository)

        artifact_coordinates = Artifact()
        artifact_coordinates.set_group_id(group_id)
        artifact_coordinates.set_artifact_id(artifact_id)
        artifact_coordinates.set_version(version)

        try:
            artifact = self.__artifact_resolver.resolve_artifact(local_repository,
                                                                 remote_repositories,
                                                                 artifact_coordinates)
        except ArtifactResolverError as err:
            raise DownloadError(err)

        return artifact.get_file()
