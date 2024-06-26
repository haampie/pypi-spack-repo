# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCoveralls(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.0.1", sha256="7bd173b3425733661ba3063c88f180127cc2b20e9740686f86d2622b31b41385", url="https://pypi.org/packages/54/f5/a6431412a456267b43b03ebd3670d8e196754f5280a2409a4c9ceaccf192/coveralls-3.0.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("pyyaml", default=False, description="pyyaml")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-coverage@4.1:5", when="@2:3.2")
        depends_on("py-docopt@0.6.1:")
        depends_on("py-requests@1:")
    # END DEPENDENCIES

