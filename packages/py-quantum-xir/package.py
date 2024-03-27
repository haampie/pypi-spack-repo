##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyQuantumXir(PythonPackage):
    version("0.2.2", sha256="5acd7955d8d854e216bdeb773afbf534d6fbe2e35ded5295ff0cacc7fd84f9fc", url="https://pypi.org/packages/98/8f/29e6eb321df7777f7b97c818f191d8db05ecbd71d0452de5fbba4605af92/quantum_xir-0.2.2-py3-none-any.whl")
    version("0.2.1", sha256="a296417eba78f79aa1bd036b10a8b85cac1841aeb71804b41090d50cfa517c5c", url="https://pypi.org/packages/2e/59/526facf31773f1cd0a3310d5a258755e47b9d1cb318330479c3c5d7c4588/quantum_xir-0.2.1-py3-none-any.whl")
    version("0.2.0", sha256="719bb1049c8042b9768cd288b9d8c6b8d8b990eb0d2c079795a6a55d5878d46b", url="https://pypi.org/packages/cb/13/2d932609a21112d2f37a223ba4416529b3972331ca4ef07ed36157aff64e/quantum_xir-0.2.0-py3-none-any.whl")
    version("0.1.1", sha256="29bfe2f7c5942e3b738fcea7ad7d1b170e118129b6c6fc428480bbb0fa4695ba", url="https://pypi.org/packages/0f/44/4695b77caf1725a1f59bcef899facc9385faa1d767624f1b934496f1e152/quantum_xir-0.1.1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-lark-parser@0.11.0:")

