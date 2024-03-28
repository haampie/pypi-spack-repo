# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPylikwid(PythonPackage):
    # BEGIN VERSIONS
    version("0.4.0", sha256="f7894a6d7ebcea7da133ef639599a314f850f55cd6c5ffdd630bb879bd2aa0b8", url="https://pypi.org/packages/1e/02/895de87e388d4eeb25c466e4ff8939660cdd0c299d46ee9a6420c9adb2a7/pylikwid-0.4.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("cuda", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

