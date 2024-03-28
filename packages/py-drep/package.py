# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDrep(PythonPackage):
    # BEGIN VERSIONS
    version("3.4.2", sha256="90d61e40b987cef85b52209720afe15c090d6af8095f5ac8d14354b374007fa7", url="https://pypi.org/packages/21/b9/d7d4088f41c98c5f7a26487b8fe77e8df09f9b6407aa6eded188afab9d62/drep-3.4.2.tar.gz")
    version("3.4.0", sha256="a6533eb585122c1ee66ae622b1b97450a3e1e493a3c3c1d55e79a580d5c46d40", url="https://pypi.org/packages/1b/15/774cc3c555f186e6ad3a6a65ab3030e514ab706cee6d805fcbaeb626f039/drep-3.4.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("anicalculator", default=False)
    variant("fastani", default=False)
    variant("prodigal", default=False)
    variant("py-checkm-genome", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

