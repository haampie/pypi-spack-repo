##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPortalocker(PythonPackage):
    version("2.8.2", sha256="cfb86acc09b9aa7c3b43594e19be1345b9d16af3feb08bf92f23d4dce513a28e", url="https://pypi.org/packages/17/9e/87671efcca80ba6203811540ed1f9c0462c1609d2281d7b7f53cef05da3d/portalocker-2.8.2-py3-none-any.whl")
    version("2.8.1", sha256="d13c79617e5644356e1a01e791e41c4b50eb4eed957567b3e9403219decd9d39", url="https://pypi.org/packages/21/1f/20af121f4f878c5d66cd29f342180becec56c435f153a920749daeb7b0c8/portalocker-2.8.1-py3-none-any.whl")
    version("2.8.0", sha256="5ea10654e42178182c63c16f608774e2a8914dc0afbdcce9879d6ef6f6845fe2", url="https://pypi.org/packages/a8/a8/b6bcc90951971cf29f3bc66d892b70071000ebb9aafeb2409809094fe4e8/portalocker-2.8.0-py3-none-any.whl")
    version("2.7.0", sha256="769c394f934f3459fab9f0989c17aa8158334f1898b9bb8407432bdc3f44be6d", url="https://pypi.org/packages/db/1e/07ab791977f4c5a6f30c74a10c3e38360cf6dea228ceda89d83a97c0c6f6/portalocker-2.7.0-py3-none-any.whl")
    version("2.6.0", sha256="102ed1f2badd8dec9af3d732ef70e94b215b85ba45a8d7ff3c0003f19b442f4e", url="https://pypi.org/packages/2a/59/dab72d0b8859a410a83dcaffb84781ffc467651b79c827a435c8945add05/portalocker-2.6.0-py2.py3-none-any.whl")
    version("2.5.1", sha256="400bae275366e7b840d4baad0654c6ec5994e07c40c423d78e9e1340279b8352", url="https://pypi.org/packages/a9/0a/21422dc681e3e59ce5ec4051015de4c2074bd0e6759099c018471f3dc4e3/portalocker-2.5.1-py2.py3-none-any.whl")
    version("2.5.0", sha256="931db460f729d6088fe7bec43a57a0d024ea927f963d9ab8d09caa7843a4239f", url="https://pypi.org/packages/e6/87/7f6218b2f9be1f123803689c6888cf904eab6c02418d8c8788c520456dbf/portalocker-2.5.0-py2.py3-none-any.whl")
    version("2.4.0", sha256="b092f48e1e30a234ab3dd1cfd44f2f235e8a41f4e310e463fc8d6798d1c3c235", url="https://pypi.org/packages/f1/4e/1030afbf2e64e676e968bbbc82014ce4ddf1cc1ed0b492585958768cf79a/portalocker-2.4.0-py2.py3-none-any.whl")
    version("2.3.2", sha256="75cfe02f702737f1726d83e04eedfa0bda2cc5b974b1ceafb8d6b42377efbd5f", url="https://pypi.org/packages/38/2e/32172e8418f2ba284cee4fd67cb547d39a7debb3eed37d514da173786112/portalocker-2.3.2.tar.gz")
    version("2.3.1", sha256="5ff2e494eccd3ff1cbaba8e4defd45bc7edb8eea3908c74f6de5d40641a1ed92", url="https://pypi.org/packages/21/23/f89c470cc056558648e5e250bed177aef2bc208987a9b582eec2c599e080/portalocker-2.3.1.tar.gz")
    version("1.7.1", sha256="6d6f5de5a3e68c4dd65a98ec1babb26d28ccc5e770e07b672d65d5a35e4b2d8a", url="https://pypi.org/packages/31/e3/b75d97109c793db0e23bcad15ab642da7517fe8dd6ad31567ed66ff51760/portalocker-1.7.1.tar.gz")
    version("1.7.0", sha256="091364838ed6fbb68ea291c28982d1e56125c0d9e3fad5a4ac001db54dd862dc", url="https://pypi.org/packages/7a/75/47453988b56b400fc73083123b15ac48f8488deec3d1060e3956dd03ee4e/portalocker-1.7.0.tar.gz")
    version("1.6.0", sha256="4013e6d17123560178a5ba28cb6fdf13fd3079dee18571ff824e05b7abc97b94", url="https://pypi.org/packages/88/e8/7423914230d9bec33c54b7b99a540d9e36503663f28c0449fa3c319bcf47/portalocker-1.6.0.tar.gz")
    version("1.5.2", sha256="dac62e53e5670cb40d2ee4cdc785e6b829665932c3ee75307ad677cf5f7d2e9f", url="https://pypi.org/packages/26/2b/b9388a8747452c5e387d39424480b9833bf6dad0152d184dbc45b600be76/portalocker-1.5.2.tar.gz")
    version("1.5.1", sha256="1ed88cff4807267ec3331d2a843529399256043851509c39487db97146dda821", url="https://pypi.org/packages/c5/dd/e55b27cd9c6e96abc2c81dddf9f4d29d957f3a4fc03bfa2cfa9ba1f26bfe/portalocker-1.5.1.tar.gz")
    version("1.5.0", sha256="d9af6b298554286a05b9fd361289fe8a86b2b0f41a82cd93b147155bd398c523", url="https://pypi.org/packages/f8/81/daafc3a912dd428b1e6ced73f89772b6c85570b51b2d898bba65c8242986/portalocker-1.5.0.tar.gz")
    version("1.4.0", sha256="3fb35648a9e03f267e54c6186513abbd1cdd321c305502545a3550eea8b2923f", url="https://pypi.org/packages/64/9f/cdf0db3a74307d9a000ec049f34a122c889f25224518d516519a2d8a7fba/portalocker-1.4.0.tar.gz")
    version("1.3.0", sha256="b5ba72ace4f50093e3841c65a24f65d4f1bddd8d47cf439e56ab30b1aebd62a0", url="https://pypi.org/packages/2b/13/c83dad209d6d0d3aa909d01d8c25e7d6c598101b57131670e71ba5e60638/portalocker-1.3.0.tar.gz")
    version("1.2.1", sha256="3f2a56d3d90e2ac5659ee744336e6953c0050bb61fccb97090a03de5c2a4db9f", url="https://pypi.org/packages/01/e1/badb92f4bbd7c8c892d943a0136dcacf123cfbc835535368c74b707bc8dd/portalocker-1.2.1.tar.gz")
    version("1.2.0", sha256="37c7d2b8eaf73a779089d8455ad90b0a38afd33e4fb8dedabe49e49550846173", url="https://pypi.org/packages/18/9f/bf662276540727fe4c8113a4ed23fabe95784ad155a48e12f2b9b495217a/portalocker-1.2.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-pywin32@226:", when="@2.4: platform=windows")

