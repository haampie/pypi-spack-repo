# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySecretstorage(PythonPackage):
    # BEGIN VERSIONS
    version("3.3.3", sha256="f356e6628222568e3af06f2eba8df495efa13b3b63081dafd4f7d9a7b7bc9f99", url="https://pypi.org/packages/54/24/b4293291fa1dd830f353d2cb163295742fa87f179fcc8a20a306a81978b7/SecretStorage-3.3.3-py3-none-any.whl")
    version("3.3.1", sha256="422d82c36172d88d6a0ed5afdec956514b189ddbfb72fefab0c8a1cee4eaf71f", url="https://pypi.org/packages/d9/1e/29cd69fdac7391aa51510dfd42aa70b4e6a826c8cd019ee2a8ab9ec0777f/SecretStorage-3.3.1-py3-none-any.whl")
    version("3.1.2", sha256="b5ec909dde94d4ae2fa26af7c089036997030f0cf0a5cb372b4cccabd81c143b", url="https://pypi.org/packages/c3/50/8a02cad020e949e6d7105f5f4530d41e3febcaa5b73f8f2148aacb3aeba5/SecretStorage-3.1.2-py3-none-any.whl")
    version("2.3.1", sha256="3af65c87765323e6f64c83575b05393f9e003431959c9395d1791d51497f29b6", url="https://pypi.org/packages/a5/a5/0830cfe34a4cfd0d1c3c8b614ede1edb2aaf999091ac8548dd19cb352e79/SecretStorage-2.3.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cryptography@2:", when="@3.2:")
        depends_on("py-cryptography", when="@3:3.1")
        depends_on("py-jeepney@0.6:", when="@3.3:")
        depends_on("py-jeepney@0.4.2:", when="@3.1.2:3.2")
    # END DEPENDENCIES

