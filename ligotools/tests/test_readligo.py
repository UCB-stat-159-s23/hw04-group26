import numpy as np
import os
import fnmatch
import pytest
from ligotools import readligo as rl

data_L1 = "data/L-L1_LOSC_4_V2-1126259446-32.hdf5"
data_H1 = "data/H-H1_LOSC_4_V2-1126259446-32.hdf5"

strain_H1, time_H1, chan_dict_H1 = rl.loaddata("data/H-H1_LOSC_4_V2-1126259446-32.hdf5", 'H1')
strain_L1, time_L1, chan_dict_L1 = rl.loaddata("data/L-L1_LOSC_4_V2-1126259446-32.hdf5", 'L1')


# +
def test_strainloaddataL1():
    assert type(strain_L1) == np.ndarray
    
def test_strainloaddataH1():
    assert type(strain_H1) == np.ndarray
    
def test_chan_dictH1():
    assert type(chan_dict_H1) == dict
    
def test_chan_dictL1():
    assert type(chan_dict_L1) == dict

test_strainloaddataL1()
test_strainloaddataH1()
test_chan_dictH1()
test_chan_dictL1()