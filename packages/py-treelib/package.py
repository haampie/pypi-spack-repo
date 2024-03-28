# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTreelib(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.7.0", sha256="c37795eaba19f73f3e1a905ef3f4f0cab660dc7617126e8ae99391e25c755416", url="https://pypi.org/packages/74/93/0944bb5ade972a5ef2dd9211a20730081ed2833024239171807d7a9bd4b0/treelib-1.7.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six", when="@1.6.3:")
    # END DEPENDENCIES

