##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureCore(PythonPackage):
    version("1.30.1", sha256="7c5ee397e48f281ec4dd773d67a0a47a0962ed6fa833036057f9ea067f688e74", url="https://pypi.org/packages/d7/70/180df3b43ebc7a1ec957d9e5c2c76e6c54398ec61a67dff88d3e0131be80/azure_core-1.30.1-py3-none-any.whl")
    version("1.30.0", sha256="3dae7962aad109610e68c9a7abb31d79720e1d982ddf61363038d175a5025e89", url="https://pypi.org/packages/be/4f/a747b2537fea6302ff3a307b1f9701853e65e215afc1a62fa931d031c57a/azure_core-1.30.0-py3-none-any.whl")
    version("1.29.7", sha256="95a7b41b4af102e5fcdfac9500fcc82ff86e936c7145a099b7848b9ac0501250", url="https://pypi.org/packages/ff/29/dbc7182bc207530c7b5858d59f429158465f878845d64a038afc1aa61e35/azure_core-1.29.7-py3-none-any.whl")
    version("1.29.6", sha256="604a005bce6a49ba661bb7b2be84a9b169047e52fcfcd0a4e4770affab4178f7", url="https://pypi.org/packages/b0/e2/b6cdd23d8d9cc430410cc309879883aff67736c02528cd1fdc07c48158b1/azure_core-1.29.6-py3-none-any.whl")
    version("1.29.5", sha256="0fa04b7b1f7d44a4fb8468c4093deb2ea01fdf4faddbf802ed9205615f99d68c", url="https://pypi.org/packages/9c/f8/1cf23a75cb8c2755c539ac967f3a7f607887c4979d073808134803720f0f/azure_core-1.29.5-py3-none-any.whl")
    version("1.29.4", sha256="b03261bcba22c0b9290faf9999cedd23e849ed2577feee90515694cea6bc74bf", url="https://pypi.org/packages/98/3a/d53e2b8a75c448ef45d7ae4b0659eb6c0d48978f25a709e2a39894a48704/azure_core-1.29.4-py3-none-any.whl")
    version("1.29.3", sha256="f8b2910f92b66293d93bd00564924ad20ad48f4a1e150577cf18d1e7d4f9263c", url="https://pypi.org/packages/0e/20/2f7a562c6a600b32c64ebe00cc9e4c3099bc42d52aadcafd3a2a8fa0d68a/azure_core-1.29.3-py3-none-any.whl")
    version("1.29.2", sha256="8e6602f322dc1070caf7e17754beb53b69ffa09df0f4786009a3107e9a00c793", url="https://pypi.org/packages/78/f5/0e2e1eee5548ef539461183024ccdd0397a920b33fdd092c9af489ab1940/azure_core-1.29.2-py3-none-any.whl")
    version("1.29.1", sha256="6bcefa1f70ff7bf3c39c07c73d8a21df73288eff7e6a1031eb8cfae71cc7bed4", url="https://pypi.org/packages/fb/4e/75fb100cdc22dde79cf10431dba3cbb1b4f77499cff63d767163d1e7511d/azure_core-1.29.1-py3-none-any.whl")
    version("1.29.0", sha256="b591cada3644523ae61fd8f120e14e2486ac70485206355db49d7de36709303a", url="https://pypi.org/packages/13/74/a6dc1d5192ac88c65605be9442aae2b5b7bdd07c81b89f82562b36600d9d/azure_core-1.29.0-py3-none-any.whl")
    version("1.28.0", sha256="dec36dfc8eb0b052a853f30c07437effec2f9e3e1fc8f703d9bdaa5cfc0043d9", url="https://pypi.org/packages/c3/0a/32b17d776a6bf5ddaa9dbad0e88de9d28a55bec1d37b8d408cc7d2e5e28d/azure_core-1.28.0-py3-none-any.whl")
    version("1.27.1", sha256="1b4b19f455eb7b4332c6f92adc2c669353ded07c2722eb436165f0c253737792", url="https://pypi.org/packages/71/fa/b6f8f8693de85c69f70ad3b0320a35b663ef1110d32ee2c1064d3dacb0f4/azure_core-1.27.1-py3-none-any.whl")
    version("1.26.4", sha256="d9664b4bc2675d72fba461a285ac43ae33abb2967014a955bf136d9703a2ab3c", url="https://pypi.org/packages/8d/12/8d1b124dcce9a695a8a8907461684ad08af4eca575e59fb2c8c70539caf7/azure_core-1.26.4-py3-none-any.whl")
    version("1.26.1", sha256="726ffd1ded04a2c1cb53f9d9155cbb05ac5c1c2a29af4ef622e93e1c0a8bc92b", url="https://pypi.org/packages/2c/e9/a58441e746621541bf122ed820f756dcfb8ede7b863b5f8e301236cf1e2f/azure_core-1.26.1-py3-none-any.whl")
    version("1.21.1", sha256="3d70e9ec64de92dfae330c15bc69085caceb2d83813ef6c01cc45326f2a4be83", url="https://pypi.org/packages/a6/07/95105c0c1cc46a5c8b14e43c66fa8b50fe1e7f0918e8809a7422cb67a1cf/azure_core-1.21.1-py2.py3-none-any.whl")
    version("1.15.0-beta1", sha256="eb9f5fea76f578e769f85e5c54636770f3427ae3186510d88b546949dff75ce1", url="https://pypi.org/packages/5b/f4/35ec076058f98e1415b9034e92c1d989b57d6f491757307d5395cf703fea/azure_core-1.15.0b1-py2.py3-none-any.whl")
    version("1.7.0", sha256="2d1aade2795ea0ac2a903af940c3e0dfe75d25351ec4fc44edf747e97d703dfb", url="https://pypi.org/packages/8b/00/efb68e2dda82139d732090fc3b7ff47fe6f34724ea7ba31e518a854b15c1/azure_core-1.7.0-py2.py3-none-any.whl")
    version("1.6.0", sha256="7bf695b017acea3da28e0390a2dea5b7e15a9fa3ef1af50ff020bcfe7dacb6a4", url="https://pypi.org/packages/a4/ed/ff9f4669e5b9a78a62fe43b83cc01e9007bbf6e99ec7ab6f73557135099f/azure_core-1.6.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-anyio@3.0.0:", when="@1.29.6")
        depends_on("py-requests@2.21:", when="@1.29.6:")
        depends_on("py-requests@2.18.4:", when="@:1.29.5")
        depends_on("py-six@1.11:", when="@1.11:")
        depends_on("py-six@1.6:", when="@1.0.0-beta4:1.10")
        depends_on("py-typing-extensions@4.6:", when="@1.29.2:")
        depends_on("py-typing-extensions@4.3:", when="@1.26.4:1.29.1")
        depends_on("py-typing-extensions@4.0.1:", when="@1.23:1.26.3")

