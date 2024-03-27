##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTerminado(PythonPackage):
    version("0.18.1", sha256="a4468e1b37bb318f8a86514f65814e1afc977cf29b3992a4500d9dd305dcceb0", url="https://pypi.org/packages/6a/9e/2064975477fdc887e47ad42157e214526dcad8f317a948dee17e1659a62f/terminado-0.18.1-py3-none-any.whl")
    version("0.18.0", sha256="87b0d96642d0fe5f5abd7783857b9cab167f221a39ff98e3b9619a788a3c0f2e", url="https://pypi.org/packages/69/df/deebc9fb14a49062a3330f673e80b100e665b54d998163b3f62620b6240c/terminado-0.18.0-py3-none-any.whl")
    version("0.17.1", sha256="8650d44334eba354dd591129ca3124a6ba42c3d5b70df5051b6921d506fdaeae", url="https://pypi.org/packages/84/a7/c7628d79651b8c8c775d27b374315a825141b5783512e82026fb210dd639/terminado-0.17.1-py3-none-any.whl")
    version("0.17.0", sha256="bf6fe52accd06d0661d7611cc73202121ec6ee51e46d8185d489ac074ca457c2", url="https://pypi.org/packages/4c/27/3ddec4ed8f8312d9c4774ae0a62469d29637176df8a5a6321070aa0edc97/terminado-0.17.0-py3-none-any.whl")
    version("0.16.0", sha256="3e995072a7178a104c41134548ce9b03e4e7f0a538e9c29df4f1fbc81c7cfc75", url="https://pypi.org/packages/8a/84/85cec8c1901b00d2c997764b1d717be4c814e8a02678e9c80b59f865660d/terminado-0.16.0-py3-none-any.whl")
    version("0.15.0", sha256="0d5f126fbfdb5887b25ae7d9d07b0d716b1cc0ccaacc71c1f3c14d228e065197", url="https://pypi.org/packages/85/be/6b89563289bc8df86f4089efcc4e28d39feaaa4c0863ddcb32dee18d0957/terminado-0.15.0-py3-none-any.whl")
    version("0.13.3", sha256="874d4ea3183536c1782d13c7c91342ef0cf4e5ee1d53633029cbc972c8760bd8", url="https://pypi.org/packages/e6/87/a6f72009fa1c6528fd016a199f5f0199841e82e72d726f55a6a96fcc6b30/terminado-0.13.3-py3-none-any.whl")
    version("0.13.2", sha256="d61f112f3beb7271d953d3934f056af185f6be0750303581fa1c511379a8a5d0", url="https://pypi.org/packages/89/48/8cb28fd9ed7c0bba3fc12638476bfabfae1ec401a9a3ad3c230c378a7828/terminado-0.13.2-py3-none-any.whl")
    version("0.13.1", sha256="f446b522b50a7aa68b5def0a02893978fb48cb82298b0ebdae13003c6ee6f198", url="https://pypi.org/packages/b9/a5/7cd16097bdb23e74b220cce6aed73cf3f3f5167122355ab1164612d8170f/terminado-0.13.1-py3-none-any.whl")
    version("0.13.0", sha256="50a18654ad0cff153fdeb58711c9a7b25e0e2b74fb721dbaddd9e80d5612fac6", url="https://pypi.org/packages/02/6c/c3b012d026678d5cac6d4e26d6857145e22b94ccef195e7c483c3f6c3731/terminado-0.13.0-py3-none-any.whl")
    version("0.12.1", sha256="09fdde344324a1c9c6e610ee4ca165c4bb7f5bbf982fceeeb38998a988ef8452", url="https://pypi.org/packages/cb/17/b1162b39786c44e14d30ee557fbf41276c4a966dab01106c15fb70f5c27a/terminado-0.12.1-py3-none-any.whl")
    version("0.8.3", sha256="a43dcb3e353bc680dd0783b1d9c3fc28d529f190bc54ba9a229f72fe6e7a54d7", url="https://pypi.org/packages/ff/96/1d9a2c23990aea8f8e0b5c3b6627d03196a73771a17a2d9860bbe9823ab6/terminado-0.8.3-py2.py3-none-any.whl")
    version("0.8.2", sha256="d9d012de63acb8223ac969c17c3043337c2fcfd28f3aea1ee429b345d01ef460", url="https://pypi.org/packages/a7/56/80ea7fa66565fa75ae21ce0c16bc90067530e5d15e48854afcc86585a391/terminado-0.8.2-py2.py3-none-any.whl")
    version("0.8.1", sha256="65011551baff97f5414c67018e908110693143cfbaeb16831b743fe7cad8b927", url="https://pypi.org/packages/2e/20/a26211a24425923d46e1213b376a6ee60dc30bcdf1b0c345e2c3769deb1c/terminado-0.8.1-py2.py3-none-any.whl")
    version("0.6", sha256="2c0ba1f624067dccaaead7d2247cfe029806355cef124dc2ccb53c83229f0126", url="https://pypi.org/packages/58/59/aabe84fce2f45da10165435cec204d982863e176f6849a4a4fe2652a20a8/terminado-0.6.tar.gz")

    with default_args(type="run"):
        depends_on("py-ptyprocess", when="@0.7")
        depends_on("py-tornado@6.1:", when="@0.15:")
        depends_on("py-tornado@4:", when="@0.7:0.13")

        # marker: os_name != "nt"
        # depends_on("py-ptyprocess", when="@0.8:")

        # marker: os_name == "nt"
        # depends_on("py-pywinpty@1.1:", when="@0.10:")
        # depends_on("py-pywinpty@0.5:", when="@0.8.1:0.9.4")

