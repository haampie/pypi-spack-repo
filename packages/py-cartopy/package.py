##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCartopy(PythonPackage):
    version("0.22.0", sha256="b300f90120931d43f11ef87c064ea1dacec1b59a4940aa76ebf82cf09548bb49", url="https://pypi.org/packages/c8/99/e2ad8a60df598de02904867ec83bc9d785b6534a503aecc9426889aa807e/Cartopy-0.22.0.tar.gz")
    version("0.21.1", sha256="89d5649712c8582231c6e11825a04c85f6f0cee94dbb89e4db23eabca1cc250a", url="https://pypi.org/packages/e8/11/ed3e364b3910f0951821e6b5a03a03ce425464b72aa3da08d47b78ae17bd/Cartopy-0.21.1.tar.gz")
    version("0.21.0", sha256="ce1d3a28a132e94c89ac33769a50f81f65634ab2bd40556317e15bd6cad1ce42", url="https://pypi.org/packages/40/0c/b673fb89eadf798654652df3dda4b8229ca747568976b7a919d7d65e656e/Cartopy-0.21.0.tar.gz")
    version("0.20.3", sha256="0d60fa2e2fbd77c4d1f6b1f9d3b588966147f07c1b179d2d34570ac1e1b49006", url="https://pypi.org/packages/98/a9/0e4000eabadfcff6373c0fec790863b543b919cbfec18aed60d71ba67d5d/Cartopy-0.20.3.tar.gz")
    version("0.20.2", sha256="4d08c198ecaa50a6a6b109d0f14c070e813defc046a83ac5d7ab494f85599e35", url="https://pypi.org/packages/f6/55/1e1c737dc9436b320deead73d1c455ddbb74b8b6992081863492f6f6378a/Cartopy-0.20.2.tar.gz")
    version("0.20.1", sha256="91f87b130e2574547a20cd634498df97d797abd12dcfd0235bc0cdbcec8b05e3", url="https://pypi.org/packages/fc/59/aa52698e3838f4cd0e7eaa75bd86837e9e0b05041dbdaee3cda2fffced06/Cartopy-0.20.1.tar.gz")
    version("0.20.0", sha256="eae58aff26806e63cf115b2bce9477cedc4aa9f578c5e477b2c25cfa404f2b7a", url="https://pypi.org/packages/0f/c0/58453b036e79046d211f083880d58dcce787e7e07647ac25dc46c6555099/Cartopy-0.20.0.tar.gz")
    version("0.19.0.post1", sha256="4b8b4773a98ed7009fe17d9b6ec87ac3ac62b7d14634d7768c190eadc647d576", url="https://pypi.org/packages/ed/ca/524ce33692df3faeaa56852fb6a33b0b410be94cc288417565b96fef3f64/Cartopy-0.19.0.post1.tar.gz")
    version("0.19.0", sha256="8e902a40f2a11bcf4a72e6e42c6eac335be23716377e42d99dc4628b7d84e790", url="https://pypi.org/packages/b7/15/c466caf7aeff118c02aedefbe80caf77effda86bcb43ccb6c5e0655c4238/Cartopy-0.19.0.tar.gz")
    version("0.18.0", sha256="7ffa317e8f8011e0d965a3ef1179e57a049f77019867ed677d49dcc5c0744434", url="https://pypi.org/packages/46/c1/04e50c9986842f00f7db0e7a65caa896840050d7328f74e5b7437aa01179/Cartopy-0.18.0.tar.gz")
    version("0.17.0", sha256="424bd9e9ddef6e48cbdee694ce589ec431be8591f15b6cb93cb2b333a29b2c61", url="https://pypi.org/packages/e5/92/fe8838fa8158931906dfc4f16c5c1436b3dd2daf83592645b179581403ad/Cartopy-0.17.0.tar.gz")
    version("0.16.0", sha256="f23dffa101f43dd91e866a49ebb5f5048be2a24ab8a921a5c07edabde746d9a4", url="https://pypi.org/packages/f5/7a/4a16db7c81f11b3c5889c5b913d9a5724c704a6947c5a87ec59c4a8985ac/Cartopy-0.16.0.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.22:")

