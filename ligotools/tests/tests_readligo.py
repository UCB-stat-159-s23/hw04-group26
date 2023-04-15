import numpy as np
import os
import fnmatch
import pytest
import readligo as rl

data_L1 = "data/L-L1_LOSC_4_V2-1126259446-32.hdf5"
data_H1 = "data/H-H1_LOSC_4_V2-1126259446-32.hdf5"

strain_H1, time_H1, chan_dict_H1 = rl.loaddata(data_H1)
strain_L1, time_L1, chan_dict_L1 = rl.loaddata(data_L1)


# +
def test_strainloaddataL1():
    assert isinstance(strain_L1, np.array)
    
def test_strainloaddataH1():
    assert isinstance(strain_H1, np.array)
    
def test_chan_dictH1():
    assert isinstance(chan_dict_H1, dict)
    
def test_chan_dictL1():
    assert isinstance(chan_dict_L1, dict)

