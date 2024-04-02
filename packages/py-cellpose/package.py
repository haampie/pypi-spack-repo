# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCellpose(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.2.3", sha256="32c4e5e820310f640108833c9f2b9e8e6f9be194e90ba9e8ba8cb5297b8c64f8", url="https://pypi.org/packages/ac/e0/faa627a4b0cb36b33e18c7c4cf0363d2274d7cef90bbcee08354178d0397/cellpose-2.2.3-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("gui", default=False, description="gui")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-fastremap")
        depends_on("py-google-cloud-storage", when="+gui")
        depends_on("py-imagecodecs", when="@2.0.5:")
        depends_on("py-llvmlite", when="@2.0.5:")
        depends_on("py-natsort")
        depends_on("py-numba@0.53.0:", when="@2.0.5:")
        depends_on("py-numpy@1.20.0:")
        depends_on("py-opencv-python-headless")
        depends_on("py-pyqt6", when="@2.2.3:+gui")
        depends_on("py-pyqt6-sip", when="@2.2.3:+gui")
        depends_on("py-pyqtgraph@0.11:", when="+gui")
        depends_on("py-qtpy", when="@2.2.3:+gui")
        depends_on("py-roifile", when="@2.2.2:")
        depends_on("py-scipy")
        depends_on("py-superqt", when="@2.2:+gui")
        depends_on("py-tifffile")
        depends_on("py-torch@1.6:")
        depends_on("py-tqdm")
    # END DEPENDENCIES

