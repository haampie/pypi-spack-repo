# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGensim(PythonPackage):
    # BEGIN VERSIONS
    version("4.3.1", sha256="8b5f11c0e6a5308086b48e8f6841223a4fa1a37d513684612b7ee854b533015f", url="https://pypi.org/packages/9a/3c/dd4351a2ef3a8fb19e26d6ccb928823fea53375de9d28b221f8cf0e53c8e/gensim-4.3.1.tar.gz")
    version("3.8.3", sha256="786adb0571f75114e9c5f7a31dd2e6eb39a9791f22c8757621545e2ded3ea367", url="https://pypi.org/packages/a0/b4/f4e45875a4cb1c4f6a76d6d07a2981753aab5f135dac2381f625e8807542/gensim-3.8.3.tar.gz")
    version("3.8.1", sha256="33277fc0a8d7b0c7ce70fcc74bb82ad39f944c009b334856c6e86bf552b1dfdc", url="https://pypi.org/packages/73/f2/e9af000df6419bf1a63ffed3e6033a1b1d8fcf2f971fcdac15296619aff8/gensim-3.8.1.tar.gz")
    version("3.8.0", sha256="ec5de7ff2bfa8692fa96a846bb5aae52f267fc322fbbe303c1f042d258af5766", url="https://pypi.org/packages/3a/bc/1415be59292a23ff123298b4b46ec4be80b3bfe72c8d188b58ab2653dee4/gensim-3.8.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cython@0.29.14", when="@3.8.3:3")
        depends_on("py-numpy@1.11.3:1.16.1", when="@3.8.1")
        depends_on("py-numpy@1.11.3:", when="@2.2:3.1,3.3:3.6,3.7.1:3.8.0,3.8.2:3")
        depends_on("py-scipy@0.18.1:", when="@2.3:3.1,3.3:3.6,3.7.1:3.8.1,3.8.3:3")
        depends_on("py-six@1.5:", when="@0.12.3:0.13.0-rc1,0.13.1,0.13.3:0,1.0.0-rc2:1,2.1:3.1,3.3:3.6,3.7.1:3")
        depends_on("py-smart-open@1.8.1:", when="@3.8.1:3")
        depends_on("py-smart-open@1.7:", when="@3.7.1:3.8.0")
    # END DEPENDENCIES

