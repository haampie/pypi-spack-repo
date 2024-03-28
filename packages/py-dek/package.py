# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDek(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.4.2", sha256="4324b9fc90d9d5f6e8957dd208c09f95d23cbfc7d488db0d1eb86d830e055f50", url="https://pypi.org/packages/65/e7/61891051cf9abdbdcdb89aaeb910372f646136643537e4a211bf74a4ec01/dek-1.4.2-py3-none-any.whl")
    version("1.4.1", sha256="e1ab1842c033404d7e09a1a2d9e81858a6be08d558d8fe0443e60032a2e3f129", url="https://pypi.org/packages/96/de/d61078784fc8152382c7f9296a79b80977045e238a9cca4abcc567913bff/dek-1.4.1-py3-none-any.whl")
    version("1.4.0", sha256="d82a87dbdae073caff63258016c20f3cf308be6fa0960b7726cbcb5376d25ee5", url="https://pypi.org/packages/da/02/8782a3c6fed3940fe227298d9dd870dfa264fff40307251ccefe13ec973b/dek-1.4.0-py3-none-any.whl")
    version("1.3.1", sha256="a2c05a1159ab906c030d057c15e439bd3648f45c68baa0f8ef4da59be953a069", url="https://pypi.org/packages/25/b9/49f36452a8d1f9781bd7411f73763ea86e77c07d347ba3c812d0b2296c0e/dek-1.3.1-py3-none-any.whl")
    version("1.3.0", sha256="decba02e75242c1b8841b3cd1a33f6724245a675559e642366d3de726c38acec", url="https://pypi.org/packages/98/bd/ca4fd60159023a335f7ff9971b6e11e61255b98b1de838fd53df8c0d9377/dek-1.3.0-py3-none-any.whl")
    version("1.2.0", sha256="bdc95d9dde0f2b83245768f8e471e1f0ef36b0cc947062264d6e13ecaad5765a", url="https://pypi.org/packages/b1/3f/c682c664c8c5aa03113791c104927acaa336a5633b871f7776ec1836cc62/dek-1.2.0-py3-none-any.whl")
    version("1.1.0", sha256="ffa4fe9cbd44124d9c64e29f0e2105514c4c06ce9c0f9c1e499a953b69a8f35d", url="https://pypi.org/packages/09/cd/f8bbf875d5304f5d8096b0428fd715dcdb0e48adc4aa5d3cdeed1bf6fe47/dek-1.1.0-py3-none-any.whl")
    version("1.0.2", sha256="c3731f73b38ef0c636d5101e1eac60a79a03823359a2d57a632b8a308e60545b", url="https://pypi.org/packages/7b/57/745bd6a72bd5199c4d3fee9bcecf3196b93d21aac3e817072b9d27dbf273/dek-1.0.2-py3-none-any.whl")
    version("1.0.1", sha256="75158f75f67f6148a93ed606850dd90bbfa3c14db99f84a2db9496c40be497da", url="https://pypi.org/packages/dd/71/ffb62bd47f23d00dfeb5da9073d59e6c3f2c4e5a37d9fc501b0a91216068/dek-1.0.1-py3-none-any.whl")
    version("1.0.0", sha256="e529bafbc6ca40d19121daa6b469a41e2ef92d5db354056301f7721052c4cd8d", url="https://pypi.org/packages/64/1f/2a20e12c40ec9e16d4bed454eba33b6ae32454534fcb06b9eb8ffdb09b5d/dek-1.0.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-xmod@1.6.1:", when="@1.3.1:1.3")
        depends_on("py-xmod@1.3.2:", when="@1.0.2:1.1")
        depends_on("py-xmod", when="@0.10.5:1.0.1,1.2:1.3.0,1.4:")
    # END DEPENDENCIES

