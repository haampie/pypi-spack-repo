# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyScipy(PythonPackage):
    # BEGIN VERSIONS
    version("1.11.4", sha256="90a2b78e7f5733b9de748f589f09225013685f9b218275257f8a8168ededaeaa", url="https://pypi.org/packages/6e/1f/91144ba78dccea567a6466262922786ffc97be1e9b06ed9574ef0edc11e1/scipy-1.11.4.tar.gz")
    version("1.11.3", sha256="bba4d955f54edd61899776bad459bf7326e14b9fa1c552181f0479cc60a568cd", url="https://pypi.org/packages/39/7b/9f265b7f074195392e893a5cdc66116c2f7a31fd5f3d9cceff661ec6df82/scipy-1.11.3.tar.gz")
    version("1.11.2", sha256="b29318a5e39bd200ca4381d80b065cdf3076c7d7281c5e36569e99273867f61d", url="https://pypi.org/packages/9c/ef/87a5565907645998d7c62e76b84b0ca9f0b7c25cd433f5617a968051cec3/scipy-1.11.2.tar.gz")
    version("1.11.1", sha256="fb5b492fa035334fd249f0973cc79ecad8b09c604b42a127a677b45a9a3d4289", url="https://pypi.org/packages/a6/98/fceb84466a74b8fe74ce2dcc3a0a89cb7b4a689d4775e0fb4c95f335ef6a/scipy-1.11.1.tar.gz")
    version("1.11.0", sha256="f9b0248cb9d08eead44cde47cbf6339f1e9aa0dfde28f5fb27950743e317bd5d", url="https://pypi.org/packages/fa/d0/724c8204f87b6f807e3e67de32b8b4922d579154a448ce94e89129064bf1/scipy-1.11.0.tar.gz")
    version("1.10.1", sha256="2cf9dfb80a7b4589ba4c40ce7588986d6d5cebc5457cad2c2880f6bc2d42f3a5", url="https://pypi.org/packages/84/a9/2bf119f3f9cff1f376f924e39cfae18dec92a1514784046d185731301281/scipy-1.10.1.tar.gz")
    version("1.10.0", sha256="c8b3cbc636a87a89b770c6afc999baa6bcbb01691b5ccbbc1b1791c7c0a07540", url="https://pypi.org/packages/d6/bd/2d13a273d95f7b7d9903c906c486040b0aebb85e008f93a5dd0891f21f1f/scipy-1.10.0.tar.gz")
    version("1.9.3", sha256="fbc5c05c85c1a02be77b1ff591087c83bc44579c6d2bd9fb798bb64ea5e1a027", url="https://pypi.org/packages/0a/2e/44795c6398e24e45fa0bb61c3e98de1cfea567b1b51efd3751e2f7ff9720/scipy-1.9.3.tar.gz")
    version("1.9.2", sha256="99e7720caefb8bca6ebf05c7d96078ed202881f61e0c68bd9e0f3e8097d6f794", url="https://pypi.org/packages/17/07/68df07679ec4a4a24bff00147a14908aa73e9e8912d142886e8d0e1e3d64/scipy-1.9.2.tar.gz")
    version("1.9.1", sha256="26d28c468900e6d5fdb37d2812ab46db0ccd22c63baa095057871faa3a498bc9", url="https://pypi.org/packages/db/af/16906139f52bc6866c43401869ce247662739ad71afa11c6f18505eb0546/scipy-1.9.1.tar.gz")
    version("1.9.0", sha256="c0dfd7d2429452e7e94904c6a3af63cbaa3cf51b348bd9d35b42db7e9ad42791", url="https://pypi.org/packages/a8/e3/4ec401f609d34162b7023a09165da491630879e4cfa2336667fe2102cd06/scipy-1.9.0.tar.gz")
    version("1.8.1", sha256="9e3fb1b0e896f14a85aa9a28d5f755daaeeb54c897b746df7a55ccb02b340f33", url="https://pypi.org/packages/26/b5/9330f004b9a3b2b6a31f59f46f1617ce9ca15c0e7fe64288c20385a05c9d/scipy-1.8.1.tar.gz")
    version("1.8.0", sha256="31d4f2d6b724bc9a98e527b5849b8a7e589bf1ea630c33aa563eda912c9ff0bd", url="https://pypi.org/packages/b4/a2/4faa34bf0cdbefd5c706625f1234987795f368eb4e97bde9d6f46860843e/scipy-1.8.0.tar.gz")
    version("1.7.3", sha256="ab5875facfdef77e0a47d5fd39ea178b58e60e454a4c85aa1e52fcb80db7babf", url="https://pypi.org/packages/61/67/1a654b96309c991762ee9bc39c363fc618076b155fe52d295211cf2536c7/scipy-1.7.3.tar.gz")
    version("1.7.2", sha256="fa2dbabaaecdb502641b0b3c00dec05fb475ae48655c66da16c9ed24eda1e711", url="https://pypi.org/packages/0e/23/58c4f995475a2a97cb5f4a032aedaf881ad87cd976a7180c55118d105a1d/scipy-1.7.2.tar.gz")
    version("1.7.1", sha256="6b47d5fa7ea651054362561a28b1ccc8da9368a39514c1bbf6c0977a1c376764", url="https://pypi.org/packages/47/33/a24aec22b7be7fdb10ec117a95e1e4099890d8bbc6646902f443fc7719d1/scipy-1.7.1.tar.gz")
    version("1.7.0", sha256="998c5e6ea649489302de2c0bc026ed34284f531df89d2bdc8df3a0d44d165739", url="https://pypi.org/packages/bb/bb/944f559d554df6c9adf037aa9fc982a9706ee0e96c0d5beac701cb158900/scipy-1.7.0.tar.gz")
    version("1.6.3", sha256="a75b014d3294fce26852a9d04ea27b5671d86736beb34acdfc05859246260707", url="https://pypi.org/packages/fe/fd/8704c7b7b34cdac850485e638346025ca57c5a859934b9aa1be5399b33b7/scipy-1.6.3.tar.gz")
    version("1.6.2", sha256="e9da33e21c9bc1b92c20b5328adb13e5f193b924c9b969cd700c8908f315aa59", url="https://pypi.org/packages/99/f1/c00d6be56e1a718a3068079e3ec8ce044d7179345280f6a3f5066068af0d/scipy-1.6.2.tar.gz")
    version("1.6.1", sha256="c4fceb864890b6168e79b0e714c585dbe2fd4222768ee90bc1aa0f8218691b11", url="https://pypi.org/packages/26/68/84dbe18583e79e56e4cee8d00232a8dd7d4ae33bc3acf3be1c347991848f/scipy-1.6.1.tar.gz")
    version("1.6.0", sha256="cb6dc9f82dfd95f6b9032a8d7ea70efeeb15d5b5fd6ed4e8537bb3c673580566", url="https://pypi.org/packages/16/48/ff7026d26dfd92520f00b109333e22c05a235f0c9115a5a2d7679cdf39ef/scipy-1.6.0.tar.gz")
    version("1.5.4", sha256="4a453d5e5689de62e5d38edf40af3f17560bfd63c9c5bd228c18c1f99afa155b", url="https://pypi.org/packages/aa/d5/dd06fe0e274e579e1dff21aa021219c039df40e39709fabe559faed072a5/scipy-1.5.4.tar.gz")
    version("1.5.3", sha256="ddae76784574cc4c172f3d5edd7308be16078dd3b977e8746860c76c195fa707", url="https://pypi.org/packages/93/63/4a566494594a13697c5d5d8a754d6e329d018ddf881520775e0229fa29ef/scipy-1.5.3.tar.gz")
    version("1.5.2", sha256="066c513d90eb3fd7567a9e150828d39111ebd88d3e924cdfc9f8ce19ab6f90c9", url="https://pypi.org/packages/53/10/776750d57ade26522478a92a2e14035868624a6a62f4157b0cc5abd4a980/scipy-1.5.2.tar.gz")
    version("1.5.1", sha256="039572f0ca9578a466683558c5bf1e65d442860ec6e13307d528749cfe6d07b8", url="https://pypi.org/packages/8a/6c/7777c60626cf620ce24d6349af69f3d2a4f298729d688cc4cd9528ae3c61/scipy-1.5.1.tar.gz")
    version("1.5.0", sha256="4ff72877d19b295ee7f7727615ea8238f2d59159df0bdd98f91754be4a2767f0", url="https://pypi.org/packages/fd/bd/86b03ed778e0428db4fec584ee43846d1017c46425679b45869a7c5fc021/scipy-1.5.0.tar.gz")
    version("1.4.1", sha256="dee1bbf3a6c8f73b6b218cb28eed8dd13347ea2f87d572ce19b289d6fd3fbc59", url="https://pypi.org/packages/04/ab/e2eb3e3f90b9363040a3d885ccc5c79fe20c5b8a3caa8fe3bf47ff653260/scipy-1.4.1.tar.gz")
    version("1.4.0", sha256="31f7cfa93b01507c935c12b535e24812594002a02a56803d7cd063e9920d25e8", url="https://pypi.org/packages/48/74/ed053620f675ce5408b8dda34949fdc403e5f40db779c07a4436631dcbfb/scipy-1.4.0.tar.gz")
    version("1.3.3", sha256="64bf4e8ae0db2d42b58477817f648d81e77f0b381d0ea4427385bba3f959380a", url="https://pypi.org/packages/a7/5c/495190b8c7cc71977c3d3fafe788d99d43eeb4740ac56856095df6a23fbd/scipy-1.3.3.tar.gz")
    version("1.3.2", sha256="a03939b431994289f39373c57bbe452974a7da724ae7f9620a1beee575434da4", url="https://pypi.org/packages/df/20/2f147945396fa74b467d696e42aa55eb603d166490a8ebe4d79e54c793df/scipy-1.3.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.11.4:")
        depends_on("python@3.9:3.12", when="@1.11:1.11.3")
        depends_on("python@3.8:", when="@1.9.0-rc3:1.9")
        depends_on("python@3.8:3.11", when="@1.9:1.9.0-rc2,1.10")
        depends_on("python@3.8:3.10", when="@1.8")
        depends_on("python@3.7:", when="@1.6:1.6.1")
        depends_on("python@3.7:3.10", when="@1.7.2:1.7")
        depends_on("python@3.7:3.9", when="@1.6.2:1.7.1")
        depends_on("py-numpy@1.21.6:1", when="@1.11")
        depends_on("py-numpy@1.19.5:1", when="@1.10")
        depends_on("py-numpy@1.18.5:1.25", when="@1.9")
        depends_on("py-numpy@1.14.5:", when="@1.5:1.5.1")
        depends_on("py-numpy@1.13.3:", when="@1.3:1.4")
    # END DEPENDENCIES

