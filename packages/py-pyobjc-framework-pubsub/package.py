# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkPubsub(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="b44f7f87de3f92ce9655344c476672f8f7a912f86ab7a615fec30cebbe7a8827", url="https://pypi.org/packages/0a/a3/61e2bdf53960b8440aa39777872c83d757cfdd4d54d775aaa93870c1a822/pyobjc_framework_PubSub-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="af0b1ed0328f06d7d96390a4b95bfb4a790d5b38142825a222923f908dc46db9", url="https://pypi.org/packages/81/29/2d577a2dd84f2fc5eb0ce95999f8fa6e5f3834e1f2ad702dd1c5497870ea/pyobjc_framework_PubSub-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="7d04a4594c232650f4caf3dbb7d3e6e9c7ec1e87847c147bb4f1c5d412efe5ce", url="https://pypi.org/packages/30/9a/da5f674a2dc2862813f7849dd73aa8d47a79b0439adc99891184cd0c7469/pyobjc_framework_PubSub-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="d285bbf1012ba214ce6954efb1c1144216b19e49b9d8145265a66332b1c009c3", url="https://pypi.org/packages/1d/f8/534f575bb095be48026ddf89e0d667d567b1864d941136624ef22c0f1c96/pyobjc_framework_PubSub-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="9abf78708ebdb30f2e32971804d369b91bee319ec1b9c6307d53aee57eb048b4", url="https://pypi.org/packages/6a/90/4579afc0ba5793c84e42eb29a8d839f328056383693800add86048e0d6d1/pyobjc_framework_PubSub-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="3a06c4ad95ec03aa4b057306a0e8584bce28ffe97ce1dbf2fecea959a997cd8a", url="https://pypi.org/packages/b9/6a/9450d5837070a339571c14a6e2716de91d49cd69073edfa8b1177e228d25/pyobjc_framework_PubSub-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="7946f9a7cefc930518763766c540a79aa93a254e6f7edb80452656da2324d297", url="https://pypi.org/packages/24/15/eb9e3c282e44459ada6f7c383d22ce4ce212a5ce3c5c2f7414be817f21e1/pyobjc_framework_PubSub-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="edc37b415b3c9b6febfd0d73b955f3956cd2d1a33e89eceb039b890c349fb2c7", url="https://pypi.org/packages/98/31/2cf4d1b1ffbbdc2bcccd3d41ee9020c6b0cf157f81c232899396b423a02a/pyobjc_framework_PubSub-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="fdda7fbc8566782ae0f0bb511995511ddc25a859065ef1154bcd1505caf20e3d", url="https://pypi.org/packages/95/d8/e062c51196636b4d980a8f422512d5937f3da13d6351bacc7e6402e2ce40/pyobjc_framework_PubSub-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="27d020fe7b9d23f2012f828d53f63dc3387274fc88f63b7c91baece7dfeb5fef", url="https://pypi.org/packages/35/8e/a09e5a603125115a9decd1e0dbfc6e396aa1aa1f643565fb6b32778cf7d4/pyobjc_framework_PubSub-8.5-py2.py3-none-any.whl")
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

