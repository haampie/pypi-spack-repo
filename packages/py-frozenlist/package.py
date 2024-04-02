# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFrozenlist(PythonPackage):
    # BEGIN VERSIONS
    version("1.3.1", sha256="3a735e4211a04ccfa3f4833547acdf5d2f863bfeb01cfd3edaffbc251f15cec8", url="https://pypi.org/packages/8a/95/229aacfe85daa28e2792481a98c336bc30d3729533e6a44db537880aca21/frozenlist-1.3.1.tar.gz")
    version("1.3.0", sha256="ce6f2ba0edb7b0c1d8976565298ad2deba6f8064d2bebb6ffce2ca896eb35b0b", url="https://pypi.org/packages/f4/f7/8dfeb76d2a52bcea2b0718427af954ffec98be1d34cd8f282034b3e36829/frozenlist-1.3.0.tar.gz")
    version("1.2.0", sha256="68201be60ac56aff972dc18085800b6ee07973c49103a8aba669dee3d71079de", url="https://pypi.org/packages/5c/ee/7c6287928ba776567603248e160387cf4143641ecf734e393ad9b2c82475/frozenlist-1.2.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@1.3")
    # END DEPENDENCIES

