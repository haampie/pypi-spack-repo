##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDxtExplorer(PythonPackage):
    version("0.3", sha256="e8779bdfc36032087a2244963c21c8fbe71e068f8e177f76b037f3d605b3f852", url="https://pypi.org/packages/0e/45/c9028d618a9808331afc6a6fd0a9a036d9802dfb6c5ce5c800f79c75108e/dxt_explorer-0.3-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-argparse")
        depends_on("py-pandas")

