# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLzstring(PythonPackage):
    # BEGIN VERSIONS
    version("1.0.4", sha256="1afa61e598193fbcc211e0899f09a9679e33f9102bccc37fbfda0b7fef4d9ea2", url="https://pypi.org/packages/ab/0c/28347673b45e5f0975cdf1f6d69ede6ad049be873194c4e164d79aecd34c/lzstring-1.0.4.tar.gz")
    version("1.0.3", sha256="82a913b08f6eaacf584624e4cbd5e5c361b546d0f9ec5620760d2ca137926811", url="https://pypi.org/packages/bd/4e/0885ee80e75b709dfb0750dacfc9bd1bff37c591c777015d43d5679d60b0/lzstring-1.0.3-py2.py3-none-any.whl")
    version("1.0.2", sha256="afd93ffb6e854390d61c72360aff164fb83665a01485e77758f46d29227227e2", url="https://pypi.org/packages/4b/77/6eca8acbe040802a281332a8c309a428558d90652949743b7d5acad1ab5f/lzstring-1.0.2-py2.py3-none-any.whl")
    version("1.0.1", sha256="dd3cf2699a5dac0a88c915ba84073d7c3bcf940dc4c8c0c73a29cca3d3b7502a", url="https://pypi.org/packages/99/f1/3df813e2cd9f9440ad278aa52cdd0bbc20f658595bf684585b9bfe370008/lzstring-1.0.1-py2.py3-none-any.whl")
    version("1.0.0", sha256="45e543dda42ac00f03bd6649f97fbbc8f311d2f1917214f231361ae19a1eea84", url="https://pypi.org/packages/2b/79/dd05f128498709d0db77b7d34aa2332992600fdb3c14b3ac7798b1ef0f04/lzstring-1.0.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-future", when="@1.0.1:1.0.3")
    # END DEPENDENCIES

