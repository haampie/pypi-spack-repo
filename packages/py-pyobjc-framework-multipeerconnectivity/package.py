##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkMultipeerconnectivity(PythonPackage):
    version("10.2", sha256="e3c1e5f39715621786f4ad5ecffa2cc9445a218e5ab3e94295c16fbcb754ee5a", url="https://pypi.org/packages/af/55/37d81cb675cff7cd3531bd9044aa94257a64f96e2727cf124dbdc0ea283f/pyobjc-framework-MultipeerConnectivity-10.2.tar.gz")
    version("10.1", sha256="ab83e57953bb3f3476c77ed863e1138ab58a0711a77a1a11924b9d22e90f116b", url="https://pypi.org/packages/21/67/c16c2c4954d0824f18da096bf5346e888223b1b22c4192624818620cc792/pyobjc-framework-MultipeerConnectivity-10.1.tar.gz")
    version("10.0", sha256="c2641b9c6d2eb2dccd3c69417f5291bd141a23afc3835f7a7822a8cfa45a1153", url="https://pypi.org/packages/60/c9/fd615fd6d67283218ce4318e427f864130b1be9e0081c669e6f94326da58/pyobjc-framework-MultipeerConnectivity-10.0.tar.gz")
    version("9.2", sha256="38e1fc350c1f2ebef1c92e16391e6e2e50b357ba16df975fee01cd1f74593eba", url="https://pypi.org/packages/e4/5f/5686e02111fc06441af985ebcd95dea4f9f768a350439a2cc1ee67f6e224/pyobjc-framework-MultipeerConnectivity-9.2.tar.gz")
    version("9.1.1", sha256="bdaf6450a4914e7d315cedaf7d538d6271bba7939c8ace4028c0ec9ca45c25bc", url="https://pypi.org/packages/23/b9/447002b0364c9b8588dec7d0ee01c4d22dff70a9f07d678d8e9f8babca3d/pyobjc-framework-MultipeerConnectivity-9.1.1.tar.gz")
    version("9.1", sha256="087eb622ce59c736d2d1e30796d7e6b4968b82aaa6d3e2ae63a016e9d431cd7c", url="https://pypi.org/packages/10/cf/76d9dc8754c3ac926fc060d3964e9d327b374204f9073c6a6a3975b1eb44/pyobjc-framework-MultipeerConnectivity-9.1.tar.gz")
    version("9.0.1", sha256="8d47607dddb5e13a64e27a7a23194573c6d478f9c8e27d1c4283949fc6adfdad", url="https://pypi.org/packages/30/03/6b6106dacb3f1ba3e2dda84f2cf21888fa7b4320eea1bc427655a96293d9/pyobjc-framework-MultipeerConnectivity-9.0.1.tar.gz")
    version("9.0", sha256="1317428dbfc6e3ec559682a2618cbd43c2d6df327bd6abd328b4e8eec4f60f89", url="https://pypi.org/packages/07/7b/b8177bbd7e423659c0aceed82a1f37571a7d3fefae18112dd759060bed51/pyobjc-framework-MultipeerConnectivity-9.0.tar.gz")
    version("8.5.1", sha256="5e929c1c7d3924a03a9ce63bddb2b1a93b20c0801c595151d404937dac589440", url="https://pypi.org/packages/e5/06/a9f0f4c9e46bb9e8a0baa841be6e76bab92d7edce3898a4986b15cf98a66/pyobjc-framework-MultipeerConnectivity-8.5.1.tar.gz")
    version("8.5", sha256="82f677ddba1861802a236a26beee6710cc36fe19f1c37e3bfa5b794476aa4155", url="https://pypi.org/packages/89/2c/addfa4ffc58bfbddf1340813552ce1bb6bcb37813b3f64ed576c50191c01/pyobjc-framework-MultipeerConnectivity-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")

