"""
This package is used on Windows only, as a container for the .pyd file and
platform-specific DLLs.

On Linux and macOS, the bare .so file is copied.
"""


# start delvewheel patch
def _delvewheel_patch_1_8_3():
    import os
    if os.path.isdir(libs_dir := os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'signalflow.libs'))):
        os.add_dll_directory(libs_dir)


_delvewheel_patch_1_8_3()
del _delvewheel_patch_1_8_3
# end delvewheel patch

from .signalflow import *