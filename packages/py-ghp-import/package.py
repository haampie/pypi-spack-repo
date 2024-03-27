##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGhpImport(PythonPackage):
    version("2.1.0", sha256="8337dd7b50877f163d4c0289bc1f1c7f127550241988d568c1db512c4324a619", url="https://pypi.org/packages/f7/ec/67fbef5d497f86283db54c22eec6f6140243aae73265799baaaa19cd17fb/ghp_import-2.1.0-py3-none-any.whl")
    version("2.0.2", sha256="5f8962b30b20652cdffa9c5a9812f7de6bcb56ec475acac579807719bf242c46", url="https://pypi.org/packages/d5/42/a00220ae61d06b5bb288c0006bfd32bd61b4ae61adaef61fe8ad3a8ff9c3/ghp_import-2.0.2-py3-none-any.whl")
    version("2.0.1", sha256="8241a8e9f8dd3c1fafe9696e6e081b57a208ef907e9939c44e7415e407ab40ea", url="https://pypi.org/packages/c1/9d/8a0e7c289232fff7f96ea30f1800d6003e98fa25f714a94daf17fa89d079/ghp_import-2.0.1-py3-none-any.whl")
    version("2.0.0", sha256="281b6aa55aafe2e3babaa6db976c343968f8ba9487d30887f286af71c107cefb", url="https://pypi.org/packages/0c/f1/00921e0f3ff336df14b6d39801d21252a34d32ddd9b3cb05625b1a98d2fe/ghp-import-2.0.0.tar.gz")
    version("1.1.0", sha256="c22a9ce10c37753e2688d164d765a700dae4b8d79fa6db0a2c3132ba7881894f", url="https://pypi.org/packages/15/6e/9cfffe6856f48852a3dc78fa6c1be989a2b22d424a80d1e5f92fc1dac02d/ghp-import-1.1.0.tar.gz")
    version("1.0.1", sha256="61aad8dae5988d548b24cfa31180c49fc704418523c3e7fffd39d368bd82d406", url="https://pypi.org/packages/16/8b/8169257160314d00881508e4a3e23bded8bfc6bce3cdbddeaa73f015266c/ghp-import-1.0.1.tar.gz")
    version("1.0.0", sha256="65e4d854dd0980096fd950a323d699daad4ff8007b8daa7e7ca60d57dfa00e1b", url="https://pypi.org/packages/ef/03/c674cf7f106b7be8719e0202537edd754040f786e9dc4799cd2c7d4d1743/ghp-import-1.0.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-python-dateutil@2.8.1:", when="@2.0.1:")

