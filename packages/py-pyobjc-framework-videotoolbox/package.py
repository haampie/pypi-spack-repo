# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkVideotoolbox(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="347259a8e920dbc3dd1fada5ab0d829485cef3165166fa65f78c23ada4f9b80a", url="https://pypi.org/packages/87/26/995dde56ec9955b27d702cb5672f56ec551ec93b83e56c964af29be4b7fb/pyobjc-framework-VideoToolbox-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coremedia@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
    # END DEPENDENCIES

