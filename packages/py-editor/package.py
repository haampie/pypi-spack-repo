##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyEditor(PythonPackage):
    version("1.6.6", sha256="e818e6913f26c2a81eadef503a2741d7cca7f235d20e217274a009ecd5a74abf", url="https://pypi.org/packages/1b/c2/4bc8cd09b14e28ce3f406a8b05761bed0d785d1ca8c2a5c6684d884c66a2/editor-1.6.6-py3-none-any.whl")
    version("1.6.5", sha256="53c26dd78333b50b8cdcf67748956afa75fabcb5bb25e96a00515504f58e49a8", url="https://pypi.org/packages/51/e3/a2f003fd307b066a3c6dbbe440ee8fe3a43495c577d1618fd6d332b4e217/editor-1.6.5-py3-none-any.whl")
    version("1.6.4", sha256="b58f1de77e1f1e78bf38c2fee755fc2ea430aaccfc4425beace4adbea64b490a", url="https://pypi.org/packages/0c/cb/7499428099b2f19bffedd2a9e69b2c089835f724d304b040d64660089c86/editor-1.6.4-py3-none-any.whl")
    version("1.6.3", sha256="b5bdfc509ad49f806ae4e08cba7b487183f094915bffc8d727eb97c791fdd067", url="https://pypi.org/packages/30/ae/5218c1f9502e4f1cce63ecdb2fde93f41401a0192de65920097648cd2792/editor-1.6.3-py3-none-any.whl")
    version("1.6.2", sha256="256f3d33ea8214ad5889066eccc32c0eb89e5fc2d2414a7ff57324f8608ca8d0", url="https://pypi.org/packages/36/bf/4780abf566cb8933e73e7bda34625f10ec9cc9bd1758448657495beffff0/editor-1.6.2-py3-none-any.whl")
    version("1.6.1", sha256="478612c9cebaf98be99afd4296ccddad10319d6be744735ef40963c838728530", url="https://pypi.org/packages/48/4c/6f350ebeeaf931d4b6cc3bdf8f054237fdf15284f459fc636dd061bdb2ba/editor-1.6.1-py3-none-any.whl")
    version("1.6.0", sha256="70e6518eb0a0cf3e691c1d5cf1b84022698704da0a47de1857caf4af819a1149", url="https://pypi.org/packages/d1/57/c9af62f76cf9c092ff38f2578fe740d7e26b5b63f5957474c7af8a1c3f70/editor-1.6.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-runs", when="@1.1:1.2,1.5:")
        depends_on("py-xmod", when="@:1.2,1.5:")

