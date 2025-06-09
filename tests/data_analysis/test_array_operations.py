import numpy as np


def test_dot_product(add_package_path):
    add_package_path("data_analysis")
    import array_operations as ao

    A = [0, 0, 1]
    B = [0, 1, 0]

    output = ao.dot_product(A, B)

    assert output[0] == 0
    assert output[1] == 0


def test_make_array_periodic(add_package_path):
    add_package_path("data_analysis")
    import array_operations as ao

    arr = np.arange(8).reshape(2, 2, 2)
    periodic = ao.make_array_periodic(arr)
    expected = np.tile(arr, (3, 3, 3))

    assert periodic.shape == (6, 6, 6)
    assert np.array_equal(periodic, expected)
