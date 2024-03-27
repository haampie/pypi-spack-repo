##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTaskgroup(PythonPackage):
    version("0.0.0-alpha4", sha256="5c1bd0e4c06114e7a4128583ab75c987597d5378a33948a3b74c662b90f61277", url="https://pypi.org/packages/2c/e5/0f8dac3d9e6314f60a725cdc9ec01f45591ddd720e59f6a4ff8bdcdf82cd/taskgroup-0.0.0a4-py2.py3-none-any.whl")
    version("0.0.0-alpha3", sha256="b367ea496124ace077632b872ffb27f07328c05dc0ec1ac94def2ac65de70473", url="https://pypi.org/packages/4b/56/54a4def6c1e9cd7aa24f5a4d0c13f090a4f1a6cf71b8b833fdfd3f8afc16/taskgroup-0.0.0a3-py2.py3-none-any.whl")
    version("0.0.0-alpha2", sha256="bd408de32661d521c84ebd34b5195b42ac0b990fc03cddab894ed9e26550b79b", url="https://pypi.org/packages/2e/c6/48b5db55e67140ea56bf4d672bf35353ea7068e5cfa2c6f4c204405284e7/taskgroup-0.0.0a2-py2.py3-none-any.whl")
    version("0.0.0-alpha1", sha256="0be1ec5af46c26b646f2fc3ecc7c9ac01bc9bbf490694c2757b4758566ba6713", url="https://pypi.org/packages/86/69/efdc16b9eff7ab6131a6a8ac994a5d8416dcbf6b3654ec5575e7736af2d9/taskgroup-0.0.0a1-py2.py3-none-any.whl")
    version("0.0.0-alpha0", sha256="53467b8a9a91b1326cd5ebbadf3a06790b0eef4e813a24d90d79cea6871156c6", url="https://pypi.org/packages/69/36/9cf067c35fc4020210cae6ae3d99cb4b90d08ddd6a1f57202cbe49a42e88/taskgroup-0.0.0a0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-exceptiongroup", when="@0.0.0-alpha1:")

