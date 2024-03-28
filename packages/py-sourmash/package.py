# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySourmash(PythonPackage):
    # BEGIN VERSIONS
    version("4.8.2", sha256="e0df78032e53ed88977445933ba3481dd10c7d3bd26d019511a6a4e6d7518475", url="https://pypi.org/packages/69/07/a4b72e899ecd3fa50951a0f7e25cce24b3ff1a3268bc4154086a5d007ac9/sourmash-4.8.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.10:", when="@4.8.5:")
        depends_on("py-bitstring@3.1.9:", when="@4.7:")
        depends_on("py-cachetools@4:", when="@4.7:")
        depends_on("py-cffi@1.14:", when="@3.3.1:3.4.0,4.7:")
        depends_on("py-deprecation@2.0.6:", when="@3.2.2,3.3.1:3.4.0,4.7:")
        depends_on("py-importlib-metadata@3.6:", when="@4.8:4.8.4 ^python@:3.9")
        depends_on("py-matplotlib", when="@3.2.2,3.3.1:3.4.0,4.7:")
        depends_on("py-numpy", when="@3.2.2,3.3.1:3.4.0,4.7:")
        depends_on("py-scipy", when="@3.2.2,3.3.1:3.4.0,4.7:")
        depends_on("py-screed@1.1.2:", when="@4.8:")
    # END DEPENDENCIES

