import sys
from pathlib import Path
import pytest

ROOT_DIR = Path(__file__).resolve().parents[1]
PACKAGE_DIR = ROOT_DIR / "own_package"

@pytest.fixture
def add_package_path():
    added_paths = []

    def _add(relative):
        path = PACKAGE_DIR / relative
        sys.path.insert(0, str(path))
        added_paths.append(str(path))
        return path

    yield _add

    for p in added_paths:
        if p in sys.path:
            sys.path.remove(p)
