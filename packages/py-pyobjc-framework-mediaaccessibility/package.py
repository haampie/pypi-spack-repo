##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkMediaaccessibility(PythonPackage):
    version("10.2", sha256="55dbf7519028fadf3ac6cb1ef185156f6df649655075a015cf87cee370255e82", url="https://pypi.org/packages/90/54/0b553941adc7e07f261c48eca5ba29dc0b3cd70fcae294fce522b8d9d26d/pyobjc_framework_MediaAccessibility-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="2301cc554396efe449b079f99a0b5812e8e3dc364195dfcd2cc2b8a9c8915f11", url="https://pypi.org/packages/c4/54/c5e6144cdb0147dd37130fdf1bfde4b2569f38108e35a508a0287b1eedaf/pyobjc_framework_MediaAccessibility-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="20b7d0dfd0680e6b19de9683025e35d2cdbdaa76ddb66ae79fea9c0deb5ac3b5", url="https://pypi.org/packages/c0/f2/60df46c976fd78882e2b93b4f13162841a2ae53ab2a678c640a3def3a802/pyobjc_framework_MediaAccessibility-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="e7919059587ffe74e79db41a3fb0846a0b3e7fa42c150d68368a477d444fdeb1", url="https://pypi.org/packages/98/85/5e3283a84d77b775e90d954c8ceb189dfb8a8f2aa79e1a2cbe39008e361d/pyobjc_framework_MediaAccessibility-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="cf285c23b5804cb46fb081d603658b75b2ffffa16ed89596ce21b7e3bfc82388", url="https://pypi.org/packages/a6/06/0b92a0a282973706c5088435bfa7bc9ffb4cb3728fe76e59173d666fca4b/pyobjc_framework_MediaAccessibility-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="991c42933ee2862f8860bf1356ce323fa5b61fe5618550c58b88e9ab3db2f2f4", url="https://pypi.org/packages/2b/eb/2a0d37e3fdccb10e621ec1fb491b13c50bddcc5cf0d1ede4e842db9808a1/pyobjc_framework_MediaAccessibility-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="dd191bb58ed82c635859f8011e44fd39ed6aa76b0e92ebf75b398132cd3413eb", url="https://pypi.org/packages/22/86/c77da54357229a33021331972a05ed5db9d8bdfdb2a101583f99fad80fa0/pyobjc_framework_MediaAccessibility-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="b0a8b156d2ae877b0e656683b97ef237af9109de6279f3f67657cf8103169715", url="https://pypi.org/packages/e5/bc/fcb0f14014d8edd857c9b9895110dc41d0ae4710fd3405c08c72ef360643/pyobjc_framework_MediaAccessibility-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="f3d05efc658c88e003a290b7b51933ab76f50352dd57ccc7df4d1350ced69e14", url="https://pypi.org/packages/e8/e4/849867f0f533b6b2d4f72d2e20e5d4d95b95728940b9a325eea7fa0f721a/pyobjc_framework_MediaAccessibility-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="c558e8d891e53bbd0f5a7c84a10fe3a4399937562c1b74fbddb8052301b9c1ec", url="https://pypi.org/packages/1f/89/02a4c1d72ab3c9e3c994f6939f2e8b11a276252ade0410b99f334b314f54/pyobjc_framework_MediaAccessibility-8.5-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-core@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-core@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-core@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-core@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-core@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-core@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-core@8.5:", when="@8.5:8.5.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-cocoa@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-cocoa@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-cocoa@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-cocoa@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-cocoa@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-cocoa@8.5:", when="@8.5:8.5.0")

