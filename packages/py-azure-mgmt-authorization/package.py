##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtAuthorization(PythonPackage):
    version("4.0.0", sha256="d8feeb3842e6ddf1a370963ca4f61fb6edc124e8997b807dd025bc9b2379cd1a", url="https://pypi.org/packages/32/b3/8ec1268082f4d20cc8bf723a1a8e6b9e330bcc338a4dbcee9c7737e9dc1c/azure_mgmt_authorization-4.0.0-py3-none-any.whl")
    version("3.0.0", sha256="b3f9e584b87d5cc39d41283211237945e620c0b868394880aeded80a126b2c40", url="https://pypi.org/packages/a6/c8/7b4d5e5dcc6e9818b6c28ec002ab999ddd589a4c8fb3e5165ca8b883580a/azure_mgmt_authorization-3.0.0-py3-none-any.whl")
    version("2.0.0", sha256="02bcf52ccd1594ebf484741f5a7110dc28ee970664bb75493561d1a180874d38", url="https://pypi.org/packages/f7/fb/11bdb372c72a30082be188a75aabcbcc5d4d8d8909b9ae3ac0ec3a203933/azure_mgmt_authorization-2.0.0-py2.py3-none-any.whl")
    version("1.0.0", sha256="151bebe4352dd5c73d1df8bfc861d6ae6c9697d09ad761c59ce7ec50c476dff7", url="https://pypi.org/packages/90/92/3cef9fef8d4053ccbf2e2eebf6401d1e8280dea263480a359c5e986fadd6/azure_mgmt_authorization-1.0.0-py2.py3-none-any.whl")
    version("0.61.0", sha256="38f8afcd5c0065e598305de15dbb6b81521ac1e05216049f10ca32a435fd5817", url="https://pypi.org/packages/b4/50/7a923f58bf053280fe1890f3332c08f6a82a208c92035ad8f7888c87b786/azure_mgmt_authorization-0.61.0-py2.py3-none-any.whl")
    version("0.60.0", sha256="9d64295cf4210ec14e98fb024a6b4d79d68ef50cdb3804f0b53f8567e52d847f", url="https://pypi.org/packages/5e/17/4724694ddb3311955ddc367eddcd0928f8ee2c7b12d5a6f0b12bca0b03db/azure_mgmt_authorization-0.60.0-py2.py3-none-any.whl")
    version("0.52.0", sha256="2152f345840d6948e41cd259e44e70dd08186f3ce42fbc1816f99a93145ed0a4", url="https://pypi.org/packages/6b/b2/c0d62a3a91c13641e09af294c13fe16929f88dc5902718388cd9b292217f/azure_mgmt_authorization-0.52.0-py2.py3-none-any.whl")
    version("0.51.1", sha256="05d14674817f3b9bb5df56c0bafd6cad584783b5f4f647973ba64925e85c7296", url="https://pypi.org/packages/a1/71/9a20913e92771b3c23564f1bea54d376d09fb30a75585087c70b769d75c8/azure_mgmt_authorization-0.51.1-py2.py3-none-any.whl")
    version("0.51.0", sha256="454192b372c6862d1cd2c5b23eb49ba5115928bc948fe73eb2f48b26a8e2aec3", url="https://pypi.org/packages/20/91/cad6fb2eb9ad106c8d5bd45514af2772c956e921f57b85db6bd0919923e7/azure_mgmt_authorization-0.51.0-py2.py3-none-any.whl")
    version("0.50.0", sha256="2b8504763ea8b1b475f2c3533b171bedb91ffae459f48f1f885ec8536df91093", url="https://pypi.org/packages/6f/17/55b974603c16be89c7a7c16bac57b7bce48527bf1bebc3f116f7215176e6/azure_mgmt_authorization-0.50.0-py2.py3-none-any.whl")
    version("0.40.0", sha256="962ed951ffe7a1283ab8b8bec1525b8fb8e8316ba26ed461a36541ae86deea14", url="https://pypi.org/packages/67/e4/b3535daae30db9b3f73046a0c151c5c2ae2d2bff96ba0c28c1f26a21dbf1/azure_mgmt_authorization-0.40.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-azure-common@1.1.12:", when="@0.50")
        depends_on("py-azure-common@1.1:", when="@0.40,0.51:")
        depends_on("py-azure-mgmt-core@1.3.2:", when="@3:")
        depends_on("py-azure-mgmt-core@1.2:", when="@1:2")
        depends_on("py-azure-mgmt-nspkg@2:", when="@0.30.0:0.50")
        depends_on("py-isodate@0.6.1:", when="@4:")
        depends_on("py-msrest@0.7.1:", when="@3")
        depends_on("py-msrest@0.6.21:", when="@2")
        depends_on("py-msrest@0.5:", when="@0.51:1")
        depends_on("py-msrestazure@0.4.32:", when="@0.51:0")
        depends_on("py-msrestazure@0.4.27:", when="@0.50")
        depends_on("py-msrestazure@0.4.20:", when="@0.40")

