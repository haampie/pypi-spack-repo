# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPython3Openid(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.2.0", sha256="6626f771e0417486701e0b4daff762e7212e820ca5b29fcc0d05f6f8736dfa6b", url="https://pypi.org/packages/e0/a5/c6ba13860bdf5525f1ab01e01cc667578d6f1efc8a1dba355700fb04c29b/python3_openid-3.2.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-defusedxml", when="@3.1:")
    # END DEPENDENCIES

