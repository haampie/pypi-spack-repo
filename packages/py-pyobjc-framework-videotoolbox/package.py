##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkVideotoolbox(PythonPackage):
    version("10.2", sha256="347259a8e920dbc3dd1fada5ab0d829485cef3165166fa65f78c23ada4f9b80a", url="https://pypi.org/packages/87/26/995dde56ec9955b27d702cb5672f56ec551ec93b83e56c964af29be4b7fb/pyobjc-framework-VideoToolbox-10.2.tar.gz")
    version("10.1", sha256="56c9d4b74965fe79f050884ffa560ff71ffe709c24923d3d0b34459fb626eb11", url="https://pypi.org/packages/da/db/23dc0e0a223f13b129126b18c1a52b007323ae96e8b9740b06b4483e1d61/pyobjc-framework-VideoToolbox-10.1.tar.gz")
    version("10.0", sha256="3c1d112ca55b56eee913697f044d69f5de6959a7503fd2fcb0822ebad45f7b6c", url="https://pypi.org/packages/0f/fc/03794bab88f4229302a58c3d5796d734bed6da453539a8904e59acf97471/pyobjc-framework-VideoToolbox-10.0.tar.gz")
    version("9.2", sha256="3b0def1735d940001e91a5e38e8822b04d4e5ee3f030256298b41a1d78735927", url="https://pypi.org/packages/7c/10/ef46c926fc2c7fa05484c605007fc54626c87c715b03d4c3a776436dddd0/pyobjc-framework-VideoToolbox-9.2.tar.gz")
    version("9.1.1", sha256="bc7d980f82ca7e81ba277e2de78ddfeb8abb151956b10e648596305f9626eaf1", url="https://pypi.org/packages/4d/f7/677210579f070cc292117be7aa470cb51ee816218f0ba9828d0db5a36cc9/pyobjc-framework-VideoToolbox-9.1.1.tar.gz")
    version("9.1", sha256="c7faadcbb0fac07228496d302fc88bf27c1a1bf2488631192eb02f3f16e1dc8e", url="https://pypi.org/packages/dc/fc/2b2a467b5f855cb40ae13b80f53c384c767326c41be40fb0eb78c37b0241/pyobjc-framework-VideoToolbox-9.1.tar.gz")
    version("9.0.1", sha256="3ff52b8a9c06bb25a6894fafbffa97607da7294cf10ad8337dc7d707d524f9f3", url="https://pypi.org/packages/2c/2a/e796b9b65b0371467934042ac4f3a800979ef20cf8891417f23312855479/pyobjc-framework-VideoToolbox-9.0.1.tar.gz")
    version("9.0", sha256="ab32a21e3184be6c6c82183b2c7acdb784904e6f4c8d264239b270186c4138d9", url="https://pypi.org/packages/79/d7/d14d467dc20fcaaa1424bf3ed9eccc1e9b6af236f632924294298ad4d537/pyobjc-framework-VideoToolbox-9.0.tar.gz")
    version("8.5.1", sha256="f3cdfb97f943dd5005e8ba33ddc03462285509a94d2cf2deb584862a84e2edd1", url="https://pypi.org/packages/26/e8/7dca2c8532f0b37ef0f6a12e088cc00ac7bf2c7e77a3079e38910fe0cdf7/pyobjc-framework-VideoToolbox-8.5.1.tar.gz")
    version("8.5", sha256="39a917ef3dda2013d01189bcffd8efcf69b879de982970b9423f3d5287ca3ee5", url="https://pypi.org/packages/da/0f/8e7e83bb6a5a55c3fd600c5fb2790cd8b9aad7dbaeca4ba6661fb7e19481/pyobjc-framework-VideoToolbox-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-coremedia@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coremedia@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-coremedia@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-quartz@10:", when="@10:10.0")

