# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyopenssl(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("24.1.0", sha256="17ed5be5936449c5418d1cd269a1a9e9081bc54c17aed272b45856a3d3dc86ad", url="https://pypi.org/packages/54/a7/2104f674a5a6845b04c8ff01659becc6b8978ca410b82b94287e0b1e018b/pyOpenSSL-24.1.0-py3-none-any.whl")
    version("24.0.0", sha256="ba07553fb6fd6a7a2259adb9b84e12302a9a8a75c44046e8bb5d3e5ee887e3c3", url="https://pypi.org/packages/3f/0e/c6656e62d9424d9c9f14b27be27220602f4af1e64b77f2c86340b671d439/pyOpenSSL-24.0.0-py3-none-any.whl")
    version("23.3.0", sha256="6756834481d9ed5470f4a9393455154bc92fe7a64b7bc6ee2c804e78c52099b2", url="https://pypi.org/packages/db/de/007b832ad7a95e6a73745609bbe123c407aa2c46bb0b8f765c8718294e7f/pyOpenSSL-23.3.0-py3-none-any.whl")
    version("23.2.0", sha256="24f0dc5227396b3e831f4c7f602b950a5e9833d292c8e4a2e06b709292806ae2", url="https://pypi.org/packages/f0/e2/f8b4f1c67933a4907e52228241f4bd52169f3196b70af04403b29c63238a/pyOpenSSL-23.2.0-py3-none-any.whl")
    version("23.1.1", sha256="9e0c526404a210df9d2b18cd33364beadb0dc858a739b885677bc65e105d4a4c", url="https://pypi.org/packages/b7/6d/d7377332703ffd8821878794aca4fb54637da654bf3e467ffb32109c2147/pyOpenSSL-23.1.1-py3-none-any.whl")
    version("23.1.0", sha256="fb96e936866ad65662c22d0de84ca0fba58397893cdfe0f01334fa93382af23c", url="https://pypi.org/packages/63/91/e5c22dd80e012e960d68c626746d9e3c525d33a056533f9ff2296d00cc35/pyOpenSSL-23.1.0-py3-none-any.whl")
    version("23.0.0", sha256="df5fc28af899e74e19fccb5510df423581047e10ab6f1f4ba1763ff5fde844c0", url="https://pypi.org/packages/73/00/b78f9fae05bb1633f7209aa394fa0c3563ef760ab7f47ac37768bf4e4d78/pyOpenSSL-23.0.0-py3-none-any.whl")
    version("22.1.0", sha256="b28437c9773bb6c6958628cf9c3bebe585de661dba6f63df17111966363dd15e", url="https://pypi.org/packages/00/3f/ea5cfb789dddb327e6d2cf9377c36d9d8607af85530af0e7001165587ae7/pyOpenSSL-22.1.0-py3-none-any.whl")
    version("22.0.0", sha256="ea252b38c87425b64116f808355e8da644ef9b07e429398bfece610f893ee2e0", url="https://pypi.org/packages/d5/9f/9c0e3288b85f907a008f9d31318b0e4de31b2f67724a8745e633741f609c/pyOpenSSL-22.0.0-py2.py3-none-any.whl")
    version("21.0.0", sha256="8935bd4920ab9abfebb07c41a4f58296407ed77f04bd1a92914044b848ba1ed6", url="https://pypi.org/packages/85/3a/fe3c98435856a1ed798977981f3da82d2685cf9df97e4d9546340d2b83db/pyOpenSSL-21.0.0-py2.py3-none-any.whl")
    version("20.0.1", sha256="818ae18e06922c066f777a33f1fca45786d85edfe71cd043de6379337a7f274b", url="https://pypi.org/packages/b2/5e/06351ede29fd4899782ad335c2e02f1f862a887c20a3541f17c3fa1a3525/pyOpenSSL-20.0.1-py2.py3-none-any.whl")
    version("20.0.0", sha256="898aefbde331ba718570244c3b01dcddb1b31a3b336613436a45e52e27d9a82d", url="https://pypi.org/packages/c9/86/e21398551956735fef8f7883908771445878ccb16cd17c0896176419cd75/pyOpenSSL-20.0.0-py2.py3-none-any.whl")
    version("19.1.0", sha256="621880965a720b8ece2f1b2f54ea2071966ab00e2970ad2ce11d596102063504", url="https://pypi.org/packages/9e/de/f8342b68fa9e981d348039954657bdf681b2ab93de27443be51865ffa310/pyOpenSSL-19.1.0-py2.py3-none-any.whl")
    version("19.0.0", sha256="c727930ad54b10fc157015014b666f2d8b41f70c0d03e83ab67624fd3dd5d1e6", url="https://pypi.org/packages/01/c8/ceb170d81bd3941cbeb9940fc6cc2ef2ca4288d0ca8929ea4db5905d904d/pyOpenSSL-19.0.0-py2.py3-none-any.whl")
    version("18.0.0", sha256="26ff56a6b5ecaf3a2a59f132681e2a80afcc76b4f902f612f518f92c2a1bf854", url="https://pypi.org/packages/96/af/9d29e6bd40823061aea2e0574ccb2fcf72bfd6130ce53d32773ec375458c/pyOpenSSL-18.0.0-py2.py3-none-any.whl")
    version("17.5.0", sha256="07a2de1a54de07448732a81e38a55df7da109b2f47f599f8bb35b0cbec69d4bd", url="https://pypi.org/packages/79/db/7c0cfe4aa8341a5fab4638952520d8db6ab85ff84505e12c00ea311c3516/pyOpenSSL-17.5.0-py2.py3-none-any.whl")
    version("17.4.0", sha256="b8a8797c50598da10526511a4a9b992b155932f86dde509906c8bee3a705b480", url="https://pypi.org/packages/b7/45/0b83f445994da6ff803d7c3a5fa016afda3c965d0c48dafa8e0264a554e7/pyOpenSSL-17.4.0-py2.py3-none-any.whl")
    version("17.3.0", sha256="aade9985b93eaec51b0c0a2a60d14bb8dcff1ff8e36fe542e3c22812ec07315e", url="https://pypi.org/packages/24/37/89bf12e53f1d27e8b2c8e5f8f9c7a958a3905f6916a9294a57a9d83fa165/pyOpenSSL-17.3.0-py2.py3-none-any.whl")
    version("17.2.0", sha256="c8959e441c2d85d646f3d6e9024ec02b2fc8dda92596e44ce3460b3a476bc694", url="https://pypi.org/packages/41/bd/751560b317222ba6b6d2e7663a990ac36465aaa026621c6057db130e2faf/pyOpenSSL-17.2.0-py2.py3-none-any.whl")
    version("17.1.0", sha256="cc21d1dcc5c4413281c59f912975209999ffb8b091b03872d2516e60be512290", url="https://pypi.org/packages/d0/39/7730559b75b565fd6983d857776fcb4982afb0e8faddb06170e59b62b41c/pyOpenSSL-17.1.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cryptography@41.0.5:42", when="@24:")
        depends_on("py-cryptography@41.0.5:41", when="@23.3:23")
        depends_on("py-cryptography@38:39,40.0.2:41", when="@23.2")
        depends_on("py-cryptography@38:40", when="@23.1")
        depends_on("py-cryptography@38:39", when="@23:23.0")
        depends_on("py-cryptography@38", when="@22.1:22")
        depends_on("py-cryptography@35:", when="@22:22.0")
        depends_on("py-cryptography@3.3:", when="@21")
        depends_on("py-cryptography@3.2:", when="@20")
        depends_on("py-cryptography@2.8:", when="@19.1:19")
        depends_on("py-cryptography@2.3:", when="@19:19.0")
        depends_on("py-cryptography@2.2.1:", when="@18")
        depends_on("py-cryptography@2.1.4:", when="@17.5:17")
        depends_on("py-cryptography@1.9:", when="@17.1:17.4")
        depends_on("py-six@1.5.2:", when="@0.15:21")
    # END DEPENDENCIES

