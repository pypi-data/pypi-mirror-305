"""""" # start delvewheel patch
def _delvewheel_patch_1_8_3():
    import os
    if os.path.isdir(libs_dir := os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'signalflow.libs'))):
        os.add_dll_directory(libs_dir)


_delvewheel_patch_1_8_3()
del _delvewheel_patch_1_8_3
# end delvewheel patch

from .signalflow_examples import download_examples, download_notebooks
