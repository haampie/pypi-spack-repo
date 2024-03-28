# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPdf2image(PythonPackage):
    # BEGIN VERSIONS
    version("1.16.3", sha256="b6154164af3677211c22cbb38b2bd778b43aca02758e962fe1e231f6d3b0e380", url="https://pypi.org/packages/e2/8c/37a7467d88c47e435429c147020c2fb53206fabfc44b8b72f9728e79ce1a/pdf2image-1.16.3-py3-none-any.whl")
    version("1.12.1", sha256="a0d9906f5507192210a8d5d7ead63145e9dec4bccc4564b1fb644e923913c31c", url="https://pypi.org/packages/c3/12/ba5aadb3ba2e9c0f15d897622aa5707d64d0b2cab1fb34bee21559fa386a/pdf2image-1.12.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pillow", when="@1.13.1:")
    # END DEPENDENCIES

