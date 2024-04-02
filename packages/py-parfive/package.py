# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyParfive(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.0.2", sha256="c6b6de349078edcfb88f76ba63f16983ba30ecb6c2105dff578c1cbe3bf15dd4", url="https://pypi.org/packages/5c/41/cf4dad1a42119d65daf2aa3fe50a91e96a474f49e6f3435deb1f8b3900d1/parfive-2.0.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("ftp", default=False, description="ftp")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:")
        depends_on("py-aioftp@0.17.1:", when="+ftp")
        depends_on("py-aiohttp")
        depends_on("py-tqdm@4.27:", when="@2:")
        depends_on("py-typing-extensions", when="@2: ^python@:3.7")
    # END DEPENDENCIES

