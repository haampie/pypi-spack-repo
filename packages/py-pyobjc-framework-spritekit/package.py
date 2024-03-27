##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSpritekit(PythonPackage):
    version("10.2", sha256="31b3e639a617c456574df8f3ce18275eff613cf49e98ea8df974cda05d13a7fc", url="https://pypi.org/packages/6b/5e/1206b83c86f1148dc08e870e712cea38a95269347298b83c41c1726c6b1e/pyobjc-framework-SpriteKit-10.2.tar.gz")
    version("10.1", sha256="998be1d6c7fd5cc66bd54bae37c45cf3394df7bc689b5d0c813f0449c8eee53f", url="https://pypi.org/packages/5c/d6/999cccaa31837a1fe07038435dec135cdb863ee8b88bc901db422dd481a6/pyobjc-framework-SpriteKit-10.1.tar.gz")
    version("10.0", sha256="c9db030232e251426575674bbe61b7bdb1cfc4a587a0a1e0d1a59e704658dc30", url="https://pypi.org/packages/62/48/0e536a64267924f2d6e09a9aee834092ed61c3162cd473dcca9c6a12b738/pyobjc-framework-SpriteKit-10.0.tar.gz")
    version("9.2", sha256="0e549aea8b075a9d8e440c333abd7dfecdae4b6d10ac1b847552e138f500cf76", url="https://pypi.org/packages/ae/63/5d946a1c4a4c40cd275082753cee4a144dd331776b1eaf3a9553e7195360/pyobjc-framework-SpriteKit-9.2.tar.gz")
    version("9.1.1", sha256="acf9299ce66e7239dba94a873c220cb4e056727e040539492e19c7fb17afae93", url="https://pypi.org/packages/57/b2/01f3b7d6a779af987c1564da8e51e1bb3e0967ec33d57c9014f496ac7400/pyobjc-framework-SpriteKit-9.1.1.tar.gz")
    version("9.1", sha256="741d3eed26b3d9822d04ddb1a53d42a729058144724673bfad1ea62e61dec406", url="https://pypi.org/packages/2f/28/c5965d0eb3b6b21f82a33ec7eb1bf83dabe0ab7fdfe168614ccd5476f8ba/pyobjc-framework-SpriteKit-9.1.tar.gz")
    version("9.0.1", sha256="7484dd95c055fdeda925ae1eec69379cc6fbb39da514c9ec71fcdeb6b0af181a", url="https://pypi.org/packages/53/0a/88ef3fed8f2f662e062651c1cef97f0895fc704188430d7046c7e98f0b76/pyobjc-framework-SpriteKit-9.0.1.tar.gz")
    version("9.0", sha256="5537dbfba45cfb0f4a6c9aca10aead7dd1c1236668c3f9fb18a2eac7c6a034dc", url="https://pypi.org/packages/a6/e0/6cda36762a9517c1f7691406f8ad1562291da85e66d3461dcc3525f56305/pyobjc-framework-SpriteKit-9.0.tar.gz")
    version("8.5.1", sha256="e87fa33a9b8cf2b8792235e048448adfbfbbf108bf2557db8dc8ddbdc2ad9e88", url="https://pypi.org/packages/d8/aa/a8e0d8697e00e64cf9e8dca48237ad4ae2675c41e216239005d7321140a3/pyobjc-framework-SpriteKit-8.5.1.tar.gz")
    version("8.5", sha256="c38ca87bafe8979fc876a2fc4803f03671151c5d17f0507095117f7635c28e99", url="https://pypi.org/packages/f4/f2/fa31c31fa893a97cfe4be6c0b56aa66a8d8cd14b7d03d5c4e6df712b4f61/pyobjc-framework-SpriteKit-8.5.tar.gz")

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

