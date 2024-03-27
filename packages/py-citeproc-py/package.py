##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCiteprocPy(PythonPackage):
    version("0.6.0", sha256="ca4c7a5158d6f68cb00a89bb47d9aa0eec7b89b18e574eb08a061b011b602bbe", url="https://pypi.org/packages/23/e8/5e42b253c40d1087a4ef341d78d88b7a9beb46e6ab9cec19c75e4e3cba78/citeproc_py-0.6.0-py3-none-any.whl")
    version("0.5.1", sha256="388985d08fc47eadb6406e3e1b53576cb08b52aca86e5b41e3a95f6349d17094", url="https://pypi.org/packages/a2/a2/b202f24040ac601cbdcca10d169558c5339ef0ec3ce95894e6bf1c72caa5/citeproc_py-0.5.1-py2.py3-none-any.whl")
    version("0.5.0", sha256="00f8919766fb07ddc6ace5e5b88282809ecae738b031bd32edeb762a31367113", url="https://pypi.org/packages/a9/c3/0862d9204c02428b9f63fed449b50b1b009573bfb1da6119e1cc780de2b9/citeproc-py-0.5.0.tar.gz")
    version("0.4.0", sha256="ed513dbc76f782b5e98126d6bebbd1284841fcf199ec9dda552e2bce864adadf", url="https://pypi.org/packages/7d/dc/e905fdd6fea087b0cae77b87a28aa0ea26899946e7f9f2537c9cf618a23c/citeproc-py-0.4.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-lxml", when="@0.5.1:")

