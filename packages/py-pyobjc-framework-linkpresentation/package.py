##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkLinkpresentation(PythonPackage):
    version("10.2", sha256="1cada96d3eb03e51e1bbb7e7c10b9c08c80fd098132541b4e992234fe43cfa37", url="https://pypi.org/packages/a3/8c/bb2eee65472555c821297871c36100296964e80ca3db5eda8740e5b80dbf/pyobjc_framework_LinkPresentation-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="077c28c038b1aac0e5cd158cbf8b80863627f1254f0a1884440fabf95d46d62f", url="https://pypi.org/packages/d6/9a/a988bc3dab9e862a78fded53b9fc4022d3bf73daaf45a7834f3777554983/pyobjc_framework_LinkPresentation-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="a3de92916daa214da87afe402feef42536e3896b6ed392e040296d01ddd927f7", url="https://pypi.org/packages/23/7e/88d1061e0153c5bdbd128083badb8ef392a2eb3f7b62afd4a28917bd41d7/pyobjc_framework_LinkPresentation-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="548e4b27546bb24fc252b8a7bd87f8be7b8e80cd66a93c010b72226703b505ae", url="https://pypi.org/packages/f5/b7/f83f4dd9e001c5873c5839f36cd31aee26a176dd211986f3d001604a0307/pyobjc_framework_LinkPresentation-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="62fdede094baaa6050e2c1036b8296cd265890ee1b4aecc0de239c1320773820", url="https://pypi.org/packages/12/96/b2f3073e9ca5b4cfa1a23ce42664c802f212d796869011fe115ed038c84b/pyobjc_framework_LinkPresentation-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="168626d0d1b062b652fb5ac6e765994b5c5861a35be70ad654d9364c9eb862b4", url="https://pypi.org/packages/84/4a/1e972ef45be364ee6a931e314b9db91cfb8a7bcab226fd91cb5f8ebe1b5b/pyobjc_framework_LinkPresentation-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="50a8fc89faeea0974dfc3d0201ea3c04c3a5396806077b42548daa1542b3bac5", url="https://pypi.org/packages/8b/e4/bbce5136c307dda71356930ed79a05948c4156afd1d275af83cb0039b2af/pyobjc_framework_LinkPresentation-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="e2d04b6b9416f695e16faf079798413b37730b1cd0ec99e36a7e4026e8ae0836", url="https://pypi.org/packages/66/eb/2db596c443c065578e71c7ec2514eb3618940816dc6afecb0253bf94a653/pyobjc_framework_LinkPresentation-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="4d95f2f4b7c5822cdcbd4e0b6763a590876b82af334221bfe48dbf3cbe88db4d", url="https://pypi.org/packages/6f/7f/606d1c94ff78b4c7f4d9423157fa6fa4aec2c5765deb32b798789dc1a7d8/pyobjc_framework_LinkPresentation-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="7334ffdfb7b033e4684f7cac6fac460a6f26229bfad690ed23144546265ee866", url="https://pypi.org/packages/57/ec/3d78bf0582af61fcdf72f796624a87a6ed5f2bc2b0c81200b7f88b943284/pyobjc_framework_LinkPresentation-8.5-py2.py3-none-any.whl")

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
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-quartz@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-quartz@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-quartz@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-quartz@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-quartz@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-quartz@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-quartz@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-quartz@8.5:", when="@8.5:8.5.0")

