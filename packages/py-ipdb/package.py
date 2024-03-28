# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyIpdb(PythonPackage):
    # BEGIN VERSIONS
    version("0.13.11", sha256="f74c2f741c18b909eaf89f19fde973f745ac721744aa1465888ce45813b63a9c", url="https://pypi.org/packages/65/49/381dbeff0a35b2f96f8847c4ca7ddac260762b3edb74722cfbcae24aa0b2/ipdb-0.13.11-py3-none-any.whl")
    version("0.13.10", sha256="6950715f491d59df6c27b49cb372f22c2f1763478a5e9ed03fb0507e2d85f460", url="https://pypi.org/packages/98/61/25480fc06aba3ecb3ce545ea78f1b15177e7953c2bcf54bda6bd1bcc9f83/ipdb-0.13.10.tar.gz")
    version("0.13.9", sha256="951bd9a64731c444fd907a5ce268543020086a697f6be08f7cc2c9a752a278c5", url="https://pypi.org/packages/fc/56/9f67dcd4a4b9960373173a31be1b8c47fe351a1c9385677a7bdd82810e57/ipdb-0.13.9.tar.gz")
    version("0.13.8", sha256="8d368fa048a93ad6c1985d7f1d78d68580c879e4053fc15714bdcf2a1b042d06", url="https://pypi.org/packages/5f/43/eb2be141dac56e502b6e35c1e4a9b1bbb2d4dcbec773c0f6563e79758909/ipdb-0.13.8.tar.gz")
    version("0.13.7", sha256="178c367a61c1039e44e17c56fcc4a6e7dc11b33561261382d419b6ddb4401810", url="https://pypi.org/packages/a9/3d/9a7fa78cf59b95ac46663cfb760e63854dd66a267cda573c1a2f95f87c19/ipdb-0.13.7.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-decorator", when="@0.13.11: ^python@:3.10")
        depends_on("py-decorator", when="@0.13.11: ^python@3.11:")
        depends_on("py-ipython@7.31.1:", when="@0.13.11: ^python@:3.10")
        depends_on("py-ipython@7.31.1:", when="@0.13.11: ^python@3.11:")
        depends_on("py-tomli", when="@0.13.11: ^python@:3.10")
    # END DEPENDENCIES

