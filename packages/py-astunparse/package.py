# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAstunparse(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.6.3", sha256="c2652417f2c8b5bb325c885ae329bdf3f86424075c4fd1a128674bc6fba4b8e8", url="https://pypi.org/packages/2b/03/13dde6512ad7b4557eb792fbcf0c653af6076b81e5941d36ec61f7ce6028/astunparse-1.6.3-py2.py3-none-any.whl")
    version("1.6.2", sha256="271fb1f3d7a2e3c66eab41000298860f046253d22ec96e4f024cfaf266805a8e", url="https://pypi.org/packages/2e/37/5dd0dd89b87bb5f0f32a7e775458412c52d78f230ab8d0c65df6aabc4479/astunparse-1.6.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six@1.6.1:", when="@1.5:")
        depends_on("py-wheel@0.23:", when="@1.5:")
    # END DEPENDENCIES

