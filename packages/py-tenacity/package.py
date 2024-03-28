# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTenacity(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("8.2.2", sha256="2f277afb21b851637e8f52e6a613ff08734c347dc19ade928e519d7d2d8569b0", url="https://pypi.org/packages/e7/b0/c23bd61e1b32c9b96fbca996c87784e196a812da8d621d8d04851f6c8181/tenacity-8.2.2-py3-none-any.whl")
    version("8.0.1", sha256="f78f4ea81b0fabc06728c11dc2a8c01277bfc5181b321a4770471902e3eb844a", url="https://pypi.org/packages/f2/a5/f86bc8d67c979020438c8559cc70cfe3a1643fd160d35e09c9cca6a09189/tenacity-8.0.1-py3-none-any.whl")
    version("6.3.1", sha256="baed357d9f35ec64264d8a4bbf004c35058fad8795c5b0d8a7dc77ecdcbb8f39", url="https://pypi.org/packages/4e/e4/bcaf6978c0811fbb480acc9bd6e024b53390a61d153fa0be4f20a6c80d94/tenacity-6.3.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six@1.9:", when="@4.5:4,5.0.3:5.0,6:7")
    # END DEPENDENCIES

