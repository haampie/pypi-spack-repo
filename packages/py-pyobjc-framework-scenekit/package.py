##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkScenekit(PythonPackage):
    version("10.2", sha256="53d2ffac43684bb7834ae570d3537bd15f2a7711b77cc9e8b7b81f63a697ba03", url="https://pypi.org/packages/62/f2/25b7ffd0b86a78992c71e4d814b796dd79a01e7300b699098e1ee572bb7d/pyobjc-framework-SceneKit-10.2.tar.gz")
    version("10.1", sha256="f6565f3dba3bacf6099677ef713f9c95bcb9d8c4ea755c1866d113f95f110fc9", url="https://pypi.org/packages/d9/72/aed299d7453eb9efd3bd1cad854efd586836bc4a58f19299db44c63fb922/pyobjc-framework-SceneKit-10.1.tar.gz")
    version("10.0", sha256="205a6706ffe271f3961255f1c55ab60b47d797c7a4154a5c9cc0a3b263c433d6", url="https://pypi.org/packages/78/cd/ec45ee8b0175ccb6c62ead052ade8f86cca4f38c922e7937774c39a57ce6/pyobjc-framework-SceneKit-10.0.tar.gz")
    version("9.2", sha256="33e7e17d2d3d3ef56b09f8f803c2288c2b9ad1c4ec0efc62551a994eef79b905", url="https://pypi.org/packages/0e/45/1e5c3db93e4fbe602fccf185a12c185ba86ad2e54cc7b11577c6d4b9f6bf/pyobjc-framework-SceneKit-9.2.tar.gz")
    version("9.1.1", sha256="d6a9b75f5e551c22c4a2828910e810e17fcd4d800a11e954ee59bf15bc41af00", url="https://pypi.org/packages/dc/64/110838301d3f137e40dfe83ab14bc3b24f1467935c2db8a2542e9e03c15e/pyobjc-framework-SceneKit-9.1.1.tar.gz")
    version("9.1", sha256="85ee9a245c6a71df69835191961fc7bd46560cf00d54e4fa1825fe2e6f16b6f3", url="https://pypi.org/packages/67/55/a71b2f36fd337532cf75fed9fb7011d42f227acdc2a046ac1fb681103a5a/pyobjc-framework-SceneKit-9.1.tar.gz")
    version("9.0.1", sha256="55861c560bfc987236100e68e4ecd39155888492e392a4caa78991e314f86f59", url="https://pypi.org/packages/7c/42/57d77fe48d4f5f323af7e1e08456852b9049163135c02dbe6ee4e30b2442/pyobjc-framework-SceneKit-9.0.1.tar.gz")
    version("9.0", sha256="98f6a3f897d71ca8bba2f6bda33f44dc3ef60069fbc51c709d12a1a4fcdac9d2", url="https://pypi.org/packages/88/55/cd2b05d16771b1c11dea92c30259631fbc572d4925276f46d278c1c55033/pyobjc-framework-SceneKit-9.0.tar.gz")
    version("8.5.1", sha256="a134d2d4389d101630648192e08968ed0f9a6c9233cb7de8c75cc4ac6f0852df", url="https://pypi.org/packages/98/0e/e758266165f3811d089c27d673e901ee2d916cf9f3056a28f1fc53baabfd/pyobjc-framework-SceneKit-8.5.1.tar.gz")
    version("8.5", sha256="b2ff4d6003f4649441d4cc46170c17e7775a82dd4b3d2e197439d7bbf15c2918", url="https://pypi.org/packages/4c/a4/e6250b894fab20eb06627353cb270ebf69e05ad0e57abad1e3c995209ae5/pyobjc-framework-SceneKit-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-quartz@10:", when="@10:10.0")

