##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkDiskarbitration(PythonPackage):
    version("10.2", sha256="dd14eb448865ca4c49e15a543f748f1ef6501ea0044eaa2cf04860547205c84f", url="https://pypi.org/packages/cc/f8/87aa1bcc317badb20e4e17a2acc42a3f5b14963fe4b34ebaae29672c9b64/pyobjc_framework_DiskArbitration-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="a3bd1883b60aa1d8cff3bc18957f81ed14e5d0406d18a4a9095539ddf51dd72e", url="https://pypi.org/packages/3f/33/1dc6abda38fc2c9a5e05b286cfc2a6ea117379513020b619cce42cad9ef9/pyobjc_framework_DiskArbitration-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="cf7dadef895980e08dc7dd646c6d819ea3b4b8321abd2af512d9bde5de389895", url="https://pypi.org/packages/4c/2b/6342aa47636f25d6ac17898ee9e4e05c9b127a11f778ee33b74461e83bb3/pyobjc_framework_DiskArbitration-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="e4f03fc83e0c7cb2d9f87ed8ed18c30fbf264457f48467652160ac1c6e805987", url="https://pypi.org/packages/28/f2/b62b4d1e7f317b18b4a5588b9b4026e594792cf8c2a46eb3e781af6aa0f8/pyobjc_framework_DiskArbitration-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="0613f0c34dc33377afe93b70e82775e245d9017261eb325324d204cebb72cfac", url="https://pypi.org/packages/b3/3f/c2a26dfc111b1bfe90a948ad7346870f18a88a02625a9f2f8dcafd80a100/pyobjc_framework_DiskArbitration-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="ab2da1ab964677648a596232cf6670a491f7298f8436c792cf126e8832477e93", url="https://pypi.org/packages/7e/73/78545a954554d8c703101d7500b045facd5719694fe2e554b452532ca3a1/pyobjc_framework_DiskArbitration-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="6609768207e7008693cbb20efaeabfe8342ddbca59d0a90304b4717b3624f04e", url="https://pypi.org/packages/7d/51/a7646c3fffd0a2af6e556044bbb3508b71992b835de427f496dd9b02c0d4/pyobjc_framework_DiskArbitration-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="a4ec3cf8646f5ab24c938dbac0b9f246bbc8541e9700b5a31092bf1285208ea3", url="https://pypi.org/packages/a6/85/c5ab21e94aa0be04e354ba09947f4dfc129004521cf3eb1095d64d69c0b5/pyobjc_framework_DiskArbitration-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="fedcd31bf261790d029035fc3f0652782ae6885010354a51a6d17dd36986213a", url="https://pypi.org/packages/2a/2e/b9262d2a763e5ab1684d3d3437ccd1b8520c107e6472e6bd645136cb4d78/pyobjc_framework_DiskArbitration-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="506ac6b88be5f828d6c2d5d4f49a093eead8151384433b97834d066c3b4be0a1", url="https://pypi.org/packages/d7/0b/40710261ee9100a6c654082197c8fba9b604d2b7f21295cd22ae264c1992/pyobjc_framework_DiskArbitration-8.5-py2.py3-none-any.whl")

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

