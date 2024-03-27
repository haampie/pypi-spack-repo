##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkDevicecheck(PythonPackage):
    version("10.2", sha256="c9c87ae40af41c4c296af40317018732bba85e589111f5286b2f136f022c8ecd", url="https://pypi.org/packages/eb/2f/7763043393a7d312b4421dd68390933dc123a808216e4a480e2d0fecc869/pyobjc_framework_DeviceCheck-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="31d5a83d85a4d95e238f432ac66cbf110a7b70afa82fd230ab4b911a5e2b9cb4", url="https://pypi.org/packages/0a/65/89282773de62099b9937c8256a6a2578e4df7e1857ace5ac6f0746121dfd/pyobjc_framework_DeviceCheck-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="e930659cb8cb3096b88f43c237951364dbd1b29d98390e0b55b48aec0442cc92", url="https://pypi.org/packages/53/77/cae0df9dd38431e1d53b9c6e66396ebf8eb31058d39388ae9d6a9915ba13/pyobjc_framework_DeviceCheck-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="5890ee8ef53bfa6dd2819de48aaf28c7c700fc806fdc439312fcec9c6d0df7c9", url="https://pypi.org/packages/59/90/5735bea965603d67e71b97624652c79436f0ac56c8bc9817076a975418f9/pyobjc_framework_DeviceCheck-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="d7524f02c1f108e27f4372f97ea485424cd40639c6fa5006511a53707f03f799", url="https://pypi.org/packages/c0/79/3b8305e04411f58449ea0f3b9a4eea7b48c725742a83d5d013685950c300/pyobjc_framework_DeviceCheck-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="f850754c3a0880ff8296c8159eb97b708e2b58d23fcdcc62aa71d95a548a3849", url="https://pypi.org/packages/24/46/c9a5fc0e0a1fd596cf296c379fa482ba7343b190ecebb228a297a2c6cb83/pyobjc_framework_DeviceCheck-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="3817406c6923789c586d40f33e3518b085c11080e6459e3a1749998e39e7c577", url="https://pypi.org/packages/6e/b5/e0f8ecfd15543e2fe183bc494e52ea430f96b128c1a84f8d4aabd38d18f8/pyobjc_framework_DeviceCheck-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="785badfc6f0f4abb27eff1d566d0fe077b8347277d15d9e6e55f0419b9182e64", url="https://pypi.org/packages/16/05/486155f9f21a9c28cbc70bf9af993056b8ea451b7690eeaa0f96f6885550/pyobjc_framework_DeviceCheck-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="bdb518e0fcfdfbdd454ae9da5aa172567509fc964e36091da7ae240dce4e609c", url="https://pypi.org/packages/8f/5d/7388d6f07a312f36dd34a8414e30f7433e992dc2afabaefef09a8d35c6f8/pyobjc_framework_DeviceCheck-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="518b052263fa43f183be4f293ba9f8b29d64f6113af3ca2625c4c18a428eaca4", url="https://pypi.org/packages/3c/a8/3664df481ffd4699769f9c8f9c20d7d91940545aade5356183dea8448a8d/pyobjc_framework_DeviceCheck-8.5-py2.py3-none-any.whl")

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

