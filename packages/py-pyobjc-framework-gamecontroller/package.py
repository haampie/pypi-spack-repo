# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkGamecontroller(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="81ad502346904995ec04b0580bab94ab32ca847fad06bca88cdf2ec6222b80ae", url="https://pypi.org/packages/7c/3c/a5b8df9c0c11ba380a2aa73e9e64e74254a5d07426507dd6a900d8197799/pyobjc-framework-GameController-10.2.tar.gz")
    version("10.1", sha256="50a17fdd151f31b3a5eae9ae811f6f48680316a5c2686413b9a607c25b6be4bc", url="https://pypi.org/packages/48/6d/ade8625a5821f4da416ac1447629d705bac8b3add7badda97b8109423df4/pyobjc-framework-GameController-10.1.tar.gz")
    version("10.0", sha256="c042d6f581a37d39564c6e7b998d6a2775adb4b937aa33e60b8aa99475157c2d", url="https://pypi.org/packages/3f/c8/ba1608df9d3232c9f151d39a1cebe4cc42221d03c7f13c5cd16250f7089e/pyobjc-framework-GameController-10.0.tar.gz")
    version("9.2", sha256="26f5b6180baadee20f90566b10879392282874212810940a4ebf4e64a77ed5b0", url="https://pypi.org/packages/a4/94/e1bd5425956fd656010067b420285e83f4f0636b95e20ea1c25cbe1c6f61/pyobjc-framework-GameController-9.2.tar.gz")
    version("9.1.1", sha256="04e13ba8b2a131c699cf2a8c9397ba5418897de7ccf8eb202a5033764103db2e", url="https://pypi.org/packages/d2/8e/1847cd8cce9e55d9955e22eeadcec515d967e27963d47d37627d34a43ede/pyobjc-framework-GameController-9.1.1.tar.gz")
    version("9.1", sha256="28becb294ae945517b484db4181144395a8547873b974b02b7b32c3938a040c2", url="https://pypi.org/packages/8b/1e/898e4b40632d6a1401d8599f0adde6fc013e5ac90a3f3490fa0c782cca56/pyobjc-framework-GameController-9.1.tar.gz")
    version("9.0.1", sha256="1a9c3d30a26a249217599be64ae93a0ee9b331b2e2461a30165c646b2e473cfb", url="https://pypi.org/packages/b9/22/eb01ace3d8f01284533c68f603a6d55cbdb7226d8ba200832514eccfeb0c/pyobjc-framework-GameController-9.0.1.tar.gz")
    version("9.0", sha256="e5c2ebee7eea3d8750f5c0029f4c3952a6bed64dc4f9d923ec01cd5539cb3140", url="https://pypi.org/packages/66/60/124bd6edd8500157db2fd0b3d4c3ae4bf3fe9b416ed00c73b4c4c7545517/pyobjc-framework-GameController-9.0.tar.gz")
    version("8.5.1", sha256="86870d769d8a2f0dbfe97a4f103960174c4901c61b82492cae17f673b9af895a", url="https://pypi.org/packages/bb/22/4eaabc16670ce85a1245eb246bd7f9a96c9be935fca749b97c58838154f5/pyobjc-framework-GameController-8.5.1.tar.gz")
    version("8.5", sha256="e89839baee98556d05d2f09b53a1e8e25ce46f891c2541a4db430c742c67da5f", url="https://pypi.org/packages/98/53/01b66af78e4e156493d1d644f0faf598bb1a8a1d75b4402a84fe7f5d1762/pyobjc-framework-GameController-8.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
    # END DEPENDENCIES

