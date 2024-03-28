# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyUvicorn(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.29.0", sha256="2c2aac7ff4f4365c206fd773a39bf4ebd1047c238f8b8268ad996829323473de", url="https://pypi.org/packages/73/f5/cbb16fcbe277c1e0b8b3ddd188f2df0e0947f545c49119b589643632d156/uvicorn-0.29.0-py3-none-any.whl")
    version("0.28.1", sha256="5162f6d652f545be91b1feeaee8180774af143965ca9dc8a47ff1dc6bafa4ad5", url="https://pypi.org/packages/6e/12/57c09286f0293e73343e95427072ec7b700324f858637887c5b7e9c687b7/uvicorn-0.28.1-py3-none-any.whl")
    version("0.28.0", sha256="6623abbbe6176204a4226e67607b4d52cc60ff62cda0ff177613645cefa2ece1", url="https://pypi.org/packages/25/bd/c20daf18824b1552d37579fc2f8cc147355c113d55aff21211443a2f89b9/uvicorn-0.28.0-py3-none-any.whl")
    version("0.27.1", sha256="5c89da2f3895767472a35556e539fd59f7edbe9b1e9c0e1c99eebeadc61838e4", url="https://pypi.org/packages/d9/fd/bac111726b6c651f1fa5563145ecba5ff70d36fb140a55e0d79b60b9d65e/uvicorn-0.27.1-py3-none-any.whl")
    version("0.27.0.post1", sha256="4b85ba02b8a20429b9b205d015cbeb788a12da527f731811b643fd739ef90d5f", url="https://pypi.org/packages/c7/f3/29caa83f5795b20ed3aca357c648f3ae995ff6ff08e38b22387017abbdc5/uvicorn-0.27.0.post1-py3-none-any.whl")
    version("0.27.0", sha256="890b00f6c537d58695d3bb1f28e23db9d9e7a17cbcc76d7457c499935f933e24", url="https://pypi.org/packages/ec/00/2555ae5c4c8550ffccf8eea97476750bd1cfc0880b4b3ab7237dff4b01d7/uvicorn-0.27.0-py3-none-any.whl")
    version("0.26.0", sha256="cdb58ef6b8188c6c174994b2b1ba2150a9a8ae7ea5fb2f1b856b94a815d6071d", url="https://pypi.org/packages/81/d1/90d8a1c0de615eb849ff0cf5cc5dfbad0e360a8bf0f5f2d41dc54260bfce/uvicorn-0.26.0-py3-none-any.whl")
    version("0.25.0", sha256="ce107f5d9bd02b4636001a77a4e74aab5e1e2b146868ebbad565237145af444c", url="https://pypi.org/packages/26/59/fddd9df489fe27f492cc97626e03663fb3b9b6ef7ce8597a7cdc5f2cbbad/uvicorn-0.25.0-py3-none-any.whl")
    version("0.24.0.post1", sha256="7c84fea70c619d4a710153482c0d230929af7bcf76c7bfa6de151f0a3a80121e", url="https://pypi.org/packages/7e/17/4b7a76fffa7babf397481040d8aef2725b2b81ae19f1a31b5ca0c17d49e6/uvicorn-0.24.0.post1-py3-none-any.whl")
    version("0.24.0", sha256="3d19f13dfd2c2af1bfe34dd0f7155118ce689425fdf931177abe832ca44b8a04", url="https://pypi.org/packages/ed/0c/a9b90a856bbdd75bf71a1dd191af1e9c9ac8a272ed337f7200950c3d3dd4/uvicorn-0.24.0-py3-none-any.whl")
    version("0.20.0", sha256="c3ed1598a5668208723f2bb49336f4509424ad198d6ab2615b7783db58d919fd", url="https://pypi.org/packages/96/f3/f39ac8ac3bdf356b4934b8f7e56173e96681f67ef0cd92bd33a5059fae9e/uvicorn-0.20.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("standard", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-click@7:", when="@0.15:")
        depends_on("py-colorama@0.4:", when="@0.13:+standard platform=windows")
        depends_on("py-h11@0.8:", when="@0.13:")
        depends_on("py-httptools@0.5:", when="@0.19:+standard")
        depends_on("py-python-dotenv@0.13:", when="@0.13:+standard")
        depends_on("py-pyyaml@5.1:", when="@0.13:+standard")
        depends_on("py-typing-extensions@4:", when="@0.23.1: ^python@:3.10")
        depends_on("py-uvloop@0.14.0:0.14,0.15.2:", when="@0.13.4:+standard platform=linux")
        depends_on("py-uvloop@0.14.0:0.14,0.15.2:", when="@0.13.4:+standard platform=freebsd")
        depends_on("py-uvloop@0.14.0:0.14,0.15.2:", when="@0.13.4:+standard platform=darwin")
        depends_on("py-uvloop@0.14.0:0.14,0.15.2:", when="@0.13.4:+standard platform=cray")
        depends_on("py-watchfiles@0.13:", when="@0.18:+standard")
        depends_on("py-websockets@10.4:", when="@0.20:+standard")
    # END DEPENDENCIES

