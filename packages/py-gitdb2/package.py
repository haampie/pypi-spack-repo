# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGitdb2(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.0.3.post1", sha256="f4c17cc3389772557b624e0208ed7cb854c6d7e95962da81e3a3ccd32f7c4b2e", url="https://pypi.org/packages/90/f4/7adc5862e6f094216c9e2d0c72dffadd89877c1626255ad1742495491ab6/gitdb2-3.0.3.post1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-smmap2@2", when="@3.0.3:3")
    # END DEPENDENCIES

