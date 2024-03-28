# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySphinxPrompt(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.8.0", sha256="369ecc633f0711886f9b3a078c83264245be1adf46abeeb9b88b5519e4b51007", url="https://pypi.org/packages/39/49/f890a2668b7cbf375f5528b549c8d36dd2e801b0fbb7b2b5ef65663ecb6c/sphinx_prompt-1.8.0-py3-none-any.whl")
    version("1.1.0", sha256="8d2ef964527884dbfca17c41332ec06c8f069564b4bbec27578f021c65994e9a", url="https://pypi.org/packages/f8/57/f031af89d9e8234efbb54b83f19415c0d5f962e2a63cab6060870e79f091/sphinx_prompt-1.1.0-py2-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.8:")
        depends_on("python@:3.10", when="@1.6:1.7")
        depends_on("py-docutils", when="@1.6:")
        depends_on("py-pygments", when="@1.1,1.3:")
        depends_on("py-sphinx@7.0.0:", when="@1.7:")
        depends_on("py-sphinx", when="@1.1,1.3:1.5")
    # END DEPENDENCIES

