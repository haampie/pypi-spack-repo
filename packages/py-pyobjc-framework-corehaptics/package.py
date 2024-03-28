# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCorehaptics(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="c67fae4b543fc070cece622cfe5803796016a36d1020812428e0f22e5f5674aa", url="https://pypi.org/packages/03/f7/4f2ba6545cb17e589596d23256cc1a825ba1461e4d94a125dc28783c0c47/pyobjc_framework_CoreHaptics-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="ae6143c041b0846a58199826c0094cfb2fb9080f139c93e6b63f51a6b2766552", url="https://pypi.org/packages/82/5e/9d494b4f294115dc6a2bdfd027842b4e754338808d49994a9aaa9456a68f/pyobjc_framework_CoreHaptics-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="5c7bbc18db031be82bdbdde8f96045220a0309e200e8779bc7e361eb2d482892", url="https://pypi.org/packages/dc/51/f4dc751825330e3920f33e54e5dc3af5704bc1eb25d4358d2b4339256c95/pyobjc_framework_CoreHaptics-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="e87105a16852c2c33393a82c4e7caa3c404fdb912e6d95e82f73b8a45ee6a68e", url="https://pypi.org/packages/2c/8e/65d525b86d335bf711c484caeb9069f0b9bf09d7f712673b31364eb35f56/pyobjc_framework_CoreHaptics-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="18bc8671482205bd83cdccbe71dfb984e476809c8326e73ffe9333a39d880633", url="https://pypi.org/packages/5c/9c/5d9ceb03ad112c971b16cdebae3d12631c371b952ca7fdc822bb9f7a58ae/pyobjc_framework_CoreHaptics-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="1f232060c6717411996c059142373c38acc93c500933751dd9c6bdae00686e16", url="https://pypi.org/packages/26/cb/ddd02b440be91c9a5258b0eab4f516c3fdbf3eddebd5f4d71ea0e99f43a7/pyobjc_framework_CoreHaptics-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="a262912910e51ec6417160d66827c05a99b6fbee89908ead4e346dc710ec1eed", url="https://pypi.org/packages/6b/40/fbf5f77ec855bc4a831458ec27ebb6562fd74db4c259fbaa1417f70c0565/pyobjc_framework_CoreHaptics-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="697e7f11b1db0060267dabadda91ee6b1d956bd7c5f2734d1739dcb1fc87eb47", url="https://pypi.org/packages/d5/8e/431cfe8e868d63daacf697317a9a0c3025d23b735237a674a05213535af0/pyobjc_framework_CoreHaptics-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="3c6fcd97f49b26d43e78063392280097ab39ea8114bf67a9f3e64ee03dde5efe", url="https://pypi.org/packages/88/7a/76e20defc9361933377d5c83e42451956a3ca399222ce468524e97e00609/pyobjc_framework_CoreHaptics-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="3b13b00d5d518a7cac3a24aaec1f2eb07b67d9658a5e4afc74d23658fba3b856", url="https://pypi.org/packages/68/b6/59357bf4d1a3253d2b97bbb2633f8225a5516a9d1062869aa1e2503cba9a/pyobjc_framework_CoreHaptics-8.5-py2.py3-none-any.whl")
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

