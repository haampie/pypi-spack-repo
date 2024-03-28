# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyIcs(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.7", sha256="bf5fbdef6e1e073afdadf1b996f0271186dd114a148e38e795919a1ae644d6ac", url="https://pypi.org/packages/42/e2/b09e44126e2858346c8b3a722d8de4b9baf4a58e9bc3931b579aaa0ac763/ics-0.7-py2.py3-none-any.whl")
    version("0.6", sha256="12cf34aed0dafa1bf99d79ca58e99949d6721511b856386e118015fe5f5d6e3a", url="https://pypi.org/packages/cf/68/e99b7c80638dd5dcc03e976ce2cb312e1a6abc8a6a7d688614bb62d61429/ics-0.6-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-arrow@0.11:0.14", when="@0.6:0.7.0")
        depends_on("py-python-dateutil", when="@0.4:0.7")
        depends_on("py-six@1.5.1:", when="@0.4:0.7")
        depends_on("py-tatsu@4.2.1:", when="@0.6:0.7")
    # END DEPENDENCIES

