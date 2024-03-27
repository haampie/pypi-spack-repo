##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTypingInspect(PythonPackage):
    version("0.9.0", sha256="9ee6fc59062311ef8547596ab6b955e1b8aa46242d854bfc78f4f6b0eff35f9f", url="https://pypi.org/packages/65/f3/107a22063bf27bdccf2024833d3445f4eea42b2e598abfbd46f6a63b6cb0/typing_inspect-0.9.0-py3-none-any.whl")
    version("0.8.0", sha256="5fbf9c1e65d4fa01e701fe12a5bca6c6e08a4ffd5bc60bfac028253a447c5188", url="https://pypi.org/packages/be/01/59b743dca816c4b6ca891b9e0f84d20513cd61bdbbaa8615de8f5aab68c1/typing_inspect-0.8.0-py3-none-any.whl")
    version("0.7.1", sha256="047d4097d9b17f46531bf6f014356111a1b6fb821a24fe7ac909853ca2a782aa", url="https://pypi.org/packages/c3/da/864ce66818e308b38209d4b1ef0585921d28eb07621ba7d905a0e96bcc80/typing_inspect-0.7.1.tar.gz")
    version("0.7.0", sha256="b0879cbc15d086f0ca7066eb775c062333e96f6d4622193d2423d8649c778480", url="https://pypi.org/packages/36/0f/66cb239f87c2a59bd91e9b6e280f04a5dd14eba4d1cf41a922c324398da2/typing_inspect-0.7.0.tar.gz")
    version("0.6.0", sha256="8f1b1dd25908dbfd81d3bebc218011531e7ab614ba6e5bf7826d887c834afab7", url="https://pypi.org/packages/84/06/8610d429f5d8d6e145abd0ac6a1a6a120c5f6fcbe174d43ddde549b1c582/typing_inspect-0.6.0.tar.gz")
    version("0.5.0", sha256="811b44f92e780b90cfe7bac94249a4fae87cfaa9b40312765489255045231d9c", url="https://pypi.org/packages/d6/d2/3c8d0a885995ee81e0a52dca5093d0c3dccf511a009944e62d4ab14c9c2f/typing_inspect-0.5.0.tar.gz")
    version("0.4.0", sha256="cf41eb276cc8955a45e03c15cd1efa6c181a8775a38ff0bfda99d28af97bcda3", url="https://pypi.org/packages/ae/6c/0f91f0d13be6a6ceba8605315fd29f1ea97f1e6556c52199eb9f3d70f0bd/typing_inspect-0.4.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-mypy-extensions@0.3:", when="@0.3.1:0.6,0.8:")
        depends_on("py-typing-extensions@3.7.4:", when="@0.5:0.6,0.8:")

