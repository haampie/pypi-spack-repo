# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPydmd(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.3", sha256="893e23fd8c3cc17d73a3828562a7bb312a8a04b882c6c1af89542a964694bf85", url="https://pypi.org/packages/f5/a9/4dc123fe2cb3c7854b68f28627723376a8da0749c47b323a5bdbcc8abeff/pydmd-0.3-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("docs", default=False, description="docs")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-future", when="@:0.0.2,0.3:0.4.0")
        depends_on("py-matplotlib", when="@:0.0.2,0.3:")
        depends_on("py-numpy", when="@:0.0.2,0.3:0.4.1.post2308")
        depends_on("py-scipy", when="@:0.0.2,0.3:")
        depends_on("py-sphinx@1.4:1.4.0", when="@0.3:0.4.0+docs")
        depends_on("py-sphinx-rtd-theme", when="@0.3:+docs")
    # END DEPENDENCIES

