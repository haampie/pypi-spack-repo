##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySqlmodel(PythonPackage):
    version("0.0.16", sha256="b972f5d319580d6c37ecc417881f6ec4d1ad3ed3583d0ac0ed43234a28bf605a", url="https://pypi.org/packages/1b/a9/5a8dde5fae37b98cd33ce0b62a1861ddbdddfab0ddb9f80d56c775ba3adc/sqlmodel-0.0.16-py3-none-any.whl")
    version("0.0.15", sha256="f57707cc16393946a86bd0567408054d34cacdae6e86b2dfd07a87fca319fe05", url="https://pypi.org/packages/ed/9c/7063ff020f20028d53577668c17381ce805cf72b57873d332dc69b047c51/sqlmodel-0.0.15-py3-none-any.whl")
    version("0.0.14", sha256="accea3ff5d878e41ac439b11e78613ed61ce300cfcb860e87a2d73d4884cbee4", url="https://pypi.org/packages/55/b2/ea0c31d2bb8d22dffd83f43028d8d1b18301702725d6b918ac15f99b6de7/sqlmodel-0.0.14-py3-none-any.whl")
    version("0.0.13", sha256="5c669293aba105dcc4874f980af34da2de9af9ca73eb7b02e0e8f1ace4374a1a", url="https://pypi.org/packages/69/9f/3388301ce63181c8ffa2c5011ef904e8641f6ac90ad9a4b615899ef70273/sqlmodel-0.0.13-py3-none-any.whl")
    version("0.0.12", sha256="5a246e184c3b41126e3f862912be732261da5dc2a1f135eb98d6dca9977345f5", url="https://pypi.org/packages/90/47/fe5544f6ab50070cfb115a4e3786166ad0bd25ec22ca948350fd7802ce09/sqlmodel-0.0.12-py3-none-any.whl")
    version("0.0.11", sha256="bc0d64c4b901d919d2f16bbd79aefb07cb268c29f7c1dd83a84758772ccc95c6", url="https://pypi.org/packages/9f/d0/8938bcf1c2d5c1f2a4aadece26364996aef437dbc7d5fcfa87cd1e13f7c6/sqlmodel-0.0.11-py3-none-any.whl")
    version("0.0.10", sha256="10b3a312f66bed2b88a7b369cd06d1c0e89f62ad8e6303eefa1ea5b3e7b141f4", url="https://pypi.org/packages/27/5a/e4f43e50c3c40517e7bc492fd66b3da2ced78e7aef00f09a689df93a8073/sqlmodel-0.0.10-py3-none-any.whl")
    version("0.0.9", sha256="29739ce1d7b02cfbbc38f42d83e975a13aa7238fc0b12b6b670d2a6d54e45957", url="https://pypi.org/packages/65/3b/e696dde1707868effa0a5d20f3dcae049a3a94353cf9edf42bcb100823ca/sqlmodel-0.0.9-py3-none-any.whl")
    version("0.0.8", sha256="0fd805719e0c5d4f22be32eb3ffc856eca3f7f20e8c7aa3e117ad91684b518ee", url="https://pypi.org/packages/90/63/65f95cf5902ccdfccec99de87666b5e039589c19db7ab62b3770171e5685/sqlmodel-0.0.8-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pydantic@2:", when="@0.0.14:")
        depends_on("py-pydantic@1.9.0:1", when="@0.0.10:0.0.13")
        depends_on("py-pydantic@1.8.2:1", when="@:0.0.9")
        depends_on("py-sqlalchemy@2.0.0:", when="@0.0.12:")
        depends_on("py-sqlalchemy@1.4.36:1", when="@0.0.9:0.0.11")
        depends_on("py-sqlalchemy@1.4.17:1.4.41", when="@0.0.7:0.0.8")
        depends_on("py-sqlalchemy2-stubs", when="@0.0.3:0.0.11")

