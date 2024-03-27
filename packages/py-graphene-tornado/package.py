##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGrapheneTornado(PythonPackage):
    version("2.6.1", sha256="291c61452917f9fa014ec69d73cef1f74f7f2f39fd85aa6a84a7e20332b7ce4d", url="https://pypi.org/packages/e2/fe/068c5e3adeaeb3245a1756748c311d7214403501c4344baf66a63d719107/graphene_tornado-2.6.1-py2.py3-none-any.whl")
    version("2.6.0", sha256="5ebbe0f5bfa41dd27b6c1311286534a93365938b76d36d068e21600d7fa2de97", url="https://pypi.org/packages/40/59/bf33621d743b8a1205331dcaca4aa8f4a9d049bcaa013078c8543549fcc8/graphene_tornado-2.6.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-graphene@2.1:2", when="@2.1.1:2.1,2.3:2")
        depends_on("py-jinja2@2.10.1:", when="@2.0.3:2.1,2.3:2,3.0.0-beta2:")
        depends_on("py-six@1.10:", when="@2.0.2:2.1,2.3:2,3.0.0-beta2:")
        depends_on("py-tornado@5.1:", when="@2.0.2:2.1,2.3:2")
        depends_on("py-werkzeug@0.12.2:0.12", when="@2.0.2:2.1,2.3:2")

