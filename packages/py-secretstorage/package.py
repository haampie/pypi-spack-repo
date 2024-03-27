##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySecretstorage(PythonPackage):
    version("3.3.3", sha256="f356e6628222568e3af06f2eba8df495efa13b3b63081dafd4f7d9a7b7bc9f99", url="https://pypi.org/packages/54/24/b4293291fa1dd830f353d2cb163295742fa87f179fcc8a20a306a81978b7/SecretStorage-3.3.3-py3-none-any.whl")
    version("3.3.2", sha256="755dc845b6ad76dcbcbc07ea3da75ae54bb1ea529eb72d15f83d26499a5df319", url="https://pypi.org/packages/54/42/7cf083c31a9739b40ed683fad17460d1db97ecd23c344df25e41fa9e85e2/SecretStorage-3.3.2-py3-none-any.whl")
    version("3.3.1", sha256="422d82c36172d88d6a0ed5afdec956514b189ddbfb72fefab0c8a1cee4eaf71f", url="https://pypi.org/packages/d9/1e/29cd69fdac7391aa51510dfd42aa70b4e6a826c8cd019ee2a8ab9ec0777f/SecretStorage-3.3.1-py3-none-any.whl")
    version("3.3.0", sha256="5c36f6537a523ec5f969ef9fad61c98eb9e017bc601d811e53aa25bece64892f", url="https://pypi.org/packages/63/a2/a6d9099b14eb5dbbb04fb722d2b5322688f8f99b471bdf2097e33efa8091/SecretStorage-3.3.0-py3-none-any.whl")
    version("3.2.0", sha256="ed5279d788af258e4676fa26b6efb6d335a31f1f9f529b6f1e200f388fac33e1", url="https://pypi.org/packages/2e/ab/9104db89ca0f1a23e5572456f39bc608164b86b4eaab048677b815327b88/SecretStorage-3.2.0-py3-none-any.whl")
    version("3.1.2", sha256="b5ec909dde94d4ae2fa26af7c089036997030f0cf0a5cb372b4cccabd81c143b", url="https://pypi.org/packages/c3/50/8a02cad020e949e6d7105f5f4530d41e3febcaa5b73f8f2148aacb3aeba5/SecretStorage-3.1.2-py3-none-any.whl")
    version("3.1.1", sha256="7a119fb52a88e398dbb22a4b3eb39b779bfbace7e4153b7bc6e5954d86282a8a", url="https://pypi.org/packages/82/59/cb226752e20d83598d7fdcabd7819570b0329a61db07cfbdd21b2ef546e3/SecretStorage-3.1.1-py3-none-any.whl")
    version("3.1.0", sha256="20196abd1a9d1310df7573d58ca6e7ed9292218c98ca3638eea07beb16080343", url="https://pypi.org/packages/d8/e8/80975fd281764c80b2eb581a7f25d2109786e273b8925e8161bd2d06d10a/SecretStorage-3.1.0-py3-none-any.whl")
    version("3.0.1", sha256="1bbf5b85a718854916d1c151fa33e6f667e3c005e033ea46d4123384d233b137", url="https://pypi.org/packages/f3/40/3cbd8b15c8f98b5c6d2480fb0087b06eb39b87992e61c966775156e1a693/SecretStorage-3.0.1-py3-none-any.whl")
    version("2.3.1", sha256="3af65c87765323e6f64c83575b05393f9e003431959c9395d1791d51497f29b6", url="https://pypi.org/packages/a5/a5/0830cfe34a4cfd0d1c3c8b614ede1edb2aaf999091ac8548dd19cb352e79/SecretStorage-2.3.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-cryptography@2:", when="@3.2:")
        depends_on("py-cryptography", when="@3:3.1")
        depends_on("py-jeepney@0.6:", when="@3.3:")
        depends_on("py-jeepney@0.4.2:", when="@3.1.2:3.2")
        depends_on("py-jeepney", when="@3:3.1.1")

