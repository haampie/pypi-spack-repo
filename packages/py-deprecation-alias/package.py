##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDeprecationAlias(PythonPackage):
    version("0.3.2", sha256="ed2e9dde582530e2a364cae4fa26077fda4adc9b28a44ce94a8ef0ee9271e312", url="https://pypi.org/packages/58/65/b1c462900b300b82d94cff397a6bd6293232644c5741fbc1fcbc385e2de5/deprecation_alias-0.3.2-py3-none-any.whl")
    version("0.3.1", sha256="8daac9bb342c293caf88ddb6b69ac6bd62e9b8bbe7108441bf916069682721e3", url="https://pypi.org/packages/3c/bd/ee6341cbb685653f4984634bfa8be151ef5b0c899c62e100772633bfa2d6/deprecation_alias-0.3.1-py3-none-any.whl")
    version("0.3.0", sha256="7cd6d2d0a444eccc928593459ecd45bb0916a3b9e8f394ffff7064b023276b17", url="https://pypi.org/packages/57/1e/20ea1dc6790a9dc2ff8a762d91a3ca9d60589af43cafebff3ac6defa28cf/deprecation_alias-0.3.0-py3-none-any.whl")
    version("0.2.0", sha256="26d784e0a3c40503c1c1cd36af5d1a98a2e8fe019740d1d5c72217c6cdfe9d6e", url="https://pypi.org/packages/4a/5f/478164c5138d1fc388f3c3af59fc4edea9b1b1328fc6d3c3305862240aae/deprecation_alias-0.2.0-py3-none-any.whl")
    version("0.1.1", sha256="f60f4c50bbbe4a264fe662b82e2f3654cfe505f83ef5156c9c0b3643ec0c5499", url="https://pypi.org/packages/eb/dd/0c7a0c7be76cfd35c669ca68fe9837e88ce80584dc5d274f4044cd15e581/deprecation_alias-0.1.1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-deprecation@2.1:")
        depends_on("py-packaging@20.4:")

