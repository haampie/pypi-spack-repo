# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMne(PythonPackage):
    # BEGIN VERSIONS
    version("1.6.1", sha256="4d36517c1eafd2399d8f1fbd62cf9416d8b2ec98cd65b1dfed2876c4220bf0f9", url="https://pypi.org/packages/79/34/06151e860d86273afd7b2f2fef560783b4afc9e2601b333f008869fb606c/mne-1.6.1-py3-none-any.whl")
    version("1.4.2", sha256="d4c2d8e8fabada619f2cee5c5861f8edef5da1755ceaf8e46072a98569714b87", url="https://pypi.org/packages/56/0b/39cff9014ba41c527e09920b69abf5753b14e5a71c7eeab6600181381c7c/mne-1.4.2-py3-none-any.whl")
    version("1.4.0", sha256="34643c9d54b3ebc39085757067b5affb228027ef3253f23d1f5a3653017ec41c", url="https://pypi.org/packages/10/58/d55896c8b4b6210b73f09a285e4cb69b6bf218069f7e7f19110ab3363f31/mne-1.4.0-py3-none-any.whl")
    version("1.3.1", sha256="805bf8e9e99f3fc5e11d504c8f200963cc489b6614cdd3e93227f818f7fdcbe8", url="https://pypi.org/packages/26/26/d6145839ca13f193670a44222e9ebfbd6f47c1bb450f4d6286aac525cc77/mne-1.3.1-py3-none-any.whl")
    version("1.2.3", sha256="0a722244eac3eb9ff5c5c45576491cbad7741a69d38e05478303842ee7c3daac", url="https://pypi.org/packages/eb/66/0b755f8b0520706942731d28c70e45d97f87a5193c8053439c2ebbebd0fb/mne-1.2.3-py3-none-any.whl")
    version("1.2.2", sha256="01a855577e831efe711023f02ae280bae9f9e71d61a2a9181ce8b419655817b6", url="https://pypi.org/packages/8c/45/3ad20a14109c302ddbe6b630280bf05953d9fa2404c3a5365715e475f658/mne-1.2.2-py3-none-any.whl")
    version("0.23.4", sha256="90f2c0e1182f42a3c5572ee023a94e347adf6cf53ebe619e8e1e4d09bb189ffa", url="https://pypi.org/packages/20/74/fb6ae8e52d74c8492deb037536456af085114a1a09c19e5d03fe28f7dcb5/mne-0.23.4-py3-none-any.whl")
    version("0.18.2", sha256="aa2e72ad3225efdad39b05e67cd5c88dbd5c3fabf5e1705e459347131f114bc6", url="https://pypi.org/packages/42/ec/08afc26ea6204473031f786d0f3034119a5a138d40062b37fbf578c81c01/mne-0.18.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("full", default=False, description="full")
    variant("hdf5", default=False, description="hdf5")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@1.4:")
        depends_on("python@3.7:", when="@0.24:1.3")
        depends_on("py-darkdetect", when="@1.6:+full")
        depends_on("py-decorator", when="@1:1.0.0,1.0.2:")
        depends_on("py-defusedxml", when="@1.6.1:+full")
        depends_on("py-dipy", when="@1.6:+full")
        depends_on("py-edflib-python", when="@1.6.1:+full")
        depends_on("py-eeglabio", when="@1.6.1:+full")
        depends_on("py-h5io", when="@1:1.0.0,1.0.2:+hdf5")
        depends_on("py-h5py", when="@1.6:+full")
        depends_on("py-imageio@2.6.1:", when="@1.6:+full")
        depends_on("py-imageio-ffmpeg@0.4.1:", when="@1.6:+full")
        depends_on("py-importlib-resources@5.10.2:", when="@1.4: ^python@:3.8")
        depends_on("py-ipyevents", when="@1.6:+full")
        depends_on("py-ipympl", when="@1.6:+full")
        depends_on("py-ipywidgets", when="@1.6:+full")
        depends_on("py-jinja2", when="@1:1.0.0,1.0.2:")
        depends_on("py-joblib", when="@1.6:+full")
        depends_on("py-jupyter", when="@1.6:+full")
        depends_on("py-lazy-loader@0.3:", when="@1.6:")
        depends_on("py-matplotlib@3.5.0:", when="@1.6:")
        depends_on("py-matplotlib@3.4.0:", when="@1.4.1:1.5")
        depends_on("py-matplotlib", when="@1:1.0.0,1.0.2:1.4.0")
        depends_on("py-mffpy@0.5.7:", when="@1.6:+full")
        depends_on("py-mne-qt-browser", when="@1.6:+full")
        depends_on("py-nibabel", when="@1.6:+full")
        depends_on("py-nilearn", when="@1.6:+full")
        depends_on("py-numba", when="@1.6:+full")
        depends_on("py-numexpr", when="@1.6:+full")
        depends_on("py-numpy@1.21.2:", when="@1.6:")
        depends_on("py-numpy@1.15.4:", when="@0.23:1.0.0,1.0.2:1.5")
        depends_on("py-openmeeg@2.5.5:", when="@1.6:+full")
        depends_on("py-packaging", when="@1:1.0.0,1.0.2:")
        depends_on("py-pandas", when="@1.6:+full")
        depends_on("py-pooch@1.5:", when="@1:1.0.0,1.0.2:")
        depends_on("py-psutil", when="@1.6:+full")
        depends_on("py-pybv", when="@1.6.1:+full")
        depends_on("py-pymatreader", when="@1:1.0.0,1.0.2:+hdf5")
        depends_on("py-pyobjc-framework-cocoa@5.2:", when="@1.6:+full platform=darwin")
        depends_on("py-pyqt6@:6.6.0", when="@1.6.1:+full")
        depends_on("py-pyqt6-qt6@:6.6.0,6.6.2:", when="@1.6.1:+full")
        depends_on("py-python-picard", when="@1.6:+full")
        depends_on("py-pyvista@0.32.0:0.35.1,0.36:0.37,0.39:0.41,0.42.1:", when="@1.6:+full")
        depends_on("py-pyvistaqt@0.4:", when="@1.6:+full")
        depends_on("py-qdarkstyle", when="@1.6:+full")
        depends_on("py-qtpy", when="@1.6:+full")
        depends_on("py-scikit-learn", when="@1.6:+full")
        depends_on("py-scipy@1.7.1:", when="@1.6:")
        depends_on("py-scipy@1.6.3:", when="@1.4:1.5")
        depends_on("py-scipy@1.1.0:", when="@0.23:1.0.0,1.0.2:1.3")
        depends_on("py-sip", when="@1.6:+full")
        depends_on("py-snirf", when="@1.6.1:+full")
        depends_on("py-statsmodels", when="@1.6:+full")
        depends_on("py-threadpoolctl", when="@1.6:+full")
        depends_on("py-tqdm", when="@1:1.0.0,1.0.2:")
        depends_on("py-traitlets", when="@1.6:+full")
        depends_on("py-trame", when="@1.6:+full")
        depends_on("py-trame-vtk", when="@1.6:+full")
        depends_on("py-trame-vuetify", when="@1.6:+full")
        depends_on("py-vtk", when="@1.6:+full")
        depends_on("py-xlrd", when="@1.6:+full")
    # END DEPENDENCIES


        # self-dependency
        # depends_on("py-mne+hdf5", when="@1.6:+full")
