# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTox(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("4.14.1", sha256="b03754b6ee6dadc70f2611da82b4ed8f625fcafd247e15d1d0cb056f90a06d3b", url="https://pypi.org/packages/ed/4c/4c7daf604fe4b136a1e25d41eb7cb2d644d1d8d4d6694eb6ffa7f7dd60cd/tox-4.14.1-py3-none-any.whl")
    version("4.14.0", sha256="35976739e39e60e913bef4cf8226be64eb9eed6fdb9a44c6924265ebe11cbcae", url="https://pypi.org/packages/dd/48/57d7f9338669686e5f60794b2291684eb89e49bbf01f695bad651a14e4b5/tox-4.14.0-py3-none-any.whl")
    version("4.13.0", sha256="1143c7e2489c68026a55d3d4ae84c02c449f073b28e62f80e3e440a3b72a4afa", url="https://pypi.org/packages/14/1a/19c783781c4638bc076f21c76c1c55d2a7bef7381b7c47911e1e65c6e340/tox-4.13.0-py3-none-any.whl")
    version("4.12.1", sha256="c07ea797880a44f3c4f200ad88ad92b446b83079d4ccef89585df64cc574375c", url="https://pypi.org/packages/f0/52/38a555b5d86be75ae198d4fc722b6581aa735a91ee260a4398fd9a1b7bf6/tox-4.12.1-py3-none-any.whl")
    version("4.12.0", sha256="c94bf5852ba41f3d9f1e3470ccf3390e0b7bdc938095be3cd96dce25ab5062a0", url="https://pypi.org/packages/89/95/25214c24c4dd5dfb94359cb14e7e6c2426227a0a5075dd380c795ec700e3/tox-4.12.0-py3-none-any.whl")
    version("4.11.4", sha256="2adb83d68f27116812b69aa36676a8d6a52249cb0d173649de0e7d0c2e3e7229", url="https://pypi.org/packages/cd/88/de28a027acdb3a1b070a8acdff62bd23fdc23ce32acc7ac4b92b088979a4/tox-4.11.4-py3-none-any.whl")
    version("4.11.3", sha256="599af5e5bb0cad0148ac1558a0b66f8fff219ef88363483b8d92a81e4246f28f", url="https://pypi.org/packages/f5/f9/963052e8b825645c54262dce7b7c88691505e3b9ee10a3e3667711eaaf21/tox-4.11.3-py3-none-any.whl")
    version("4.11.2", sha256="91bff3220e808759a22b61524bbc8e657ebbc89ff6efde0a1c1372cac4cdf2b0", url="https://pypi.org/packages/43/c5/d2353c1840a68aaa0264d08fa8f835130c51083cbaebdd1c5c9013702b69/tox-4.11.2-py3-none-any.whl")
    version("4.11.1", sha256="da761b4a57ee2b92b5ce39f48ff723fc42d185bf2af508effb683214efa662ea", url="https://pypi.org/packages/d7/d0/2e3ebb844591e66bd389007af9d759bc2af5a06ae415ab3dce55fc15ec2f/tox-4.11.1-py3-none-any.whl")
    version("4.11.0", sha256="7f7e5f1b20115560e610b9a11143bbcf48270ec3293f36c0a18be7b287c3b41f", url="https://pypi.org/packages/d9/ba/203988c4d03ba315effdf75163aa1749c34ce990d6102845bcb10ae0a451/tox-4.11.0-py3-none-any.whl")
    version("3.14.2", sha256="8dd653bf0c6716a435df363c853cad1f037f9d5fddd0abc90d0f48ad06f39d03", url="https://pypi.org/packages/a7/64/73ee95a48a69fb40f9ce415cdeda09c0c2721da483aae0687884f3cb0586/tox-3.14.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cachetools@5.3.2:", when="@4.12:")
        depends_on("py-cachetools@5.3.1:", when="@4.6.1:4.11")
        depends_on("py-chardet@5.2:", when="@4.9:")
        depends_on("py-colorama@0.4.6:", when="@4.0.0-beta3:")
        depends_on("py-colorama@0.4.1:", when="@3.14.2:3 platform=windows")
        depends_on("py-filelock@3.13.1:", when="@4.12:")
        depends_on("py-filelock@3.12.3:", when="@4.11")
        depends_on("py-filelock@3:", when="@:0.0,3.5:3.15.0")
        depends_on("py-packaging@23.2:", when="@4.12:")
        depends_on("py-packaging@23.1:", when="@4.5:4.11")
        depends_on("py-packaging", when="@3.13:3")
        depends_on("py-platformdirs@4.1:", when="@4.12:")
        depends_on("py-platformdirs@3.10:", when="@4.9:4.11")
        depends_on("py-pluggy@1.3:", when="@4.11:")
        depends_on("py-pluggy@0.12:0", when="@3.13:3.15.0")
        depends_on("py-py@1.4.17:", when="@:0.0,3.1:3.15.0")
        depends_on("py-pyproject-api@1.6.1:", when="@4.11:")
        depends_on("py-six@1.0.0:", when="@:0.0,3.1:3.14.3")
        depends_on("py-toml@0.9.4:", when="@:0.0,3.3:3.25")
        depends_on("py-tomli@2.0.1:", when="@3.26:3,4.0.0-beta3: ^python@:3.10")
        depends_on("py-virtualenv@20.25:", when="@4.12:")
        depends_on("py-virtualenv@20.24.3:", when="@4.9:4.11")
        depends_on("py-virtualenv@16:", when="@3.14.1:3.14.5")
    # END DEPENDENCIES

