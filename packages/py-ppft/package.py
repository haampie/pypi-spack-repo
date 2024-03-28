# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPpft(PythonPackage):
    # BEGIN VERSIONS
    version("1.6.6.4", sha256="63d12035786dfd52e7a0fedcd75a498b68b80e6ac54720cd8a4282512608131c", url="https://pypi.org/packages/e1/95/17253538621d21308a6e7ca67cd8f87c64e81f95477e57ee78766cf79aaa/ppft-1.6.6.4-py3-none-any.whl")
    version("1.6.4.9", sha256="5537b00afb7b247da0f59cc57ee5680178be61c8b2e21b5a0672b70a3d247791", url="https://pypi.org/packages/a5/6c/16bdc13a8defc8ccab8b5c1a3dfb1331343b313f52984be0f4d6521eb92c/ppft-1.6.4.9.tar.gz")
    version("1.6.4.7.1", sha256="f94b26491b4a36adc975fc51dba7568089a24756007a3a4ef3414a98d7337651", url="https://pypi.org/packages/af/5c/1caaa791e4bd77a977692250b0fe5c14fc816576485c88e8ccf328f03fc9/ppft-1.6.4.7.1.zip")
    version("1.6.4.6", sha256="92d09061f5425634c43dbf99c5558f2cf2a2e1e351929f8da7e85f4649c11095", url="https://pypi.org/packages/d6/6b/dcd9898e6fa21cf708ce95b45eaa7ac867453ae104ec510c22d1365e8943/ppft-1.6.4.6.zip")
    version("1.6.4.5", sha256="800f4fbb797305a7f1074db22fe90618181ffe0a0c8212fe518bbaed831e78b6", url="https://pypi.org/packages/65/ec/0fd42f9c7496c5a4c4d244d49acc976ccb3ae276c314c0e525c1bcbe416d/ppft-1.6.4.5.tgz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six@1.7.3:", when="@1.6.6.3:1.7.6.5")
    # END DEPENDENCIES

