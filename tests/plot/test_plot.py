import sys
import os
import numpy as np
import types

cmasher_stub = types.SimpleNamespace(bubblegum=None)
sys.modules['cmasher'] = cmasher_stub
matplotlib_stub = types.ModuleType('matplotlib')
matplotlib_stub.rcParams = {'lines.color': 'k'}
transforms_stub = types.ModuleType('matplotlib.transforms')
pyplot_stub = types.ModuleType('matplotlib.pyplot')
matplotlib_stub.pyplot = pyplot_stub
matplotlib_stub.transforms = transforms_stub
sys.modules['matplotlib'] = matplotlib_stub
sys.modules['matplotlib.pyplot'] = pyplot_stub
sys.modules['matplotlib.transforms'] = transforms_stub
sys.modules.setdefault('mpl_toolkits', types.ModuleType('mpl_toolkits'))
axes_grid1_stub = types.ModuleType('mpl_toolkits.axes_grid1')
axes_grid1_stub.make_axes_locatable = lambda *a, **k: None
sys.modules['mpl_toolkits.axes_grid1'] = axes_grid1_stub

cwd = os.path.dirname(__file__)
for i in range(len(cwd.split("/"))):
    if cwd.split("/")[i] == "own_package":
        break

# Take the path of the package
package_abs_path = "/".join(cwd.split("/")[: i + 1]) + "/own_package/"

sys.path.insert(0, f"{package_abs_path}plot/")
import plot_histogram as ph


def test_1d_hist_calc():

    test_arr = np.ones(100)

    hst = ph.calc_histogram_1d(test_arr)

    assert np.sum(hst[0]) == 100
