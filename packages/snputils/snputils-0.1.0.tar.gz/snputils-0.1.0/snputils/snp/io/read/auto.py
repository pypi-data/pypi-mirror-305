from __future__ import annotations

import pathlib

from snputils.snp.io.read.base import SNPBaseReader


class AutoReader(object):
    def __new__(cls, filename: str | pathlib.Path) -> SNPBaseReader:
        """
        Automatically detect the file format and read it into a SNPObject.

        Args:
            filename: Filename of the file to read.

        Raises:
            ValueError: If the filename does not have an extension or the extension is not supported.
        """
        filename = pathlib.Path(filename)
        extension = filename.suffix
        if extension == "":
            raise ValueError(
                "The filename should have an extension when using AutoReader."
            )
        extension = extension.lower()

        if extension == ".vcf":
            from snputils.snp.io.read.vcf import VCFReader

            return VCFReader(filename)
        elif extension == ".bed":
            from snputils.snp.io.read.bed import BEDReader

            return BEDReader(filename)
        elif extension == ".pgen":
            from snputils.snp.io.read.pgen import PGENReader

            return PGENReader(filename)
        else:
            raise ValueError(f"File format not supported: {filename}")
