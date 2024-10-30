import numpy as np

from snputils.snp.io.read import AutoReader


def test_auto_reader(data_path, snpobj_pgen):
    reader = AutoReader(data_path + "/pgen/subset.pgen")
    snpobj = reader.read()
    assert np.array_equal(snpobj.calldata_gt, snpobj_pgen.calldata_gt)
