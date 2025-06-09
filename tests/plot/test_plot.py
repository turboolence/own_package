import numpy as np


def test_1d_hist_calc(add_package_path):
    add_package_path("plot")
    import plot_histogram as ph

    test_arr = np.ones(100)

    hst = ph.calc_histogram_1d(test_arr)

    assert np.sum(hst[0]) == 100
