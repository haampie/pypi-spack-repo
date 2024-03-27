##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPatsy(PythonPackage):
    version("0.5.6", sha256="19056886fd8fa71863fa32f0eb090267f21fb74be00f19f5c70b2e9d76c883c6", url="https://pypi.org/packages/43/f3/1d311a09c34f14f5973bb0bb0dc3a6e007e1eda90b5492d082689936ca51/patsy-0.5.6-py2.py3-none-any.whl")
    version("0.5.5", sha256="6067516e97c1d5da5d24603853834e3555e943ffb419ea32020f7ba561fa6d0d", url="https://pypi.org/packages/32/0e/0039df17094e8d9d26b69bd8e976e179b1f6cc772f9ffb597640d5016772/patsy-0.5.5-py2.py3-none-any.whl")
    version("0.5.4", sha256="0486413077a527db51ddea8fa94a5234d0feb17a4f4dc01b59b6086c58a70f80", url="https://pypi.org/packages/29/ab/373449d6f741732f94e2d15d116a90f050b2857cb727b26d2f7bead50815/patsy-0.5.4-py2.py3-none-any.whl")
    version("0.5.3", sha256="7eb5349754ed6aa982af81f636479b1b8db9d5b1a6e957a6016ec0534b5c86b7", url="https://pypi.org/packages/2a/e4/b3263b0e353f2be7b14f044d57874490c9cef1798a435f038683acea5c98/patsy-0.5.3-py2.py3-none-any.whl")
    version("0.5.2", sha256="cc80955ae8c13a7e7c4051eda7b277c8f909f50bc7d73e124bc38e2ee3d95041", url="https://pypi.org/packages/87/7f/d37cd027c25145eeba92b1a756976931c831803d92547c8637a3400c339f/patsy-0.5.2-py2.py3-none-any.whl")
    version("0.5.1", sha256="5465be1c0e670c3a965355ec09e9a502bf2c4cbe4875e8528b0221190a8a5d40", url="https://pypi.org/packages/ea/0c/5f61f1a3d4385d6bf83b83ea495068857ff8dfb89e74824c6e9eb63286d8/patsy-0.5.1-py2.py3-none-any.whl")
    version("0.5.0", sha256="14269536ecedaae0a5a2f300faac7d0afa1cc47aa98c561f54ba7300d0ec4011", url="https://pypi.org/packages/5d/eb/92c4b45ca47a2dd1339c958636e083b50ffadb5162a599a1cbbe92f89832/patsy-0.5.0-py2.py3-none-any.whl")
    version("0.4.1", sha256="63102f77df5c6b0c3fe3bf9d57bcea112d1e06d00a41823662b5044ce681f22c", url="https://pypi.org/packages/02/8a/255f80a7f939006ec479275fde6301feedf3fdd9ecee782bb64987b84de8/patsy-0.4.1-py2.py3-none-any.whl")
    version("0.4.0", sha256="57bd83b876064562d54c61a6082dd57be9801a02d34a071e918117a4b7919f23", url="https://pypi.org/packages/76/0a/17046bb24666b5503809415b879ed7820ea53a9e3269ef77a85edb9d3074/patsy-0.4.0-py2.py3-none-any.whl")
    version("0.3.0", sha256="01dd39f43e0ed2f819c12ae6314a2bfb8ae5823769dd5aa2497c40c1f0ea78c4", url="https://pypi.org/packages/07/13/2b5dadce7da41de7c8adc39e3dd5ab7d5f9852761606e62b72f008844b5c/patsy-0.3.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-numpy@1.4:", when="@0.5:")
        depends_on("py-numpy", when="@0.4.1:0.4")
        depends_on("py-six", when="@0.4.1:")

