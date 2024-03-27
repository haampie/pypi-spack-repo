##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkPhotos(PythonPackage):
    version("10.2", sha256="ba05d1208158e6de6d14782c182991c0d157254be7254b8d3bb0a9a53bf113fb", url="https://pypi.org/packages/60/9b/87b03e8c48c2c7ceda0051cdf9c5c50b8279483602b65c1b73122f8953cb/pyobjc-framework-Photos-10.2.tar.gz")
    version("10.1", sha256="eb0e83d01c8eb0652fac8382e68fd9643b7530f6580c2a51846444cae09ec094", url="https://pypi.org/packages/df/40/027767d8af5c0fe225862ce74a8b7c5ec8b122499a038ce6f4fd7afcdf1e/pyobjc-framework-Photos-10.1.tar.gz")
    version("10.0", sha256="b284e2ede913081570f862fde99fe22c5f254a36b53105fedad4ce66d4dd93af", url="https://pypi.org/packages/a2/d6/3d3a3f34fddbfb775cc78861904f083cc001687fc22155b344c0159bdba8/pyobjc-framework-Photos-10.0.tar.gz")
    version("9.2", sha256="b2a3c28eea5fced4dff85838fb59594e352bcc1f1fc997e7b1ab221b27c6056a", url="https://pypi.org/packages/83/aa/de694bff02eb45e3ed8c661fa8902d099957a89697dab01ceafea2cbdec3/pyobjc-framework-Photos-9.2.tar.gz")
    version("9.1.1", sha256="9756d24ba6759ff08bb829f32c7d0d6129a7b981b14a91d31b557690da7029b9", url="https://pypi.org/packages/b5/e2/335ed2206d5da52f52ffed449249750d208e029bf8af8e99c8410c832889/pyobjc-framework-Photos-9.1.1.tar.gz")
    version("9.1", sha256="f09148de230f3499311b6b13c89ef997e25f4281850e88951c1980861931cad7", url="https://pypi.org/packages/2a/0c/e0c9817e6cd408c2caa5d5783a27180effc53b99bfdaa12811445588ebea/pyobjc-framework-Photos-9.1.tar.gz")
    version("9.0.1", sha256="26bb7e2e92deb52d1641ae61faa095ef06dded2d245e00d0fe8be651e062f378", url="https://pypi.org/packages/16/ea/6116de327f31830c4be32ee877f523263f784d2abbc0e44e74025591d343/pyobjc-framework-Photos-9.0.1.tar.gz")
    version("9.0", sha256="6df1f5d3eb7de1d5578fc93839f3de273f4a9c572cc020fb7da564323e2bef65", url="https://pypi.org/packages/d8/65/6d455e7ffc7e558b13d17bd2fdcb88852937f32700f84dc6a157b2edf7f3/pyobjc-framework-Photos-9.0.tar.gz")
    version("8.5.1", sha256="20fddeb8be409645cebda37e51d74e3a56961b334f1349a8fd03ba402f1fcf97", url="https://pypi.org/packages/8b/fc/2e6c6d5fe7243aadfdfbd65fd2622d4cb24aee546627c16c65c090b3186d/pyobjc-framework-Photos-8.5.1.tar.gz")
    version("8.5", sha256="6ea5586d69472cec98737df6c66edbe38df7d4ad5c894b8081a9abbf1d6a1801", url="https://pypi.org/packages/1f/d0/b01c1b971b74c34ed1dc422f2434eb9903c43444babc29273abca6755d94/pyobjc-framework-Photos-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")

