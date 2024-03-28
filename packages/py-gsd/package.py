# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGsd(PythonPackage):
    # BEGIN VERSIONS
    version("3.2.0", sha256="cf3c8419ec66085b2b9853577058861d9e738bfe397b0170ead821b866ab49b9", url="https://pypi.org/packages/35/2c/48ed80548e753c94a76f871ce242d93fad1b937f29a685907ede1c46e188/gsd-3.2.0.tar.gz")
    version("3.1.1", sha256="6802b79d7f078536faf5a96ac300518613dd285cf3bc21ed81e1f2d0f7155bf5", url="https://pypi.org/packages/7f/d5/ba084d26f60667153685a40f3ebb2d598d8d0b0ce8fb101505b6e0bbec68/gsd-3.1.1.tar.gz")
    version("3.1.0", sha256="35a70419c6a519825afd9d5e47a570d98cec7273c39f43e2ab0aa3e7166ad198", url="https://pypi.org/packages/14/61/10e139928d0ca01798e6f0f7b60e40bfbb9a5d1add7dbaeaa6aa4ca64d8d/gsd-3.1.0.tar.gz")
    version("3.0.1", sha256="7b3ce7428d9f9f708618b3a2ef19ab122cc36b658ea53b70d0de40189d19647c", url="https://pypi.org/packages/1f/aa/c9f1d8107fad358a33b066de2c47530240eccce3c4adf8d07db78676a32c/gsd-3.0.1.tar.gz")
    version("2.8.0", sha256="f2b031a26a7a5bee5f3940dc2f36c5a5b6670307b297c526adf2e26c1f5b46ae", url="https://pypi.org/packages/2d/84/9f89b59705404ab78f5a49bee477832369515c9bc68448292843a4ffc3ae/gsd-2.8.0.tar.gz")
    version("1.9.3", sha256="c6b37344e69020f69fda2b8d97f894cb41fd720840abeda682edd680d1cff838", url="https://pypi.org/packages/22/59/a32c08d7308ff6b46736cd17ba14ab73d8f9bcb248b3a68013aa91676464/gsd-1.9.3.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.9.3:", when="@3.2:")
        depends_on("py-numpy@1.9.3:1", when="@1.6.2:1.9")
    # END DEPENDENCIES

