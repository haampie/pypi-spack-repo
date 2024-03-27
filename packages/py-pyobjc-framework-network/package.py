##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkNetwork(PythonPackage):
    version("10.2", sha256="b39bc26f89cf9fc56cc9c4a99099aef68c388d45b62dc1ec16772ee290b225d4", url="https://pypi.org/packages/a6/1e/0cea1fa634e05a1488cdee39c8a4e00cf55a2fef0b30dc089b48bbcf2cc8/pyobjc-framework-Network-10.2.tar.gz")
    version("10.1", sha256="39c02fdcac4e487e14296f5d60458b9a0cd58c2a830591a7cfacc0bca191e03f", url="https://pypi.org/packages/e0/2a/862a89d588070954c585c30d36c588d13197a82ebba7b430082e450775d3/pyobjc-framework-Network-10.1.tar.gz")
    version("10.0", sha256="4e92b1271f999dea0297a844cc101b5c0c908168428d77caab054d25ca8e4e69", url="https://pypi.org/packages/f5/4e/f8b4f1404492e08b25b92ba4c248dd9533065ad0f25368feec240f8b182f/pyobjc-framework-Network-10.0.tar.gz")
    version("9.2", sha256="5f6aade9bac72379a57272414e085c14f4f99560644af91e4d2236c3dfe3da5f", url="https://pypi.org/packages/eb/7f/69566ed242fa6bc6ce81386becfc4b7b67014ba782f32c15e242c0c7a5a5/pyobjc-framework-Network-9.2.tar.gz")
    version("9.1.1", sha256="0881c24da1a707e05d040882aa67a85a965a03198125e2c01e1f617604554360", url="https://pypi.org/packages/34/f0/4ebe0d5cf5f6bddeddc400c5b7b40b69a4086d3de12d5358af955fe6d46d/pyobjc-framework-Network-9.1.1.tar.gz")
    version("9.1", sha256="23f18ca178b646dc6b39dc4228dcdb94e71b98285c65c9ca0faa2ac09fafe6ee", url="https://pypi.org/packages/97/e0/b3412d10e0bd595d1960c7d66e9ee0b15b1099ab6c64ba6ea3732407651d/pyobjc-framework-Network-9.1.tar.gz")
    version("9.0.1", sha256="51840027f24f555249db93261b111173408a2736c9aabad4732e7b74117f12cf", url="https://pypi.org/packages/63/d7/440fddcfbbb55ef541cb0b65afec62ca539d737cee89ca33235f129a629c/pyobjc-framework-Network-9.0.1.tar.gz")
    version("9.0", sha256="ce870ba580790d48eaac4e7ea51a0a090733c56ca5c380361dc59e8d764e1897", url="https://pypi.org/packages/8e/47/2725ce617352ff0953decc573d2b6265ec02ae9dabbd45c7507af352b93b/pyobjc-framework-Network-9.0.tar.gz")
    version("8.5.1", sha256="0b986e938d3587d5bcc1ff666c6c18daf041860e0c6cbbf0a484790fc7e3153b", url="https://pypi.org/packages/c7/c7/1e017ebf620994bc7a0f31bd6546b1e4b3e76fda7a85aac39dab98b74a30/pyobjc-framework-Network-8.5.1.tar.gz")
    version("8.5", sha256="387b79527d287bb743fbd77bd0ab41d82d04e76b059f31e3b7095280e7aa632c", url="https://pypi.org/packages/c0/72/245c5f75a6d88e396b7be879a2319f9e6241eb1fecf62e313dab712fa165/pyobjc-framework-Network-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")

