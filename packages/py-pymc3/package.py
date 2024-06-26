# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPymc3(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.8", sha256="99bde24af8114555047504f106f652d22444ae5dacf85675cf2e996875cfb0df", url="https://pypi.org/packages/32/19/6c94cbadb287745ac38ff1197b9fadd66500b6b9c468e79099b110c6a2e9/pymc3-3.8-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-arviz@0.4.1:", when="@3.8")
        depends_on("py-h5py@2.7.0:", when="@3.8:3.9")
        depends_on("py-numpy@1.13.0:", when="@3.8:3.10")
        depends_on("py-pandas@0.18:", when="@3.8:3.10")
        depends_on("py-patsy@0.4:", when="@3.8")
        depends_on("py-scipy@0.18.1:", when="@3.8:3.10")
        depends_on("py-theano@1.0.4:", when="@3.8:3.9.2")
        depends_on("py-tqdm@4.8.4:", when="@3.8")
    # END DEPENDENCIES

