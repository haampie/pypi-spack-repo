# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAutomat(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("22.10.0", sha256="c3164f8742b9dc440f3682482d32aaff7bb53f71740dd018533f9de286b64180", url="https://pypi.org/packages/29/90/64aabce6c1b820395452cc5472b8f11cd98320f40941795b8069aef4e0e0/Automat-22.10.0-py2.py3-none-any.whl")
    version("20.2.0", sha256="b6feb6455337df834f6c9962d6ccf771515b7d939bca142b29c20c2376bc6111", url="https://pypi.org/packages/dd/83/5f6f3c1a562674d65efc320257bdc0873ec53147835aeef7762fe7585273/Automat-20.2.0-py2.py3-none-any.whl")
    version("0.8.0", sha256="81c93c55d2742c55e74e6497a48e048a859fa01d7aa0b91a032be432229837e2", url="https://pypi.org/packages/e5/11/756922e977bb296a79ccf38e8d45cafee446733157d59bcd751d3aee57f5/Automat-0.8.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-attrs@19.2:", when="@20:")
        depends_on("py-attrs@16.1:", when="@0.7:0")
        depends_on("py-six")
    # END DEPENDENCIES

