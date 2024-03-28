# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMarshmallow(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.21.1", sha256="f085493f79efb0644f270a9bf2892843142d80d7174bbbd2f3713f2a589dc633", url="https://pypi.org/packages/38/04/37055b7013dfaaf66e3a9a51e46857cc9be151476a891b995fa70da7e139/marshmallow-3.21.1-py3-none-any.whl")
    version("3.21.0", sha256="e7997f83571c7fd476042c2c188e4ee8a78900ca5e74bd9c8097afa56624e9bd", url="https://pypi.org/packages/f5/97/6e4ddd6713bba5ede1d18f3959d7bffde38e56f7f7ae7c031c9a3d746b95/marshmallow-3.21.0-py3-none-any.whl")
    version("3.20.2", sha256="c21d4b98fee747c130e6bc8f45c4b3199ea66bc00c12ee1f639f0aeca034d5e9", url="https://pypi.org/packages/57/e9/4368d49d3b462da16a3bac976487764a84dd85cef97232c7bd61f5bdedf3/marshmallow-3.20.2-py3-none-any.whl")
    version("3.20.1", sha256="684939db93e80ad3561392f47be0230743131560a41c5110684c16e21ade0a5c", url="https://pypi.org/packages/ed/3c/cebfdcad015240014ff08b883d1c0c427f2ba45ae8c6572851b6ef136cad/marshmallow-3.20.1-py3-none-any.whl")
    version("3.20.0", sha256="217d7d47793c8cb240d94f96b0a00285213d1ac29cc2bd56019ac4cd6ff8852b", url="https://pypi.org/packages/13/01/f066374378cc8f003dff4dfb45d45ba195a80f33299e5968785bcb044a0b/marshmallow-3.20.0-py3-none-any.whl")
    version("3.19.0", sha256="93f0958568da045b0021ec6aeb7ac37c81bfcccbb9a0e7ed8559885070b3a19b", url="https://pypi.org/packages/ae/53/980a20d789029329fdf1546c315f9c92bf862c7f3e7294e3667afcc464f5/marshmallow-3.19.0-py3-none-any.whl")
    version("3.18.0", sha256="35e02a3a06899c9119b785c12a22f4cda361745d66a71ab691fd7610202ae104", url="https://pypi.org/packages/c3/06/e0300cb5f9b5ff9b6d0accdd3536c01bd2300f8154781455914752ab8903/marshmallow-3.18.0-py3-none-any.whl")
    version("3.17.1", sha256="1172ce82765bf26c24a3f9299ed6dbeeca4d213f638eaa39a37772656d7ce408", url="https://pypi.org/packages/5a/29/d079618690e82362d908ed1778b4b28aec045559f67082322e5c576dc41e/marshmallow-3.17.1-py3-none-any.whl")
    version("3.17.0", sha256="00040ab5ea0c608e8787137627a8efae97fabd60552a05dc889c888f814e75eb", url="https://pypi.org/packages/19/35/07a369156dc53384c381c9b2b9fa63c35478b2289b47b4ee7d81418637e5/marshmallow-3.17.0-py3-none-any.whl")
    version("3.16.0", sha256="53a1e0ee69f79e1f3e80d17393b25cfc917eda52f859e8183b4af72c3390c1f1", url="https://pypi.org/packages/5d/32/14422e07e6363051133c5a89e8275c81ee7b64daf34f0c2e394941a2f914/marshmallow-3.16.0-py3-none-any.whl")
    version("3.15.0", sha256="ff79885ed43b579782f48c251d262e062bce49c65c52412458769a4fb57ac30f", url="https://pypi.org/packages/d3/87/a83cac9b3b10b1324196611162c3c434f1fe722a9ae50c642c20d5476022/marshmallow-3.15.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-packaging@17:", when="@3.16:")
        depends_on("py-packaging", when="@3.15")
    # END DEPENDENCIES

