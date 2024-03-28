# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAttmap(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.13.2", sha256="9c76af312c3678927a03ebb8fd2fa3a9cab37f7ce34f1dc574ea890c778f2f26", url="https://pypi.org/packages/2b/14/20b368acd5aacbd0f01004f7ac8b57ced1a961833795c053fd87774ce7e8/attmap-0.13.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-ubiquerg@0.2.1:", when="@0.13:")
    # END DEPENDENCIES

