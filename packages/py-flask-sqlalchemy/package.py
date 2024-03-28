# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFlaskSqlalchemy(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.1.1", sha256="4ba4be7f419dc72f4efd8802d69974803c37259dd42f3913b0dcf75c9447e0a0", url="https://pypi.org/packages/1d/6a/89963a5c6ecf166e8be29e0d1bf6806051ee8fe6c82e232842e3aeac9204/flask_sqlalchemy-3.1.1-py3-none-any.whl")
    version("3.1.0", sha256="3f7060d00edb229ef2f2d98b414bc49fc1a4b26562af94cc1f090fc6c41bf41d", url="https://pypi.org/packages/f2/43/41158f14ebf519f1f0edda4c0bd2ff983cdee8777d541621cc41c9192cec/flask_sqlalchemy-3.1.0-py3-none-any.whl")
    version("3.0.5", sha256="cabb6600ddd819a9f859f36515bb1bd8e7dbf30206cc679d2b081dff9e383283", url="https://pypi.org/packages/d8/1d/c3c5afdaebd5d5f82d2c25762f5356416bd7bc109a550c79247134e48ca3/flask_sqlalchemy-3.0.5-py3-none-any.whl")
    version("3.0.4", sha256="23d44ca566b02b0b5ee5b29d81b435079402ad73c116bf9918dbda5b03aa30ba", url="https://pypi.org/packages/2a/47/8f9010cd80553e26c7d4533f1972d04648f49edde2aa2895636792364aad/flask_sqlalchemy-3.0.4-py3-none-any.whl")
    version("3.0.3", sha256="add5750b2f9cd10512995261ee2aa23fab85bd5626061aa3c564b33bb4aa780a", url="https://pypi.org/packages/cf/93/606d1967d6ef1c663ccccc739b361e7672ec057bf086ca7e4cd23eda18a9/Flask_SQLAlchemy-3.0.3-py3-none-any.whl")
    version("3.0.2", sha256="7d0cd9cf73e64a996bb881a1ebd01633fc5a6d11c36ea27f7b5e251dc45476e7", url="https://pypi.org/packages/1b/9c/2b3ce12b3f7eca00d1f54a6eb84e6cb57b628aa2891a81bb12dfd8b6d604/Flask_SQLAlchemy-3.0.2-py3-none-any.whl")
    version("3.0.1", sha256="649eddf17ae18814f87f33eb26d9d7b37412ec7ee67985873b3cf882aca099f5", url="https://pypi.org/packages/84/83/b7bc5e3ee7b91790d57438ff955cdd7ada8f50770b6dddbd144ca886f19e/Flask_SQLAlchemy-3.0.1-py3-none-any.whl")
    version("3.0.0", sha256="741dabf0903569a89e4793667e25be5bb9581e614fa0eeb81a395cc7dee40c4b", url="https://pypi.org/packages/8b/f7/ee9396c347cdc61d95f20574ae20490d9f474d6255d75a01592ea95f8cbc/Flask_SQLAlchemy-3.0.0-py3-none-any.whl")
    version("2.5.1", sha256="f12c3d4cc5cc7fdcc148b9527ea05671718c3ea45d50c7e732cceb33f574b390", url="https://pypi.org/packages/26/2c/9088b6bd95bca539230bbe9ad446737ed391aab9a83aff403e18dded3e75/Flask_SQLAlchemy-2.5.1-py2.py3-none-any.whl")
    version("2.5.0", sha256="0d5153bf451c42880540eea7650300cf0dfec0c16c554f0de5541e78c7cc0443", url="https://pypi.org/packages/68/85/fd40f11861d97cbaf4b0369288a293f2017dcea1fd52da2a652b2ceae15a/Flask_SQLAlchemy-2.5.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-flask@2.2.5:", when="@3.0.4:")
        depends_on("py-flask@2.2:", when="@3.0.0:3.0.3")
        depends_on("py-flask@0.10:", when="@2.2:2")
        depends_on("py-sqlalchemy@2.0.16:", when="@3.1:")
        depends_on("py-sqlalchemy@1.4.18:", when="@3.0.0:3.0")
        depends_on("py-sqlalchemy@0.8.0:", when="@2.2:2")
    # END DEPENDENCIES

