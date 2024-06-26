# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBackportsCachedProperty(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0.2", sha256="baeb28e1cd619a3c9ab8941431fe34e8490861fb998c6c4590693d50171db0cc", url="https://pypi.org/packages/eb/ae/69e52acdcf381b108b36d989ea58656de4a9ab8863aba6176d80d01041df/backports.cached_property-1.0.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-typing@3.6:", when="^python@:3.6")
    # END DEPENDENCIES

