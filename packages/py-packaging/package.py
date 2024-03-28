# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPackaging(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("24.0", sha256="2ddfb553fdf02fb784c234c7ba6ccc288296ceabec964ad2eae3777778130bc5", url="https://pypi.org/packages/49/df/1fceb2f8900f8639e278b056416d49134fb8d84c5942ffaa01ad34782422/packaging-24.0-py3-none-any.whl")
    version("23.2", sha256="8c491190033a9af7e1d931d0b5dacc2ef47509b34dd0de67ed209b5203fc88c7", url="https://pypi.org/packages/ec/1a/610693ac4ee14fcdf2d9bf3c493370e4f2ef7ae2e19217d7a237ff42367d/packaging-23.2-py3-none-any.whl")
    version("23.1", sha256="994793af429502c4ea2ebf6bf664629d07c1a9fe974af92966e4b8d2df7edc61", url="https://pypi.org/packages/ab/c3/57f0601a2d4fe15de7a553c00adbc901425661bf048f2a22dfc500caf121/packaging-23.1-py3-none-any.whl")
    version("23.0", sha256="714ac14496c3e68c99c29b00845f7a2b85f3bb6f1078fd9f72fd20f0570002b2", url="https://pypi.org/packages/ed/35/a31aed2993e398f6b09a790a181a7927eb14610ee8bbf02dc14d31677f1c/packaging-23.0-py3-none-any.whl")
    version("22.0", sha256="957e2148ba0e1a3b282772e791ef1d8083648bc131c8ab0c1feba110ce1146c3", url="https://pypi.org/packages/8f/7b/42582927d281d7cb035609cd3a543ffac89b74f3f4ee8e1c50914bcb57eb/packaging-22.0-py3-none-any.whl")
    version("21.3", sha256="ef103e05f519cdc783ae24ea4e2e0f508a9c99b2d4969652eed6a2e1ea5bd522", url="https://pypi.org/packages/05/8e/8de486cbd03baba4deef4142bd643a3e7bbe954a784dc1bb17142572d127/packaging-21.3-py3-none-any.whl")
    version("21.2", sha256="14317396d1e8cdb122989b916fa2c7e9ca8e2be9e8060a6eff75b6b7b4d8a7e0", url="https://pypi.org/packages/b1/09/464d5df9f9ec1ab5054af6d097df6793e542f4aa426ba3062ec64409cab7/packaging-21.2-py3-none-any.whl")
    version("21.1", sha256="b23af879fda9abe603cc254cce7b64edbb5c2b05ea84f658cd2b67ab8a25eea4", url="https://pypi.org/packages/a6/d6/d72354a24a7e18f8965ba88c54abea847946e3b28adfbb3a917b75c5f59e/packaging-21.1-py3-none-any.whl")
    version("21.0", sha256="c86254f9220d55e31cc94d69bade760f0847da8000def4dfe1c6b872fd14ff14", url="https://pypi.org/packages/3c/77/e2362b676dc5008d81be423070dd9577fa03be5da2ba1105811900fda546/packaging-21.0-py3-none-any.whl")
    version("20.9", sha256="67714da7f7bc052e064859c05c595155bd1ee9f69f76557e21f051443c20947a", url="https://pypi.org/packages/3e/89/7ea760b4daa42653ece2380531c90f64788d979110a2ab51049d92f408af/packaging-20.9-py2.py3-none-any.whl")
    version("20.8", sha256="24e0da08660a87484d1602c30bb4902d74816b6985b93de36926f5bc95741858", url="https://pypi.org/packages/b1/a7/588bfa063e7763247ab6f7e1d994e331b85e0e7d09f853c59a6eb9696974/packaging-20.8-py2.py3-none-any.whl")
    version("20.7", sha256="eb41423378682dadb7166144a4926e443093863024de508ca5c9737d6bc08376", url="https://pypi.org/packages/28/87/8edcf555adaf60d053ead881bc056079e29319b643ca710339ce84413136/packaging-20.7-py2.py3-none-any.whl")
    version("20.6", sha256="518de9cf1a577c24d2d567033050bb2a8e3528dd48fa195350b59a8548270728", url="https://pypi.org/packages/06/ef/89d5ce843d4ccaf93d78c93c3c1973897552afafe69df20fb0ed6a1ed40f/packaging-20.6-py2.py3-none-any.whl")
    version("20.5", sha256="1a67848015ca7e7879eee30a7ae1053bc04d031e31eccbde6082820150f08621", url="https://pypi.org/packages/0e/75/dc57e8d75c9f4e7ada4d30230875b66633e250504566bdb4d98615808cd1/packaging-20.5-py2.py3-none-any.whl")
    version("20.4", sha256="998416ba6962ae7fbd6596850b80e17859a5753ba17c32284f67bfff33784181", url="https://pypi.org/packages/46/19/c5ab91b1b05cfe63cccd5cfc971db9214c6dd6ced54e33c30d5af1d2bc43/packaging-20.4-py2.py3-none-any.whl")
    version("19.2", sha256="d9551545c6d761f3def1677baf08ab2a3ca17c56879e70fecba2fc4dde4ed108", url="https://pypi.org/packages/cf/94/9672c2d4b126e74c4496c6b3c58a8b51d6419267be9e70660ba23374c875/packaging-19.2-py2.py3-none-any.whl")
    version("19.1", sha256="a7ac867b97fdc07ee80a8058fe4435ccd274ecc3b0ed61d852d7d53055528cf9", url="https://pypi.org/packages/ec/22/630ac83e8f8a9566c4f88038447ed9e16e6f10582767a01f31c769d9a71e/packaging-19.1-py2.py3-none-any.whl")
    version("19.0", sha256="9e1cbf8c12b1f1ce0bb5344b8d7ecf66a6f8a6e91bcb0c84593ed6d3ab5c4ab3", url="https://pypi.org/packages/91/32/58bc30e646e55eab8b21abf89e353f59c0cc02c417e42929f4a9546e1b1d/packaging-19.0-py2.py3-none-any.whl")
    version("17.1", sha256="e9215d2d2535d3ae866c3d6efc77d5b24a0192cce0ff20e42896cc0664f889c0", url="https://pypi.org/packages/ad/c2/b500ea05d5f9f361a562f089fc91f77ed3b4783e13a08a3daf82069b1224/packaging-17.1-py2.py3-none-any.whl")
    version("16.8", sha256="99276dc6e3a7851f32027a68f1095cd3f77c148091b092ea867a351811cfe388", url="https://pypi.org/packages/87/1b/c39b7c65b5612812b83d6cab7ef2885eac9f6beb0b7b8a7071a186aea3b1/packaging-16.8-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-attrs", when="@19.1")
        depends_on("py-pyparsing@2.0.2:3.0.4,3.0.6:", when="@21.3:21")
        depends_on("py-pyparsing@2.0.2:2", when="@21.1:21.2")
        depends_on("py-pyparsing@2.0.2:", when="@17:21.0")
        depends_on("py-pyparsing", when="@16")
        depends_on("py-six", when="@16.1:20.4")
    # END DEPENDENCIES

