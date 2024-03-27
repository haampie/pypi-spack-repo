##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestRemotedata(PythonPackage):
    version("0.4.1", sha256="4e840bd8733091c2a84e52528ee2c2a98aa2d4a26376ba20448f211bccd30a35", url="https://pypi.org/packages/02/70/9d5e2a5020c4721115b48fa6efa765ffff1cd679ed89049fa4c9a3c62f55/pytest_remotedata-0.4.1-py3-none-any.whl")
    version("0.4.0", sha256="48ebd360d24bc670cfeca43fff62c1866251af9cfe53f2662f225f74b3496357", url="https://pypi.org/packages/b3/b3/f08170b2a24a108f555ce517aae70628ce152e195b53d5dfac1dd33d94d2/pytest_remotedata-0.4.0-py3-none-any.whl")
    version("0.3.3", sha256="7ee2801f20afc9174676d85c9a22e8fb960c3fff94c86d80b7dc8ac5c03163f3", url="https://pypi.org/packages/0e/37/872bab8f32ea31c06596a2b2a97316cbb0f0aff90791acc750680f40ab95/pytest_remotedata-0.3.3-py3-none-any.whl")
    version("0.3.2", sha256="3be58f09116f3ce80cff9e5076cda528a84ae36d21ca9645abf782e112c281bc", url="https://pypi.org/packages/33/a3/f5b4605290b9767e1b95eb55a0464a15ce10bac1ba353953dd5b73c52312/pytest_remotedata-0.3.2-py2.py3-none-any.whl")
    version("0.3.1", sha256="15b75a38431da96a4da5e48b20a18e4dcc40d191abc199b17cb969f818530481", url="https://pypi.org/packages/4e/d0/38326c8e1af493b50c140b1be7e4c27511372c1f47f0e787a64d1ec284ea/pytest-remotedata-0.3.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-packaging", when="@0.3.3:")
        depends_on("py-pytest@4.6:", when="@0.3.3:")
        depends_on("py-pytest@3.1:", when="@0.3.2")
        depends_on("py-six", when="@0.3.2")

