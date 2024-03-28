# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOsloI18n(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("6.3.0", sha256="698eb5c63a01359ed6d91031d6331098190d38be0bdda7d270264d6f86bc79e7", url="https://pypi.org/packages/e2/60/662cfd4906746f40f88ba930d1af7990f8da1027baea49702880ce946db2/oslo.i18n-6.3.0-py3-none-any.whl")
    version("6.2.0", sha256="5cd6d0659bec2013107d235a8cf5e61475cc9dd33ef9ffc7aa2776bc1c6b56c9", url="https://pypi.org/packages/51/3e/01e63f546fec2550f0001d29037d8d24e7e2c0c2f4a66a50d5dff9c762d6/oslo.i18n-6.2.0-py3-none-any.whl")
    version("6.1.0", sha256="4a7ee58c5aba57c3c6f49f3138b36f4b96fa5f93ddf3e41d4f19e8b343a8a470", url="https://pypi.org/packages/d3/80/5a5eaf71c5bae50a53c9d99a14cb58fec41183baac9f18131e8e75a6a49c/oslo.i18n-6.1.0-py3-none-any.whl")
    version("6.0.0", sha256="080fedf41b05d4dcd23a91d23ee2dea0863996e860a59695856269a42d939fc1", url="https://pypi.org/packages/62/5a/ced9667f5a35d712734bf3449afad763283e31ea9a903137eb42df29d948/oslo.i18n-6.0.0-py3-none-any.whl")
    version("5.1.0", sha256="75086cfd898819638ca741159f677e2073a78ca86a9c9be8d38b46800cdf2dc9", url="https://pypi.org/packages/0d/78/d4079dc5a6adc19e91ed3f62af3061a3e3be2d4de12fdd802db38ceaeec1/oslo.i18n-5.1.0-py3-none-any.whl")
    version("5.0.1", sha256="99a6453b9b7a9d1603ba6c32e6ab8c738af95f6573215682a33c8028340bdccd", url="https://pypi.org/packages/89/ac/b71a66e54c8fcf22c4205efe2b5f94dbf282c194f9f07dbf0a1ac52d4633/oslo.i18n-5.0.1-py3-none-any.whl")
    version("5.0.0", sha256="55914fbdcb7de1d766bc3910c61b5071fe1288ba605bfe90f635000a033c4ec4", url="https://pypi.org/packages/45/7d/dfe3783932540eb382b244efbdc8df8a6aa09dff4d6644653bb642c81f92/oslo.i18n-5.0.0-py3-none-any.whl")
    version("4.0.1", sha256="ec357b430b29d5890101c0d24502615e0dc05204ff8c626b1e761edc737dfe71", url="https://pypi.org/packages/d1/59/16e07470ba39f9a18d679755d66452acd36ca3e03e98aa109f3ff7def649/oslo.i18n-4.0.1-py3-none-any.whl")
    version("4.0.0", sha256="b511fb702f25e48ff50eb5af3e600b5481b35ba405e16a098ee9d972949f59d8", url="https://pypi.org/packages/8b/c4/e8f5cf9269ea3d0b4afbe6b40871443ded752bedad591d8a107dae71c08c/oslo.i18n-4.0.0-py3-none-any.whl")
    version("3.25.1", sha256="04aebc4134e1144dce7947caf25f276e3af5a34caae3a3365a728f05d90ff316", url="https://pypi.org/packages/4e/a4/e2c71ea714266097b2edc5188462cfc8f0fffd277ef148a33430199b4a0a/oslo.i18n-3.25.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-babel@2.3.4:2.3,2.5:", when="@3.15.1,3.15.3:4")
        depends_on("py-pbr@2:2.0,3:", when="@3.15.1:")
        depends_on("py-six@1.10:", when="@3.19:5.0")
    # END DEPENDENCIES

