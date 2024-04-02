# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBrian2(PythonPackage):
    # BEGIN VERSIONS
    version("2.5.0.2", sha256="70e6f88fb26f04ccafb91e0a29999774e45899771357aff7043951c853919a0f", url="https://pypi.org/packages/a1/c5/f090582e66c27e56a982ecca8ba4850948daa4b3f14bef48cfa0951b25ea/Brian2-2.5.0.2.tar.gz")
    version("2.5.0.1", sha256="1f719b563ae38658c4c59bac5aeb06b41970c6eedc52021ddf6d9254913733d3", url="https://pypi.org/packages/c1/43/013cdfd8066c7129ffc56fcb0f78ba18cd91dc7928af6d1f57d8e23aedf1/Brian2-2.5.0.1.tar.gz")
    version("2.4.2", sha256="7a711af40145d8c62b0bc0861d352dc64f341c3a738174d87ef9d71e50e959f2", url="https://pypi.org/packages/9a/c7/565012c479953d041d5e828938515d3c402d0c3f4942180f1c44cb0f472e/Brian2-2.4.2.tar.gz")
    version("2.2.2.1", sha256="02075f66d42fd243fc5e28e1add8862709ae9fdabaffb69858e6d7f684a91525", url="https://pypi.org/packages/5f/56/41fd9d50bcb4912b9bfab06aa36093683c18d73042f9275b598b2a8a2dae/Brian2-2.2.2.1.tar.gz")
    version("2.0.1", sha256="93964fe2306108cd468df0d5bfe106a90beb4480d107e9bc0806536e55817213", url="https://pypi.org/packages/87/74/05a47ca1edcb0ea4dc27a9c53a541bbc31553ea12669a2833a8941b4e6f3/Brian2-2.0.1.tar.bz2")
    version("2.0-rc3", sha256="4da0061cc2d2c3195f1bc8585515df2e6c46d990c1d297abb55ac7e425fcdc9d", url="https://pypi.org/packages/e2/50/0fc89b9ebc3b870d63e98960261faaff14c69fe9f20ab8db71bb3d88688e/Brian2-2.0rc3.zip")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@2.5:2.5.1")
        depends_on("py-jinja2@2.7:", when="@2.0-rc3,2.6:")
        depends_on("py-numpy@1.8.2:", when="@2.0-rc3")
        depends_on("py-py-cpuinfo@0.1.6:", when="@2.0-rc3")
        depends_on("py-pyparsing", when="@2.0-rc3,2.6:")
        depends_on("py-setuptools@6:", when="@2.0-rc3")
        depends_on("py-sympy@0.7.6:", when="@2.0-rc3")
    # END DEPENDENCIES

