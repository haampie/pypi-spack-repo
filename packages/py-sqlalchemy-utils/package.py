# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySqlalchemyUtils(PythonPackage):
    # BEGIN VERSIONS
    version("0.41.2", sha256="85cf3842da2bf060760f955f8467b87983fb2e30f1764fd0e24a48307dc8ec6e", url="https://pypi.org/packages/d5/f0/dc4757b83ac1ab853cf222df8535ed73973e0c203d983982ba7b8bc60508/SQLAlchemy_Utils-0.41.2-py3-none-any.whl")
    version("0.41.1", sha256="6c96b0768ea3f15c0dc56b363d386138c562752b84f647fb8d31a2223aaab801", url="https://pypi.org/packages/73/d8/3863fdfe6b27f6c0dffc650aaa2929f313b33aea615b102279fd46ab550b/SQLAlchemy_Utils-0.41.1-py3-none-any.whl")
    version("0.41.0", sha256="986b4140f7740ff37244f6ed9182e8c997caa334150773de5932009b2490fb50", url="https://pypi.org/packages/5b/cc/6385cce6ebd60e4852e6a130774aaf911ca76098dfefae1de97b53561101/SQLAlchemy_Utils-0.41.0-py3-none-any.whl")
    version("0.40.0", sha256="4c7098d4857d5cad1248bf7cd940727aecb75b596a5574b86a93b37079929520", url="https://pypi.org/packages/99/12/73a5f6b2bd385361c7741d56b6a177b5661ac408050ee58ac133acb6c4ae/SQLAlchemy_Utils-0.40.0-py3-none-any.whl")
    version("0.39.0", sha256="9da26a9b20c6979167772ba5dc2a1d01265648f18c82995f082279a399ea308b", url="https://pypi.org/packages/12/c2/131e1c6ff887fde1783c1f21e9d132fb799b9c5680abb88c35f40a32a26c/SQLAlchemy_Utils-0.39.0-py3-none-any.whl")
    version("0.38.3", sha256="5c13b5d08adfaa85f3d4e8ec09a75136216fad41346980d02974a70a77988bf9", url="https://pypi.org/packages/e1/90/6ff1829b55cf752994be76bdf5f718db053dcb8d738f9df5b622207a4ab8/SQLAlchemy_Utils-0.38.3-py3-none-any.whl")
    version("0.38.2", sha256="622235b1598f97300e4d08820ab024f5219c9a6309937a8b908093f487b4ba54", url="https://pypi.org/packages/b1/f9/7fdb5a12d63f1d059530dd807e696f16062fa0630fac6b4ce1c74c4056f5/SQLAlchemy_Utils-0.38.2-py3-none-any.whl")
    version("0.38.1", sha256="a484ccfdc7f9298df49d2558a5309691e5e3e51c815a23a33b3355989176cb3e", url="https://pypi.org/packages/93/26/7de04d1cdf6085821266f8e56bf3804ba2f3370d2bbcd991265ee30638cb/SQLAlchemy_Utils-0.38.1-py3-none-any.whl")
    version("0.38.0", sha256="72b00a99941c376e03e4b4dd4df128b8237b1fc4f36601ab116ceab18cb22e1b", url="https://pypi.org/packages/36/54/f1e5dece9a89bd55cb6f100d80541e68315367276a6247f9936093644780/SQLAlchemy_Utils-0.38.0-py3-none-any.whl")
    version("0.37.9", sha256="bb6f4da8ac044cb0dd4d0278b1fb434141a5ee9d1881c757a076830ddbb04160", url="https://pypi.org/packages/81/13/042b6e1d500acd531a264d84a351203f4cb28b9f38a4ce49af1f2c17c90d/SQLAlchemy_Utils-0.37.9-py3-none-any.whl")
    version("0.36.8", sha256="fb66e9956e41340011b70b80f898fde6064ec1817af77199ee21ace71d7d6ab0", url="https://pypi.org/packages/14/68/e5301c4c960c79a32333b8805e52cb69d3d237aa869a773b4157ccb3eb26/SQLAlchemy-Utils-0.36.8.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six", when="@0.37:0.38.2")
        depends_on("py-sqlalchemy@1.3.0:", when="@0.38.3:")
        depends_on("py-sqlalchemy@1.0.0:", when="@0.37:0.38.2")
    # END DEPENDENCIES

