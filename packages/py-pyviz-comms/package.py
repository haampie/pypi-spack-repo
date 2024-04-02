# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyvizComms(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.2.1", sha256="aba28430cf28b39f2605acb48f7fddf0e3025394a8286adfeb40d74b0ae0f4f9", url="https://pypi.org/packages/2f/78/72bec6805be44a11dc80e949752fcaacc21661c3423e26623263d19a73d1/pyviz_comms-2.2.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-param")
    # END DEPENDENCIES

