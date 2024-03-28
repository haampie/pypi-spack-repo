# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPybtex(PythonPackage):
    # BEGIN VERSIONS
    version("0.24.0", sha256="e1e0c8c69998452fea90e9179aa2a98ab103f3eed894405b7264e517cc2fcc0f", url="https://pypi.org/packages/ad/5f/40d8e90f985a05133a8895fc454c6127ecec3de8b095dd35bba91382f803/pybtex-0.24.0-py2.py3-none-any.whl")
    version("0.21", sha256="af8a6c7c74954ad305553b118d2757f68bc77c5dd5d5de2cc1fd16db90046000", url="https://pypi.org/packages/82/59/d46b4a84faacd7c419cfc9a442b7940d6d625d127b83d83666e2a8b203d8/pybtex-0.21.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-latexcodec@1.0.4:", when="@0.22:")
        depends_on("py-pyyaml", when="@0.22:")
        depends_on("py-six", when="@0.22:")
    # END DEPENDENCIES

