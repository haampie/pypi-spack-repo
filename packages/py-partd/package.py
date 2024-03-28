# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPartd(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.4.1", sha256="27e766663d36c161e2827aa3e28541c992f0b9527d3cca047e13fb3acdb989e6", url="https://pypi.org/packages/11/8a/b7a58e208b144a7315208a0dd627e23f5f50b47fa89c2924bb2e9238ecfb/partd-1.4.1-py3-none-any.whl")
    version("1.4.0", sha256="7a63529348cf0dff14b986db641cd1b83c16b5cb9fc647c2851779db03282ef8", url="https://pypi.org/packages/1a/56/900aae94a28a7bcc0aa90a4be7b739d2221be98c2dfae6f51e34bba29aab/partd-1.4.0-py3-none-any.whl")
    version("1.3.0", sha256="6393a0c898a0ad945728e34e52de0df3ae295c5aff2e2926ba7cc3c60a734a15", url="https://pypi.org/packages/4d/ea/879a276326ed87ab2595c13bb1d43ba49a2e435386417e95bf23b131a209/partd-1.3.0-py3-none-any.whl")
    version("1.2.0", sha256="5c3a5d70da89485c27916328dc1e26232d0e270771bd4caef4a5124b6a457288", url="https://pypi.org/packages/41/94/360258a68b55f47859d72b2d0b2b3cfe0ca4fbbcb81b78812bd00ae86b7c/partd-1.2.0-py3-none-any.whl")
    version("1.1.0", sha256="7a491cf254e5ab09e9e6a40d80195e5e0e5e169115bfb8287225cb0c207536d2", url="https://pypi.org/packages/44/e1/68dbe731c9c067655bff1eca5b7d40c20ca4b23fd5ec9f3d17e201a6f36b/partd-1.1.0-py3-none-any.whl")
    version("1.0.0", sha256="f278ded3a62560db4a0d1529664fedc440585c520407a53b071fdbfb043187b9", url="https://pypi.org/packages/8b/17/09c352519da1db31634979c3aa9126078e9ece0f561c5f641e0649b78905/partd-1.0.0-py2.py3-none-any.whl")
    version("0.3.10", sha256="826e8034dc1503005f86b67c8542bc8c71cc35b33741b413e82d25a09cc26ad9", url="https://pypi.org/packages/9e/f5/c02903ad5a444c9f80e4d1fe4d512afd76e3801de2fba80ea9ed28f9290c/partd-0.3.10-py3-none-any.whl")
    version("0.3.8", sha256="041ef0bd589e2d803b6ff6ac2b559adadcaf40a161a8eeb5a367d5e0f399ac1e", url="https://pypi.org/packages/4a/ca/207a28fd81111f6a88e79a006745ff432b9cae850fbafa27486e98d459da/partd-0.3.8-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-locket", when="@0.3.3,0.3.5,0.3.7:")
        depends_on("py-toolz", when="@0.3.3,0.3.5,0.3.7:")
    # END DEPENDENCIES

