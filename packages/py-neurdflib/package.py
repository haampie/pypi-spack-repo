# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNeurdflib(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("5.0.1", sha256="b542bf337d3ffea111e8fe35ceb35c85172949e42c0597acc12820f7f27344d8", url="https://pypi.org/packages/41/66/304a1ad40fecee3504a315d831afcaebe156a62ff1628311bac3cb8d55c8/neurdflib-5.0.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-isodate")
        depends_on("py-pyparsing")
        depends_on("py-six")
    # END DEPENDENCIES

