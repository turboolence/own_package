import os
import sys
import numpy as np
import types

sys.modules.setdefault('yt', types.SimpleNamespace(load=lambda *a, **k: None))

cwd = os.path.dirname(__file__)
for i in range(len(cwd.split("/"))):
    if cwd.split("/")[i] == "own_package":
        break
package_abs_path = "/".join(cwd.split("/")[: i + 1]) + "/own_package/"

import importlib.util

data_read_path = os.path.join(package_abs_path, "arepo", "data_read.py")
spec = importlib.util.spec_from_file_location("arepo_data_read", data_read_path)
dr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dr)


def _dummy_data():
    return {
        ("PartType0", "Coordinates"): np.array([0.0]),
        ("PartType0", "Density"): np.array([1.0]),
        ("PartType0", "InternalEnergy"): np.array([1.0]),
        ("PartType0", "mfDensity"): np.array([1.0]),
        ("PartType0", "mfInternalEnergy"): np.array([1.0]),
        ("PartType0", "velocity_x"): np.array([0.0]),
        ("PartType0", "velocity_y"): np.array([0.0]),
        ("PartType0", "velocity_z"): np.array([0.0]),
    }


def test_extraction_fn_selective():
    data = _dummy_data()
    out = dr.extraction_fn(data, ["rho"], False)
    assert set(out.keys()) == {"rho"}


def test_extraction_fn_temperature():
    data = _dummy_data()
    out = dr.extraction_fn(data, ["T"], False)
    assert set(out.keys()) == {"rho", "prs", "IE", "T"}
