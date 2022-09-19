from hkpilot.utils.cmake import CMake

import inspect
import os


class WCSim(CMake):

    def __init__(self, path):
        super().__init__(path)

        self._package_name = "WCSim"
        self._package_version = "v1.10.0"
        self._git_url = "git@github.com:WCSim/WCSim.git"
        self._git_branch = "develop"
        # self._git_tag = "test_v1"
        self._git_clone_dir = "src"
        self._cmakelist_path = "src"
        self._depends_on = {"ROOT": "*", "Geant4": "*"}
        self._cmake_options = {
            "CMAKE_CXX_STANDARD": "14",
        }

