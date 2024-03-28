# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPybv(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.8.0", sha256="a2e36a965dc69a9287dadf047dbb30407274d5da50e21d3d6a27a3cfe06dc373", url="https://pypi.org/packages/b4/cf/1dccbab4e6eefc2967feb928762bcf2c380caf1bdd0e68d09e672e7a60e0/pybv-0.8.0-py3-none-any.whl")
    version("0.7.5", sha256="02b7a7b478d8b2cf722f523a557f7e8aa9a2280193e917a0aa5a545807c1aa7f", url="https://pypi.org/packages/ff/0a/533702d81e02f351b9dbc3679a48035c1a9de4aae48ef7f4b4e7e4102fed/pybv-0.7.5-py2.py3-none-any.whl")
    version("0.7.4", sha256="2c965eb753692a0b47d83fc2250ac3d9a7565410d33a1e187458dbceb7041bbd", url="https://pypi.org/packages/f5/a5/e4f7cc516464364c90b23d3afedc331038d46236b4c5a5b0c92b70cd581f/pybv-0.7.4-py3-none-any.whl")
    version("0.7.3", sha256="340286828d12cbc76539408ad8be6da4153e91046e65db2fc6568e846f52e756", url="https://pypi.org/packages/b4/c8/35fcbfdd617f47dbf2eb46f89239c07caa60e9520dd0e3e3a9724473b69f/pybv-0.7.3-py3-none-any.whl")
    version("0.7.2", sha256="9146cb3d1431d2af8d702f26654f1d09b00af12133bb7e20828ca31441d42f33", url="https://pypi.org/packages/45/0d/c2e828e45d69105652e1761eb6d8e6fa164e0e685c7139609a2c786c5b3e/pybv-0.7.2-py3-none-any.whl")
    version("0.7.1", sha256="b9a7815046276f08a4ac548cd493f92a30f1df6442c4ec18199ded182726890b", url="https://pypi.org/packages/30/91/7c8123516a08f99d5222f46847a03db5574c2563f9b9c435ed2b55461ade/pybv-0.7.1-py3-none-any.whl")
    version("0.7.0", sha256="1df65b481e3ff26e3e8d52f23a873dd97ad9cb19066d1bfbf57e9ae679aca509", url="https://pypi.org/packages/3a/86/06471c64dbf0c8021dda1bab4238f73fd595ac2131942a6e5636b013e45d/pybv-0.7.0-py3-none-any.whl")
    version("0.6.0", sha256="7bff80d3d44b088a98a7df2877b4d70595dbfbef3a200a10a67acb0c99ba7553", url="https://pypi.org/packages/48/31/9077784e2d5baa994fb61e266105096b7dc196902134777a3d876ddea412/pybv-0.6.0-py3-none-any.whl")
    version("0.5.0", sha256="c024b89058b210d97829754ffde9c01fd8ec83f465e819eeaee43a4e8c9f886a", url="https://pypi.org/packages/5f/54/360beb86672acb8ed8262b21f26ccace8d08ce7758e49bb9623b5f3e093f/pybv-0.5.0-py3-none-any.whl")
    version("0.4.0", sha256="4b2f8290ee3be2faf62c8dfb37e5633ed2034e78aeb765d74a6570808bf64cad", url="https://pypi.org/packages/f5/f0/04ae70952a1a1652ca6e19de12b06ae3ccf43f66f354239548d0349746b2/pybv-0.4.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.18.1:", when="@0.7:")
        depends_on("py-numpy@1.16.0:", when="@0.6")
        depends_on("py-numpy@1.15.4:", when="@0.5")
    # END DEPENDENCIES

