##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySphinxThemeBuilder(PythonPackage):
    version("0.2.0-beta2", sha256="75c7aa71c977aedfca6b368f69d5f5a6e8444222e7716dc927dd8749511147aa", url="https://pypi.org/packages/fc/b3/64215aa620ab5d8d00118b378e43b94b8ba01d3640cf1e6bbdb01a7389ab/sphinx_theme_builder-0.2.0b2-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-nodeenv", when="@0.2.0-alpha3:")
        depends_on("py-packaging", when="@0.2:")
        depends_on("py-pyproject-metadata", when="@0.2.0-beta1:")
        depends_on("py-rich", when="@0.2:")
        depends_on("py-setuptools", when="@0.2.0-alpha5:")
        depends_on("py-tomli", when="@0.2.0-beta2: ^python@:3.10")
        depends_on("py-tomli", when="@0.2:0.2.0-beta1")

