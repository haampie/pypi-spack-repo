##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCoreservices(PythonPackage):
    version("10.2", sha256="90fa09e68e840fdd229b33354f4b2e55e9f95a221fcc30612f4bd92cdc530518", url="https://pypi.org/packages/2f/eb/5b87d6b59745386df3d30a57d4b13d6708fdc4fd3bf62b224f509f5b9cb3/pyobjc-framework-CoreServices-10.2.tar.gz")
    version("10.1", sha256="43d507f2b3d84a5aab808c3f67bf21fb6a7d1367d506e2e9877bf1cac9bad2eb", url="https://pypi.org/packages/49/0e/591ad9387e58a5e1385f6272ec9922a32f6367f4e352d4f62197c0915f18/pyobjc-framework-CoreServices-10.1.tar.gz")
    version("10.0", sha256="a6e80770ead727979e9ffd4ea97c30889e1fdec49873bb5129bf3ef3c5b90005", url="https://pypi.org/packages/ca/98/9a5b01126ffacb6c4d79e9417480e07f5933e4c06ec9276d38c86f0113af/pyobjc-framework-CoreServices-10.0.tar.gz")
    version("9.2", sha256="cc0287dccc7089ad13b0a44472d7fc1ce804f06ea1f4c44c5a7c5c9eb8388d72", url="https://pypi.org/packages/c0/6d/7f42e55281194169d4d41e97fd1aa2a761fe408b1f740576bcbf3c29faab/pyobjc-framework-CoreServices-9.2.tar.gz")
    version("9.1.1", sha256="6de26cb55e3b20346b8d585a5df21a10a90f4c4b1f13f73a05d62d120faf1a6b", url="https://pypi.org/packages/e8/aa/14df488596c92fda6ccfb18851b5126acfd9ab378bc08784c58ff96a788f/pyobjc-framework-CoreServices-9.1.1.tar.gz")
    version("9.1", sha256="5f6b806385309de799c27c282639884468572bc799fba02588e900cddc35daf0", url="https://pypi.org/packages/3f/19/b0cbdd9bd74f69cae37a8a2a0ee39b21a7808838c41baccba765af31d4c9/pyobjc-framework-CoreServices-9.1.tar.gz")
    version("9.1-beta1", sha256="7089111ff021bb2f799482c6d414941201c7636f2db123ddc4f290728551b6d6", url="https://pypi.org/packages/de/32/75dede10d6c5f692a65cfc88222044585daa736c36a711dccb618027e824/pyobjc-framework-CoreServices-9.1b1.tar.gz")
    version("9.0.1", sha256="35dee25133c935593b8eb71333166b9b69b25a85e2d648eaabd9fa1eec57d10f", url="https://pypi.org/packages/9b/af/9ac887eb9156097338db79424811341ebdcf49ef924f0e56c6b9cf9a2558/pyobjc-framework-CoreServices-9.0.1.tar.gz")
    version("9.0", sha256="476d6d4aa3afa7706f09dc9b9c8ec22c724953d123bed4d2c419db825cd1d66b", url="https://pypi.org/packages/2f/c9/5fccdd5b3d72322bd46bb68509c548d2b8e2b08492d691c749847b795b68/pyobjc-framework-CoreServices-9.0.tar.gz")
    version("8.5.1", sha256="97e8b27b32a32ca7d7d0c780b4e5812a09b109f9867fc3890031f2bb42fd37ee", url="https://pypi.org/packages/01/36/c94eb0148ffadaf693a01d73023ac1f72309152252a78c6a1d86112fd649/pyobjc-framework-CoreServices-8.5.1.tar.gz")
    version("8.5", sha256="58bad844c8e5ee82852d860b117d1238c3ed2db8dd57f754feb6bd5801fe878d", url="https://pypi.org/packages/51/9d/cbc424195e9a8834c84075979fa519d2675cce577fb827d3b638fcccc28b/pyobjc-framework-CoreServices-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-fsevents@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-fsevents@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-fsevents@10:", when="@10:10.0")

