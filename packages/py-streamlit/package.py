# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyStreamlit(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.20.0", sha256="41a544b8dc618ee65726da3ac76149c5b2bf3da7bde6d50625c4f7ec95e6c9e8", url="https://pypi.org/packages/ed/7c/04aafd3877ab37635b6dbbf72dc95264cd7679e9e9f08978437e7a597809/streamlit-1.20.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@:1.23")
        depends_on("py-altair@3.2:4", when="@1.20:1.22")
        depends_on("py-blinker@1:", when="@:1.22")
        depends_on("py-cachetools@4:", when="@:1.22")
        depends_on("py-click@7:", when="@:1.22")
        depends_on("py-gitpython@:3.1.18,3.1.20:", when="@:1.22")
        depends_on("py-importlib-metadata@1.4:", when="@:1.22")
        depends_on("py-numpy", when="@:1.22")
        depends_on("py-packaging@14.1:", when="@:1.22")
        depends_on("py-pandas@0.25.0:1", when="@1.20:1.21")
        depends_on("py-pillow@6.2:", when="@:1.22")
        depends_on("py-protobuf@3.12.0:3", when="@:1.22")
        depends_on("py-pyarrow@4:", when="@:1.24")
        depends_on("py-pydeck@0.1.dev5:", when="@:1.22")
        depends_on("py-pympler@0.9:", when="@:1.22")
        depends_on("py-python-dateutil", when="@:1.22")
        depends_on("py-requests@2.4:", when="@:1.22")
        depends_on("py-rich@10.11:", when="@:1.22")
        depends_on("py-semver", when="@:1.20")
        depends_on("py-toml", when="@:1.22")
        depends_on("py-tornado@6.0.3:", when="@1.18:1.22")
        depends_on("py-typing-extensions@3.10:", when="@:1.23.0")
        depends_on("py-tzlocal@1.1:", when="@:1.22")
        depends_on("py-validators@0.2:", when="@:1.22")
        depends_on("py-watchdog", when="@:1.24 platform=windows")
        depends_on("py-watchdog", when="@:1.24 platform=linux")
        depends_on("py-watchdog", when="@:1.24 platform=freebsd")
        depends_on("py-watchdog", when="@:1.24 platform=cray")
    # END DEPENDENCIES

