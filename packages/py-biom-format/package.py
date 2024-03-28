# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBiomFormat(PythonPackage):
    # BEGIN VERSIONS
    version("2.1.15", sha256="3bda2096e663dc1cb6f90f51b394da0838b9be5164a44370c134ce5b3b2a4dd3", url="https://pypi.org/packages/fc/db/daf7c3872dd49acf6233873fb6f1ab7b6ca324bba25bf28fc9cf7dfd4c7b/biom-format-2.1.15.tar.gz")
    version("2.1.14", sha256="c8bac94ab6aa8226c0d38af7a3341d65e5f3664b9f45ec44fdf8b5275b2f92c1", url="https://pypi.org/packages/8e/2c/132267e58172821fc15fa3856f53ed09b607837fe06e2bb60b230005951d/biom-format-2.1.14.tar.gz")
    version("2.1.13", sha256="c48ed8fe978adaff5832f9d65ffcf8b735298bb2175b0360251d556baac5d4dc", url="https://pypi.org/packages/90/57/0a326e17005b25e56f6e25b8b1e3eae299b7f6d53af06b11c4830d631612/biom-format-2.1.13.tar.gz")
    version("2.1.12", sha256="a4460e803b2abfcabe76d5d8fec0f3f7e76a8cd0e09bf22bb38dea9fca224ac2", url="https://pypi.org/packages/fc/3f/7eb762b52f490b810b1686fd41cd6f3f7f33c0dab29c4273c96e9a1641a2/biom-format-2.1.12.tar.gz")
    version("2.1.11", sha256="ff895d5d4544de2a18fcc4011f28a1bea3a46e4afdf8dc33a1e57862dec5e3e8", url="https://pypi.org/packages/9a/8d/c89194f53e09454a7b742f8e9b9542fb8d1a93cbb4d3d26f3445a3e51d07/biom-format-2.1.11.tar.gz")
    version("2.1.10", sha256="f5a277a8144f0b114606852c42f657b9cfde44b3cefa0b2638ab1c1d5e1d0488", url="https://pypi.org/packages/2b/8f/ef865d43a06dd3d1b09808fbd129074e64127fa8db0b93b5e0cf1d1a50de/biom-format-2.1.10.tar.gz")
    version("2.1.9", sha256="18a6e4d4b4b2a6bf2d5544fa357ad168bedeac93f0837015ef9c72f41fa89491", url="https://pypi.org/packages/4b/50/65e535736597ce91e82a8e3e83cf1e88735368b58f99585f600b854f0bc9/biom-format-2.1.9.tar.gz")
    version("2.1.8", sha256="3711de5807e5b29d944cd2713a16f26b6148eefd5b831ccad6a10c06cbd42649", url="https://pypi.org/packages/c1/c6/3b4284680b390a6c0a39de2fddddfe19a28d1bdceb5951713c483c147f44/biom-format-2.1.8-1.tar.gz")
    version("2.1.7", sha256="b47e54282ef13cddffdb00aea9183a87175a2372c91a915259086a3f444c42f4", url="https://pypi.org/packages/25/92/ca4688a006b784bcc1f118c4a53e9aadc78d78abf8ff58ee11d29ac950a4/biom-format-2.1.7.tar.gz")
    version("2.1.6", sha256="8eefc275a85cc937f6d6f408d91b7b45eae854cd5d1cbda411a3af51f5b49b0d", url="https://pypi.org/packages/46/a6/fccc2f5db587d7d896b52054aa5a9f0f7fd8fb6ad23ab9a02934d4cb1739/biom-format-2.1.6.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-click", when="@2.1.7")
        depends_on("py-future@0.16:", when="@2.1.7")
        depends_on("py-numpy@1.9.2:", when="@2.1.7")
        depends_on("py-pandas@0.20.0:", when="@2.1.7")
        depends_on("py-scipy@0.13:", when="@2.1.7")
        depends_on("py-six@1.10:", when="@2.1.7")
    # END DEPENDENCIES

