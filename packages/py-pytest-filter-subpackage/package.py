# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestFilterSubpackage(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2.0", sha256="b4a8c21b52110c3fefe949229c387c18be081132138ca3acc4953869a459b3f6", url="https://pypi.org/packages/ac/f8/2ed436b6ef3fb46743ba6e562c5421493d695c6534f051420ef2b5a99258/pytest_filter_subpackage-0.2.0-py2.py3-none-any.whl")
    version("0.1.2", sha256="39a1fb6f559e0579851c1e447d3c876f6a5c2e49ab356c568b90e4f5b0d4a19e", url="https://pypi.org/packages/f0/23/67097daf438eef3b4c7bf90939445e89983801c1c40e2c377ebd234c55ad/pytest_filter_subpackage-0.1.2-py2.py3-none-any.whl")
    version("0.1.1", sha256="75c49105ec3d7850606d63ef1d583427140d2b71c39540633cb22dffd8da1ddb", url="https://pypi.org/packages/a7/0f/a9625b73f6dde09bf766123bf9e98b97018a8cc36d564553ec6484b5349a/pytest_filter_subpackage-0.1.1-py2.py3-none-any.whl")
    version("0.1", sha256="35dd8e6c9543634ed6ef7c53aaa7edb59459055bb20e370584094c9026545a41", url="https://pypi.org/packages/d8/6e/5223667342d3e78b1bb5425708e60f7ee1356ed1fdf7dd73ef83ce48fe9f/pytest_filter_subpackage-0.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-packaging", when="@0.2:")
        depends_on("py-pytest@4.6:", when="@0.2:")
        depends_on("py-pytest@3:", when="@:0.1")
    # END DEPENDENCIES

