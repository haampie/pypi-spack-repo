##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCoremediaio(PythonPackage):
    version("10.2", sha256="12f9fd93e610e61258f1acb023b868ed196e9444c69e38dfd314f8c256d07c9e", url="https://pypi.org/packages/9c/0d/c6641bd2bb653911612fc2580dbce1cc71d1a354c02051afb2603c068ebb/pyobjc-framework-CoreMediaIO-10.2.tar.gz")
    version("10.1", sha256="c07177c58c88b6de229f88f3b88b4d97bfc59d2406f751b5aff6bed5cac4d938", url="https://pypi.org/packages/68/3c/3862a33a2d5a4c26b98b1488fe509850e09b672b11059c6bf70caac26b39/pyobjc-framework-CoreMediaIO-10.1.tar.gz")
    version("10.0", sha256="d535c67d287d21e25d739c72ae9f7ce8b0f96eacfd3e19758da69ba355553483", url="https://pypi.org/packages/d2/6f/9999865965e6a40871696fc2bdb3d0753514e6047bf213cc9904bfdd1465/pyobjc-framework-CoreMediaIO-10.0.tar.gz")
    version("9.2", sha256="9bf200deaff29799281fe6df5c8dd36b4bfc30ea5aab1d37f16f36c9d8125e22", url="https://pypi.org/packages/af/77/7b964ff6eabb676fc177837c6af773ea5ebd43f8b16fc3c7c570821c242b/pyobjc-framework-CoreMediaIO-9.2.tar.gz")
    version("9.1.1", sha256="3fc90fa2ab8f4a9ac7bdfe1551e293567699b2d2af10d0fa7bf15d1b5b9c74e9", url="https://pypi.org/packages/33/be/c81e4cefe79a7822f7455548b503182fc7fef24f9fe10ea80e4609ff927f/pyobjc-framework-CoreMediaIO-9.1.1.tar.gz")
    version("9.1", sha256="83d80f678f55604671af4783c7e0528804036162cc78b0ef65f2871e9afa963c", url="https://pypi.org/packages/10/5c/f814a2c0e9c3f5c9fac7ccf8dcc1c1b6fa5aaed8b068a91023e2caf14e54/pyobjc-framework-CoreMediaIO-9.1.tar.gz")
    version("9.0.1", sha256="0e561f1c4de73495d87bef01649cb777338b149808dcd90ded5bbc14e4bd5e0e", url="https://pypi.org/packages/0d/f2/fd1792e631ef258ec9762ad30d06dbd53d02f790332a4389aca39c1a3b99/pyobjc-framework-CoreMediaIO-9.0.1.tar.gz")
    version("9.0", sha256="960610ebd31536899d2d03126b0020fa87c26ddf5c7744bedf92bd15df68414a", url="https://pypi.org/packages/e6/e4/81d9c7610aad6f5c37b844ca9d0148d23e9d4dd2ee224f4051ebe215ff08/pyobjc-framework-CoreMediaIO-9.0.tar.gz")
    version("8.5.1", sha256="8696176ad0bee246f192516e6143d666dd5db532303ad799eeba72ba87a4ec1c", url="https://pypi.org/packages/8f/f0/4683b19a71cf5a0239089b1b21967a087f6213504a08fdd94e60319348cc/pyobjc-framework-CoreMediaIO-8.5.1.tar.gz")
    version("8.5", sha256="0f6c5c0c5fb8b2e2875a465eda127949574f46989df05a1a099019c9aac0a126", url="https://pypi.org/packages/a5/9a/d7ecbf3fac988acad783532d25506c94c295d2ad213b4a19bbadc706043d/pyobjc-framework-CoreMediaIO-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")

