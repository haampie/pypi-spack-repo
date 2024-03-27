##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCellpose(PythonPackage):
    version("2.2.3", sha256="32c4e5e820310f640108833c9f2b9e8e6f9be194e90ba9e8ba8cb5297b8c64f8", url="https://pypi.org/packages/ac/e0/faa627a4b0cb36b33e18c7c4cf0363d2274d7cef90bbcee08354178d0397/cellpose-2.2.3-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-fastremap", when="@0.7:")
        depends_on("py-google-cloud-storage", when="@:0.0.1.0,0.0.1.10:0.0.1.23")
        depends_on("py-imagecodecs", when="@2.0.5:")
        depends_on("py-llvmlite", when="@2.0.5:")
        depends_on("py-natsort", when="@:0.0,0.7:")
        depends_on("py-numba@0.53.0:", when="@2.0.5:")
        depends_on("py-numpy@1.20.0:", when="@0.7:")
        depends_on("py-opencv-python-headless", when="@0.0.3:0.0,0.7:")
        depends_on("py-roifile", when="@2.2.2:")
        depends_on("py-scipy", when="@:0.0,0.7:")
        depends_on("py-tifffile", when="@0.0.3:0.0,0.7:")
        depends_on("py-torch@1.6:", when="@0.7:")
        depends_on("py-tqdm", when="@:0.0,0.7:")

