# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyZcBuildout(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.13.1", sha256="968e318d1a8c46acab0e5feddb16358fccc4f7f3c2a3b425a02f3471e2209570", url="https://pypi.org/packages/da/7e/f8174cafc7616ddc7230c4cb1f2e39efffcb7be110d49d50d2ff9709ebef/zc.buildout-2.13.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-setuptools@8:", when="@2.4.4:2.5,2.7:2.9.2,2.9.4:2.13.1,2.13.3,3:")
    # END DEPENDENCIES

