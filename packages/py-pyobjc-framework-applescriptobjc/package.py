##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkApplescriptobjc(PythonPackage):
    version("10.2", sha256="41156fcc36acc3ca7bd0a62af47af4ab8089330c6072db6047b91b52f815f049", url="https://pypi.org/packages/52/3c/766600c3677e87a8d9314be7f7d125295d100ac7b0fdaf6252f2abd8c405/pyobjc_framework_AppleScriptObjC-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="500ed0e39bf2a4f2413d8d6dc398bb58f233ca3670f6946aa5c6d14d1b563465", url="https://pypi.org/packages/cf/c4/e8cb9a3c4e17bd199b936624639a44e530f281c65829d70c5960398f638e/pyobjc_framework_AppleScriptObjC-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="ef800eae5cd54a41f88c8bf83fcc7ab3c902ecaf104e469a6f1ead15da517479", url="https://pypi.org/packages/d5/e3/544a73932aa3b442531202185b3afbaafbc5d7d70d076b2e8943ac7609d2/pyobjc_framework_AppleScriptObjC-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="66c1fa4239c344a1750afd5beaf6550136d777c3073c47303c8ed224e2517282", url="https://pypi.org/packages/85/d8/ef8a1c0768c72a87c76f9277456cb0c4c55fe9afbc92637cd0f3b4054670/pyobjc_framework_AppleScriptObjC-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="b55c1de2b1712c0730f57a593e9c7943d5f90d5724065bda1aa77568a0a3b2f4", url="https://pypi.org/packages/79/81/d41d60474029d4ae982f2fbc8ac793d6c595749f69f7482dace1ed6cd4cf/pyobjc_framework_AppleScriptObjC-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="524a39cb1de1a97ff85343acbb7951f99229642d76c37344390597836849f1a1", url="https://pypi.org/packages/d2/b9/8f1c5f77e8adff3677847159412202bd1734b71ba0bbdca51898a86d91cd/pyobjc_framework_AppleScriptObjC-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="793d854fb27286016dc6621e9a7af7e520c390cd46d68308d142b918b4a16d70", url="https://pypi.org/packages/f9/e4/81c3ed29d5d37607f44da08a1b454c7a71cd1975166055f2a415a4616968/pyobjc_framework_AppleScriptObjC-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="1a74a8a88174fe0eaafcfc9c7c77493c6162c339f2bcafd2369a039800236817", url="https://pypi.org/packages/97/2a/3014fdf144532e259eb6c6a3509167ef8c1f345855a402ea96d5d4a93f96/pyobjc_framework_AppleScriptObjC-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="51ac4a445096663e9665fb33fd0d517a32d50a6277c4403bf96349632c23d9d8", url="https://pypi.org/packages/2c/ce/11a6a8e0dd0ab9bab180ec4f6bcf91b3b81fd9bfd57dfcd99d995a69ed7d/pyobjc_framework_AppleScriptObjC-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="68ed0548de2d99b7f6c989ac499986136162f48a996a75fd1a6131507c1bb8d5", url="https://pypi.org/packages/5d/48/01460808766660cdecef576671f52e51ce4b85189e0125ff49d00fe4fdc1/pyobjc_framework_AppleScriptObjC-8.5-py2.py3-none-any.whl")

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

