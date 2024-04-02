# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCryodrgn(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.3.0", sha256="a42a55e99c28fef2d2eb1151397bb69089b4c73920945e5e7ca73e62aeaccdf9", url="https://pypi.org/packages/03/29/f9750c89414937c8700d9d5aa167d9ed1e3157ebb6a9971effb4bcbe8bec/cryodrgn-2.3.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@:3.1")
        depends_on("py-cufflinks")
        depends_on("py-healpy", when="@2:")
        depends_on("py-ipywidgets@:7")
        depends_on("py-jupyterlab")
        depends_on("py-matplotlib", when="@:3.0.0")
        depends_on("py-numpy", when="@:3.0")
        depends_on("py-pandas@:1", when="@2.3:")
        depends_on("py-pyyaml", when="@2.3:")
        depends_on("py-scikit-learn")
        depends_on("py-scipy@1.3.1:")
        depends_on("py-seaborn@:0.11", when="@2:")
        depends_on("py-torch@1:")
        depends_on("py-umap-learn")
    # END DEPENDENCIES

