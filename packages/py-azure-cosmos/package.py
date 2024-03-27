##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureCosmos(PythonPackage):
    version("4.0.0", sha256="2dbcb33e091b6c3284026472cf3fc3d3ca3cc8bfdc200d469dbd9089f8ba0e54", url="https://pypi.org/packages/af/42/f9df4e1cba74ee5058782ef838b0f6caa0c271670e054c263d69702884e2/azure_cosmos-4.0.0-py2.py3-none-any.whl")
    version("3.2.0", sha256="313e766bcf5a1779802c274dec94d5b9cc0e4d0d269489c56606fd2464070fad", url="https://pypi.org/packages/4a/4f/23ffc8e870df94ea6def08121245301e763eaee7236fb8c3d02d5ff66687/azure_cosmos-3.2.0-py2.py3-none-any.whl")
    version("3.1.2", sha256="7f8ac99e4e40c398089fc383bfadcdc83376f72b88532b0cac0b420357cd08c7", url="https://pypi.org/packages/9c/47/c77b0008c9f3bf90c533a7f538b149c7cd28d2d9c5303d3fc017ada6c09c/azure-cosmos-3.1.2.tar.gz")
    version("3.1.1", sha256="f3922891baf59742556cbc8bd96aaba4f582a6a8f9bbccb8f2b0376539a21761", url="https://pypi.org/packages/42/0a/b004ff6f20d851460c0e02f474642e86552fc21d893fe51ef7b4b3bf4a07/azure-cosmos-3.1.1.tar.gz")
    version("3.1.0", sha256="f4a718cc4d26e90ad22abbd0d208f43040cbb4b7768144632dd3042fec9da5a4", url="https://pypi.org/packages/5d/24/d7dca6df234404d8a11c9df59533d79331e8ba20c471cb2e7d73efbaf0d2/azure-cosmos-3.1.0.tar.gz")
    version("3.0.2", sha256="081b3f592c3cf88c4d423fbb8184732cae0427cc5188cfed4835d9cdb64fa5f7", url="https://pypi.org/packages/f8/af/d1e22dcc61ba299f0786518e68f2287b73be027b16ee0120548e652a1aa8/azure-cosmos-3.0.2.tar.gz")

    with default_args(type="run"):
        depends_on("py-azure-core@1.0.0:", when="@4.0.0-beta5:4.3.0-beta1")
        depends_on("py-requests@2.10:", when="@:3.1.1,3.2:4.0.0-alpha2")
        depends_on("py-six@1.6:", when="@:3.1.1,3.2:4.2")

