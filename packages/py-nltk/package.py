# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNltk(PythonPackage):
    # BEGIN VERSIONS
    version("3.8.1", sha256="fd5c9109f976fa86bcadba8f91e47f5e9293bd034474752e92a520f81c93dda5", url="https://pypi.org/packages/a6/0a/0d20d2c0f16be91b9fa32a77b76c60f9baf6eba419e5ef5deca17af9c582/nltk-3.8.1-py3-none-any.whl")
    version("3.5", sha256="845365449cd8c5f9731f7cb9f8bd6fd0767553b9d53af9eb1b3abf7700936b35", url="https://pypi.org/packages/92/75/ce35194d8e3022203cca0d2f896dbb88689f9b3fce8e9f9cff942913519d/nltk-3.5.zip")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("data", default=False, description="data")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@3.7:")
        depends_on("py-click", when="@3.6:")
        depends_on("py-joblib", when="@3.6:")
        depends_on("py-regex@2021.8:", when="@3.6.5:")
        depends_on("py-tqdm", when="@3.6:")
    # END DEPENDENCIES

