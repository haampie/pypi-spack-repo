# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonSubunit(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.4.4", sha256="27b27909cfb20c3aa59add6ff97471afd869daa3c9035ac7ef5eed8dc394f7a5", url="https://pypi.org/packages/ce/6c/e8e8d9db91a1ad9a1869ab0c539f8f37cfef9ad3486c5f5987e47e0e81a8/python_subunit-1.4.4-py3-none-any.whl")
    version("1.4.3", sha256="67bed9d7a923c3010446e821dac170da1b11bd4133e18095fa86c30d09b15006", url="https://pypi.org/packages/54/6a/e98ee731948fbe5a5f79d51fa71d10947758371b6d3269db9993173d59f2/python_subunit-1.4.3-py3-none-any.whl")
    version("1.4.2", sha256="c08d6de7e09bf6ac69dcd8e4e57a247a267d1e786493ba559cfb744747d82c8c", url="https://pypi.org/packages/1a/c9/97b34eba09bab1c5a12aa888365e8dacb9d2bc032c85da469af82ee2aae5/python_subunit-1.4.2-py3-none-any.whl")
    version("1.4.1", sha256="840fad67988b43b6fc89495b29f85e3223771e19eec31ea7d74113727fa1925e", url="https://pypi.org/packages/1d/bd/3ea01ddceda0e807dfa0c1555851857b9fbcd99c695ced074d67c4377efa/python_subunit-1.4.1-py3-none-any.whl")
    version("1.4.0", sha256="40f34660c3da3e513cf2e59498a87ef04ebe2b5fe144fa25d476e1f888b19659", url="https://pypi.org/packages/88/de/be89fff5c30810afb101bdac2c8706764fafa8e950dc6ffa22092ad81035/python_subunit-1.4.0-py2.py3-none-any.whl")
    version("1.3.0", sha256="693f1bcb4fe4bd53438ee0b524c8280143e538d663fb92fb66bad05f744a0132", url="https://pypi.org/packages/ee/3a/b8a93e1f5b9a9f7e0a7630146f1c62878b6949ac5e4bac6ae2ae13fa9f83/python_subunit-1.3.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-extras", when="@1.4.1:1.4.2")
        depends_on("py-iso8601", when="@1.4.3:")
        depends_on("py-testtools@0.9.34:", when="@1.4.1:")
    # END DEPENDENCIES

