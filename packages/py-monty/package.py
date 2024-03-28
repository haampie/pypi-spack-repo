# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMonty(PythonPackage):
    # BEGIN VERSIONS
    version("2021.8.17", sha256="adeda46dbf2231f0647be725fea9b290c292899d4f39d6d1e18838b4c5a6ca0c", url="https://pypi.org/packages/d0/ad/c19627ffddbd45097780431333ab1659dcbfcafede32c28d85c202b55467/monty-2021.8.17-py3-none-any.whl")
    version("0.9.6", sha256="bbf05646c4e86731c2398a57b1044add7487fc4ad03122578599ddd9a8892780", url="https://pypi.org/packages/53/61/b42d8ed8d28ee5ebd4dd3dce315e1e5176f70a138c869b15e2cc6f1ef468/monty-0.9.6.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@2023.11:")
    # END DEPENDENCIES

