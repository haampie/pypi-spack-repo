# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyWheel(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.41.2", sha256="75909db2664838d015e3d9139004ee16711748a52c8f336b52882266540215d8", url="https://pypi.org/packages/b8/8b/31273bf66016be6ad22bb7345c37ff350276cfd46e389a0c2ac5da9d9073/wheel-0.41.2-py3-none-any.whl")
    version("0.37.1", sha256="bbb2658b04929e445a903697c9588dd7d20b1b5f9e717843b62963ac92be502d", url="https://pypi.org/packages/53/fa/dcb07518f988a02de7a5dc5f0706555c203177fc9291c583fa021ffaec9c/wheel-0.37.1-py3-none-any.whl")
    version("0.37.0", sha256="21014b2bd93c6d0034b6ba5d35e4eb284340e09d63c59aef6fc14b0f346146fd", url="https://pypi.org/packages/04/80/cad93b40262f5d09f6de82adbee452fd43cdff60830b56a74c5930f7e277/wheel-0.37.0-py2.py3-none-any.whl")
    version("0.36.2", sha256="78b5b185f0e5763c26ca1e324373aadd49182ca90e825f7853f4b2509215dc0e", url="https://pypi.org/packages/65/63/39d04c74222770ed1589c0eaba06c05891801219272420b40311cd60c880/wheel-0.36.2-py2.py3-none-any.whl")
    version("0.35.1", sha256="497add53525d16c173c2c1c733b8f655510e909ea78cc0e29d374243544b77a2", url="https://pypi.org/packages/a7/00/3df031b3ecd5444d572141321537080b40c1c25e1caa3d86cdd12e5e919c/wheel-0.35.1-py2.py3-none-any.whl")
    version("0.34.2", sha256="df277cb51e61359aba502208d680f90c0493adec6f0e848af94948778aed386e", url="https://pypi.org/packages/8c/23/848298cccf8e40f5bbb59009b32848a4c38f4e7f3364297ab3c3e2e2cd14/wheel-0.34.2-py2.py3-none-any.whl")
    version("0.33.6", sha256="f4da1763d3becf2e2cd92a14a7c920f0f00eca30fdde9ea992c836685b9faf28", url="https://pypi.org/packages/00/83/b4a77d044e78ad1a45610eb88f745be2fd2c6d658f9798a15e384b7d57c9/wheel-0.33.6-py2.py3-none-any.whl")
    version("0.33.4", sha256="5e79117472686ac0c4aef5bad5172ea73a1c2d1646b808c35926bd26bdfb0c08", url="https://pypi.org/packages/bb/10/44230dd6bf3563b8f227dbf344c908d412ad2ff48066476672f3a72e174e/wheel-0.33.4-py2.py3-none-any.whl")
    version("0.33.1", sha256="8eb4a788b3aec8abf5ff68d4165441bc57420c9f64ca5f471f58c3969fe08668", url="https://pypi.org/packages/96/ba/a4702cbb6a3a485239fbe9525443446203f00771af9ac000fa3ef2788201/wheel-0.33.1-py2.py3-none-any.whl")
    version("0.32.3", sha256="1e53cdb3f808d5ccd0df57f964263752aa74ea7359526d3da6c02114ec1e1d44", url="https://pypi.org/packages/ff/47/1dfa4795e24fd6f93d5d58602dd716c3f101cfd5a77cd9acbe519b44a0a9/wheel-0.32.3-py2.py3-none-any.whl")
    version("0.29.0", sha256="ea8033fc9905804e652f75474d33410a07404c1a78dd3c949a66863bd1050ebd", url="https://pypi.org/packages/8a/e9/8468cd68b582b06ef554be0b96b59f59779627131aad48f8a5bce4b13450/wheel-0.29.0-py2.py3-none-any.whl")
    version("0.26.0", sha256="c92ed3a2dd87c54a9e20024fb0a206fe591c352c745fff21e8f8c6cdac2086ea", url="https://pypi.org/packages/d9/6f/cfb45d489703e4843b30c28e01ab39c87b0648bfa11a6c4a959f426fe217/wheel-0.26.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@0.37.1:0.42")
        depends_on("py-setuptools@57:", when="@0.37.1:0.38.0")
    # END DEPENDENCIES

