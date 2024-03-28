# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMypy(PythonPackage):
    # BEGIN VERSIONS
    version("1.9.0", sha256="3cc5da0127e6a478cddd906068496a97a7618a21ce9b54bde5bf7e539c7af974", url="https://pypi.org/packages/72/1e/a587a862c766a755a58b62d8c00aed11b74a15dc415c1bf5da7b607b0efd/mypy-1.9.0.tar.gz")
    version("1.8.0", sha256="6ff8b244d7085a0b425b56d327b480c3b29cafbd2eff27316a004f9a7391ae07", url="https://pypi.org/packages/16/22/25fac51008f0a4b2186da0dba3039128bd75d3fab8c07acd3ea5894f95cc/mypy-1.8.0.tar.gz")
    version("1.7.1", sha256="fcb6d9afb1b6208b4c712af0dafdc650f518836065df0d4fb1d800f5d6773db2", url="https://pypi.org/packages/ae/30/05a7c016431b3fdbaf0bcf663aee7c5e4b3d2293cd4e0568140cecae4967/mypy-1.7.1.tar.gz")
    version("1.7.0", sha256="1e280b5697202efa698372d2f39e9a6713a0395a756b1c6bd48995f8d72690dc", url="https://pypi.org/packages/71/c8/dd3bee454333df813c97938a64c516e838ca5bc17ef35a74ceeb0f31869d/mypy-1.7.0.tar.gz")
    version("1.6.1", sha256="4d01c00d09a0be62a4ca3f933e315455bde83f37f892ba4b08ce92f3cf44bcc1", url="https://pypi.org/packages/50/f8/0a8d4d8781b41b445534bc4f9210b7793bf0ab52aacfd06ebd2699663e2c/mypy-1.6.1.tar.gz")
    version("1.6.0", sha256="4f3d27537abde1be6d5f2c96c29a454da333a2a271ae7d5bc7110e6d4b7beb3f", url="https://pypi.org/packages/f0/d2/28b0e3f058c2950236d176e93167f0b503bd2e4e4cbd54e306d3c95d413f/mypy-1.6.0.tar.gz")
    version("1.5.1", sha256="b031b9601f1060bf1281feab89697324726ba0c0bae9d7cd7ab4b690940f0b92", url="https://pypi.org/packages/33/f9/c84b68e4a754f5ce200dcf0786aa489164fa9d9dee84e375bd7d99caf637/mypy-1.5.1.tar.gz")
    version("1.5.0", sha256="f3460f34b3839b9bc84ee3ed65076eb827cd99ed13ed08d723f9083cada4a212", url="https://pypi.org/packages/a0/02/865c2fb735f08eb8068d54dc88d7544477f9ea792f6145eeedbe0e847df9/mypy-1.5.0.tar.gz")
    version("1.4.1", sha256="9bbcd9ab8ea1f2e1c8031c21445b511442cc45c89951e49bbf852cbb70755b1b", url="https://pypi.org/packages/b3/28/d8a8233ff167d06108e53b7aefb4a8d7350adbbf9d7abd980f17fdb7a3a6/mypy-1.4.1.tar.gz")
    version("1.4.0", sha256="de1e7e68148a213036276d1f5303b3836ad9a774188961eb2684eddff593b042", url="https://pypi.org/packages/1b/49/c5c7b9445ee563e09e71382e7fb147480fb85fa2356846488114f61549f8/mypy-1.4.0.tar.gz")
    version("1.3.0", sha256="e1f4d16e296f5135624b34e8fb741eb0eadedca90862405b1f1fde2040b9bd11", url="https://pypi.org/packages/f9/88/3bfe07521fb9e74b449cbc4367434067ec70bfd8a24c652fa3e0f9597389/mypy-1.3.0.tar.gz")
    version("1.2.0", sha256="f70a40410d774ae23fcb4afbbeca652905a04de7948eaf0b1789c8d1426b72d1", url="https://pypi.org/packages/9a/d0/d96d26e7a6f5a2ed4add8c649f30bce26fc413f25a6ecc5d93ab22c270e1/mypy-1.2.0.tar.gz")
    version("1.1.1", sha256="ae9ceae0f5b9059f33dbc62dea087e942c0ccab4b7a003719cb70f9b8abfa32f", url="https://pypi.org/packages/62/54/be80f8d01f5cf72f774a77f9f750527a6fa733f09f78b1da30e8fa3914e6/mypy-1.1.1.tar.gz")
    version("1.0.1", sha256="28cea5a6392bb43d266782983b5a4216c25544cd7d80be681a155ddcdafd152d", url="https://pypi.org/packages/52/56/afddb0a1654cf7f192419fbd9e46e01bceb11b1a6778a9d4257387f71dd8/mypy-1.0.1.tar.gz")
    version("1.0.0", sha256="f34495079c8d9da05b183f9f7daec2878280c2ad7cc81da686ef0b484cea2ecf", url="https://pypi.org/packages/1d/06/9a40050ef10f0e9ddfd667f29e98dd650db31612128e3e8925cda6621944/mypy-1.0.0.tar.gz")
    version("0.991", sha256="3c0165ba8f354a6d9881809ef29f1a9318a236a6d81c690094c5df32107bde06", url="https://pypi.org/packages/0e/5c/fbe112ca73d4c6a9e65336f48099c60800514d8949b4129c093a84a28dc8/mypy-0.991.tar.gz")
    version("0.990", sha256="72382cb609142dba3f04140d016c94b4092bc7b4d98ca718740dc989e5271b8d", url="https://pypi.org/packages/96/43/f50e6a373ef3402616ef65e450e5a1ceac0073b0a3ebefb4472e257152d4/mypy-0.990.tar.gz")
    version("0.982", sha256="85f7a343542dc8b1ed0a888cdd34dca56462654ef23aa673907305b260b3d746", url="https://pypi.org/packages/0d/75/a1ec1af4153f7b7ae825705ada667bf445418277153c76972ba0ad782bb9/mypy-0.982.tar.gz")
    version("0.981", sha256="ad77c13037d3402fbeffda07d51e3f228ba078d1c7096a73759c9419ea031bf4", url="https://pypi.org/packages/98/d1/39861ecddba2616663f3cb52920fd70c465867b8cfe858d377fac0dd1b4b/mypy-0.981.tar.gz")
    version("0.971", sha256="40b0f21484238269ae6a57200c807d80debc6459d444c0489a102d7c6a75fa56", url="https://pypi.org/packages/5e/66/00f7f751140fe6953603fb0cd56dee0314842cfe358884ca3025589ca81c/mypy-0.971.tar.gz")
    version("0.961", sha256="f730d56cb924d371c26b8eaddeea3cc07d78ff51c521c6d04899ac6904b75492", url="https://pypi.org/packages/67/48/e73045183ce9824d98365f18255a79d0b01638f40a0a68f898dc8f3cebcc/mypy-0.961.tar.gz")
    version("0.960", sha256="d4fccf04c1acf750babd74252e0f2db6bd2ac3aa8fe960797d9f3ef41cf2bfd4", url="https://pypi.org/packages/22/22/49792504e249a774554cd473e69af411a62c7d0591651104538fbcdaec10/mypy-0.960.tar.gz")
    version("0.950", sha256="1b333cfbca1762ff15808a0ef4f71b5d3eed8528b23ea1c3fb50543c867d68de", url="https://pypi.org/packages/73/ef/a3b56028305971a7130992702097e6cde5dcfa2ee01fd5f0d66880cce012/mypy-0.950.tar.gz")
    version("0.942", sha256="17e44649fec92e9f82102b48a3bf7b4a5510ad0cd22fa21a104826b5db4903e2", url="https://pypi.org/packages/e3/7b/3fa271e904b0e8689fb0f0083a43a8bf84b9b47b8f3f5a36e0ee2c064eb4/mypy-0.942.tar.gz")
    version("0.941", sha256="cbcc691d8b507d54cb2b8521f0a2a3d4daa477f62fe77f0abba41e5febb377b7", url="https://pypi.org/packages/3e/9f/9f408ca2ed4004e4303649087449556db769b341390dbc21a6075f02bc7d/mypy-0.941.tar.gz")
    version("0.940", sha256="71bec3d2782d0b1fecef7b1c436253544d81c1c0e9ca58190aed9befd8f081c5", url="https://pypi.org/packages/02/7e/fb5618b53809c4c5736465eeea89bd3517f10d9e88d8f6533a7286ef15ea/mypy-0.940.tar.gz")
    version("0.931", sha256="0038b21890867793581e4cb0d810829f5fd4441aa75796b53033af3aa30430ce", url="https://pypi.org/packages/4b/b2/9c71fd84086e96518b1d7a940788d704d3a67aead3e3a7ff9bf8e9b5746d/mypy-0.931.tar.gz")
    version("0.930", sha256="51426262ae4714cc7dd5439814676e0992b55bcc0f6514eccb4cf8e0678962c2", url="https://pypi.org/packages/8e/79/116f9828cfb88904c94640c683ca1f24d9abc89c688e31d436eba82e09a1/mypy-0.930.tar.gz")
    version("0.921", sha256="eca089d7053dff45d6dcd5bf67f1cabc311591e85d378917d97363e7c13da088", url="https://pypi.org/packages/4e/a2/686871fae023daa8c2ac04f01c4a4c730761561adf25cf7a997f10899f44/mypy-0.921.tar.gz")
    version("0.920", sha256="a55438627f5f546192f13255a994d6d1cf2659df48adcf966132b4379fd9c86b", url="https://pypi.org/packages/d4/0f/3c74d419a1d2e1c683cc174b8a0fac36dfb0d14c8b9b28905e1ca401ec03/mypy-0.920.tar.gz")
    version("0.910", sha256="704098302473cb31a218f1775a873b376b30b4c18229421e9e9dc8916fd16150", url="https://pypi.org/packages/33/46/b5d01f8844c84772e950bfc6adcaaa94cd22fedeb7c01776fd6effb3c2f6/mypy-0.910.tar.gz")
    version("0.900", sha256="65c78570329c54fb40f956f7645e2359af5da9d8c54baa44f461cdc7f4984108", url="https://pypi.org/packages/a9/f3/13ca053f0c938873380679199e86427b27600992f19376a6b11dfe12207c/mypy-0.900.tar.gz")
    version("0.800", sha256="e0202e37756ed09daf4b0ba64ad2c245d357659e014c3f51d8cd0681ba66940a", url="https://pypi.org/packages/80/5b/8b3ed91920fe20ffa4b6473966b4a98e9759f7245e2232faf29c6c56d150/mypy-0.800.tar.gz")
    version("0.790", sha256="2b21ba45ad9ef2e2eb88ce4aeadd0112d0f5026418324176fd494a6824b74975", url="https://pypi.org/packages/17/42/cb8f0c1d8191bee469538ccc901c07d0ba1c545a84ea85da82f45c669a41/mypy-0.790.tar.gz")
    version("0.740", sha256="48c8bc99380575deb39f5d3400ebb6a8a1cb5cc669bbba4d3bb30f904e0a0e7d", url="https://pypi.org/packages/af/38/7f4f8a52b6062d63193cdb86b17757e8668367cca7ddae08be99ab98fafc/mypy-0.740.tar.gz")
    version("0.670", sha256="308c274eb8482fbf16006f549137ddc0d69e5a589465e37b99c4564414363ca7", url="https://pypi.org/packages/88/11/8092fdd9cf4c507e6c799bf663e713a5418beb9fda422df810f72641224c/mypy-0.670-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-mypy-extensions@1:", when="@1.6:")
        depends_on("py-mypy-extensions@0.4:0", when="@0.630:0.650,0.670:0.750")
        depends_on("py-psutil@5.4", when="@0.550:0.560")
        depends_on("py-tomli@1.1:", when="@1.6: ^python@:3.10")
        depends_on("py-typed-ast@1.4", when="@0.710:0.782")
        depends_on("py-typed-ast@1.3.1:1.3", when="@0.670:0.701")
        depends_on("py-typing-extensions@4.1:", when="@1.6:")
        depends_on("py-typing-extensions@3.7.4:", when="@0.720:0.782")
    # END DEPENDENCIES

