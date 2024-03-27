##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDebtcollector(PythonPackage):
    version("3.0.0", sha256="46f9dacbe8ce49c47ebf2bf2ec878d50c9443dfae97cc7b8054be684e54c3e91", url="https://pypi.org/packages/9c/ca/863ed8fa66d6f986de6ad7feccc5df96e37400845b1eeb29889a70feea99/debtcollector-3.0.0-py3-none-any.whl")
    version("2.5.0", sha256="1393a527d2c72f143ffa6a629e9c33face6642634eece475b48cab7b04ba61f3", url="https://pypi.org/packages/a8/b8/3ab00e60d1c5665e831fa33bb47623ad613acb16c0d67e32e355efac44bd/debtcollector-2.5.0-py3-none-any.whl")
    version("2.4.0", sha256="637a1d2cc95c7158dc843dd74ee9f191410af87375a9e66575ea01057cd5015a", url="https://pypi.org/packages/7f/b5/2eb7b0aca147720bbf24059e0e78dbe983fa4cd48d0df7e14b2abc3384fe/debtcollector-2.4.0-py3-none-any.whl")
    version("2.3.0", sha256="6f1fae29c9091a6f7e8f68da7ec17f3167f98abac13c019968e144108f381b7e", url="https://pypi.org/packages/01/f2/a08f299e66a4c689f6d86491a28571460b9dc2aca25097c1f46685be6cc5/debtcollector-2.3.0-py3-none-any.whl")
    version("2.2.0", sha256="34663e5de257c67bf38827cfbea259c4d4ad27eba6b5a9d9242cb54076bfb4ad", url="https://pypi.org/packages/8e/50/07a7ccf4dbbe90b58e96f97b747ff98aef9d8c841d2616c48cc05b07db33/debtcollector-2.2.0-py3-none-any.whl")
    version("2.1.0", sha256="89db3d25c4adcd888d05648f1bc64b572d3e848dc2ad810f474fec0fb259c13a", url="https://pypi.org/packages/9e/1c/8eb78c8458c759973ed76458a67f3999486eaed5ebe25efedd96e2eb939c/debtcollector-2.1.0-py3-none-any.whl")
    version("2.0.1", sha256="96bde97db3de77218c9198db72e1ff4b8a794056ca2773356a6ac636418c602d", url="https://pypi.org/packages/d0/9e/d3c893e756fa4901f6851bd1cc625629c1f57804ebce6726884aa1efa5e0/debtcollector-2.0.1-py3-none-any.whl")
    version("2.0.0", sha256="bdef71fc362fadfde363d78c08820dfac38757bc99ebf2bf3cae72f6d93d1f60", url="https://pypi.org/packages/bf/f5/0591d1fd42a546e543cff78d264511b63a176d2b406a94c6bec111cf25fa/debtcollector-2.0.0-py3-none-any.whl")
    version("1.22.0", sha256="f0bccd85595fbca1e5c4f05789f6ce50f29e5b1a004462978bdd4330921e802a", url="https://pypi.org/packages/ca/ab/e34b13877f84a198b043166a82baf0ae8b9ed1daa83b6ebde776e8628b0a/debtcollector-1.22.0-py2.py3-none-any.whl")
    version("1.21.0", sha256="721b508130c2f133dcc14145c1e213967a84e31a15619b73d51dee79baef7f54", url="https://pypi.org/packages/59/33/d2a0fb2e8b1b51cec64e121ba4bbe0e3abdc597732074d425e0bde4aadb8/debtcollector-1.21.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pbr@2:2.0,3:", when="@1.14:2.4")
        depends_on("py-six@1.10:", when="@1.19:2.3")
        depends_on("py-wrapt@1.7:", when="@0.2:")

