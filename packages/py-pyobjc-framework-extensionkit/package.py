##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkExtensionkit(PythonPackage):
    version("10.2", sha256="343c17ec1696947cde6764b32f741d00d7424a620cdbaa91d9bcf47025b77718", url="https://pypi.org/packages/98/50/cf74917661bf524e9fcc2c8ce5925c08e3b8b8d022ef80b9e488723b8d81/pyobjc-framework-ExtensionKit-10.2.tar.gz")
    version("10.1", sha256="4f0a5256149502eeb1b4e1af1455de629a3c3326aaf4d766937212e56355ad58", url="https://pypi.org/packages/d3/ce/a76cec1fe1c30762840c5c3f554f5d9f8e4273c8d6f3f48370e9016448b7/pyobjc-framework-ExtensionKit-10.1.tar.gz")
    version("10.0", sha256="ed9c596728819a58803841bb36d0a5773929d6bd32279b924dcd004266a901df", url="https://pypi.org/packages/d8/0f/35112b9e05d58543e10746c68f540513db69d9408fa08680b7954eba66e3/pyobjc-framework-ExtensionKit-10.0.tar.gz")
    version("9.2", sha256="a674bb7a824c1a2db9e7f88f691adb999feacf929fc7aca198b77ff30bc02233", url="https://pypi.org/packages/00/e4/6dd82b0d821bce4f976ba11e3fa3dc05574d00040849edec5342fb0071b2/pyobjc-framework-ExtensionKit-9.2.tar.gz")
    version("9.1.1", sha256="8cc8af22b6df8bc869f263ba252e39e751fb4d2f20b23ceeb9e2b386b8055eca", url="https://pypi.org/packages/8d/4d/897d2e11ea5c087bb24808a6c072db85c41ec838eae5c1e241ef4ce4b84e/pyobjc-framework-ExtensionKit-9.1.1.tar.gz")
    version("9.1", sha256="e9def7722270d87cdd49d49bdff80bfa8357c3f50fff68a1131d2c6e9878a66e", url="https://pypi.org/packages/f0/17/a0ebf73c996207de374035ec8b4b64eb8bbb07725cee551f6e18e082f97a/pyobjc-framework-ExtensionKit-9.1.tar.gz")
    version("9.0.1", sha256="9752522f5e681c2e19519ff8b0bdaad0e48e33e6c5b23bdcec37ef997573a013", url="https://pypi.org/packages/73/86/5a862f111f2b49cb516985db66e8e16bc0229565387a152bffd8cb926fd7/pyobjc-framework-ExtensionKit-9.0.1.tar.gz")
    version("9.0", sha256="bd0ba44b65f2a92931b607c9c21001ef288623aea2f2846d09921d3436e3bfcd", url="https://pypi.org/packages/b5/3b/4c2aedf70a5eda5f749120c40b6be3d34b072915cc1a34c29571c29811a6/pyobjc-framework-ExtensionKit-9.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")

