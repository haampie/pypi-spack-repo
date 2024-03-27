##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyYacs(PythonPackage):
    version("0.1.8", sha256="efc4c732942b3103bea904ee89af98bcd27d01f0ac12d8d4d369f1e7a2914384", url="https://pypi.org/packages/44/3e/4a45cb0738da6565f134c01d82ba291c746551b5bc82e781ec876eb20909/yacs-0.1.8.tar.gz")
    version("0.1.7", sha256="4e47a59c9852b5d9cdc3777587864e9771060340d8f1b92b2c68f45244550c02", url="https://pypi.org/packages/dc/32/8cc179b5ce8bcb9e334d218d4fd26266acc3ff4a60aa673a1cc6580ed661/yacs-0.1.7.tar.gz")
    version("0.1.6", sha256="602de7d0f2f4311d8aba599495c0321944bc41d5a19c166114ff60bc9c813cc7", url="https://pypi.org/packages/01/c0/5dde2cf2ab9783f04d557038875d4595f710730a6f82c2a9e79d4dc0001c/yacs-0.1.6.tar.gz")
    version("0.1.5", sha256="e9d10aabae40a02011354348c3b4293bee677667cab19cc52e3c09a6069e0625", url="https://pypi.org/packages/f0/88/0787bdef6dffa7f366b8feb138990b95930305882f539c70b1e170cfe86c/yacs-0.1.5.tar.gz")
    version("0.1.4", sha256="2ae48bd89224d0d0fa73d7d084ca02f892664e4a08776b495ae569493e2d0f57", url="https://pypi.org/packages/84/79/db039405644c37d0f10853edb39a3aa10b2f70a5d060fe2a60b95d75f0f1/yacs-0.1.4.tar.gz")
    version("0.1.3", sha256="ae1ae5fca50891747fab0867980c11f0b98873a7901cd1d041f4f8b88a8a73cc", url="https://pypi.org/packages/d3/cf/e0b2b7ea99e6f2869cd472e609bc9d17969dd104536e060147459ab0300a/yacs-0.1.3.tar.gz")
    version("0.1.2", sha256="7cf76233a9b617134b5d3313ab42abb5de9711e63b5aaef70675b34b082b4d5f", url="https://pypi.org/packages/4b/19/1c34be248ac8d7c6eea1f8596b38c1344972b5c46b0386c7db4e98f3e879/yacs-0.1.2.tar.gz")
    version("0.1.1", sha256="4d63c7dbea227d6e70d2025f6306ee38ab640a37948da73cc9aa2a8faafcdde6", url="https://pypi.org/packages/d8/f2/30a33298f67ae5e7fe7955521b1031cf2858ef10496cd88c333b0a96cc18/yacs-0.1.1.tar.gz")
    version("0.1.0", sha256="325c983c95e584c928b650d0975545434b972d491ca288a4d28af6607f0a4520", url="https://pypi.org/packages/7e/0f/f2dc321ff540b2385961491885801096e78c8dff917d8a92ba7e95eda055/yacs-0.1.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyyaml", when="@0.1.2:0.1.7")

