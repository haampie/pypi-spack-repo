# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBlosc2(PythonPackage):
    # BEGIN VERSIONS
    version("2.2.8", sha256="59065aac5e9b01b0e9f3825d8e7f69f64b59bbfab148a47c54e4115f62a97474", url="https://pypi.org/packages/0a/66/ed9545df299067df5e87e49d6cdce6db594d7f32ee39f9deb4f0933c3422/blosc2-2.2.8.tar.gz")
    version("2.0.0", sha256="f19b0b3674f6c825b490f00d8264b0c540c2cdc11ec7e81178d38b83c57790a1", url="https://pypi.org/packages/6e/bb/339a2ea90db9c2c78ac6de8b4627f9d1ff1551fc260de2d54999f91a6538/blosc2-2.0.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@2.2.8")
        depends_on("py-msgpack", when="@2.2.7:")
        depends_on("py-ndindex@1.4:", when="@2.2.7:")
        depends_on("py-numpy@1.20.3:", when="@2.2.7:")
        depends_on("py-py-cpuinfo", when="@2.2.7:")
    # END DEPENDENCIES

