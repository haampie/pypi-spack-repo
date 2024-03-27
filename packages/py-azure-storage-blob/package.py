##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureStorageBlob(PythonPackage):
    version("12.19.1", sha256="c5530dc51c21c9564e4eb706cd499befca8819b10dd89716d3fc90d747556243", url="https://pypi.org/packages/39/96/c0964ea207da669fb6c51a370aef647269c4a21608112a1057440dda8aea/azure_storage_blob-12.19.1-py3-none-any.whl")
    version("12.19.0", sha256="7bbc2c9c16678f7a420367fef6b172ba8730a7e66df7f4d7a55d5b3c8216615b", url="https://pypi.org/packages/f6/82/24b0d7cf67ea63af86f11092756b8fe2adc1d55323241dc4107f5f5748e2/azure_storage_blob-12.19.0-py3-none-any.whl")
    version("12.19.0-beta1", sha256="5f80b72fee0e4e5dee5ec2159d78f0a628ffb6177117ac81d0bed9a1ebf825b2", url="https://pypi.org/packages/a4/89/1bc063d758bcd4cfde5ea0b206b75de59ea45fdc460ca8acc60a4480fda3/azure_storage_blob-12.19.0b1-py3-none-any.whl")
    version("12.18.3", sha256="c278dde2ac41857a68d615c9f2b36d894ba877a7e84d62795603c7e79d0bb5e9", url="https://pypi.org/packages/be/cd/30306c04f962b55cae44cab2859b5496d0d75521a3bf2e92ec4a6bb61ddb/azure_storage_blob-12.18.3-py3-none-any.whl")
    version("12.18.2", sha256="ffd864bf9abf33dfc72c6ef37899a19bd9d585a946a2c61e288b4420c035df3a", url="https://pypi.org/packages/7c/14/03baf5163186a95469d5f86031bde2bd35f3dec6ed3c8b87c876aa0f68d4/azure_storage_blob-12.18.2-py3-none-any.whl")
    version("12.18.1", sha256="00b92568e91d608c04dfd4814c3b180818e690023493bb984c22dfc1a8a96e55", url="https://pypi.org/packages/14/c3/9b6a7f5fee1bf833384925f9741b182d170bb65d0142fbf73b1683a055d2/azure_storage_blob-12.18.1-py3-none-any.whl")
    version("12.18.0", sha256="11e033f91a9c2bee72251951ef60d45cfcad2eb199476e924074bb1d124e2fed", url="https://pypi.org/packages/37/11/89b45a62e3fe5faf94780fad626a1a7de3edb5040f8ecb19103ee83ae531/azure_storage_blob-12.18.0-py3-none-any.whl")
    version("12.18.0-beta1", sha256="18efad68cdb769a30ef451cb6aef019a2bb77f8aa98f83664655f0cfc8ed290a", url="https://pypi.org/packages/69/58/387f5cf6a235c02460806fe45a8ae949c51882e7fb6bd68b0529ac41bd0e/azure_storage_blob-12.18.0b1-py3-none-any.whl")
    version("12.17.0", sha256="0016e0c549a80282d7b4920c03f2f4ba35c53e6e3c7dbcd2a4a8c8eb3882c1e7", url="https://pypi.org/packages/f1/06/68c50a905e1e5481b04a6166b69fecddb87681aae7a556ab727f8e8e6f70/azure_storage_blob-12.17.0-py3-none-any.whl")
    version("12.16.0", sha256="91bb192b2a97939c4259c72373bac0f41e30810bbc853d5184f0f45904eacafd", url="https://pypi.org/packages/95/e7/db8bfa32d44436e3753c60be51577420e0836ec101e3209452f3c84920c6/azure_storage_blob-12.16.0-py3-none-any.whl")
    version("12.15.0", sha256="08d8807c577c63a436740627927c1a03a97c963efc29af5c818aed906590e1cf", url="https://pypi.org/packages/46/cf/ef1daa7b7df2b2d72db82fa2a777bf50133f4797b4bdfa6b3bbea09660fe/azure_storage_blob-12.15.0-py3-none-any.whl")
    version("12.14.0", sha256="073c9e99154975644b32ed5c900832d8aa3c041b972b2f34ef269760d023e69b", url="https://pypi.org/packages/c3/04/636de31f41279f21d1b74f7acfcced80b9d2e2f27d8a729b1e3134102c6f/azure_storage_blob-12.14.0-py3-none-any.whl")
    version("12.13.1", sha256="726b86f733dc76218ce45b7a3254b61ba4f0cc3d68b7621be4985248c92ee483", url="https://pypi.org/packages/dd/fb/1501707ae8d921079ea826d16926e1b9b179d15264a2d239a08d7b374522/azure_storage_blob-12.13.1-py3-none-any.whl")
    version("12.12.0", sha256="1eac4c364309ccc193c80ee26c78d25dfbf10926b1309095a448a7a0388526eb", url="https://pypi.org/packages/85/2f/7b8ba0676118a451598c73ad772e47e13b5e66f68a2fc2dfca5c50d17ec4/azure_storage_blob-12.12.0-py3-none-any.whl")
    version("12.11.0", sha256="f3dfa605aefb453e7489328b76811a937a411761d7a1613a58c3975c556ec778", url="https://pypi.org/packages/4d/4f/de7f58a5449d75b1a43610d069472b7b686fd73205de42a41e66631a4dce/azure_storage_blob-12.11.0-py3-none-any.whl")
    version("12.10.0", sha256="a70995c4f9310eb704594f30505d1499286b4caac5543a2ebfe84431c4a38b0b", url="https://pypi.org/packages/64/e4/dcd968e113786fb946007dd76c6fb459a511ac63984dfa09737cfb3b7d69/azure_storage_blob-12.10.0-py3-none-any.whl")
    version("12.9.0", sha256="859195b4850dcfe77ffafbe53500abb74b001e52e77fe6d9492fa73639a22127", url="https://pypi.org/packages/41/f3/e2b3fa9de629ab76031588daf54b4c28d71bd3c209d8a3d4f470d87e98a7/azure_storage_blob-12.9.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-azure-core@1.28:", when="@12.17.0:")
        depends_on("py-azure-core@1.26:", when="@12.15:12.17.0-beta1")
        depends_on("py-azure-core@1.24.2:", when="@12.14")
        depends_on("py-azure-core@1.23.1:", when="@12.12:12.13")
        depends_on("py-azure-core@1.15.0:", when="@12.10.0-beta4:12.11")
        depends_on("py-azure-core@1.10:", when="@12.7.0:12.10.0-beta2")
        depends_on("py-cryptography@2.1.4:", when="@12:")
        depends_on("py-isodate@0.6.1:", when="@12.15:")
        depends_on("py-msrest@0.7.1:", when="@12.14.0-beta2:12.14")
        depends_on("py-msrest@0.6.21:", when="@12.9:12.14.0-beta1")
        depends_on("py-typing-extensions@4.3:", when="@12.17.0:")
        depends_on("py-typing-extensions@4.0.1:", when="@12.15:12.17.0-beta1")

