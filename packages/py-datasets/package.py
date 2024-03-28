# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDatasets(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.8.0", sha256="f36cb362bb5587659bab18e594b6d25d9d28486d735a571319c82efeb5a4e5df", url="https://pypi.org/packages/24/57/6b07e4dc51479ae3e9bbc774af348b0307e2b66957ceae94d25e3f9d7dcf/datasets-2.8.0-py3-none-any.whl")
    version("1.8.0", sha256="9d449ff7dbb67e2af52f9658c19902890e9f3672053bdb56500717fd8888b3fd", url="https://pypi.org/packages/08/a2/d4e1024c891506e1cee8f9d719d20831bac31cb5b7416983c4d2f65a6287/datasets-1.8.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-aiohttp", when="@1.12:")
        depends_on("py-dill@:0.3.6", when="@2.7:2.9")
        depends_on("py-dill", when="@1:2.2.1")
        depends_on("py-fsspec@2021.11.1:+http", when="@2.4:2.14.4")
        depends_on("py-fsspec", when="@1.3:1.8")
        depends_on("py-huggingface-hub@0.2:", when="@2.5.2:2.10")
        depends_on("py-huggingface-hub@:0.0", when="@1.5:1.11")
        depends_on("py-multiprocess", when="@1.1:")
        depends_on("py-numpy@1.17.0:", when="@1:")
        depends_on("py-packaging", when="@1.6:")
        depends_on("py-pandas", when="@1:")
        depends_on("py-pyarrow@6:", when="@2.2:2.10")
        depends_on("py-pyarrow@1:3", when="@1.7:1.8")
        depends_on("py-pyyaml@5.1:", when="@2.6:")
        depends_on("py-requests@2.19:", when="@1:")
        depends_on("py-responses@:0.18", when="@1.18.4:2.12")
        depends_on("py-tqdm@4.62.1:", when="@1.12:")
        depends_on("py-tqdm@4.27:4.49", when="@1.1.2:1.8")
        depends_on("py-xxhash", when="@1:")

        # marker: (sys_platform != "darwin" or platform_machine != "arm64") and extra == "dev"
        # depends_on("py-tensorflow@2.2.0:2.6.0-rc2,2.6.2:", when="@2.14.1:")
        # depends_on("py-tensorflow@2.3.0:2.6.0-rc2,2.6.2:", when="@2.7:")

        # marker: (sys_platform != "darwin" or platform_machine != "arm64") and extra == "docs"
        # depends_on("py-tensorflow@2.2.0:2.6.0-rc2,2.6.2:", when="@2.14.1:")

        # marker: (sys_platform != "darwin" or platform_machine != "arm64") and extra == "tensorflow"
        # depends_on("py-tensorflow@2.2.0:2.6.0-rc2,2.6.2:", when="@2.7:")

        # marker: (sys_platform != "darwin" or platform_machine != "arm64") and extra == "tests"
        # depends_on("py-tensorflow@2.3.0:2.6.0-rc2,2.6.2:", when="@2.7:")

        # marker: (sys_platform == "darwin" and platform_machine == "arm64") and extra == "dev"
        # depends_on("py-tensorflow-macos", when="@2.7:")

        # marker: (sys_platform == "darwin" and platform_machine == "arm64") and extra == "docs"
        # depends_on("py-tensorflow-macos", when="@2.14.1:")

        # marker: (sys_platform == "darwin" and platform_machine == "arm64") and extra == "tensorflow"
        # depends_on("py-tensorflow-macos", when="@2.7:")

        # marker: (sys_platform == "darwin" and platform_machine == "arm64") and extra == "tests"
        # depends_on("py-tensorflow-macos", when="@2.7:")
    # END DEPENDENCIES

