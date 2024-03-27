##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGrayskull(PythonPackage):
    version("2.5.0", sha256="81477d18cb1c96de06173337a5fe46eb2e04a793dd1773ec990d3efa2c9f8949", url="https://pypi.org/packages/68/3e/bc10142d64e27d66144cd462e1c11325bd1beccdce6dda1810cf86f8dc37/grayskull-2.5.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-beautifulsoup4", when="@2:")
        depends_on("py-colorama")
        depends_on("py-conda-souschef@2.2.3:", when="@1.8.2:")
        depends_on("py-packaging@21.3:", when="@1.7:")
        depends_on("py-pip")
        depends_on("py-pkginfo", when="@1.1:")
        depends_on("py-progressbar2@3.53:", when="@0.8.2:")
        depends_on("py-rapidfuzz@3:", when="@2.3.1:")
        depends_on("py-requests")
        depends_on("py-ruamel-yaml@0.16.10:", when="@0.8.2:")
        depends_on("py-ruamel-yaml-jinja2")
        depends_on("py-semver@3.0.0:3.0.0.0,3.0.1:", when="@2.3.1:")
        depends_on("py-setuptools@30.3:")
        depends_on("py-stdlib-list")
        depends_on("py-tomli", when="@1.4.1:")
        depends_on("py-tomli-w", when="@1.4.1:")
