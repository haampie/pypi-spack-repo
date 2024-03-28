# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkExecutionpolicy(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="4d95d55f82a15286035bb5bc01b339d6c36103a1cbf7d6a3d7a9feac71663626", url="https://pypi.org/packages/e9/1e/7c422232fdfd39485141c8f72e38a36a14fdc37bc9fe7701ad6dfb5e7a4e/pyobjc_framework_ExecutionPolicy-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="556aa28220438b64e6f75f539f133616a343abe3e2565f0d016091f4dc4a9c3d", url="https://pypi.org/packages/be/17/2fe8bbbdb22f58dd9945ef3cdc8072f02d3dadce263d803dcefa6dae3084/pyobjc_framework_ExecutionPolicy-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="823eda14ad797436101f365cb3a5cd7bc46bb8a8972418851427d478b9274ded", url="https://pypi.org/packages/44/ee/ce302f86a01c5d82226a0eb3702062b9ca395b4d156f18de6bfbbb82fc2e/pyobjc_framework_ExecutionPolicy-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="a728cdf00b427f48aae2ae6cee9eaf32db70bb61eaed306eb3cf5d0d197b141b", url="https://pypi.org/packages/eb/38/167032b89c71400104957a7c6b48d6952c0f486eaf5ed4ae3943c2c7b3c4/pyobjc_framework_ExecutionPolicy-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="479a814f8bb363db392c94edc484e18ad17e34bfa1fa05d34f2d19bac12b60ce", url="https://pypi.org/packages/66/15/1504bffa4618d745975980c39cc1c1c1381e82f0bec2ebcde0f59ad89d4d/pyobjc_framework_ExecutionPolicy-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="df70eca5572414b6ee79a402776c1783a42b4385c767de58710cba7b869e24dd", url="https://pypi.org/packages/4a/c6/f10e7341eafa3f2e3d555d98b45022549027843f56ee0399f2c3a47b461a/pyobjc_framework_ExecutionPolicy-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="2c86a869846a2daac39117f2989f3b079214a1dcd06e528a73adb5908237a8ad", url="https://pypi.org/packages/c3/93/3f3316cf784207d86d4f0ad3bcefa072cbf28b003ee43be8635b80045ca6/pyobjc_framework_ExecutionPolicy-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="65a03cb576c09681426019eed8eff33d1121a8d0b58e504e80f76ed3186a9eaa", url="https://pypi.org/packages/15/a8/cf4988060fc0f57b79708489fdd7cef2f8077c9c16efd620ab561d2fd3e3/pyobjc_framework_ExecutionPolicy-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="38f1e6b34135dd55ef627a8c39b96c7f074da785542b3122c87e0f7bdb6fa778", url="https://pypi.org/packages/3f/cc/ac9aa187182bab347ab8df46e908a6aaa9292db78a531af24e2a2d44b220/pyobjc_framework_ExecutionPolicy-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="bf1a1f43d25ef4ab85f1abcdc60d3197a8c8fa15f1a7b38240c4666d4f74cd9f", url="https://pypi.org/packages/55/39/572fe317b4a7462cd17292588a0a052349de7635b7a67fef727cdf54f9f2/pyobjc_framework_ExecutionPolicy-8.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
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
    # END DEPENDENCIES

