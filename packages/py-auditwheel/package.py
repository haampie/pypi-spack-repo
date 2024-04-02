# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAuditwheel(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("5.1.2", sha256="4d06aea3ab59a2b8aa733798ac221556a3f5c021fddc42e5de5bcef20201c031", url="https://pypi.org/packages/5e/6d/252b892a851cc43edb523982178da19cf69efc45f5f3aea9752a61813beb/auditwheel-5.1.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-importlib-metadata", when="@5 ^python@:3.7")
        depends_on("py-pyelftools@0.24:", when="@3.1.1:3.1,3.3:")
    # END DEPENDENCIES

