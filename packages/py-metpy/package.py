##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMetpy(PythonPackage):
    version("1.0.1", sha256="7e1a730e370286ca3ec2f8cac80bd1b98b0c313bcb9bc57512229437ba41a139", url="https://pypi.org/packages/0b/6b/3391a378ba85a0a33d538df3653c3c4e3f2ce3bd60be41ef9e4e5512da84/MetPy-1.0.1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.6:")
        depends_on("py-importlib-resources@1.3:", when="@1:1.5 ^python@:3.8")
        depends_on("py-matplotlib@2.1.0:", when="@0.11:1.0")
        depends_on("py-numpy@1.16.0:", when="@0.12.1:1.0")
        depends_on("py-pandas@0.22:", when="@0.11:1.0")
        depends_on("py-pint@0.10.1:", when="@0.12.1:1.3")
        depends_on("py-pooch@0.1:", when="@0.10.2:1.2")
        depends_on("py-pyproj@2.3:", when="@1.0.1:1.1")
        depends_on("py-scipy@1.0.0:", when="@0.12:1.0")
        depends_on("py-traitlets@4.3.0:", when="@0.10:1.3")
        depends_on("py-xarray@0.14.1:", when="@1:1.3")

