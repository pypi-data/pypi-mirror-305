"""fourier_left_hand description."""

from os import getenv as _getenv
from os import path as _path

from ._cache import clone_to_cache as _clone_to_cache

REPOSITORY_PATH: str = _clone_to_cache(
    "fourier_grx_descriptions",
    commit=_getenv("ROBOT_DESCRIPTION_COMMIT", None),
)

PACKAGE_PATH: str = _path.join(REPOSITORY_PATH, "fourier_hand")

URDF_PATH: str = _path.join(PACKAGE_PATH, "urdf", "fourier_right_hand.urdf")
