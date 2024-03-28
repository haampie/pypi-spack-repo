# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMunch(PythonPackage):
    # BEGIN VERSIONS
    version("2.5.0", sha256="6f44af89a2ce4ed04ff8de41f70b226b984db10a91dcc7b9ac2efc1c77022fdd", url="https://pypi.org/packages/cc/ab/85d8da5c9a45e072301beb37ad7f833cd344e04c817d97e0cc75681d248f/munch-2.5.0-py2.py3-none-any.whl")
    version("2.2.0", sha256="62fb4fb318e965a464b088e6af52a63e0905a50500b770596a939d3855e7aa15", url="https://pypi.org/packages/92/58/c17cf679a2b9b65541cc71ba13a950289b7d34dd0967e34b8816a4d87044/munch-2.2.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six", when="@2.4:3")
    # END DEPENDENCIES

