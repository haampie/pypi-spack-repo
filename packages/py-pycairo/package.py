# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPycairo(PythonPackage):
    # BEGIN VERSIONS
    version("1.24.0", sha256="1444d52f1bb4cc79a4a0c0fe2ccec4bd78ff885ab01ebe1c0f637d8392bcafb6", url="https://pypi.org/packages/a2/dd/bc2c9ee9485308a29c18b1241329e677917af25c60b127857f0fb23d0c6e/pycairo-1.24.0.tar.gz")
    version("1.20.0", sha256="5695a10cb7f9ae0d01f665b56602a845b0a8cb17e2123bfece10c2e58552468c", url="https://pypi.org/packages/9d/6e/499d6a6db416eb3cdf0e57762a269908e4ab6638a75a90972afc34885b91/pycairo-1.20.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@1.24:")
        depends_on("python@:3", when="@1.19:1.20")
    # END DEPENDENCIES

