# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPymatgen(PythonPackage):
    # BEGIN VERSIONS
    version("2022.9.8", sha256="2250e05b81af3313bc0fc70cb558c2f528ed4eefb32d943ed9bd7a9756f03652", url="https://pypi.org/packages/92/f5/f85118b4ca8af05b147fda11dda53a699f5932293fd78268e3c5438b1d31/pymatgen-2022.9.8.tar.gz")
    version("2021.3.9", sha256="a6f22d69133a48b7801bfd5e6a2878b47b4b4b2ef1a377b87c6c573be14cbf16", url="https://pypi.org/packages/18/06/8f4a5288ea5d940773d9c8651aee59535006353b1b592ac1e61802b0749f/pymatgen-2021.3.9.tar.gz")
    version("2020.12.31", sha256="5002490facd47c55d2dae42c35712e061c1f5d881180485c0543a899589856d6", url="https://pypi.org/packages/e1/18/274b40cff34257a728071199d21105ced3116b42dd60793113eee7b1b5ca/pymatgen-2020.12.31.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@2022.1:2023.8")
        depends_on("python@3.7:", when="@2021.3.4:2022.0")
    # END DEPENDENCIES

