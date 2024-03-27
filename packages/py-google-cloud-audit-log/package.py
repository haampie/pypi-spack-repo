##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGoogleCloudAuditLog(PythonPackage):
    version("0.2.5", sha256="18b94d4579002a450b7902cd2e8b8fdcb1ea2dd4df3b41f8f82be6d9f7fcd746", url="https://pypi.org/packages/55/9b/2920117f37aff47b5b7d6081e2d5e13441d0952e5bd449babc392e03b621/google_cloud_audit_log-0.2.5-py2.py3-none-any.whl")
    version("0.2.4", sha256="29ed77fe0b21eb2d5dfb998edb59ee2adc65fea5d5ac9fcf17828d60d25b58b3", url="https://pypi.org/packages/f6/e5/2505fe28b04675a21c9187786a60cbddaf7c46a504e43b391f285a680f33/google_cloud_audit_log-0.2.4-py2.py3-none-any.whl")
    version("0.2.3", sha256="8485c6d84ff665391f526a9ac5db4c8298d68c8e87bfbc3479afdc888a93b72c", url="https://pypi.org/packages/cb/cf/d0c7a445fdcb2cadc04cfefecaf3e4658ed966e9acadfb5fce67079d7447/google_cloud_audit_log-0.2.3-py2.py3-none-any.whl")
    version("0.2.2", sha256="80aa3816e85756ec9ba84f09fb4aae4a09ad9fd6637b8392ece42ad88f6e7efe", url="https://pypi.org/packages/e8/b1/ea92cecacafc4773a2169301e5623128a0674d0fb1a06688617f3cdbc7f4/google_cloud_audit_log-0.2.2-py2.py3-none-any.whl")
    version("0.2.1", sha256="157cb17b469057d88e846a6505a74bbfd9cf52e097a44060b3f60f4f2e55ee6f", url="https://pypi.org/packages/99/a6/bd698f3e7e07a81b957742a3c5641f267eb16f96a8f7084fd404c96cfecb/google_cloud_audit_log-0.2.1-py2.py3-none-any.whl")
    version("0.2.0", sha256="ecc7f5f2168ad4014331d6397fcea3750b2d41900f0ef6d1081cd78b3a6420e9", url="https://pypi.org/packages/6c/84/cc06d8079eed8388bf5a6271dcc2103eb943c42d3acb5e4d6f589ee64b15/google_cloud_audit_log-0.2.0-py2.py3-none-any.whl")
    version("0.1.1", sha256="33a8e5fdc9d98c1c0b4b0502d723941215a586c04ccc44558ec63c16e9194152", url="https://pypi.org/packages/78/27/72f8990e50f578f7faaa33e5ad5ce52b99e4cb149b8755269a915d7c2763/google_cloud_audit_log-0.1.1-py2.py3-none-any.whl")
    version("0.1.0", sha256="a17064203b985ffa9219937d339cab3583548f07d38e96d67a498aba69c1387d", url="https://pypi.org/packages/f8/f0/d94f19f4290aa9a442ad1fcffd6c50896163459b7cdeefbdcd84ef8dbd51/google_cloud_audit_log-0.1.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-googleapis-common-protos@1.56.2:", when="@0.2.1:")
        depends_on("py-googleapis-common-protos@1.52:", when="@:0.2.0")
        depends_on("py-protobuf@3.19.5:3.20.0-rc2,3.20.1-rc1,3.20.2:4.21.0,4.21.6:4", when="@0.2.5:")
        depends_on("py-protobuf@3.6:4", when="@0.2.4")
        depends_on("py-protobuf@3.6:3", when="@0.2.1:0.2.3")
        depends_on("py-protobuf@3.6:", when="@:0.2.0")

