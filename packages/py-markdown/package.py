# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMarkdown(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.4.1", sha256="08fb8465cffd03d10b9dd34a5c3fea908e20391a2a90b88d66362cb05beed186", url="https://pypi.org/packages/86/be/ad281f7a3686b38dd8a307fa33210cdf2130404dfef668a37a4166d737ca/Markdown-3.4.1-py3-none-any.whl")
    version("3.3.4", sha256="96c3ba1261de2f7547b46a00ea8463832c921d3f9d6aba3f255a6f71386db20c", url="https://pypi.org/packages/6e/33/1ae0f71395e618d6140fbbc9587cc3156591f748226075e0f7d6f9176522/Markdown-3.3.4-py3-none-any.whl")
    version("3.1.1", sha256="56a46ac655704b91e5b7e6326ce43d5ef72411376588afa1dd90e881b83c7e8c", url="https://pypi.org/packages/c0/4e/fd492e91abdc2d2fcb70ef453064d980688762079397f779758e055f6575/Markdown-3.1.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-importlib-metadata@4.4:", when="@3.3.6: ^python@:3.9")
        depends_on("py-setuptools@36:", when="@3.1:3.2.1")
    # END DEPENDENCIES

