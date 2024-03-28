# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkAvrouting(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="133d646cf36cfa329c2b3a060c7b81368a95bfbb24f30e2bae2804be65b93ec9", url="https://pypi.org/packages/d9/0b/9c2686f2ea430a555d6f92d00be491e0eb630e2f4c0d7acfc0ff4dfa6db4/pyobjc-framework-AVRouting-10.2.tar.gz")
    version("10.1", sha256="148fc29d0d5e73fb23ed64edede3f74d902ec41b7a7869435816a7a1b37aa038", url="https://pypi.org/packages/5f/cd/9bd4de868b83037591dd5e77380b805ae35285746b6cba6c60d8fd528594/pyobjc-framework-AVRouting-10.1.tar.gz")
    version("10.0", sha256="41213eb9fdff4ec58dddee240de7100601cef74e458265623763b460a422438c", url="https://pypi.org/packages/97/71/f2c214125aed89aeedb08aa6eb30497effcc341cabed7459498ada0d1f4e/pyobjc-framework-AVRouting-10.0.tar.gz")
    version("9.2", sha256="c82794218db58fcbc066f016a273f24977c639aa4a844d3f659f236736b50d3e", url="https://pypi.org/packages/d3/67/cd26cc741171ce733c8077b26760b5e333b24f9cebf3002cb309b9b1ba78/pyobjc-framework-AVRouting-9.2.tar.gz")
    version("9.1.1", sha256="8e0b6108aafa8e9ad78dfefb4f8a3136be08c5bcd8785861a807eddfeb94209b", url="https://pypi.org/packages/8a/e4/dd731e88c5a4c6d30abac2bb7fc6f873b16722b0e648da3f95dff91e3d61/pyobjc-framework-AVRouting-9.1.1.tar.gz")
    version("9.1", sha256="a5cda5131f4ac06a6fc89c87e19fda340e525cf93d5e04959a5f7e2d890cb29c", url="https://pypi.org/packages/23/42/7e0abb332ce877092a741983f745d782750fbf04ffdac2f6ae723d0ca026/pyobjc-framework-AVRouting-9.1.tar.gz")
    version("9.0.1", sha256="1236a46bece3766383b3bd73d78f49e9b501cc9824474c3db6bfc2ab84cb3cb4", url="https://pypi.org/packages/8e/c7/e75ca5b959a931b1fd7bbdf81f8a3460277df55b13b70b366c1598f6570c/pyobjc-framework-AVRouting-9.0.1.tar.gz")
    version("9.0", sha256="a183c9be184a9ea3a387726f69175ad8ff39eae0144a2b554ef4040f33a14ce2", url="https://pypi.org/packages/bb/0b/27592c41af65f6a6c911476ddaf83f288396dd647451a4e6f69f95bbed03/pyobjc-framework-AVRouting-9.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
    # END DEPENDENCIES

