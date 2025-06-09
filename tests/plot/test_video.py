import sys
import os
from unittest.mock import patch

cwd = os.path.dirname(__file__)
for i in range(len(cwd.split("/"))):
    if cwd.split("/")[i] == "own_package":
        break

package_abs_path = "/".join(cwd.split("/")[: i + 1]) + "/own_package/"

sys.path.insert(0, f"{package_abs_path}plot/")

import video as vid


def test_make_video_error():
    with patch("video.subprocess.run") as mock_run:
        mock_run.return_value.returncode = 1
        mock_run.return_value.stderr = "fail"
        try:
            vid.make_video("img", "out")
            assert False, "Expected RuntimeError"
        except RuntimeError as exc:
            assert "fail" in str(exc)

