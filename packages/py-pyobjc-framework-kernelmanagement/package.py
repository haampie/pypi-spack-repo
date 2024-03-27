##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkKernelmanagement(PythonPackage):
    version("10.2", sha256="d8dca9dc1f756bfa894a32f56857ecefb4d188aec590433ee302529261dffb68", url="https://pypi.org/packages/d2/3c/43ca3ccb63395fa113a45f94e8697cd611f89dae8e6e69abea2699175597/pyobjc_framework_KernelManagement-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="923ff2bbab35a92b9becd9762348f6f690fa463ef07a0e5c4a2b8eb1d3e096af", url="https://pypi.org/packages/f6/da/d03874299c24949a193d87b5d261bfad167ce70ff049174190cbe17f87d5/pyobjc_framework_KernelManagement-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="d3573fb51b0132b6814a0fd56a7fb7d648fd627b459ea3157c3d778a5ea4cdbd", url="https://pypi.org/packages/a7/26/ce8f0d85352eae5d8b02d7c75156daec44464db8130d5fbc6cd4f1863797/pyobjc_framework_KernelManagement-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="5a1ea8261031c22c969bd752b97dbdf1685983dbabb6c156f844be9298540bbd", url="https://pypi.org/packages/ed/15/05f4a63ba2ec0535962b8b277f9d29c8b57f75b9247f28dcbf9b73e8a6fe/pyobjc_framework_KernelManagement-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="f04fd3a94db36535aa2951b7dff05cc283217dea30ec3d1b19e3d2dd870d158f", url="https://pypi.org/packages/41/d4/05b5e5bd935ab4d0ecd42f6bb75e2cbdb9d8f6e4df50fe760597093f1048/pyobjc_framework_KernelManagement-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="93771e04d408a332d7f4eabf55e4bb9faec55dba7ee73035f92312ee56b2d22c", url="https://pypi.org/packages/8b/20/2f5a3aeab78af6ce00ffc69ea492891e8e9e0b77d663b8c9b3be6632ba87/pyobjc_framework_KernelManagement-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="6c8ba8a8cd32039f559e7fa1247709d7e712547479b9e13a0a2f2bf4cc3654ce", url="https://pypi.org/packages/80/58/9566ce77b1584cefb97ad7b29e61e8a1f084d0410d0823d06a0b170dbf55/pyobjc_framework_KernelManagement-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="b2611d51d4a168b35fa4c6d016ccbb9490088ed3ced9a76aa21a166aa57113c0", url="https://pypi.org/packages/01/6b/ca1a2b9258c767a75e2eb32d9ce36d83d6c24fca35646dc9201f73559cfb/pyobjc_framework_KernelManagement-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="ad33102a1cff0109b6f407b165bc3d5518b5a69ff4cc3e5427d23b0625734ef5", url="https://pypi.org/packages/b2/53/0a0fa0ddb31e3aa18a33e9e3a61c908467106756d47ea67b4fda11804878/pyobjc_framework_KernelManagement-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="bc4d2109c0c9faebc26246e8c90a63e647cea790c08431ca28a5d4cf0524a23b", url="https://pypi.org/packages/4f/4a/fa50f1210277eb8aa284aca5bcdd020d883cd849fff1b481a787e8a8214a/pyobjc_framework_KernelManagement-8.5-py2.py3-none-any.whl")

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

