# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHelpdev(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.7.1", sha256="779a761b18c2d96fb181aa699609f802347806125f2fee2f60dad875a625e38e", url="https://pypi.org/packages/0c/af/b7549206bf1b4c618dfefb7650bb09be80fdbe1858e5ab4f1f69db51d9bb/helpdev-0.7.1-py3-none-any.whl")
    version("0.6.10", sha256="6cb2c604d97101a47b81d6d234b48e0f452efe4490b4cc67c33708420c2deaa0", url="https://pypi.org/packages/56/23/7bc32827ea3a34bdb19bded6c6be86e4ae69fceb21a5e27956fa6ef624f2/helpdev-0.6.10-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-importlib-metadata", when="@0.6.3:0.6")
        depends_on("py-psutil@5.6:", when="@:0.6")
    # END DEPENDENCIES

