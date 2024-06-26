# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyResponses(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.13.3", sha256="b54067596f331786f5ed094ff21e8d79e6a1c68ef625180a7d34808d6f36c11b", url="https://pypi.org/packages/ba/00/0e63b7024c2d873bf57411ab0ed77eeafd5f44bace7cbf1d56bca8ab3be2/responses-0.13.3-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-requests@2:", when="@:0.17")
        depends_on("py-six", when="@:0.17")
        depends_on("py-urllib3@1.25.10:", when="@0.10.16:0.23.1")
    # END DEPENDENCIES

