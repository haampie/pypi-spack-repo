##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFenicsDijitso(PythonPackage):
    version("2019.1.0", sha256="ddb2c54e3e567b2639f492943c5457bf391c49eccda7343edf7d9414b10841a5", url="https://pypi.org/packages/f2/62/c061cb9f8f5547915804cdf8046fe2989c5b7317445fb1246ac77a9bad7f/fenics_dijitso-2019.1.0-py3-none-any.whl")
    version("2018.1.0", sha256="a9d5b4b190109bfce81e5a10d0934c2c84a85d0356dc7e3a70079897a5dd6d66", url="https://pypi.org/packages/07/3b/fbe922ff06bf750a618b6d171d7c5a3762e0f2ae0ea5ca3f27ffb92c3db9/fenics_dijitso-2018.1.0-py3-none-any.whl")
    version("2017.2.0", sha256="e54d1e7bbb3184340b923d8c71c3baf1ce7c93a7557c639b25315a225d2f3c24", url="https://pypi.org/packages/24/99/985e9df445fd156ce274f58109e8a32e01dd8a80c5ef0128b2342b77cbee/fenics-dijitso-2017.2.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-numpy", when="@2018:")

