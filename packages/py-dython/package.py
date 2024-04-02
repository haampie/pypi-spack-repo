# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDython(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.7.4", sha256="3ae49dc2c654decc55166fe0210f494903a7cd61cd99637f43ab16643d946753", url="https://pypi.org/packages/16/65/7e2ba587f7854ce45ac5a69348fdfb1872fd39c138dc5ebf45934beda65b/dython-0.7.4-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@0.7.3:")
        depends_on("py-matplotlib@3.5.3:", when="@0.7.3:0.7.4")
        depends_on("py-numpy@1.23.0:", when="@0.7.3:")
        depends_on("py-pandas@1.4.2:", when="@0.7.3:")
        depends_on("py-psutil@5.9.1:", when="@0.7.2:")
        depends_on("py-scikit-learn@0.24.2:", when="@0.7:")
        depends_on("py-scikit-plot@0.3.7:", when="@:0.7.4")
        depends_on("py-scipy@1.7.1:", when="@0.7:")
        depends_on("py-seaborn@0.12.0:", when="@0.7.3:")
    # END DEPENDENCIES

