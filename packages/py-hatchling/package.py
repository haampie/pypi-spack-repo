# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHatchling(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.22.3", sha256="f6602529d17f4c91123b4ffbcd4e0f143d92ba9603716edab4a83785f66e2942", url="https://pypi.org/packages/2d/31/b4ffda996d1e21bb7096fd377b0437f4925351c2f60dbe9563e83705744c/hatchling-1.22.3-py3-none-any.whl")
    version("1.22.2", sha256="5fdf7b689c1e76cf280bfe002e5e3d7efe99f63e559d2dc3e5d5f49de489d57d", url="https://pypi.org/packages/7d/a4/c69d252d72d61591c2f9354f30fe39927256ec0615f77d16d419a7b98d28/hatchling-1.22.2-py3-none-any.whl")
    version("1.22.1", sha256="4715939b657441c050e1b11fd8f13359dcd650eb36d7d5bfcbb305604408af3a", url="https://pypi.org/packages/42/d4/7efdf54bdf0005a1da0359753123a45a7f3b8a03df3135ece52f8d2600e9/hatchling-1.22.1-py3-none-any.whl")
    version("1.22.0", sha256="df5a37b7270cc0f37a507c1ba0b04da6f947f8c85584f5c65caa00eb0ec88206", url="https://pypi.org/packages/f7/92/2f698e9ff35ad9682bcb77462a267a2b99b316fec48a2083ade7d1750b59/hatchling-1.22.0-py3-none-any.whl")
    version("1.21.1", sha256="21e8c13f8458b219a91cb84e5b61c15bf786695d1c4fabc29e91e78f94bfe892", url="https://pypi.org/packages/3a/bb/40528a09a33845bd7fd75c33b3be7faec3b5c8f15f68a58931da67420fb9/hatchling-1.21.1-py3-none-any.whl")
    version("1.21.0", sha256="b33ef0ecdee6dbfd28c21ca30df459ba1d566050d033f8b5a1d0e26e5606d26b", url="https://pypi.org/packages/04/35/aa8738d6674aba09d3f0c77a1c40aee1dbf10e1b26d03cbd987aa6642e86/hatchling-1.21.0-py3-none-any.whl")
    version("1.20.0", sha256="872c63aa7e8aca85e8dba07b05c6a9b28d5a149fe00638f1a47e36930197248f", url="https://pypi.org/packages/87/4a/7d22a92b55809c579d8deafb0dabeb102b411a0ef9439949cccef3071527/hatchling-1.20.0-py3-none-any.whl")
    version("1.19.1", sha256="f79bf5bd914daf05edfce109bc1d3937329bb5dc65954b47d5540a574ec77cae", url="https://pypi.org/packages/ee/a3/497660b2e44609af17fa2c29a8d9a38f2833e2e59949332ee563d79b13fe/hatchling-1.19.1-py3-none-any.whl")
    version("1.19.0", sha256="517e744d54c924b01e3a8faf205acc3a5a59bdbb24bb13baee2f48c483231776", url="https://pypi.org/packages/be/ee/6f75ebb0e15860c96fabb713a1e3487339dfe5bc32c354434b88227c065c/hatchling-1.19.0-py3-none-any.whl")
    version("1.18.0", sha256="b66dc254931ec42aa68b5febd1d342c58142cc5267b7ff3b12ba3fa5b4900c93", url="https://pypi.org/packages/76/56/8ccca673e2c896931722f876bf040c0b6a7d8c1a128be60516a8a55bb27a/hatchling-1.18.0-py3-none-any.whl")
    version("1.17.0", sha256="2d022a72a027de26e783b3a597bd046a6ead8edd435ea29ee87a20d60bfea1fe", url="https://pypi.org/packages/30/28/58bc90ec306e18881c3cb75084a6a203ad974829c1b5ac81dda4e58cf2a8/hatchling-1.17.0-py3-none-any.whl")
    version("1.14.0", sha256="545163d58ab1f908dd1bb1092432738848329d5eaadedb4b38b6bc1f37d9b4ea", url="https://pypi.org/packages/d0/a2/58a005a7fe8d0c23bc8905ad9f17e4921f5378e18d34f9279b5345987543/hatchling-1.14.0-py3-none-any.whl")
    version("1.13.0", sha256="357d5a5abac0d28e24fa87534efc63f5ba3f9b3306675678049ca4ba9f2a6674", url="https://pypi.org/packages/2a/8a/a2d2b9f93d382ad3d805847f74b33ed38da2eaac2bcf82686c55d3450f80/hatchling-1.13.0-py3-none-any.whl")
    version("1.10.0", sha256="fb28c3106247022da0e794899502e3164d4a3ccf8f55b1826ff72ee1af087046", url="https://pypi.org/packages/26/d3/fca2fb066cd41967b6f0041bc57c34d02aeef43f23590875618635afbc0c/hatchling-1.10.0-py3-none-any.whl")
    version("1.8.1", sha256="09171ed1404e636ef572b370d34c5cb36a8029825c0a7859ac93989080ba2630", url="https://pypi.org/packages/19/93/bd81c789331a317351b2887a508843804de1414d9455a37bce78f6722c25/hatchling-1.8.1-py3-none-any.whl")
    version("1.4.1", sha256="c26200c9ec13f58ffb48bfb067ffd6bb90ba4d9c24f1d7e932ef58aa9621477d", url="https://pypi.org/packages/5e/fc/8265418d0605309e7458a1dd63c7071920763a40578be50a0aa9800d7b28/hatchling-1.4.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-editables@0.3:", when="@0.23:1.21")
        depends_on("py-packaging@21.3:", when="@0.20:")
        depends_on("py-pathspec@0.10.1:", when="@1.9:")
        depends_on("py-pathspec@0.9:", when="@0.20:1.8")
        depends_on("py-pluggy@1:1.0.0.0,1.1:", when="@0.20:")
        depends_on("py-tomli@1.2.2:", when="@0.23: ^python@:3.10")
        depends_on("py-tomli@1.2.2:", when="@0.20:0.22")
        depends_on("py-trove-classifiers", when="@1.14:")
    # END DEPENDENCIES

