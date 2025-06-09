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

data_read_path = os.path.join(package_abs_path, "athena", "data_read.py")
spec = importlib.util.spec_from_file_location("athena_data_read", data_read_path)
dr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dr)


def _dummy_ds():
    return {
        "Time": 0.0,
        "rho": np.array([1.0]),
        "press": np.array([1.0]),
        "vel1": np.array([0.0]),
        "vel2": np.array([0.0]),
        "vel3": np.array([0.0]),
        "x1v": np.array([0.0]),
        "x2v": np.array([0.0]),
        "x3v": np.array([0.0]),
        "Bcc1": np.array([0.0]),
        "Bcc2": np.array([0.0]),
        "Bcc3": np.array([0.0]),
    }


def test_get_array_athena_selective(monkeypatch):
    ds = _dummy_ds()
    monkeypatch.setattr(dr.ar, "athdf", lambda fn: ds)
    out = dr.get_array_athena("dummy", fields=["rho"])
    assert set(out.keys()) == {"time", "rho"}


def test_get_array_athena_temperature(monkeypatch):
    ds = _dummy_ds()
    monkeypatch.setattr(dr.ar, "athdf", lambda fn: ds)
    out = dr.get_array_athena("dummy", fields=["T"])
    assert set(out.keys()) == {"time", "T"}
