# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCerberus(PythonPackage):
    # BEGIN VERSIONS
    version("1.3.5", sha256="7649a5815024d18eb7c6aa5e7a95355c649a53aacfc9b050e9d0bf6bfa2af372", url="https://pypi.org/packages/fb/17/335e0a4daf5475ada5eaa74735f765cc088ace306fbfdd2f4c2285320cc3/Cerberus-1.3.5-py3-none-any.whl")
    version("1.3.4", sha256="d1b21b3954b2498d9a79edf16b3170a3ac1021df88d197dc2ce5928ba519237c", url="https://pypi.org/packages/c4/87/55f8b2e36a5f97c5aaf6424e75f7a21cbd69d0365f6e2e332d03d029bb15/Cerberus-1.3.4.tar.gz")
    version("1.3.3", sha256="7aff49bc793e58a88ac14bffc3eca0f67e077881d3c62c621679a621294dd174", url="https://pypi.org/packages/7f/2c/4e0755ad65cce6d2c847ce09e5c327c4e10a8db2c90b34aaccf6752b6c60/Cerberus-1.3.3-py3-none-any.whl")
    version("1.3.2", sha256="302e6694f206dd85cb63f13fd5025b31ab6d38c99c50c6d769f8fa0b0f299589", url="https://pypi.org/packages/90/a7/71c6ed2d46a81065e68c007ac63378b96fa54c7bb614d653c68232f9c50c/Cerberus-1.3.2.tar.gz")
    version("1.3.1", sha256="0be48fc0dc84f83202a5309c0aa17cd5393e70731a1698a50d118b762fbe6875", url="https://pypi.org/packages/c9/0e/f78e23b778c2234972d364d0f8bea2de0a09f450f65d3f05ce091dd0f104/Cerberus-1.3.1.tar.gz")
    version("1.3", sha256="7ffefb2ea4159040750ae6e8e8d85660d3ccb8895926b95c90508b803aaad029", url="https://pypi.org/packages/2d/fd/5358504b5b9109abeeec7f85e93091f1222a6c3ee1cdabc855ad1c508419/Cerberus-1.3.tar.gz")
    version("1.2", sha256="f5c2e048fb15ecb3c088d192164316093fcfa602a74b3386eefb2983aa7e800a", url="https://pypi.org/packages/90/31/e30784a1f9a4b46875cfed1c9f806c188e2181e7ba3b568e81e7b0bc5718/Cerberus-1.2.tar.gz")
    version("1.1", sha256="a5b39090fde3ec3294c9d7030b8eda935b42222160a66a922e0c8aea34cabfdf", url="https://pypi.org/packages/e0/7e/3949c86f4e60bc2b3d24ebc94af55ffaf9d62ad221f47c194edc9bd7fa94/Cerberus-1.1.tar.gz")
    version("1.0.1", sha256="b4d6a6a355fef497875ccca2ad482b3511c3e8739919f2cbf58a0dacf09d9f9f", url="https://pypi.org/packages/5e/49/a4ab98865ce395945d3930c4495844d67091363c589d92ee7f4b5e538c0a/Cerberus-1.0.1.tar.gz")
    version("0.9.2", sha256="b122c7b2cbf856ea2587e187fac968fc8dcd49d47aa1f239abd9eaa0ed86a7ce", url="https://pypi.org/packages/c1/7a/65f3aa48279cda81208ccca4c932e63fedaf02f80f1fb6a482a7b8d8f239/Cerberus-0.9.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-setuptools", when="@1.3.3")
    # END DEPENDENCIES

