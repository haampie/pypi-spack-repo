# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGeomdl(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("5.3.1", sha256="0f36a4bacde5b218c73aadc69ff152e7f7fb3aa7260df0e6647a701a5351d76a", url="https://pypi.org/packages/48/32/559b938e6654ecdf87d256ac2bfd9a25464560a312a58aaf25076d0ce48e/geomdl-5.3.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("viz", default=False, description="viz")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

