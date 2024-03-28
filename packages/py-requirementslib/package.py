# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRequirementslib(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.0.0", sha256="67b42903d7c32f89c7047d1020c619d37cb515c475a4ae6f4e5683e1c56d7bf7", url="https://pypi.org/packages/8a/6e/2d0c72c224f760d49e954f6c0eb5e4075b589c7e99e895ba0b250dc6e469/requirementslib-3.0.0-py2.py3-none-any.whl")
    version("2.3.0", sha256="04782a1dd69668b633a981c6e3013c0daa37b612feb0c7cba76080ff1d5fc7c3", url="https://pypi.org/packages/d7/8a/8ad519e00450cdb83615c3736daa3a8185a30281b75fa2412574d27f9d6b/requirementslib-2.3.0-py2.py3-none-any.whl")
    version("2.2.6", sha256="2c03b9a9e4125729d987915d06244b546de0db0835a08b7ad270fd837233b338", url="https://pypi.org/packages/2d/e6/9089c350bd9ca8163c4707d63a38447f08b6a207ac3e41f708b8acd7652a/requirementslib-2.2.6-py2.py3-none-any.whl")
    version("2.2.5", sha256="5447bee24d500fd91574bbe239da241d879208de63ead941b31526811db71fd1", url="https://pypi.org/packages/61/d5/317b857d0433c5f6c6cf1cbe4f2f23fca017804fce9ea744f2c93ba4cc20/requirementslib-2.2.5-py2.py3-none-any.whl")
    version("2.2.4", sha256="1c9a7692d07fe05f9400acae5059af7c37589eea8db4374a50439a79074d0f7a", url="https://pypi.org/packages/fe/17/23fbce0797f6c2219b08a1166d88c2ea8e2703040982c2b8d8177437c90d/requirementslib-2.2.4-py2.py3-none-any.whl")
    version("2.2.3", sha256="6f8184757a59357fb87c8357beabd1af9f5e8d7556b56f3092ba964fdcb7e9a5", url="https://pypi.org/packages/4c/17/1a7e9b576797648b8f44c331dac8d72ec4b9e4958efa2364e3ba8c37dac7/requirementslib-2.2.3-py2.py3-none-any.whl")
    version("2.2.2", sha256="4e0e8b2a1cf7fcdf690c37b3b89c654f20c200f85da78b74028963541c8dcf2e", url="https://pypi.org/packages/0c/36/18833128c6a894add409ecaad06071a11e12b5eba48bc3f3315634409cfd/requirementslib-2.2.2-py2.py3-none-any.whl")
    version("2.2.1", sha256="0607e330a65385a556e76c6fb31567a3053f53a081c46c690dadc800f7fc9d5d", url="https://pypi.org/packages/5c/2f/1465db7c28ab78a26faa88100b9bb98ec7196f57a5523623c7a3eb7d648d/requirementslib-2.2.1-py2.py3-none-any.whl")
    version("2.2.0", sha256="b8fcc5402bcb3dcc66d4f9e86735b318f1285e7c4cd7dd67edb60affd2cccead", url="https://pypi.org/packages/66/72/7caed0b2301cfa33ec9736d73ae93510613d32666754b6942b039cf6825a/requirementslib-2.2.0-py2.py3-none-any.whl")
    version("2.1.0", sha256="09f86c3ed61b3fe65b7c2c6afae4e6266f0099841118cf51af455b58bb1cad06", url="https://pypi.org/packages/3d/f8/c536312c556d507d9ae3414588971482520367aadf4c28a86896c4f15392/requirementslib-2.1.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-attrs@19.2:", when="@1.5.16:2.3.0")
        depends_on("py-cached-property", when="@1.4.1:2.2.5")
        depends_on("py-distlib@0.2.8:", when="@1.3.2:")
        depends_on("py-pep517@0.5:", when="@1.5:")
        depends_on("py-pip@23.1:", when="@2.2.5:")
        depends_on("py-pip@22.2:", when="@2:2.2.4")
        depends_on("py-platformdirs", when="@1.6:")
        depends_on("py-plette+validation", when="@1.1.7:")
        depends_on("py-pydantic", when="@2.3.1:")
        depends_on("py-requests", when="@1.1:")
        depends_on("py-setuptools@40.8:", when="@1.4.1:")
        depends_on("py-tomlkit@0.5.3:", when="@1.4.1:")
        depends_on("py-vistir@0.8:", when="@2.2.4:2.2.5")
        depends_on("py-vistir@0.7.5:0.7", when="@2.2.1:2.2.3")
        depends_on("py-vistir@0.7.4", when="@2.2:2.2.0")
        depends_on("py-vistir@0.6.1:0.6", when="@2.0.1:2.1")
    # END DEPENDENCIES

