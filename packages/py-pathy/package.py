##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPathy(PythonPackage):
    version("0.11.0", sha256="5027f44744cdcd6b6ffd0b0570133dc1bc4af4b87a4f574ecdd810552b1a9fb0", url="https://pypi.org/packages/42/54/c8f12c7cfb9b7a994acd3d92e816130940b3d4510f87ed1c66b3e7976b73/pathy-0.11.0-py3-none-any.whl")
    version("0.10.3", sha256="c5fe70867c79037d5fb34bfeef57d5c19a0b948cdf9286894ca44d72dfa53066", url="https://pypi.org/packages/0e/6b/d64babaaeaea0311e55a193d6385bcd2b342e30158ce336cbc05eae7fec6/pathy-0.10.3-py3-none-any.whl")
    version("0.10.2", sha256="681bc98dbff28e7de3e50efa8246910f727e8ac254c4318c47ce341f7c1ce21d", url="https://pypi.org/packages/b5/c3/04a002ace658133f5ac48d30258ed9ceab720595dc1ac36df02fe52018af/pathy-0.10.2-py3-none-any.whl")
    version("0.10.1", sha256="a7613ee2d99a0a3300e1d836322e2d947c85449fde59f52906f995dbff67dad4", url="https://pypi.org/packages/82/c6/683e3955de9a13b14dfa3ea358cd58f3914057e8064a2dcbfd450958e72e/pathy-0.10.1-py3-none-any.whl")
    version("0.10.0", sha256="205d6da31c47334227d364ad8c13b848eb3254701553eb179f3faaec3abd0204", url="https://pypi.org/packages/28/cf/ed6851cb49da2fbf7f929c0d538ffde55bb7d12a3ca532918e843915f3f0/pathy-0.10.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-google-cloud-storage@1.26:1", when="@:0.2")
        depends_on("py-pathlib-abc@0.1.1:0.1", when="@0.11:")
        depends_on("py-smart-open@5.2.1:6", when="@0.10.1:")
        depends_on("py-smart-open@5.2.1:5", when="@0.6.2:0.10.0")
        depends_on("py-typer@0.3:", when="@0.1.3:")

