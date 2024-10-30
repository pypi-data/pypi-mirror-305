import logging
import numpy as np
import sys

log = logging.getLogger(__name__)

from .base import BaseWideReader
from snputils.ancestry.genobj.wide import WideAncestryObject

@BaseWideReader.register
class AdmixtureReader(BaseWideReader):
    def read(self):
        log.info("Reading Q matrix...")
        Q_mat = np.genfromtxt(self.Q_file, delimiter=' ')
        log.info("Reading P matrix...")
        P_mat = np.genfromtxt(self.P_file, delimiter=' ')
        sample_IDs = self._read_sample_ids()
        snps = self._read_snps()
        ancestries = self._read_ancestries()
        return WideAncestryObject(Q_mat,
                                  P_mat,
                                  sample_IDs=sample_IDs,
                                  snps=snps,
                                  ancestries=ancestries)
