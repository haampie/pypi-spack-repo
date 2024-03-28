# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyClassDoc(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2.0-beta0", sha256="df9fcd0bba659e0fb491769bc4c9e2619ce571d392960c4def6f5472ba76cf64", url="https://pypi.org/packages/8f/3d/8af3ba66964a5f1325558150039a2880830292d631fa26114a1060364f92/class_doc-0.2.0b0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-more-itertools@7.2:7", when="@:0.2.5")
    # END DEPENDENCIES

