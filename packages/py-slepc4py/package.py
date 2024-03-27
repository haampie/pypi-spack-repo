##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySlepc4py(PythonPackage):
    version("3.20.2", sha256="89ebd1964edd0eb63d4dbfa977d6f35408f4e19a3da290696fd1197901544bd8", url="https://pypi.org/packages/3a/e4/0bea7dbb95359dcacaea61fe821f3c1a3427141803d2ec376ae5361705a6/slepc4py-3.20.2.tar.gz")
    version("3.20.1", sha256="7e6d156f7b0891bfa0616b38a502460c62797f16ca146b321e16cce4cf139d07", url="https://pypi.org/packages/1f/c2/6ada11c80bae84902323128a87b7f52aa474dc0e2199adae8b943cebc50e/slepc4py-3.20.1.tar.gz")
    version("3.20.0", sha256="56cbea1f56746136e5a934bf4a481e566f35e475cb950c0a5bce7d5c3cc7690a", url="https://pypi.org/packages/a9/8c/aaaf0841b558179c47130c78bd9475ed52bc6535560053b9fff603586b43/slepc4py-3.20.0.tar.gz")
    version("3.19.2", sha256="da8b6a7aaaf5e4497b896b2e478c42dd9de4fb31da93eb294181bea3bb60c767", url="https://pypi.org/packages/7f/4c/a3d5171ea4d9308403664be9215a153475487e163e2de549fce4a768db1e/slepc4py-3.19.2.tar.gz")
    version("3.19.1", sha256="68303f4acef8efc0542ab288a19159d0e6cdf313726f573e0bea2edb3d2c9595", url="https://pypi.org/packages/89/6b/7bc400eeb7848ea7b1e4828485ec867f71e518ac38c0d5f7a53446808efb/slepc4py-3.19.1.tar.gz")
    version("3.19.0", sha256="46f85a98b25f64fa7e86f22f59cf4121a7f5e67c0193293a6d608efb36f01c74", url="https://pypi.org/packages/8d/85/7fc56fda88e9d03c2ec455d2110a81cc7f08d4af06840a5818ad0de2f971/slepc4py-3.19.0.tar.gz")
    version("3.18.3", sha256="93c978f115683900a575026111ff2abe6f3ce4de8c21eec53c07dfd97ea43c85", url="https://pypi.org/packages/4b/63/105669c3d5146a30db636cbb88c8d876569cac9ea21280e0491b4abee7ef/slepc4py-3.18.3.tar.gz")
    version("3.18.2", sha256="402297fd8e583ed2618d2cba05e5cae8e9d0a2c3943812a1a138f431ef3479b3", url="https://pypi.org/packages/9b/e6/0f1fae203ae2f5a6698ea532b0268f5bffb091678ae8e083a59704634cb1/slepc4py-3.18.2.tar.gz")
    version("3.18.1", sha256="4c2bc0947d6a9cdb209e3174b7f54fe7b029220e2c90106f52844e8f8795f8f0", url="https://pypi.org/packages/3c/cc/b5bee04499cdb958c628b3619f94c05dbcf2ffd3c90e2dde555c95a02c29/slepc4py-3.18.1.tar.gz")
    version("3.18.0", sha256="aa83f46f942aca05ffcbc8be29b496f56837f564e0396f5b39cec4946654ee78", url="https://pypi.org/packages/2c/08/233c27288b13a2c894a7ca00639c9b3541ee81f676553111e784e32b8d88/slepc4py-3.18.0.tar.gz")
    version("3.17.2", sha256="e5b235486b6901cd4ff0d94083f0e5eeacaef3a2893e1714769717ad488a3885", url="https://pypi.org/packages/be/ab/634491d5daad8a1d72bc5cf9ac153202a0f0f788dc7d3f7b033ea27515bb/slepc4py-3.17.2.tar.gz")
    version("3.17.1", sha256="967d5d045526088ff5b7b2cde76f8b4d1fee3a2a68481f85224b0795e6613eb9", url="https://pypi.org/packages/7c/e5/38dc918f1a5e97468297dcbe94774d58c3085aed0b5f6558eadc90bd2377/slepc4py-3.17.1.tar.gz")
    version("3.17.0", sha256="cab298eb794739579167fd60ff900db90476c4c93b4ae4e0204e989a6eeb3767", url="https://pypi.org/packages/e8/8a/f779fe13aea81dea71e8df5f0e3d62dd8f88564d9864b90d49972f110617/slepc4py-3.17.0.tar.gz")
    version("3.16.3", sha256="d97652efe60163d30c24eb1ef1b1ba98bb8239fd7452bdf8207c2505da48d77e", url="https://pypi.org/packages/94/d0/213d1951602d09fe0b626399c7a6e8dd2ad3e255a93f68789e23675bfcca/slepc4py-3.16.3.tar.gz")
    version("3.16.1", sha256="3ce93de975fa3966794efb09c315b6aff17e412197f99edb66bbfa71fc49093b", url="https://pypi.org/packages/98/80/1bf162fa2d062e6225aa213c9099354766c69bf11e092e32178a9148f244/slepc4py-3.16.1.tar.gz")
    version("3.16.0", sha256="e18850ebccb1e7c59accfbdbe4d004402abbde7f4e1291b0d2c5b560b308fb88", url="https://pypi.org/packages/d8/05/6a4f8fc5420e47e27de2e8c9ac864fe98600c830a6cb7fa84b614b9ccef4/slepc4py-3.16.0.tar.gz")
    version("3.15.1", sha256="bcdab6d2101ae00e189f4b33072805358cee2dda806a6b6a8e3c2f1b9f619dfd", url="https://pypi.org/packages/dd/cb/443f00cb4190cae46b1c51f9ae2c8d483c1e48acbe2b4eae4ea8e2efee61/slepc4py-3.15.1.tar.gz")
    version("3.15.0", sha256="2f5f5cc25ab4dd3782046c65e97265b39be0cf9cc74c5c0100c3c580c3c32395", url="https://pypi.org/packages/2b/ca/7cfed46eef7be6f1f7fa08c2441f980d4aaf460be3f8327d0b0fb3ccdaeb/slepc4py-3.15.0.tar.gz")
    version("3.13.0", sha256="ce05d8a1990771141689517a42682a27b1ac3f145fd3f1d12d820a15445e3549", url="https://pypi.org/packages/d6/13/4d30f65091b6292b736b0fa321f7a845cf0fd16755ada1256fe3c996267b/slepc4py-3.13.0.tar.gz")
    version("3.12.0", sha256="6310a641ebe4b02a547a9f8a9a3c72d44c9fb05b7a5c0c3a9bf6e6a3f1ff07ce", url="https://pypi.org/packages/47/b4/bf00aae9f0861958b9a68c8020296be50be4a145c13cb5926a9e7e41c895/slepc4py-3.12.0.tar.gz")
    version("3.11.0", sha256="9812d8b398fd6f30e872993421e420c64387c74fc3dab410208f13d7270257cf", url="https://pypi.org/packages/90/56/3d2b6c7b272b82c4a7ba49544978eceee3492e749e93bc2f7f1225b7d3b1/slepc4py-3.11.0.tar.gz")


