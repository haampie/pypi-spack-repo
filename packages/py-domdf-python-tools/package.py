# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDomdfPythonTools(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.6.1", sha256="e18158460850957f18e740eb94ede56f580ddb0cb162ab9d9834ed8bbb1b6431", url="https://pypi.org/packages/1d/02/3f4c36a3f2c4ee55bf28c31c36b0a795ccaed144cebb4ece9c94ac587952/domdf_python_tools-3.6.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-importlib-metadata@3.6:", when="@3: ^python@:3.8")
        depends_on("py-natsort@7.0.1:", when="@3:")
        depends_on("py-typing-extensions@3.7.4.1:", when="@3:")
    # END DEPENDENCIES

