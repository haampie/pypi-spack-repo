# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAiosignal(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.3.1", sha256="f8376fb07dd1e86a584e4fcdec80b36b7f81aac666ebc724e2c090300dd83b17", url="https://pypi.org/packages/76/ac/a7305707cb852b7e16ff80eaf5692309bde30e2b1100a1fcacdc8f731d97/aiosignal-1.3.1-py3-none-any.whl")
    version("1.2.0", sha256="26e62109036cd181df6e6ad646f91f0dcfd05fe16d0cb924138ff2ab75d64e3a", url="https://pypi.org/packages/3b/87/fe94898f2d44a93a35d5aa74671ed28094d80753a1113d68b799fab6dc22/aiosignal-1.2.0-py3-none-any.whl")
    version("1.2.0-alpha0", sha256="c2a993c5a6ed4d59f288ff381580cca56a1a3602a49e13bb77a4fabddebfe2ee", url="https://pypi.org/packages/56/c1/10009f8d026984ca71b5164c1e8f5ebe8d5b9f27a22470cb1a6a6371e02c/aiosignal-1.2.0a0-py3-none-any.whl")
    version("1.1.2", sha256="8e99b2b25a185f678f0c90dccc067ee6d13855996ef5c2e0ea808a2608bc6003", url="https://pypi.org/packages/c4/5a/e91461e28a7d53bdb37bce73fc0f5b0fc986fb90e37b97e0ec72650794c0/aiosignal-1.1.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-frozenlist@1.1:", when="@1.1:")
    # END DEPENDENCIES

