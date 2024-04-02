# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkPhotos(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="ba05d1208158e6de6d14782c182991c0d157254be7254b8d3bb0a9a53bf113fb", url="https://pypi.org/packages/60/9b/87b03e8c48c2c7ceda0051cdf9c5c50b8279483602b65c1b73122f8953cb/pyobjc-framework-Photos-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

