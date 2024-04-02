# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPygraphviz(PythonPackage):
    # BEGIN VERSIONS
    version("1.10", sha256="457e093a888128903251a266a8cc16b4ba93f3f6334b3ebfed92c7471a74d867", url="https://pypi.org/packages/ee/7e/7366c082f959db7ee18a16fc38dc594158ede65ca789bef87751ed5130c7/pygraphviz-1.10.zip")
    version("1.7", sha256="a7bec6609f37cf1e64898c59f075afd659106cf9356c5f387cecaa2e0cdb2304", url="https://pypi.org/packages/3a/d6/2c56f09ee83dbebb62c40487e4c972135661b9984fec9b30b77fb497090c/pygraphviz-1.7.zip")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@1.9:1.11")
        depends_on("python@3.7:", when="@1.7-rc1:1.8")
    # END DEPENDENCIES

