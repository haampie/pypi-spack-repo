##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkApptrackingtransparency(PythonPackage):
    version("10.2", sha256="de140b6b6ca1df928d13d986b093f19b8be0c9ab7c42f4121bdbf58f5c69df48", url="https://pypi.org/packages/cb/09/697d7f0e3f123359b946bd91031bf1ab58a4c7766a9723ff2b9453b9342b/pyobjc_framework_AppTrackingTransparency-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="5dee7e163a6b325315410ca4929f1e07162403fc0f62d7d6a8dd504b544e1626", url="https://pypi.org/packages/fc/42/256808ce61f8824681b52d06d48bd9ad0557cc221082440bdd70f1fc991e/pyobjc_framework_AppTrackingTransparency-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="20d1c8516c2ac568b90f3daf7d93b91a37ea61aa874b4a541d276c7fdac623e4", url="https://pypi.org/packages/9e/d9/ed0b3c22882ac07ae59074cbf4d041a82f05cbb51b129d986482b7362a56/pyobjc_framework_AppTrackingTransparency-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="6b82dcff01a683cf4f78cf47e869ed1d0444821208beed4ec92cacc5a69cd972", url="https://pypi.org/packages/cc/ea/04abc6e2629f964690b3e0850ec2ae2c85d3e1b6d414dd154ff15380b012/pyobjc_framework_AppTrackingTransparency-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="7550b75a734ada61e64ce1ea72ca8c71b2d23210c4bd215e34b5c3dd14d57fbc", url="https://pypi.org/packages/82/6f/f6ce01ff697b4e1b7ea9750091b46a907cae163c8ab40a1dbddccc649678/pyobjc_framework_AppTrackingTransparency-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="ba20f5123ced3584e27af9f8cdb09cb454e5eac3879c5808d062346c7bac9619", url="https://pypi.org/packages/b6/45/f10f59edba1baddf82da71a429626f11c0996825db91da63d3b737bf068b/pyobjc_framework_AppTrackingTransparency-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="b371ce30e8c9f4b92148f9df60c36aff809b55be41a5cc41718fe11a7889b43e", url="https://pypi.org/packages/6a/3c/b5f33a5af29d2af50aedfdf61606f6671a96892d2599a4939cb4d9525b36/pyobjc_framework_AppTrackingTransparency-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="53c7b8565ee276f4828f44d04e9b3d78b275fe8713debf4e992c3c8e74125c07", url="https://pypi.org/packages/62/bc/15864621694cd0e8038d31c0a3676b816739967909a99d2a5e7a188cf18b/pyobjc_framework_AppTrackingTransparency-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="e5efdb749dead08d498b5b0737e37c69212e330e6502173e0d927977a4e94cb9", url="https://pypi.org/packages/71/9c/6536dea8180efa174c678448c01227da1475c75be260fb33a5ab828c2058/pyobjc_framework_AppTrackingTransparency-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="0aed6d40245aae09bcb3bb2616b80b6c6debcbb2c4efc875b60fe6c35f77eaa0", url="https://pypi.org/packages/75/54/e73c2da4017a25834b98875c7f3eb4b19041acccc7d83eaba1f837960fd6/pyobjc_framework_AppTrackingTransparency-8.5-py2.py3-none-any.whl")

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

