# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureGraphrbac(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.61.1", sha256="7b4e0f05676acc912f2b33c71c328d9fb2e4dc8e70ebadc9d3de8ab08bf0b175", url="https://pypi.org/packages/3e/93/02056aca45162f9fc275d1eaad12a2a07ef92375afb48eabddc4134b8315/azure_graphrbac-0.61.1-py2.py3-none-any.whl")
    version("0.61.0", sha256="1c882b97b8ca67e987d7d545479c0260c229f5c68a6c02fdedfe40001c89564b", url="https://pypi.org/packages/89/74/00a5ae6e8c823ff0a9c8550931fc42f5f1e5b614f7a45f602f52ec794ac9/azure_graphrbac-0.61.0-py2.py3-none-any.whl")
    version("0.60.0", sha256="0b266602dfc631dca13960cc64bac172bf9dea2cccbb1aa13d1631ce76f14d79", url="https://pypi.org/packages/bd/11/f78acb88061fbfb3678cb7f2c7d6ad73b69b08bc558aa56246e9ce0d9998/azure_graphrbac-0.60.0-py2.py3-none-any.whl")
    version("0.53.0", sha256="45362821c0928a9edbcdd72262a650c9d6ee32a6de72e3158ecee76e508a519f", url="https://pypi.org/packages/da/a8/3d3d6fe8458b2b07bad10195c79928ea9ba87b5cc0c08903b387dd27c6f0/azure_graphrbac-0.53.0-py2.py3-none-any.whl")
    version("0.52.0", sha256="b2e120b3ace8a9ac7a2f95b8851de88891c6806759893c67be4e4448deb5decd", url="https://pypi.org/packages/97/84/b4558e3f469c67497a2a5eaeb05321f91b1ee2d1205992a33f001d9c4bf9/azure_graphrbac-0.52.0-py2.py3-none-any.whl")
    version("0.51.1", sha256="49c0f1dd4feafa9d250b2765151c52d374f717f5781427a4a9a327da9959a1ff", url="https://pypi.org/packages/b2/72/af79ab4d8f7950306b9fede21a636729706045100dd017bb09aca5c8a22f/azure_graphrbac-0.51.1-py2.py3-none-any.whl")
    version("0.51.0", sha256="e813892859a629689cf99f3a220004b9f6c97747cb2c93081de95af8586c00c4", url="https://pypi.org/packages/ba/74/c5b233fe49b1a9909f8e7c18f9ddbf57bafce55f92ddd6edfbfdce1718fd/azure_graphrbac-0.51.0-py2.py3-none-any.whl")
    version("0.50.0", sha256="7ecb7d09a5246825e2bef156f79250181990273f629125899e0664a77c125189", url="https://pypi.org/packages/2c/b1/0fb8d3932c6ec6329e30e6ce0b7754046ecdda46b6076bb024d853fc1fcb/azure_graphrbac-0.50.0-py2.py3-none-any.whl")
    version("0.40.0", sha256="825b397665f478fab511e521f3f3f4b64189cb9f6c2e7e873b3b7333dc533974", url="https://pypi.org/packages/89/0a/29f7e2914033e2536026b8f0d7f8deb1edda68c9a93ce4757b2b1e39568b/azure_graphrbac-0.40.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-common@1.1:", when="@0.31:")
        depends_on("py-azure-nspkg@2:", when="@0.30.0:0.40")
        depends_on("py-msrest@0.5:", when="@0.50:")
        depends_on("py-msrestazure@0.4.32:", when="@0.50:")
        depends_on("py-msrestazure@0.4.20:", when="@0.40")
    # END DEPENDENCIES

