# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPastedeploy(PythonPackage):
    # BEGIN VERSIONS
    version("3.1.0", sha256="76388ad53a661448d436df28c798063108f70e994ddc749540d733cdbd1b38cf", url="https://pypi.org/packages/85/30/cdddd9a88969683a59222a6d61cd6dce923977f2e9f9ffba38e1324149cd/PasteDeploy-3.1.0-py3-none-any.whl")
    version("3.0.1", sha256="6195c921b1c3ed9722e4e3e6aa29b70deebb2429b4ca3ff3d49185c8e80003bb", url="https://pypi.org/packages/ab/8a/1ed1b777d0105bfbf82d83b0a93e4e41d35ed459ab37aaf39f46bc0e9a63/PasteDeploy-3.0.1-py3-none-any.whl")
    version("3.0", sha256="6c792d12ddc1840fa2dbecd8241f8f94da1230032f53fadeb59412de458ecb6e", url="https://pypi.org/packages/fa/4f/8652b63a66468119de491e62dc64abcb0674874935cfe865e04c7623be3e/PasteDeploy-3.0-py3-none-any.whl")
    version("2.1.1", sha256="14923cfd6ad4281b570693afc278bab5076fbdd4cd15aa9d99b042d694aa4217", url="https://pypi.org/packages/8f/0b/d47ea894587f3155f8c4520aa74d57c856189d0bbe27e831881d655a3386/PasteDeploy-2.1.1-py2.py3-none-any.whl")
    version("2.1.0", sha256="bc6578735a32c77435a3e0769426983d3df6dc53a7229290c495ec10aefb81a5", url="https://pypi.org/packages/fb/18/196e5070ced83bb81edd83c79545232d1d2ec55e3a099a146a3333244a6b/PasteDeploy-2.1.0-py2.py3-none-any.whl")
    version("2.0.1", sha256="fe53697ec2754703096b75d0ba29112b0590b4ce46726fe4f9408fd006e4eefc", url="https://pypi.org/packages/67/0c/faa9971b2e5e048b3b30008d04c72e4d5f63b42f48937c169acce2c5e70a/PasteDeploy-2.0.1-py2.py3-none-any.whl")
    version("2.0.0", sha256="3a2fb2a52a29154aabfdb0432d14bcbeefcf75c22b395009435023e7e513557c", url="https://pypi.org/packages/d3/f9/2342db435959dd1b4937592110939884d96e902f39e47d6ccc52f73a8381/PasteDeploy-2.0.0-py2.py3-none-any.whl")
    version("1.5.2", sha256="39973e73f391335fac8bc8a8a95f7d34a9f42e2775600ce2dc518d93b37ef943", url="https://pypi.org/packages/31/28/51201a54aeecbd02eff767d17050b302f6fd98fdfecb4e3f4c9301ba6ef8/PasteDeploy-1.5.2-py2.py3-none-any.whl")
    version("1.5.1", sha256="63218790313cc5b33cd6b201349c92aefac55111f308745376f4cabe213a142e", url="https://pypi.org/packages/34/ae/6485b6c5c6326e803f2b9af577b339b0bda89c44d3fb193137ba442527b5/PasteDeploy-1.5.1-py2.py3-none-any.whl")
    version("1.5.0", sha256="61c205633adae996cd0e306451c8a28deca0499524e2a38c65ff1570f35a8a53", url="https://pypi.org/packages/b0/a5/e83f581f1da123ae29b0386c3d4156d7e1a77d36af6415dff04aada44422/PasteDeploy-1.5.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-setuptools", when="@2.1.1:2")
    # END DEPENDENCIES

