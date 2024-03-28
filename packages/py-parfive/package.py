# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyParfive(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.0.2", sha256="c6b6de349078edcfb88f76ba63f16983ba30ecb6c2105dff578c1cbe3bf15dd4", url="https://pypi.org/packages/5c/41/cf4dad1a42119d65daf2aa3fe50a91e96a474f49e6f3435deb1f8b3900d1/parfive-2.0.2-py3-none-any.whl")
    version("2.0.1", sha256="0ba827f7f1dd558eae36a27445eae7fce503273e9914c9f71ff4a83b529f7e5a", url="https://pypi.org/packages/9e/19/3d0ce34f7e5bce631371ad96600fa978f38f633ac9f8fe5e13e2e63c8078/parfive-2.0.1-py3-none-any.whl")
    version("2.0.0", sha256="6653f6cc9c65eb8ad87bc8e1a15726295285cbbdbb70738f39bd81d5108e5e5e", url="https://pypi.org/packages/c8/50/f5753ff4a497c71674ebaa3526beb0a8c564353ab43bf7234681099cfab6/parfive-2.0.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("ftp", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-aioftp@0.17.1:", when="@1.1.1:+ftp")
        depends_on("py-aiohttp", when="@1.1.1:")
        depends_on("py-tqdm@4.27:", when="@2:")
    # END DEPENDENCIES

