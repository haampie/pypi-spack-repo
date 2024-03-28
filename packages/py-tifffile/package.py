# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTifffile(PythonPackage):
    # BEGIN VERSIONS
    version("2023.8.30", sha256="62364eef35a6fdcc7bc2ad6f97dd270f577efb01b31260ff800af76a66c1e145", url="https://pypi.org/packages/12/3e/89513f44a10c625121b7d5bc54390d7ac7f2c92a19755c052888febf9730/tifffile-2023.8.30-py3-none-any.whl")
    version("2022.10.10", sha256="87f3aee8a0d06b74655269a105de75c1958a24653e1930d523eb516100043503", url="https://pypi.org/packages/d2/cb/1ecf9f39113a7ad0529a0441a16982791e7b37a4efdba2f89a687fdf15c9/tifffile-2022.10.10-py3-none-any.whl")
    version("2021.11.2", sha256="2e0066f90e2dbeb3e6a287cfd78bafbd2f142fabbca4a76a8ff809573baf5ad5", url="https://pypi.org/packages/d8/38/85ae5ed77598ca90558c17a2f79ddaba33173b31cf8d8f545d34d9134f0d/tifffile-2021.11.2-py3-none-any.whl")
    version("2020.10.1", sha256="9611ac348b4db6844b6555db2b5f8f2be1715728a0011352acb55e0171ee2949", url="https://pypi.org/packages/e8/8c/166c88fcbe3b3632dcf93a106f6d13892b1a2b822b61eb7cd9a5ab68b259/tifffile-2020.10.1-py3-none-any.whl")
    version("0.12.1", sha256="802367effe86b0d1e64cb5c2ed886771f677fa63260b945e51a27acccdc08fa1", url="https://pypi.org/packages/41/d2/086654909995176e34228ed0e5673fed505651083f0d8b277867fb4d9f3a/tifffile-0.12.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@2023.7.18:")
        depends_on("py-numpy", when="@2023:")
        depends_on("py-numpy@1.19.2:", when="@2022")
        depends_on("py-numpy@1.15.1:", when="@2020:2021")
    # END DEPENDENCIES

