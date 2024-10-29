from typing import Sequence

from parsomics_core.entities.files.file_factory import FileFactory
from parsomics_core.entities.files.gtdbtk.validated_file import GTDBTkValidatedFile


class GTDBTkFileFactory(FileFactory):
    def __init__(self, path: str, dereplicated_genomes: Sequence[str]):
        return super().__init__(
            validation_class=GTDBTkValidatedFile,
            path=path,
            dereplicated_genomes=dereplicated_genomes,
        )
