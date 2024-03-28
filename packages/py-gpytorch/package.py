# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGpytorch(PythonPackage):
    # BEGIN VERSIONS
    version("1.11", sha256="188bfdbcafcb8f754382e54dc19bd21a86220aaf3ec1587cb8cbb7808876c4ef", url="https://pypi.org/packages/12/24/805d9a4fcb5d105b95b2dac56d0764cfcceba31319437ca94a6592552f84/gpytorch-1.11-py3-none-any.whl")
    version("1.10", sha256="8fc9025b5735dde411a4e7213b21f33cfb1c4316a9f5420a80389ac8959f80d2", url="https://pypi.org/packages/3f/29/a45716beb67e5dac4a6f4b86af0231d759684005b538288f91f26e0c4931/gpytorch-1.10-py3-none-any.whl")
    version("1.9.1", sha256="feeedb9fd4230a8a6bf7ed32ff749a0de7fbe52ed72318a0ce2cc85f3d9d49a8", url="https://pypi.org/packages/0b/8d/2baa077efc7ad94fa47b8a80324166538f75d76cb4ac2c7833bbc2938cc9/gpytorch-1.9.1-py3-none-any.whl")
    version("1.9.0", sha256="27b871963fd548c1a53a62b290acb4d82d9b6a2ef85e93e446ec8e28f37f4d17", url="https://pypi.org/packages/4d/51/f37ae45530cd4a4e703c31e9da5c846e2066af97f711530c0948ab9eccfd/gpytorch-1.9.0-py3-none-any.whl")
    version("1.8.1", sha256="74f51469175fc9e52c86e0f2a5524605439ce307393e5d0bf3a9dc78cfef3244", url="https://pypi.org/packages/67/30/80921ea672e94f2fd17f92161d82749c86e7aa909c2717e6615434193c86/gpytorch-1.8.1-py2.py3-none-any.whl")
    version("1.8.0", sha256="54516d2daffdb0567362fff8efb10710dc977ea7f081b938482581d8ec6eef5b", url="https://pypi.org/packages/32/e6/2384f884fdf236e0309e3ffc8ced94c6dcda9e029c9e7c1cca30138a7d7c/gpytorch-1.8.0-py2.py3-none-any.whl")
    version("1.7.0", sha256="9f81c0106f81c1f28232fd67471f578007487b806034af9bb969e4d78df5dce9", url="https://pypi.org/packages/cc/29/9ba94f9eb70ac5b74d8e9b73aa03401782bdda68488ddf9b83e8347e248c/gpytorch-1.7.0-py2.py3-none-any.whl")
    version("1.6.0", sha256="08e8f1a80669dc3eee5ba237fc00c867a8858f9b186bbec8571a8cf9af36f543", url="https://pypi.org/packages/e0/91/19d4cd8a3a6948e132341c0ea0c6abc4cb96d325315a809b5a2e5093958b/gpytorch-1.6.0.tar.gz")
    version("1.5.1", sha256="906fbde6998fa58739d166a44bb867d25908a59fc3d5d65b5761516db64b681d", url="https://pypi.org/packages/31/9b/25fe1e86be169190ff3ba91230e61f0a787f5dabfb787143d5690eb78d39/gpytorch-1.5.1-py2.py3-none-any.whl")
    version("1.2.1", sha256="ddd746529863d5419872610af23b1a1b0e8a29742131c9d9d2b4f9cae3c90781", url="https://pypi.org/packages/c4/9d/84ee6a49ce095ae2f218cbb3e23c4c732518482d13620ad35038c8038e79/gpytorch-1.2.1.tar.gz")
    version("1.2.0", sha256="fcb216e0c1f128a41c91065766508e91e487d6ffadf212a51677d8014aefca84", url="https://pypi.org/packages/6f/2f/6343548d88284ebf18d241dee12d0975cd7dbdee63c0fb749b23c8f536a1/gpytorch-1.2.0.tar.gz")
    version("1.1.1", sha256="76bd455db2f17af5425f73acfaa6d61b8adb1f07ad4881c0fa22673f84fb571a", url="https://pypi.org/packages/5d/c7/0c31802b84fc55aa069943c844eaccb0e420e91d7f4ed07cc5e1d127c458/gpytorch-1.1.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-linear-operator@0.5:", when="@1.11:")
        depends_on("py-linear-operator@0.4:", when="@1.10")
        depends_on("py-linear-operator@0.2:", when="@1.9.1:1.9")
        depends_on("py-linear-operator@0.1.1:", when="@1.9:1.9.0")
        depends_on("py-numpy", when="@1.7:1.8")
        depends_on("py-scikit-learn@:1.0", when="@1.7")
        depends_on("py-scikit-learn", when="@1.4.1:1.5,1.8:")
        depends_on("py-scipy", when="@1.4.1:1.5,1.7:1.8")
        depends_on("py-torch@1.10:", when="@1.7:1.8")
        depends_on("py-torch@1.8.1:", when="@1.5")
    # END DEPENDENCIES

