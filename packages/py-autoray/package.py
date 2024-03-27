##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAutoray(PythonPackage):
    version("0.6.9", sha256="5685759f6e705f33cc3c614e57a55ba4822dc601969511465985159f2ea1573f", url="https://pypi.org/packages/78/45/56f9b430900db6f9e4402693646d07db7ffc8a235b43ef37fd594b303cd2/autoray-0.6.9-py3-none-any.whl")
    version("0.6.8", sha256="56ce1a1e105e14fd74e5e2d724a92421af7601b34b73f10c0cf58d678958fde4", url="https://pypi.org/packages/ea/23/cd4104e209b29ea11ae9cfdff0d5859121981d59af77249117d6bfd60d0b/autoray-0.6.8-py3-none-any.whl")
    version("0.6.7", sha256="7372d416b018c49a62d23e1e2566dee7fa5aa59a1b43fa7501d7d071b50ae481", url="https://pypi.org/packages/ad/93/c274651e4b9994edf77ab0af094c858c6a949c372f8d459920b1818f570e/autoray-0.6.7-py3-none-any.whl")
    version("0.6.6", sha256="e1918ec9fc2f730b21e2fd229394632b388a3ce25649e4ab32e035f127b39316", url="https://pypi.org/packages/7b/c2/c6aa844448722e795925560f39be3d5c737d5cc83770ef00505440be4b83/autoray-0.6.6-py3-none-any.whl")
    version("0.6.5", sha256="125ee66e10625d47121dd5b12cda6ea9ccdd9e31ba9b67e1e58ea0cfb7c8d6e9", url="https://pypi.org/packages/30/a7/fbbba4e56a718acd6fc27ff2d11d26871ef5b6b34a85b96ba20dd617f20a/autoray-0.6.5-py3-none-any.whl")
    version("0.6.4", sha256="cc9f02453ec21c0c6eb66074ff5ccc4f20db958b90e4c5bc14155ab854a582b4", url="https://pypi.org/packages/32/15/ce4679f09219d2d9d714f32e0659c6ad01a18d44f868673726c82c7d6baa/autoray-0.6.4-py3-none-any.whl")
    version("0.6.3", sha256="eb2d38186f443bea5e41dc757273fda2d2a1948dc7487668a6240072be0f4e08", url="https://pypi.org/packages/84/d9/3343427803e9e8232e4c8924a0a9b5ce5a3ebea446ae4c9cb8ec80ebc9a1/autoray-0.6.3-py3-none-any.whl")
    version("0.6.1", sha256="923f0f2a4ae211fdab4f96f8f4656189633a6f87b490243575249e164c956b80", url="https://pypi.org/packages/80/a9/c7d230492e8c3ba9524c3952b2505dc8abcf37d6508ce3c4bb32195d2e84/autoray-0.6.1-py3-none-any.whl")
    version("0.6.0", sha256="e4b0e40f3145f843da6971635aab892da41a7a1baffd06ef2df53caa1eb7f8cc", url="https://pypi.org/packages/e1/89/c93432a49029e285b34f9d2d7e7ffbe82196274cf3022134799f42147c99/autoray-0.6.0-py3-none-any.whl")
    version("0.5.3", sha256="84ccca6f095445559540cc2b2dd25cf258d204ee7608cdc958f49c56b5ae20a2", url="https://pypi.org/packages/60/66/628602262963edbd8e8997cb0082022e7064b8f2585315423a899c437edf/autoray-0.5.3-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-numpy", when="@:0.5.1")

