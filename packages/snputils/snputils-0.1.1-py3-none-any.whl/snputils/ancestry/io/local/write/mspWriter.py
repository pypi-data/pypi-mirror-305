import logging
import warnings
import numpy as np
import pandas as pd
import sys

log = logging.getLogger(__name__)

from snputils.ancestry.genobj.local import LocalAncestryObject
from .base import LAIBaseWriter

@LAIBaseWriter.register
class MSPWriter(LAIBaseWriter):
    def write(self):
        file_extension = (".msp")
        if not self._filename.endswith(file_extension):
            self._filename += ".msp"
        
        savingPath = self.filename.rsplit("/")[:-1]
        filename = self.filename.split("/")[-1]
        log.info(f"Writing msp file with name {filename}. The file will be stored in: {savingPath}")
        log.info(f"Data corresponds to LAI Object with {self.laiobj.n_samples} samples "+\
                 f"from {self.laiobj.n_ancestries} different ancestries from the "+\
                 f"following IDs: {self.laiobj.sample_IDs}")
        
        laiobj = self.laiobj
        
        columns = ["spos", "epos", "sgpos", "egpos", "n snps"]
        lai_dic = {"#chm" : laiobj.chromosome,
                   "spos" : laiobj.physical_pos[:,0],
                   "epos" : laiobj.physical_pos[:,1],
                   "sgpos" : laiobj.centimorgan_pos[:,0],
                   "egpos" : laiobj.centimorgan_pos[:,1],
                   "n snps" : laiobj.window_size
                  }

        ilai = 0
        for ID in laiobj.sample_IDs:
            lai_dic[ID+".0"] = laiobj.lai[:,ilai]
            columns.append(ID+".0")
            lai_dic[ID+".1"] = laiobj.lai[:,ilai+1]   
            columns.append(ID+".1")
            ilai += 2
            
        lai_df = pd.DataFrame(lai_dic)        
        lai_df.to_csv(self.filename, sep="\t", index=False, header=False)
        
        second_line="#chm"
        for c in columns:
            second_line += "\t"+c
        
        if laiobj.ancestry_map is not None:
            ancestries = list(laiobj.ancestry_map.values())
            ancestries_codes = list(laiobj.ancestry_map.keys())
            
            first_line = "#Subpopulation order/codes: "
            for ai, a in enumerate(ancestries):
                if ai == 0:
                    first_line += a+"="+ancestries_codes[ai]
                else:
                    first_line += "\t"+a+"="+ancestries_codes[ai]
                    
            with open(self.filename, "r+") as f:
                content = f.read()
                f.seek(0,0)
                f.write(first_line.rstrip('\r\n') + '\n' + second_line + '\n' + content)

        else:
            with open(self.filename, "w") as f:
                lai_df.to_csv(f, sep="\t", index=False, header=False)
                        
        log.info(f"Finished writing msp file: {self.filename}")

        return None
