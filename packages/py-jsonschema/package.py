# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJsonschema(PythonPackage):
    # BEGIN VERSIONS
    version("4.21.1", sha256="7996507afae316306f9e2290407761157c6f78002dcf7419acb99822143d1c6f", url="https://pypi.org/packages/39/9d/b035d024c62c85f2e2d4806a59ca7b8520307f34e0932fbc8cc75fe7b2d9/jsonschema-4.21.1-py3-none-any.whl")
    version("4.21.0", sha256="70a09719d375c0a2874571b363c8a24be7df8071b80c9aa76bc4551e7297c63c", url="https://pypi.org/packages/76/f4/41e31ff45e30a9ed80f3e399b23481ac3db1cb796d315bc8813716ed8d5f/jsonschema-4.21.0-py3-none-any.whl")
    version("4.20.0", sha256="ed6231f0429ecf966f5bc8dfef245998220549cbbcf140f913b7464c52c3b6b3", url="https://pypi.org/packages/0f/ed/0058234d8dd2b1fc6beeea8eab945191a05e9d391a63202f49fe23327586/jsonschema-4.20.0-py3-none-any.whl")
    version("4.19.2", sha256="eee9e502c788e89cb166d4d37f43084e3b64ab405c795c03d343a4dbc2c810fc", url="https://pypi.org/packages/ce/aa/d1bd0b5ec568a903cc3ebcb6b096ab65c1d971c8a01ca3bf3cf788c3c646/jsonschema-4.19.2-py3-none-any.whl")
    version("4.19.1", sha256="cd5f1f9ed9444e554b38ba003af06c0a8c2868131e56bfbef0550fb450c0330e", url="https://pypi.org/packages/0f/bf/a84bc75f069f4f156e1c0d9892fb7325945106c6ecaad9f29d24360872af/jsonschema-4.19.1-py3-none-any.whl")
    version("4.19.0", sha256="043dc26a3845ff09d20e4420d6012a9c91c9aa8999fa184e7efcfeccb41e32cb", url="https://pypi.org/packages/2b/ff/af59fd34bc4d7ac3e6e0cd1f3c10317d329b6c1aee179e8b24ad9a79fbac/jsonschema-4.19.0-py3-none-any.whl")
    version("4.18.6", sha256="dc274409c36175aad949c68e5ead0853aaffbe8e88c830ae66bb3c7a1728ad2d", url="https://pypi.org/packages/b5/5c/ae834dd4160bbe9a4feb6e1f3e6189ab7772408823e294bd12eb6b4b4f44/jsonschema-4.18.6-py3-none-any.whl")
    version("4.18.5", sha256="c6b4c2b83389e504717f2392adbc74bc9ed07341ae0ced18dde132f3a7f70a5b", url="https://pypi.org/packages/d3/a4/54273ac37a667c3fcf93916fda59b36f0ad79950e4e56ad839ef2e3e1159/jsonschema-4.18.5-py3-none-any.whl")
    version("4.18.4", sha256="971be834317c22daaa9132340a51c01b50910724082c2c1a2ac87eeec153a3fe", url="https://pypi.org/packages/a1/ba/28ce987450c6afa8336373761193ddaadc1ba2004fbf23a6407db036f558/jsonschema-4.18.4-py3-none-any.whl")
    version("4.18.3", sha256="aab78b34c2de001c6b692232f08c21a97b436fe18e0b817bf0511046924fceef", url="https://pypi.org/packages/3a/34/ea34f7979d4f9ed1fa3b5c66000bc4e445c570f642ad478796f5ebaae45a/jsonschema-4.18.3-py3-none-any.whl")
    version("4.17.3", sha256="a870ad254da1a8ca84b6a2905cac29d265f805acc57af304784962a2aa6508f6", url="https://pypi.org/packages/c1/97/c698bd9350f307daad79dd740806e1a59becd693bd11443a0f531e3229b3/jsonschema-4.17.3-py3-none-any.whl")
    version("4.17.1", sha256="410ef23dcdbca4eaedc08b850079179883c2ed09378bd1f760d4af4aacfa28d7", url="https://pypi.org/packages/9f/df/824fdaa0d7228fa2e8a5171a408dbabe2c66955afd5be5211725389640b5/jsonschema-4.17.1-py3-none-any.whl")
    version("4.17.0", sha256="f660066c3966db7d6daeaea8a75e0b68237a48e51cf49882087757bb59916248", url="https://pypi.org/packages/f2/c5/8e4cdbcbf81c5003a88722c34009bbda692d495dbccc2bf23edf9402d83d/jsonschema-4.17.0-py3-none-any.whl")
    version("4.16.0", sha256="9e74b8f9738d6a946d70705dc692b74b5429cd0960d58e79ffecfc43b2221eb9", url="https://pypi.org/packages/d8/ad/b96e267a185d0050ac0f128827da6f16a7fd0fd5e045294771b3c265f2e9/jsonschema-4.16.0-py3-none-any.whl")
    version("4.15.0", sha256="2df0fab225abb3b41967bb3a46fd37dc74b1536b5296d0b1c2078cd072adf0f7", url="https://pypi.org/packages/11/fe/20cbff273341943e6f9f1c5b5f7a09be9eb51cc7e169e53980292ce273a4/jsonschema-4.15.0-py3-none-any.whl")
    version("4.14.0", sha256="9892b8d630a82990521a9ca630d3446bd316b5ad54dbe981338802787f3e0d2d", url="https://pypi.org/packages/61/fe/e45dbe1cff8bbc7c84845ac4cd7c1380393d8479eb68b2392ed2ed01e1bd/jsonschema-4.14.0-py3-none-any.whl")
    version("4.13.0", sha256="870a61bb45050b81103faf6a4be00a0a906e06636ffcf0b84f5a2e51faf901ff", url="https://pypi.org/packages/e7/aa/ce2e22033d55746591c4cb7af9f6e056d8b84df98d84b3dd15304a2873cd/jsonschema-4.13.0-py3-none-any.whl")
    version("4.12.1", sha256="05f975aee3f1244a1ea0e018e8ad2672f6ca5fd1a28bc46ffc7d4b3e9896cac4", url="https://pypi.org/packages/c3/cb/e85ce855d79d72ece2636c2e1014596ee36956496de6577a5552b197d17a/jsonschema-4.12.1-py3-none-any.whl")
    version("4.12.0", sha256="157ca0686fabe326933edc1a113de238f2fcfc4320fc0eb8c096d4305cbd459a", url="https://pypi.org/packages/b7/8f/28e76c499f5da53112a595bb260f79ece83649c8093e045a4b681582f9de/jsonschema-4.12.0-py3-none-any.whl")
    version("4.11.0", sha256="2ac503b91b4a9dcf9c93764b26e926e386ec1065fec4f685c0e458a375dadedf", url="https://pypi.org/packages/df/7d/ade7c0eac18b3c55b54dc609aaa886bb1dc604b3bdde93a3c08bee847278/jsonschema-4.11.0-py3-none-any.whl")
    version("4.10.0", sha256="92128509e5b700bf0f1fd08a7d018252b16a1454465dfa6b899558eeae584241", url="https://pypi.org/packages/60/17/8c0f01efcde8920ab6e4e5ec01e19056dc7fa00aebeeae8b6423b736696f/jsonschema-4.10.0-py3-none-any.whl")
    version("4.4.0", sha256="77281a1f71684953ee8b3d488371b162419767973789272434bbc3f29d9c8823", url="https://pypi.org/packages/55/b2/2c4af6a97c3f12c6d5a72b41d328c3996e14e1e46701df3fac1ed65119c9/jsonschema-4.4.0-py3-none-any.whl")
    version("3.2.0", sha256="4e5b3cf8216f577bee9ce139cbe72eca3ea4f292ec60928ff24758ce626cd163", url="https://pypi.org/packages/c5/8f/51e89ce52a085483359217bc72cdbf6e75ee595d5b1d4b5ade40c7e018b8/jsonschema-3.2.0-py2.py3-none-any.whl")
    version("3.1.1", sha256="94c0a13b4a0616458b42529091624e66700a17f847453e52279e35509a5b7631", url="https://pypi.org/packages/ce/6c/888d7c3c1fce3974c88a01a6bc553528c99d3586e098eee23e8383dd11c3/jsonschema-3.1.1-py2.py3-none-any.whl")
    version("3.1.0", sha256="4f4ddc3d51f33a5363c042dc62c85010e9e3b8353bcf108afff394dde70854b3", url="https://pypi.org/packages/11/9c/a0a2c70be340603c8ff5a692a8e6a4997fb858c7fd8701ff2afe087a3b58/jsonschema-3.1.0-py2.py3-none-any.whl")
    version("3.0.2", sha256="5f9c0a719ca2ce14c5de2fd350a64fd2d13e8539db29836a86adc990bb1a068f", url="https://pypi.org/packages/54/48/f5f11003ceddcd4ad292d4d9b5677588e9169eef41f88e38b2888e7ec6c4/jsonschema-3.0.2-py2.py3-none-any.whl")
    version("3.0.1", sha256="a5f6559964a3851f59040d3b961de5e68e70971afb88ba519d27e6a039efff1a", url="https://pypi.org/packages/aa/69/df679dfbdd051568b53c38ec8152a3ab6bc533434fc7ed11ab034bf5e82f/jsonschema-3.0.1-py2.py3-none-any.whl")
    version("3.0.0", sha256="dd3f8ecb1b52d94d45eedb67cb86cac57b94ded562c5d98f63719e55ce58557b", url="https://pypi.org/packages/cd/e6/be1b2a6ebebdaf1f790f1e750bb720fbda0335c2a19601ea9d8bb5059f38/jsonschema-3.0.0-py2.py3-none-any.whl")
    version("2.6.0", sha256="000e68abd33c972a5248544925a0cae7d1125f9bf6c58280d37546b946769a08", url="https://pypi.org/packages/77/de/47e35a97b2b05c2fadbec67d44cfcdcd09b8086951b331d82de90d2912da/jsonschema-2.6.0-py2.py3-none-any.whl")
    version("2.5.1", sha256="71e7b3bcf9fca408bcb65bb60892f375d3abdd2e4f296eeeb8fe0bbbfcde598e", url="https://pypi.org/packages/bd/cc/5388547ea3504bd8cbf99ba2ae7a3231598f54038e9b228cbd174f8ec6a1/jsonschema-2.5.1-py2.py3-none-any.whl")
    version("2.5.0", sha256="d3daa59dc98bf8cbad0d8c18a751a739fb752461c509597598cf2d9595702c65", url="https://pypi.org/packages/7b/ba/139de79e48de67999ac3b0de5503fd46dbe11d105b70c3611b1538f61fb5/jsonschema-2.5.0.zip")
    version("2.4.0", sha256="5af36686c271097f25ec023546c397cb99bc67a5db3836e52e6b37bdb45ca21e", url="https://pypi.org/packages/5e/55/9e973774cb3a47d0d025fc9626c8cff96b104e3764493f91b49fa125d8ec/jsonschema-2.4.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("format", default=False)
    variant("format-nongpl", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-attrs@22.2:", when="@4.18:")
        depends_on("py-attrs@17.4:", when="@3.0.0-alpha4:4.17")
        depends_on("py-fqdn", when="@4:+format-nongpl")
        depends_on("py-fqdn", when="@4:+format")
        depends_on("py-functools32", when="@2.5:2.5.0")
        depends_on("py-idna", when="@3.2:+format-nongpl")
        depends_on("py-idna", when="@3.0.0-alpha4:+format")
        depends_on("py-importlib-metadata", when="@3.1")
        depends_on("py-importlib-resources@1.4:", when="@4.2.1: ^python@:3.8")
        depends_on("py-isoduration", when="@4.0.0-alpha3:+format-nongpl")
        depends_on("py-isoduration", when="@4.0.0-alpha3:+format")
        depends_on("py-js-regex@1:", when="@3.1:3.1.0")
        depends_on("py-jsonpointer@1.14:", when="@3.2:+format-nongpl")
        depends_on("py-jsonpointer@1.14:", when="@3.0.0-alpha4:+format")
        depends_on("py-jsonschema-specifications@2023.3.6:", when="@4.18.0-alpha3:")
        depends_on("py-pkgutil-resolve-name@1.3:", when="@4.9: ^python@:3.8")
        depends_on("py-pyrsistent@0.14:0.16,0.17.3:", when="@4.0.0-alpha3:4.17")
        depends_on("py-pyrsistent@0.14:", when="@3.0.0-alpha4:4.0.0-alpha2")
        depends_on("py-referencing@0.28.4:", when="@4.18.0-alpha8:")
        depends_on("py-rfc3339-validator", when="@4.0.0-alpha6:+format")
        depends_on("py-rfc3339-validator", when="@3.2:+format-nongpl")
        depends_on("py-rfc3986-validator@0.1.1:", when="@3.2:+format-nongpl")
        depends_on("py-rfc3987", when="@2.5,3.0.0-alpha4:+format")
        depends_on("py-rpds-py@0.7.1:", when="@4.18.0-alpha3:")
        depends_on("py-setuptools", when="@3.0.0-alpha4:3")
        depends_on("py-six@1.11:", when="@3.0.0-alpha4:3")
        depends_on("py-strict-rfc3339", when="@2.5,3.0.0-alpha4:4.0.0-alpha5+format")
        depends_on("py-uri-template", when="@4.0.0-alpha2:+format-nongpl")
        depends_on("py-uri-template", when="@4.0.0-alpha2:+format")
        depends_on("py-webcolors@1.11:", when="@4.0.0-alpha6:+format-nongpl")
        depends_on("py-webcolors@1.11:", when="@4.0.0-alpha6:+format")
        depends_on("py-webcolors", when="@3.2:4.0.0-alpha5+format-nongpl")
        depends_on("py-webcolors", when="@2.5,3.0.0-alpha4:4.0.0-alpha5+format")
    # END DEPENDENCIES

