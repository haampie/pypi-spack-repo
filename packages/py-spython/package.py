# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySpython(PythonPackage):
    # BEGIN VERSIONS
    version("0.3.13", sha256="3c16e05261647dc4f5931d641adb179f21b4bd117572c161bdf54fe511cda4d8", url="https://pypi.org/packages/eb/22/80e6468f3978e0d67833d5bf0b89338f5f3e9fc62618797e63f227961e14/spython-0.3.13-py3-none-any.whl")
    version("0.3.11", sha256="a48756520d7b2ab727b9b607d9122ca701a543deffc3d178bf92073c8e37d0f2", url="https://pypi.org/packages/de/db/61849739fcfe99c018499eec3649ad06934d87c30f6ebe0b0d52a893935f/spython-0.3.11-py3-none-any.whl")
    version("0.3.1", sha256="6c0519abee020a27532890ecf2d9360e361af7aac8fb0b84b497ab595fc5ecf2", url="https://pypi.org/packages/2d/f8/61e554883703b48d1d2d4c8c31ca09f6eeb243b239a75d023c2872eef20a/spython-0.3.1-py3-none-any.whl")
    version("0.3.0", sha256="a6819e6c82b759536ce6855647cdcf62177408d7818acb4360a95d64c1ad7ef6", url="https://pypi.org/packages/0e/ca/704861ab71d1ac4dff92ebf8208cd79db8b43096905e706bf9e502bc6b05/spython-0.3.0-py3-none-any.whl")
    version("0.2.14", sha256="49e22fbbdebe456b27ca17d30061489db8e0f95e62be3623267a23b85e3ce0f0", url="https://pypi.org/packages/42/ad/0ed334e53b3f093817fe9973d08ceacc83854784e69547aeb1202ad8538a/spython-0.2.14.tar.gz")
    version("0.2.13", sha256="d50632275d4cd60839124f4d5b0a548b4cdedae5e71de0da80b768f8e37e9a6f", url="https://pypi.org/packages/8c/f7/67818c7eaea6f5a4db1a763f393ec69c29a9f9d567bcf5095dbf19aa5624/spython-0.2.13.tar.gz")
    version("0.2.12", sha256="cec8bbd3beec28943c528906a0ba0e39e640289d6fd0f65639e6b8fe1abcb150", url="https://pypi.org/packages/23/02/63d5ce2921511b1685509b4758d1e0114c56cb78fb2777104aab5fac6c1e/spython-0.2.12.tar.gz")
    version("0.2.11", sha256="6c7db36b56b1e07814c49501dafa7bcca1698c5a0c3867d7b5fcaddf3ad797c4", url="https://pypi.org/packages/d9/0f/fc1bed0bf5f2226dedc5a913ed9f8ff85f8e3d12248b0e3d05d369183bad/spython-0.2.11.tar.gz")
    version("0.2.1", sha256="b1126c7b7da30d5bca508de29ef6aa3dc937b230c7aac6d021157bfc5a28bfe5", url="https://pypi.org/packages/ba/35/b877536673bf862b81f77b963d443ba612375d4d7dbe5474324729db8c9d/spython-0.2.1-py3-none-any.whl")
    version("0.2.0", sha256="25eef961ac5bbb4b3d1663713505b2b2f89c1dc6ab9ff6d5c464b04f066c7ff1", url="https://pypi.org/packages/36/9f/1430e1d5dbf95149097d7deb0a22901a3391ddc5e15a7cfc0528b8a05189/spython-0.2.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("runtime", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-semver@2.8.1:", when="@0.2:0.2.1")
    # END DEPENDENCIES

