# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonKeystoneclient(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("5.4.0", sha256="9918043849032f387a0000104c553aac5ace02918a6b7afcdb99690164029867", url="https://pypi.org/packages/22/d4/ed2d06aff0a9e8405d3774617f93c45e1a6775dee71303c8835c7deab7b5/python_keystoneclient-5.4.0-py3-none-any.whl")
    version("5.3.0", sha256="c7e867e41499020fcb27c49e88ec07a59c8d9c59a7a339ecc2d9d4807e970ac7", url="https://pypi.org/packages/81/6f/23539337528a2dfd5700f216b1cb1eb04046c8b0686f0a09614f4899b91c/python_keystoneclient-5.3.0-py3-none-any.whl")
    version("5.2.0", sha256="03293c2f5b96d32cfe04ab0d2d109c484dcd0f4d071a42543387efd129e9248e", url="https://pypi.org/packages/28/5e/ce530ac6b5859eaf882a02c29839641c566e0b9ed782d994620e6dffd958/python_keystoneclient-5.2.0-py3-none-any.whl")
    version("5.1.0", sha256="9c2e0b1700f553ca625e987f4cd8ef62d7a27ad88c5104e96e16904d2ae1d918", url="https://pypi.org/packages/87/b1/29a005e387db31a21c2ebf4970de5f2d363ce285645c70530dd503c0d4f5/python_keystoneclient-5.1.0-py3-none-any.whl")
    version("5.0.1", sha256="628d52a9676be1f9a00fd987b7b2b72fe66ddae853351606d7e85d8701d5fdc2", url="https://pypi.org/packages/a8/3b/0cabae3d86040e0688bbe29c6590a6b44a70c87bc2fde457a43afe0e902b/python_keystoneclient-5.0.1-py3-none-any.whl")
    version("5.0.0", sha256="f650d3fbe94b069bba0aafd07fc2681c62263acddc2a57bb7fddb42d2b1ef5f4", url="https://pypi.org/packages/0b/da/c4a6fbf2d3fcfe9b17b6d0746fca1924b21b9720cf8f3eb0584196a1e797/python_keystoneclient-5.0.0-py3-none-any.whl")
    version("4.5.0", sha256="5bad91bda4f6f5658e1e03daa2f19f4cdc6c1f1b611afacca9ca1a3ace2ab99a", url="https://pypi.org/packages/0f/51/0fa8581d645b6123c7273dc7a6db77ff01fd2356a2f09aaedd9ce639e761/python_keystoneclient-4.5.0-py3-none-any.whl")
    version("4.4.0", sha256="1a9f30bfa3a5bf004159736d8cec91f8ce47301a0e5ad976b9cd064f5de39295", url="https://pypi.org/packages/6f/ab/74a449230bbfa6950fe80a75799314476a1ef0f732390492a740ef03eb0d/python_keystoneclient-4.4.0-py3-none-any.whl")
    version("4.3.0", sha256="a2bf1fce6505f7a47631cf5e1e019331b518d3499a5e7e82b45f703a7339ffb9", url="https://pypi.org/packages/9c/18/90620c5b2afbb23382c646cfe294f7213b5322c776bc4087991fc7b3d190/python_keystoneclient-4.3.0-py3-none-any.whl")
    version("4.2.0", sha256="5702f387e2a3f3645459a0850ef3e92bc8fc0eb36bd2f8ba1004a50dfed1e5f4", url="https://pypi.org/packages/26/71/a9ccf1faf72123909c87a06352366088a7f936ea04e5e4fe38e422dc2c1e/python_keystoneclient-4.2.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-debtcollector@1.2:", when="@2.2:")
        depends_on("py-keystoneauth1@3.4:", when="@3.16:")
        depends_on("py-oslo-config@5.2:", when="@3.16:")
        depends_on("py-oslo-i18n@3.15.3:", when="@3.14:")
        depends_on("py-oslo-serialization@2.18:2.19.0,2.20:", when="@3.14:")
        depends_on("py-oslo-utils@3.33:", when="@3.15:")
        depends_on("py-packaging@20.4:", when="@4.5:")
        depends_on("py-pbr@2:2.0,3:", when="@3.11:")
        depends_on("py-requests@2.14.2:", when="@3.12:")
        depends_on("py-six@1.10:", when="@3.14:5.3")
        depends_on("py-stevedore@1.20:", when="@3.11:")
    # END DEPENDENCIES

