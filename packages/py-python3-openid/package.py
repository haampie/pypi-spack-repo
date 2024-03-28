# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPython3Openid(PythonPackage):
    # BEGIN VERSIONS
    version("3.2.0", sha256="6626f771e0417486701e0b4daff762e7212e820ca5b29fcc0d05f6f8736dfa6b", url="https://pypi.org/packages/e0/a5/c6ba13860bdf5525f1ab01e01cc667578d6f1efc8a1dba355700fb04c29b/python3_openid-3.2.0-py3-none-any.whl")
    version("3.1.0", sha256="0086da6b6ef3161cfe50fb1ee5cceaf2cda1700019fda03c2c5c440ca6abe4fa", url="https://pypi.org/packages/bd/de/52c5699f52dcee3037db587196dcaf63ffedf5fbeba3183afe9b21a3a89f/python3_openid-3.1.0-py3-none-any.whl")
    version("3.0.10", sha256="915d9adcf77b7ae801e377c7732ab3208eaedc4fe99cb2b37f8155b076c6eb1e", url="https://pypi.org/packages/8c/4b/c387251a9124fe0623fca93d744fdc164c094f895b5ddb04709c8b5300a1/python3-openid-3.0.10.zip")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-defusedxml", when="@3.1:")
    # END DEPENDENCIES

