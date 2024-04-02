# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRuamelYaml(PythonPackage):
    # BEGIN VERSIONS
    version("0.17.32", sha256="23cd2ed620231677564646b0c6a89d138b6822a0d78656df7abda5879ec4f447", url="https://pypi.org/packages/d9/0e/2a05efa11ea33513fbdf4a2e2576fe94fd8fa5ad226dbb9c660886390974/ruamel.yaml-0.17.32-py3-none-any.whl")
    version("0.17.16", sha256="ea21da1198c4b41b8e7a259301cc9710d3b972bf8ba52f06218478e6802dd1f1", url="https://pypi.org/packages/d3/cc/248dfb697bb98152c187ced584e505124ed952529d7f8e74b28f6f4d6f31/ruamel.yaml-0.17.16-py3-none-any.whl")
    version("0.16.10", sha256="0962fd7999e064c4865f96fb1e23079075f4a2a14849bcdc5cdba53a24f9759b", url="https://pypi.org/packages/a6/92/59af3e38227b9cc14520bf1e59516d99ceca53e3b8448094248171e9432b/ruamel.yaml-0.16.10-py2.py3-none-any.whl")
    version("0.16.5", sha256="0db639b1b2742dae666c6fc009b8d1931ef15c9276ef31c0673cc6dcf766cf40", url="https://pypi.org/packages/fa/90/ecff85a2e9c497e2fa7142496e10233556b5137db5bd46f3f3b006935ca8/ruamel.yaml-0.16.5-py2.py3-none-any.whl")
    version("0.11.7", sha256="c89363e16c9eafb9354e55d757723efeff8682d05e56b0881450002ffb00a344", url="https://pypi.org/packages/f0/85/36931437a58010067837946bd31823072c827657e1a3c50ba5f4848163d4/ruamel.yaml-0.11.7.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-ruamel-yaml-clib@0.2.7:", when="@0.17.23:0.17.33 ^python@:3.11")
        depends_on("py-ruamel-yaml-clib@0.1.2:", when="@0.16.13:0.17.17 ^python@:3.9")
    # END DEPENDENCIES

