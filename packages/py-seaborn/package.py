# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySeaborn(PythonPackage):
    # BEGIN VERSIONS
    version("0.13.2", sha256="636f8336facf092165e27924f223d3c62ca560b1f2bb5dff7ab7fad265361987", url="https://pypi.org/packages/83/11/00d3c3dfc25ad54e731d91449895a79e4bf2384dc3ac01809010ba88f6d5/seaborn-0.13.2-py3-none-any.whl")
    version("0.12.2", sha256="ebf15355a4dba46037dfd65b7350f014ceb1f13c05e814eda2c9f5fd731afc08", url="https://pypi.org/packages/8f/2e/17bbb83fbf102687bb2aa3d808add39da820a7698159302a1a69bb82e01c/seaborn-0.12.2-py3-none-any.whl")
    version("0.12.0", sha256="cbeff3deef7c2515aa0af99b2c7e02dc5bf8b42c936a74d8e4b416905b549db0", url="https://pypi.org/packages/c2/03/14991c1f18422eb640f6fe6eadf9a675bb21d9339236d64c3d12bd0eb1a4/seaborn-0.12.0-py3-none-any.whl")
    version("0.11.2", sha256="85a6baa9b55f81a0623abddc4a26b334653ff4c6b18c418361de19dbba0ef283", url="https://pypi.org/packages/10/5b/0479d7d845b5ba410ca702ffcd7f2cd95a14a4dfff1fde2637802b258b9b/seaborn-0.11.2-py3-none-any.whl")
    version("0.11.1", sha256="4e1cce9489449a1c6ff3c567f2113cdb41122f727e27a984950d004a88ef3c5c", url="https://pypi.org/packages/68/ad/6c2406ae175f59ec616714e408979b674fe27b9587f79d59a528ddfbcd5b/seaborn-0.11.1-py3-none-any.whl")
    version("0.9.0", sha256="42e627b24e849c2d3bbfd059e00005f6afbc4a76e4895baf44ae23fe8a4b09a5", url="https://pypi.org/packages/a8/76/220ba4420459d9c4c9c9587c6ce607bf56c25b3d3d2de62056efe482dadc/seaborn-0.9.0-py3-none-any.whl")
    version("0.7.1", sha256="fa274344b1ee72f723bab751c40a5c671801d47a29ee9b5e69fcf63a18ce5c5d", url="https://pypi.org/packages/ed/dc/f168ff9db34f8c03c568987b4f81603cd3df40dd8043722d526026381a91/seaborn-0.7.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("stats", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-matplotlib@3.4.0:3.6.0,3.6.2:", when="@0.13.1:")
        depends_on("py-matplotlib@3.1.0:3.6.0,3.6.2:", when="@0.12.1:0.12")
        depends_on("py-matplotlib@3.1.0:", when="@0.12:0.12.0")
        depends_on("py-matplotlib@2.2.0:", when="@0.11")
        depends_on("py-matplotlib@1.4.3:", when="@0.9:0.9.0")
        depends_on("py-numpy@1.20.0:1.24.0-rc2,1.24.1:", when="@0.13:")
        depends_on("py-numpy@1.17.0:1.24.0-rc2,1.24.1:", when="@0.12.2:0.12")
        depends_on("py-numpy@1.17.0:", when="@0.12:0.12.1")
        depends_on("py-numpy@1.15.0:", when="@0.11")
        depends_on("py-numpy@1.9.3:", when="@0.9:0.9.0")
        depends_on("py-pandas@1.2.0:", when="@0.13:")
        depends_on("py-pandas@0.25.0:", when="@0.12")
        depends_on("py-pandas@0.23.0:", when="@0.11")
        depends_on("py-pandas@0.15.2:", when="@0.9:0.9.0")
        depends_on("py-scipy@1.7.0:", when="@0.13:+stats")
        depends_on("py-scipy@1.3.0:", when="@0.12.0-rc0:0.12+stats")
        depends_on("py-scipy@1.0.0:", when="@0.11")
        depends_on("py-scipy@0.14:", when="@0.9:0.9.0")
        depends_on("py-statsmodels@0.12.0:", when="@0.13:+stats")
        depends_on("py-statsmodels@0.10.0:", when="@0.12.0-rc0:0.12+stats")
    # END DEPENDENCIES

