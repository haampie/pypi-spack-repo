# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkPhase(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="f29cd40e5be860758d8444e761d43f313915e2750b8b03b8a080dd86260f6f91", url="https://pypi.org/packages/0a/56/1ec5abb4316fa3984b487fd2c01d4bbb203995a021456954b2e24c9b6c61/pyobjc_framework_PHASE-10.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-avfoundation@10.2:", when="@10.2:")
    # END DEPENDENCIES

