# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySrsly(PythonPackage):
    # BEGIN VERSIONS
    version("2.4.8", sha256="b24d95a65009c2447e0b49cda043ac53fecf4f09e358d87a57446458f91b8a91", url="https://pypi.org/packages/59/7f/17259e0962bb9433f39aa99ec45fd36851961491c562bc2f8c731cc476a6/srsly-2.4.8.tar.gz")
    version("2.4.7", sha256="93c2cc4588778261ccb23dd0543b24ded81015dd8ab4ec137cd7d04965035d08", url="https://pypi.org/packages/3c/65/95b58400f96ff8db3a60e1dd0b8915790df9e9e87d72f91cd96f031358b3/srsly-2.4.7.tar.gz")
    version("2.4.6", sha256="47b41f323aba4c9c3311abf60e443c03a9efe9c69f65dc402d173c32f7744a6f", url="https://pypi.org/packages/7d/50/c5dcea9cba3f3d698a847bda584be85e414a4a5cdae8019c4a7f4434d377/srsly-2.4.6.tar.gz")
    version("2.4.5", sha256="c842258967baa527cea9367986e42b8143a1a890e7d4a18d25a36edc3c7a33c7", url="https://pypi.org/packages/1c/9e/6497a75e4d72f21a56c8b1ddd21a5be3962850ff52e6c309ce6f2fcad881/srsly-2.4.5.tar.gz")
    version("2.4.5.dev1", sha256="ff667e7e34338b9594ac5d6a21b2e059493457c641d8cae2ece02ddb0eec0f32", url="https://pypi.org/packages/0a/51/6e2dd22f87402328f9cd348d8570195d813811708f1de2f347090ad99a07/srsly-2.4.5.dev1.tar.gz")
    version("2.4.4", sha256="e8a06581627b6712f19c60241b7c14c2bb29ce86ef04f791379a79f1b249a128", url="https://pypi.org/packages/3e/4e/dd97c89bba33748fb30ecce609cfa7d3f08629fd9b366ee4c1764abee86f/srsly-2.4.4.tar.gz")
    version("2.4.3", sha256="dbe91f6dd4aea9e819493628356dc715bd9c606486297bb7ca5748e6e003841c", url="https://pypi.org/packages/11/0a/3ba48157c25ac5cb80233c35332e04b185bc98048a7928e91f5c58f0c743/srsly-2.4.3.tar.gz")
    version("2.4.2", sha256="2aba252292767875086adf4e4380e27b024d73655456f796f8e07eb3a4dfacc0", url="https://pypi.org/packages/ea/1e/e456a751b70714e97ca931825ae983f934adec3b06064546d854938f2c80/srsly-2.4.2.tar.gz")
    version("2.4.1", sha256="b0f2aec0a329e6e7e742a0a60e99a74968ca29be71f35c5c4de221e328176926", url="https://pypi.org/packages/3f/ea/367e2a83354463447ca959feaf8248c72a2e6bc47c55bfd071716975cb41/srsly-2.4.1.tar.gz")
    version("2.4.0", sha256="e29730be53015970e4a59050e8e9f9be44d762108a617df56c9dfc981b515ab7", url="https://pypi.org/packages/fd/63/a9240c5e37b08e2fd9fc68a1ff30175f586d9d31a5f21529c4022ddcfc90/srsly-2.4.0.tar.gz")
    version("2.0.1", sha256="fa3c7375be8fe75f23c27feafbfb5f738d55ffdbf02964c6896fb7684f519a52", url="https://pypi.org/packages/f4/0b/22c6caff32757e6c350dcaecf3a55f4df57e15c9a8eaa8c6db6f29b99b54/srsly-2.0.1.tar.gz")
    version("2.0.0", sha256="785b00e00406120dbef4ca82925051e6b60fe870c5f84f0d22b3632d574eb870", url="https://pypi.org/packages/46/2f/8938af85873f1249a771788a82acbb8b684c444ba1a17d769ac28aeac55f/srsly-2.0.0.tar.gz")
    version("1.0.7", sha256="e7bfed757b38f2962f71c521856486f5b24909bba390cad15dc771bf739d3d2d", url="https://pypi.org/packages/f5/2c/23fb8b8b6698d5cb03860a5b82ab244583f908844fb454dc4d2219c27561/srsly-1.0.7.tar.gz")
    version("1.0.6", sha256="48d8bc622c4713e3d57f5706e9aa012df11e9a64089edc238ecd741e7450eb2f", url="https://pypi.org/packages/51/20/c3c53cafa02fbcba98e6dfc418b884b7eb55b5365e0d5d18954d60ef5f27/srsly-1.0.6.tar.gz")
    version("1.0.5", sha256="d3dd796372367c71946d0cd6f734e49db3d99dd13a57bdac937d9eb62689fc9e", url="https://pypi.org/packages/c7/08/abe935f33b69a08d365b95e62b47ef48f93a69ab734e623248a8a4079ecb/srsly-1.0.5.tar.gz")
    version("1.0.4", sha256="9ca5633a5303ce0d0b84d1bdb6d029f665ba2b7d320f5482525b125ddfb8a390", url="https://pypi.org/packages/d1/61/5a503487f711f42136a3a0986ac1bb46b2c96134634332238cc003e78a05/srsly-1.0.4.tar.gz")
    version("1.0.3", sha256="25bd33819a0e95dbe5d49072d07c361827658cf5f7d69d15e580c43d5adb873a", url="https://pypi.org/packages/9a/78/317b51c66faabbfc521fa93ce766df16925ad9487f258021ead49be66dad/srsly-1.0.3.tar.gz")
    version("1.0.2", sha256="59258b81d567df207f8a0a33c4b5fa232afccf1d927c8ce3ba5395bfd64c0ed8", url="https://pypi.org/packages/c4/28/ffb9f0b940041aeaec2194e840b5ffe19d0ae252de89579fa8b810174d9f/srsly-1.0.2.tar.gz")
    version("1.0.1", sha256="1102b4984f9f56364540e47d83fac3e7543903dfbb92f0d0e5dd3bfd40528934", url="https://pypi.org/packages/bc/3a/73c6e385afcbdb71218f83d44c67691a3ee5c47931838f92d607586a7a0e/srsly-1.0.1.tar.gz")
    version("0.2.0", sha256="aa02e2a62093ef09d7904343ee7381b9c9bab5b4f06960dfbeaa12035d0f0a3e", url="https://pypi.org/packages/1e/5b/f83e478fbf44c0d04f182e56db0871a53f5096febb8eb0be7cec75dca73b/srsly-0.2.0.tar.gz")
    version("0.1.0", sha256="5cc0dc561fa70cf12d21d192990a48388a78c8062cd3dcadcf336fc1c3953ed1", url="https://pypi.org/packages/b0/63/b68061954228346cbab2c41adb36339678605c47da016f5c71c7ef65f510/srsly-0.1.0.tar.gz")
    version("0.0.7", sha256="f3a2948b088064f719918ef46a1f14ffbd3ccab4c639c4ecb65053814fb036ed", url="https://pypi.org/packages/84/59/6f276ab6d74888eed0e999d617101ed7357fc1ee073e9aac92d53260bd23/srsly-0.0.7.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-catalogue@2.0.3:2.0", when="@2.4.8:")
    # END DEPENDENCIES

