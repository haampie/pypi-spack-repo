# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTerminado(PythonPackage):
    # BEGIN VERSIONS
    version("0.17.1", sha256="8650d44334eba354dd591129ca3124a6ba42c3d5b70df5051b6921d506fdaeae", url="https://pypi.org/packages/84/a7/c7628d79651b8c8c775d27b374315a825141b5783512e82026fb210dd639/terminado-0.17.1-py3-none-any.whl")
    version("0.15.0", sha256="0d5f126fbfdb5887b25ae7d9d07b0d716b1cc0ccaacc71c1f3c14d228e065197", url="https://pypi.org/packages/85/be/6b89563289bc8df86f4089efcc4e28d39feaaa4c0863ddcb32dee18d0957/terminado-0.15.0-py3-none-any.whl")
    version("0.12.1", sha256="09fdde344324a1c9c6e610ee4ca165c4bb7f5bbf982fceeeb38998a988ef8452", url="https://pypi.org/packages/cb/17/b1162b39786c44e14d30ee557fbf41276c4a966dab01106c15fb70f5c27a/terminado-0.12.1-py3-none-any.whl")
    version("0.8.3", sha256="a43dcb3e353bc680dd0783b1d9c3fc28d529f190bc54ba9a229f72fe6e7a54d7", url="https://pypi.org/packages/ff/96/1d9a2c23990aea8f8e0b5c3b6627d03196a73771a17a2d9860bbe9823ab6/terminado-0.8.3-py2.py3-none-any.whl")
    version("0.8.2", sha256="d9d012de63acb8223ac969c17c3043337c2fcfd28f3aea1ee429b345d01ef460", url="https://pypi.org/packages/a7/56/80ea7fa66565fa75ae21ce0c16bc90067530e5d15e48854afcc86585a391/terminado-0.8.2-py2.py3-none-any.whl")
    version("0.8.1", sha256="65011551baff97f5414c67018e908110693143cfbaeb16831b743fe7cad8b927", url="https://pypi.org/packages/2e/20/a26211a24425923d46e1213b376a6ee60dc30bcdf1b0c345e2c3769deb1c/terminado-0.8.1-py2.py3-none-any.whl")
    version("0.6", sha256="2c0ba1f624067dccaaead7d2247cfe029806355cef124dc2ccb53c83229f0126", url="https://pypi.org/packages/58/59/aabe84fce2f45da10165435cec204d982863e176f6849a4a4fe2652a20a8/terminado-0.6.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-ptyprocess", when="@0.7")
        depends_on("py-tornado@6.1:", when="@0.15:")
        depends_on("py-tornado@4:", when="@0.7:0.13")

        # marker: os_name != "nt"
        # depends_on("py-ptyprocess", when="@0.8:")

        # marker: os_name == "nt"
        # depends_on("py-pywinpty@1.1:", when="@0.10:")
        # depends_on("py-pywinpty@0.5:", when="@0.8.1:0.9.4")
    # END DEPENDENCIES

