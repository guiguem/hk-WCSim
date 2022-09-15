from hkpilot.utils.cmake import CMake

import inspect
import os


class WCSim(CMake):

    def __init__(self, path):
        super().__init__(path)

        self._package_name = "WCSim"
        self._package_version = "v1.10.0"
        # self._download_url = "https://github.com/WCSim/WCSim/archive/refs/tags/v1.10.0.zip"
        self._git_url = "git@github.com:guiguem/WCSim.git"
        # self._git_branch = "master"
        # self._git_tag = "v4.3.482"
        self._git_clone_dir = "src"
        self._cmakelist_path = "src"
        self._depends_on = {"ROOT": "*", "Geant4": "*"}
        self._cmake_options = {
            "CMAKE_CXX_STANDARD": "14",
            # "Geant4_DIR": "/Users/mguigue/Work/T2K/HK/Software/newSystem/hkpilot/../Geant4/install-Darwin_arm64-gcc_13.1.6-python_3.9.13"
        }

        # self._path = os.path.relpath(inspect.getfile(self.__class__))
