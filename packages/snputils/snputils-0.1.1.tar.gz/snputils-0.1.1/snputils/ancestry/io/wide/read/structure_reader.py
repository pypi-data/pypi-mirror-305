import logging
import numpy as np
import sys

log = logging.getLogger(__name__)

from .base import BaseWideReader

@BaseWideReader.register
class StructureReader(BaseWideReader):
    def read(self):
        raise NotImplementedError
        