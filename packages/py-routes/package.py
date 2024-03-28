# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRoutes(PythonPackage):
    # BEGIN VERSIONS
    version("2.5.1", sha256="fab5a042a3a87778eb271d053ca2723cadf43c95b471532a191a48539cb606ea", url="https://pypi.org/packages/9b/d4/d3c7d029de6287ff7bd048e628920d4336b4f8d82cfc00ff078bdbb212a3/Routes-2.5.1-py2.py3-none-any.whl")
    version("2.5.0", sha256="60544f0f0220a0899c704cc5d1eb49a7c32eb3f8b60c1a24817af984b1be1ed7", url="https://pypi.org/packages/53/1b/24b3f2032ee367804d9dfaa4d9b2fd141dcf71f93b08350671ab2469d6b7/Routes-2.5.0-py2.py3-none-any.whl")
    version("2.4.1", sha256="d64b8ae22bef127d856afd9266a3e4cfc9e0dda0e120195e38268a95d20de135", url="https://pypi.org/packages/50/50/c1c0666778c7986368896b0e0f640e41160a43cd3ffc7ff008f61f0f6cfd/Routes-2.4.1-py2.py3-none-any.whl")
    version("2.3.1", sha256="8854ba8c2e18cf731ec9ef1bd78dee73dd24f3aeac336b5143eefdf8867ebe8a", url="https://pypi.org/packages/26/ef/3a37527b7c3451bd92a479b6a719bedb2f314b4373c39dcd21961f4471f0/Routes-2.3.1-py2.py3-none-any.whl")
    version("2.3", sha256="01a10b4edf25eb63b3d268f4e5de8b792bc9fb62487e81c30b79ec17d762ac9e", url="https://pypi.org/packages/2c/a2/08cada091c251cb6c598f0e422e0ab5c0b3deb1f98ed2c04fb162381d538/Routes-2.3-py2-none-any.whl")
    version("2.2", sha256="1a41a5b61e8715300841395684527cb6cc85848053ffb6d42b75b34a2fa9bc8b", url="https://pypi.org/packages/22/34/017eb6771d63d5d0fde58d490f4a1a3a911cf2c6b7d7f75a884a3963e5dd/Routes-2.2-py2-none-any.whl")
    version("2.1", sha256="ebf4126e244cf11414653b5ba5f27ed4abfad38b906a01e5d4c93d3ce5568ea3", url="https://pypi.org/packages/f6/e8/ea8fe1eefe02f12e80cbd5878b8fdb1c451d0381f6c5ee98099e6ed0e138/Routes-2.1.tar.gz")
    version("2.0", sha256="0860aa5a4bbccdd063c1281b02ac55548247290afede28d692fc993d27e7aaec", url="https://pypi.org/packages/b1/3d/3c8deb7fd918e60f24cfac7f4271bdc37fedf88950caa349a87a72050cde/Routes-2.0-py27-none-any.whl")
    version("1.13", sha256="cc03d1a357cdb7af82e3909ee8ff93cb2b2afb48aca23bfde0117d6f49f624a7", url="https://pypi.org/packages/88/d3/259c3b3cde8837eb9441ab5f574a660e8a4acea8f54a078441d4d2acac1c/Routes-1.13.tar.gz")
    version("1.12.3", sha256="eacc0dfb7c883374e698cebaa01a740d8c78d364b6e7f3df0312de042f77aa36", url="https://pypi.org/packages/d3/a2/6f8fbc920d1410859e9bbb14b3273f9ade6aebae281204f15cc518d8f969/Routes-1.12.3.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-repoze-lru@0.3:", when="@2.4:")
        depends_on("py-six", when="@2.4:")
    # END DEPENDENCIES

