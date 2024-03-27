##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRoutes(PythonPackage):
    version("2.5.1", sha256="fab5a042a3a87778eb271d053ca2723cadf43c95b471532a191a48539cb606ea", url="https://pypi.org/packages/9b/d4/d3c7d029de6287ff7bd048e628920d4336b4f8d82cfc00ff078bdbb212a3/Routes-2.5.1-py2.py3-none-any.whl")
    version("2.5.0", sha256="60544f0f0220a0899c704cc5d1eb49a7c32eb3f8b60c1a24817af984b1be1ed7", url="https://pypi.org/packages/53/1b/24b3f2032ee367804d9dfaa4d9b2fd141dcf71f93b08350671ab2469d6b7/Routes-2.5.0-py2.py3-none-any.whl")
    version("2.4.1", sha256="d64b8ae22bef127d856afd9266a3e4cfc9e0dda0e120195e38268a95d20de135", url="https://pypi.org/packages/50/50/c1c0666778c7986368896b0e0f640e41160a43cd3ffc7ff008f61f0f6cfd/Routes-2.4.1-py2.py3-none-any.whl")
    version("2.3", sha256="2d2388cecbae402d8d5cbcee1cbe4e39e742649e780b3bc63e9464c405d153d9", url="https://pypi.org/packages/9a/b8/c116afad71b0478a739240c76812e47e6c1f48c6dc1ee72e9ef947289dca/Routes-2.3.tar.gz")
    version("2.2", sha256="9fa78373d63e36c3d8af6e33cfcad743f70c012c7ad6f2c3bf89ad973b9ab514", url="https://pypi.org/packages/db/0a/ff1ad39029f07fca303be80cf2487860acb133c5fea34a606a694ebf0224/Routes-2.2.tar.gz")
    version("2.1", sha256="ebf4126e244cf11414653b5ba5f27ed4abfad38b906a01e5d4c93d3ce5568ea3", url="https://pypi.org/packages/f6/e8/ea8fe1eefe02f12e80cbd5878b8fdb1c451d0381f6c5ee98099e6ed0e138/Routes-2.1.tar.gz")
    version("2.0", sha256="6e4eb6437a9def22e1344ee8f766d7795bedfe6f615d3ea138e4035d6fbd33f8", url="https://pypi.org/packages/2e/ab/504325e47b4c79ff2f734a9324b602532a45318f1cf29dc7b6c8e9fe83c3/Routes-2.0.tar.gz")
    version("1.13", sha256="cc03d1a357cdb7af82e3909ee8ff93cb2b2afb48aca23bfde0117d6f49f624a7", url="https://pypi.org/packages/88/d3/259c3b3cde8837eb9441ab5f574a660e8a4acea8f54a078441d4d2acac1c/Routes-1.13.tar.gz")
    version("1.12.3", sha256="eacc0dfb7c883374e698cebaa01a740d8c78d364b6e7f3df0312de042f77aa36", url="https://pypi.org/packages/d3/a2/6f8fbc920d1410859e9bbb14b3273f9ade6aebae281204f15cc518d8f969/Routes-1.12.3.tar.gz")
    version("1.12.1", sha256="53062a49493685ecfe5c3f78a03deb4e4e46061e90f16b766125a52b390f3910", url="https://pypi.org/packages/91/94/a0c6c2e490e84c87be22fa5e7fd14780c70ecdae1526b595d314600d905b/Routes-1.12.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-repoze-lru@0.3:", when="@2.4:")
        depends_on("py-six", when="@2.4:")

