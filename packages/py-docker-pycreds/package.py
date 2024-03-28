# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDockerPycreds(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.4.0", sha256="7266112468627868005106ec19cd0d722702d2b7d5912a28e19b826c3d37af49", url="https://pypi.org/packages/f5/e8/f6bd1eee09314e7e6dee49cbe2c5e22314ccdb38db16c9fc72d2fa80d054/docker_pycreds-0.4.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six@1.4:", when="@0.2.2:")
    # END DEPENDENCIES

