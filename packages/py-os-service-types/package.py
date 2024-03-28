# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOsServiceTypes(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.7.0", sha256="0505c72205690910077fb72b88f2a1f07533c8d39f2fe75b29583481764965d6", url="https://pypi.org/packages/10/2d/318b2b631f68e0fc221ba8f45d163bf810cdb795cf242fe85ad3e5d45639/os_service_types-1.7.0-py2.py3-none-any.whl")
    version("1.6.0", sha256="b42991f7116e0a88c9cf8d8a228866656e23e99215dc25218dfafb0ba8d93c82", url="https://pypi.org/packages/fa/09/8875a02f9bc9cfa655fb358ccb1846d64c5cfe3d860e767bfd8f34d13ab1/os_service_types-1.6.0-py2.py3-none-any.whl")
    version("1.5.0", sha256="581f3ece6e072db705b7cb5d9836d4696216433f1ce43966c9ed8c15b9702623", url="https://pypi.org/packages/d6/fa/05438aae031491cf9f60c5616fa4e062abc954ac68406f7be5094e04b114/os_service_types-1.5.0-py2.py3-none-any.whl")
    version("1.4.0", sha256="c8198e4bc8aaa3469b2cd0719cb39ed6488fc5e274720dcd59a39057fc39c514", url="https://pypi.org/packages/06/65/37c1c495ec596a5f05eee8ba4f2b394409737a00b025cf2711cb0beec2b3/os_service_types-1.4.0-py2.py3-none-any.whl")
    version("1.3.0", sha256="2021b68c3c16843e0c863326dcd1f3c41da8c0d5909cd29ed36897113a75f528", url="https://pypi.org/packages/e2/81/de0853fdfb2a040c3729a7a063a70b7f7f8bc9e4f0aff156581905e58912/os_service_types-1.3.0-py3-none-any.whl")
    version("1.2.0", sha256="4dd42c728b7f33e80a44996ace3c044b2544b58c226d7552f5ccc19eb01668b6", url="https://pypi.org/packages/c7/ec/7ef45820d4fa2964f0fea5b264bbb1594b68e330513a161ddcf0efd963e4/os_service_types-1.2.0-py2-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pbr@2:2.0,3:", when="@1:")
    # END DEPENDENCIES

