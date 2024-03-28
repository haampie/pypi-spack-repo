# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLibsonata(PythonPackage):
    # BEGIN VERSIONS
    version("0.1.25", sha256="b332efa718123ee265263e1583a5998eaa945a13b8a22903873764cf1d8173fa", url="https://pypi.org/packages/e0/18/3de1dd868e56e339146da5bd14efe864748e4847920094b46f0f277399ac/libsonata-0.1.25.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.17.3:", when="@0.1.24:")
    # END DEPENDENCIES

