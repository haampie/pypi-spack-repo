# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMpldock(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.1", sha256="54366800cd2963d35a8942355714a6a28361906c54ca9d89a6882bf281610131", url="https://pypi.org/packages/ab/ee/babafc1920fedba594160487e5ec8c7be524cbf9f167a85a660f3e631746/mpldock-0.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-appdirs", when="@:0.0.1,0.0.3:")
        depends_on("py-matplotlib", when="@:0.0.1,0.0.3:")
        depends_on("py-pyqt5", when="@:0.0.1,0.0.3:")
    # END DEPENDENCIES

