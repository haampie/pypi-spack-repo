##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtContainerregistry(PythonPackage):
    version("10.3.0", sha256="851e1c57f9bc4a3589c6b21fb627c11fd6cbb57a0388b7dfccd530ba3160805f", url="https://pypi.org/packages/93/04/e6e206b9392b39e90d84891bf069a4673ba9fe4bc8ba6be78f0bc684c746/azure_mgmt_containerregistry-10.3.0-py3-none-any.whl")
    version("10.2.0", sha256="fd85ea0f07f94bfb1b72ea0e7c678ef37a8918e228292f6755d1310a00cf59fb", url="https://pypi.org/packages/2c/67/5e4a94ebe42bb28317be58e7d11d823b318e9eb6b5c6d3cf8b13670b5b06/azure_mgmt_containerregistry-10.2.0-py3-none-any.whl")
    version("10.1.0", sha256="35c838a43c5009b935589efa63c7057cf0b1c6578b98196f819214727e344977", url="https://pypi.org/packages/e3/51/4a01768c5fecf286e1059ce65c4dc6b4df0508687f68e0c03fd8b126ce5a/azure_mgmt_containerregistry-10.1.0-py3-none-any.whl")
    version("10.0.0", sha256="182463e7ae212a90f360ea6159b0739f14733b4d325f1e77bb1808bb2936dcd8", url="https://pypi.org/packages/18/b0/a34d37102860f9bf0c279c65d9eba306ee24bd4059ee52337d041fe6e51c/azure_mgmt_containerregistry-10.0.0-py3-none-any.whl")
    version("9.1.0", sha256="06ab1bb871063a83b32d0d188b9da6cec4d7937102213f01491f3e53680ea2d3", url="https://pypi.org/packages/a5/00/83a27f6e951bb2b4964c9991d964e78a06cb5295da38088e0be44d5fbe1e/azure_mgmt_containerregistry-9.1.0-py3-none-any.whl")
    version("9.0.0", sha256="016d2def7baccfa5f81b3060f56a8ff2c14a588183c270b4db1ba02ebccd58e6", url="https://pypi.org/packages/94/29/aa6bc68d612c8012701de1daf61a61e913ed293296879d23094c6bca4768/azure_mgmt_containerregistry-9.0.0-py3-none-any.whl")
    version("8.2.0", sha256="02836de341eaa597733b3d959a6167812f7dc80340fe82a5e9ba71bca2f2afd1", url="https://pypi.org/packages/4c/15/a20fe04b4e6d45a168e5aa6c60209fc51d9599325b89144c43c644de7510/azure_mgmt_containerregistry-8.2.0-py2.py3-none-any.whl")
    version("8.1.0", sha256="78dea71a1b4ccb98e085f47ed8b31825fd3a83a3600fad497d59254204955755", url="https://pypi.org/packages/cd/a2/7fd1888c262d0f2a0c025d8aa3222bf84a4b1123774d3701623e588a5ce6/azure_mgmt_containerregistry-8.1.0-py2.py3-none-any.whl")
    version("8.0.0", sha256="28678bdb9f678f85b88e003fd4f435b462bc5566348c6030da2277a9cb152b76", url="https://pypi.org/packages/36/d3/c3a18ee144c641576f34207bd1804a2f6dcdc8261f636f36c99cc6c980b3/azure_mgmt_containerregistry-8.0.0-py2.py3-none-any.whl")
    version("3.0.0-rc14", sha256="bac9a280b7c25a0a2acb0e8a00500ebfcaf9c580a2f2a3302b77ab2f4b09261e", url="https://pypi.org/packages/7e/ba/c61d1194088d88de079ae0d02529229dc15c2f84d43c6b7f6c3ed06fa39d/azure_mgmt_containerregistry-3.0.0rc14-py2.py3-none-any.whl")
    version("2.8.0", sha256="7de7c542e29b441f3858447694c4e5ab933eeef74bce2dd5bdab32b6d521ecd3", url="https://pypi.org/packages/97/70/8c2d0509db466678eba16fa2b0a539499f3b351b1f2993126ad843d5be13/azure_mgmt_containerregistry-2.8.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-azure-common@1.1:", when="@1,2.2:")
        depends_on("py-azure-mgmt-core@1.3.2:", when="@10.1:")
        depends_on("py-azure-mgmt-core@1.3.0:", when="@9:10.0")
        depends_on("py-azure-mgmt-core@1.2:", when="@8")
        depends_on("py-isodate@0.6.1:", when="@10.2:")
        depends_on("py-msrest@0.7.1:", when="@10.1")
        depends_on("py-msrest@0.6.21:", when="@8.0.0:10.0")
        depends_on("py-msrest@0.5:", when="@2.1:8.0.0-beta1")
        depends_on("py-msrestazure@0.4.32:", when="@2.1:3")

