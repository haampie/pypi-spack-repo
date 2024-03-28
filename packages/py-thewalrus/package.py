# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyThewalrus(PythonPackage):
    # BEGIN VERSIONS
    version("0.21.0", sha256="5f393d17fc8362e7156337faed769e99f15149040ef298d2a1be27f234aa8cb9", url="https://pypi.org/packages/34/b7/dc4666f631ef43b555f2740272c20579508e3cfa203f3daa8691cca33faa/thewalrus-0.21.0-py3-none-any.whl")
    version("0.20.0", sha256="adf6ae2976828bf2b8e26d49013d1175f6562c5a36f35f17363b985092c0b4df", url="https://pypi.org/packages/e9/c5/2d4f187642591634676086f1c93a549d65e77f7d8618e20babed2de6c9fc/thewalrus-0.20.0.tar.gz")
    version("0.19.0", sha256="07b6e2969bf5405a2df736c442b1500857438bbd2afc2053b8b600b8b0c67f97", url="https://pypi.org/packages/92/ec/aec87db2151afd4527b119f524203f8631d3c2457a127c8d1ed4ce9f59a9/thewalrus-0.19.0-py3-none-any.whl")
    version("0.18.0", sha256="743c9ad2416f57d66fcd0fdd136d6c3ba14c6040df3e3bda496a6a7576db274e", url="https://pypi.org/packages/8f/45/0ec0b63d1583bb9f3b1fe2c1104c5e0af14e48c0af9eaec36562616b374e/thewalrus-0.18.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-dask+delayed", when="@0.12:0.13.0-rc1,0.18:0.19,0.21:")
        depends_on("py-numba@0.49.1:", when="@0.19,0.21:")
        depends_on("py-numba@0.49.1:0.53", when="@0.18")
        depends_on("py-numpy@1.19.2:", when="@0.18:0.19,0.21:")
        depends_on("py-scipy@1.2.1:", when="@:0.13.0-rc1,0.18:0.19,0.21:")
        depends_on("py-sympy@1.5.1:", when="@0.13:0.13.0-rc1,0.18:0.19,0.21:")
    # END DEPENDENCIES

