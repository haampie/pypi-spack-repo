# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAiocontextvars(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2.2", sha256="885daf8261818767d8f7cbd79f9d4482d118f024b6586ef6e67980236a27bfa3", url="https://pypi.org/packages/db/c1/7a723e8d988de0a2e623927396e54b6831b68cb80dce468c945b849a9385/aiocontextvars-0.2.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-contextvars@2.4:", when="@0.2.2: ^python@:3.6")
    # END DEPENDENCIES

