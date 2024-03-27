##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyXgboost(PythonPackage):
    version("2.0.3", sha256="462f131d7bfb1bc42f67c57fa5aa3e57d2b5755b1573a6e0d2c7e8895164e0fc", url="https://pypi.org/packages/24/ec/ad387100fa3cc2b9b81af0829b5ecfe75ec5bb19dd7c19d4fea06fb81802/xgboost-2.0.3-py3-none-win_amd64.whl")
    version("2.0.2", sha256="f07f42441f05a289bc4d34342c2335726763ae0759d7241ef25d0eab007dbec4", url="https://pypi.org/packages/bc/43/242432efc3f60052a4a534dc4926b21e236ab4ec8d4920c593da3f65c65d/xgboost-2.0.2-py3-none-win_amd64.whl")
    version("2.0.1", sha256="70219cdbd58c8c71156ac27e6a71fd73b19cb813fd35fd72e541004e2fe65fb7", url="https://pypi.org/packages/ee/2c/03d466d00818c8e0ffcf778946ca4a5e05694a11b85bc51f1bc5c18ca54e/xgboost-2.0.1-py3-none-manylinux2014_x86_64.whl")
    version("2.0.0", sha256="0a1041718a0d7026aa51c9abc5270f22620b9ac930c0785c2178216fe073c512", url="https://pypi.org/packages/6d/d1/3e954de1d492129710e8625349a7b86eb287a4f413c5b5c15522f89a6c04/xgboost-2.0.0-py3-none-macosx_12_0_arm64.whl")
    version("1.7.6", sha256="4c34675b4d2678c624ddde5d45361e7e16046923e362e4e609b88353e6b87124", url="https://pypi.org/packages/94/41/143e80c1f48f7e826380f382dff6caf93a698c77bf2e9e38290bbbfbfe42/xgboost-1.7.6-py3-none-macosx_10_15_x86_64.macosx_11_0_x86_64.macosx_12_0_x86_64.whl")
    version("1.7.5", sha256="1d1dda6b84ea50a2ea1ed18390e93e275d57dc4cffd682014dc30ae5a116c92b", url="https://pypi.org/packages/7e/94/164786127eed50283df0b62a3da9521695163b1596a1667e3856438da6e7/xgboost-1.7.5-py3-none-manylinux2014_x86_64.whl")
    version("1.7.4", sha256="31aec5c4acb9e23bee9b9200444de1d808a1a44f48136ec6a4fbe8d57fc1b13b", url="https://pypi.org/packages/27/6c/eda071252da7026eba24dab5df9ca2e8db701e77ad71ab100bd5987cabf9/xgboost-1.7.4-py3-none-macosx_12_0_arm64.whl")
    version("1.7.3", sha256="86dfc7d7da6fae751dc5c316e862f3395d9eddef5d10622a43d47deceb3257df", url="https://pypi.org/packages/c4/73/3dd0356bb7f41727639417b4acdb68f6cd60d3c6a5e51a972d5969cfdd3f/xgboost-1.7.3-py3-none-macosx_12_0_arm64.whl")
    version("1.7.2", sha256="08ca6b3400dfd16f6159b2881f41b7443024339c14c5dbe10bba117af79126ab", url="https://pypi.org/packages/d5/c9/6f1295071016507cb8e37f69d33c9a17144dc2bd8d29abe6243efea79add/xgboost-1.7.2-py3-none-win_amd64.whl")
    version("1.7.1", sha256="fbe06896e1b12843c7f428ae56da6ac1c5975545d8785f137f73fd591c54e5f5", url="https://pypi.org/packages/e4/36/ba9ba7b0b68a41f1ce325dbc59eb7f1d7a4205805b3ec44ceec6f5854cf9/xgboost-1.7.1-py3-none-win_amd64.whl")
    version("1.6.2", sha256="1ce15d3292d6ee75be4491ff6463c76ca548b7d77ca70f707cb23ea051e2faf7", url="https://pypi.org/packages/24/14/d9ecb9fa86727f51bfb35f1c2b0428ebc6cd5ffde24c5e2dc583d3575a6f/xgboost-1.6.2-py3-none-win_amd64.whl")
    version("1.6.1", sha256="6207c77f611b54d9f056edede819ead03f0235615675f88030ff9fe10d359551", url="https://pypi.org/packages/e4/ed/8e2a7ae4e856f4887afc0beee897088ed8dbbc1b19b0f49971019939452a/xgboost-1.6.1-py3-none-manylinux2014_x86_64.whl")
    version("1.5.2", sha256="51b5dfe553d78ab92f2c60ccead6abc38196c2961f6952f6ec14b1feba6ffd25", url="https://pypi.org/packages/a3/6e/45a86bb2c3f969fec4893f299e48f1be980b42e66e362bbecb5db26bdc3a/xgboost-1.5.2-py3-none-macosx_10_15_x86_64.macosx_11_0_x86_64.macosx_12_0_x86_64.whl")
    version("1.3.3", sha256="92fe1d12ca95d0bea1a7518090e75d7460aec4f7372c87013376b1533fa8a89d", url="https://pypi.org/packages/7f/85/b9c2fc5758abb2084e75a74ff4ee0152c2df661826eba3bc652a4cb559e4/xgboost-1.3.3-py3-none-macosx_10_14_x86_64.macosx_10_15_x86_64.macosx_11_0_x86_64.whl")

    with default_args(type="run"):
        depends_on("py-numpy", when="@0.80:1.0.0-rc2,1.0.1:")
        depends_on("py-scipy", when="@0.80:1.0.0-rc2,1.0.1:")

