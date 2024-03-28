# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBranca(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.7.1", sha256="70515944ed2d1ed2784c552508df58037ca19402a8a1069d57f9113e3e012f51", url="https://pypi.org/packages/17/ce/14166d0e273d12065516625fb02426350298e7b4ba59198b5fe454b46202/branca-0.7.1-py3-none-any.whl")
    version("0.7.0", sha256="c653d9a3fef1e6cd203757c77d3eb44810f11998506451f9a27d52b983500c16", url="https://pypi.org/packages/2f/e7/603b136221de923055716d23e3047da71f92e0d8ba2c4517ce49a54fe768/branca-0.7.0-py3-none-any.whl")
    version("0.6.0", sha256="ae706fc7a88dd0296a58bb11c0cb3c6be358491a3b0abee08fe16b4db17814c0", url="https://pypi.org/packages/a6/18/cea6374623d82efc292996997cee0a13ae99359c7e66db22f92dc8484dd1/branca-0.6.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-jinja2@3.0.0:", when="@0.7.1:")
        depends_on("py-jinja2", when="@0.2:0.7.0")
    # END DEPENDENCIES

