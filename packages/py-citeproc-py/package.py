# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCiteprocPy(PythonPackage):
    # BEGIN VERSIONS
    version("0.6.0", sha256="ca4c7a5158d6f68cb00a89bb47d9aa0eec7b89b18e574eb08a061b011b602bbe", url="https://pypi.org/packages/23/e8/5e42b253c40d1087a4ef341d78d88b7a9beb46e6ab9cec19c75e4e3cba78/citeproc_py-0.6.0-py3-none-any.whl")
    version("0.5.1", sha256="388985d08fc47eadb6406e3e1b53576cb08b52aca86e5b41e3a95f6349d17094", url="https://pypi.org/packages/a2/a2/b202f24040ac601cbdcca10d169558c5339ef0ec3ce95894e6bf1c72caa5/citeproc_py-0.5.1-py2.py3-none-any.whl")
    version("0.5.0", sha256="00f8919766fb07ddc6ace5e5b88282809ecae738b031bd32edeb762a31367113", url="https://pypi.org/packages/a9/c3/0862d9204c02428b9f63fed449b50b1b009573bfb1da6119e1cc780de2b9/citeproc-py-0.5.0.tar.gz")
    version("0.4.0", sha256="ee1569e8b1f2c057c7893bbb067986bc362a6c861009d310700a12a1a0107b57", url="https://pypi.org/packages/22/9a/d3383c4af068d0e82ec71fd88c74ae55e85b49c0acaf9951b3075c8a3b40/citeproc_py-0.4.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-lxml", when="@0.5.1:")
    # END DEPENDENCIES

