import numpy as np


def test_get_array_athena(add_package_path, monkeypatch):
    add_package_path("athena")
    import data_read as dr

    fake_data = {
        "Time": 0.0,
        "x1v": np.array([0.0, 1.0]),
        "x2v": np.array([0.0, 1.0]),
        "x3v": np.array([0.0, 1.0]),
        "rho": np.ones((1, 1, 1)),
        "press": np.full((1, 1, 1), 2.0),
        "vel1": np.zeros((1, 1, 1)),
        "vel2": np.ones((1, 1, 1)),
        "vel3": np.full((1, 1, 1), 2.0),
        "Bcc1": np.full((1, 1, 1), 3.0),
        "Bcc2": np.full((1, 1, 1), 4.0),
        "Bcc3": np.full((1, 1, 1), 5.0),
    }

    monkeypatch.setattr(dr.ar, "athdf", lambda fn: fake_data)

    out = dr.get_array_athena(
        "dummy",
        fields=["rho", "vel", "B", "T", "coord"],
        MHD_flag=True,
    )

    expected_T = (fake_data["press"] / fake_data["rho"]) * dr.un.KELVIN * dr.un.mu

    assert np.allclose(out["T"], expected_T)
    assert np.array_equal(out["rho"], fake_data["rho"])
    assert np.array_equal(out["vel"][1], fake_data["vel2"])
    assert np.array_equal(out["B"][2], fake_data["Bcc3"])
    assert len(out["coord"]) == 3
