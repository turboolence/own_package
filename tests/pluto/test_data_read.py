import sys
import os
import types

cwd = os.path.dirname(__file__)
for i in range(len(cwd.split("/"))):
    if cwd.split("/")[i] == "own_package":
        break
package_abs_path = "/".join(cwd.split("/")[: i + 1]) + "/own_package/"

sys.path.insert(0, f"{package_abs_path}pluto/")

class DummyD:
    def __init__(self):
        self.SimTime = 1.23
        self.x1 = [0, 1]
        self.x2 = [0, 2]
        self.dx1 = [0.5, 0.5]
        self.dx2 = [1.0, 1.0]

def dummy_pload(ns, w_dir=None):
    return DummyD()

def dummy_nlast_info(w_dir=None, datatype=None):
    return {"nlast": 0}

stub_pyPLUTO = types.ModuleType("pyPLUTO")
stub_pload_module = types.ModuleType("pyPLUTO.pload")
stub_pload_module.pload = dummy_pload
stub_pyPLUTO.pload = stub_pload_module
stub_pyPLUTO.nlast_info = dummy_nlast_info

sys.modules['pyPLUTO'] = stub_pyPLUTO
sys.modules['pyPLUTO.pload'] = stub_pload_module

import data_read as dr

def test_coord_loading():
    result = dr.get_array(0, "dummy", ["coord"], dim=2, nlast_flag=False)
    assert result["coord"] == [[0, 1], [0, 2]]
    assert result["dx"] == [[0.5, 0.5], [1.0, 1.0]]
