# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAgateDbf(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2.3", sha256="b36e5a8321f9c42f812750256cadd600f779a19e334a80fee6e032395c0b9aa0", url="https://pypi.org/packages/d9/99/cd4729cb51d6c7de8ad00eab375021cb34b8ca132350efe401488af10483/agate_dbf-0.2.3-py2.py3-none-any.whl")
    version("0.2.2", sha256="632a8826ecde3dffb28f15e3ccb9d523bc15b79eb157f063f2febc2c4078957a", url="https://pypi.org/packages/fc/75/32847937627c8fe2271606d71de85486ffaf01b28a091ecdc43e58876b1b/agate_dbf-0.2.2-py2.py3-none-any.whl")
    version("0.2.1", sha256="f618fadb413d41468c90d72fca945681d82d9e4d1b3d89f9bda52e607b828c0b", url="https://pypi.org/packages/3d/d0/5a161b906a7eaa2b3d5690bbf0de5ceb4398e21d3e915f69869cfeef906f/agate_dbf-0.2.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-agate@1.5:", when="@0.2.2:")
        depends_on("py-dbfread@2.0.5:", when="@0.2.2:")
    # END DEPENDENCIES

