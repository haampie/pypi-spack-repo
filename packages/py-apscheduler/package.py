# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyApscheduler(PythonPackage):
    # BEGIN VERSIONS
    version("3.3.1", sha256="bc9f96e498adb362beb5f1d3715a2570d100183add4ace5227c1a7d5dbaac900", url="https://pypi.org/packages/22/ff/eb9d27536f25253c09573cc7afc6db9708ea0abad02f5ac031b412d5cbda/APScheduler-3.3.1-py2.py3-none-any.whl")
    version("2.1.0", sha256="3b4b44387616902ad6d13122961013630eb25519937e5aa7c450de85656c9753", url="https://pypi.org/packages/09/49/828c768c015ca3ca18b9a2e2029b6acc4c809e37c916659d3b54d69e67b1/APScheduler-2.1.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pytz", when="@3")
        depends_on("py-setuptools@0.7:", when="@3.1:3.10.1")
        depends_on("py-six@1.4:", when="@3.1:3")
        depends_on("py-tzlocal@1.2:", when="@3.1:3.6")
    # END DEPENDENCIES

