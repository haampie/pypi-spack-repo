# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySphinxPrompt(PythonPackage):
    # BEGIN VERSIONS
    version("1.8.0", sha256="369ecc633f0711886f9b3a078c83264245be1adf46abeeb9b88b5519e4b51007", url="https://pypi.org/packages/39/49/f890a2668b7cbf375f5528b549c8d36dd2e801b0fbb7b2b5ef65663ecb6c/sphinx_prompt-1.8.0-py3-none-any.whl")
    version("1.1.0", sha256="3d9cf382b750291f73d1f6f1713c4af0557c30208af124cd3d8731e607a4febf", url="https://pypi.org/packages/16/1e/0dd94829b97676b7d7cdf2f0e86cb169d6f2ffb56590427833d281370116/sphinx-prompt-1.1.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:3", when="@1.8:")
        depends_on("py-docutils", when="@1.6:")
        depends_on("py-pygments", when="@1.1,1.3:")
        depends_on("py-sphinx@7.0.0:", when="@1.7:")
        depends_on("py-sphinx", when="@1.1,1.3:1.5")
    # END DEPENDENCIES

