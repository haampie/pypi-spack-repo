# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTwine(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("5.0.0", sha256="a262933de0b484c53408f9edae2e7821c1c45a3314ff2df9bdd343aa7ab8edc0", url="https://pypi.org/packages/9a/d4/4db90c4a2b8c1006ea3e6291f36b50b66e45887cf17b3b958b5d646fb837/twine-5.0.0-py3-none-any.whl")
    version("4.0.2", sha256="929bc3c280033347a00f847236564d1c52a3e61b1ac2516c97c48f3ceab756d8", url="https://pypi.org/packages/3a/38/a3f27a9e8ce45523d7d1e28c09e9085b61a98dab15d35ec086f36a44b37c/twine-4.0.2-py3-none-any.whl")
    version("4.0.1", sha256="42026c18e394eac3e06693ee52010baa5313e4811d5a11050e7d48436cf41b9e", url="https://pypi.org/packages/38/ab/5adc82687fea5cc0414a2bb6a871ef269f8c80e808d279ee5be6fa9ad911/twine-4.0.1-py3-none-any.whl")
    version("4.0.0", sha256="6f7496cf14a3a8903474552d5271c79c71916519edb42554f23f42a8563498a9", url="https://pypi.org/packages/43/73/ee90189836c095a664c03c13ef7a5d87e35c9cd5945346eba6394e288986/twine-4.0.0-py3-none-any.whl")
    version("3.8.0", sha256="d0550fca9dc19f3d5e8eadfce0c227294df0a2a951251a4385797c8a6198b7c8", url="https://pypi.org/packages/5e/74/ea7dfb86223695fd8efa256a24d1520729dde79a4e628ee6879f0f136d40/twine-3.8.0-py3-none-any.whl")
    version("3.7.1", sha256="8c120845fc05270f9ee3e9d7ebbed29ea840e41f48cd059e04733f7e1d401345", url="https://pypi.org/packages/24/aa/636b8eb9637944d2d94b766997d0420d1911abfd6392a6e3e2a75347949a/twine-3.7.1-py3-none-any.whl")
    version("3.7.0", sha256="5a3e3fb52b926827c99e050f0c1e5d8ae599848f3eb27764f19b886c09134590", url="https://pypi.org/packages/08/b9/cd146d64842da5a7e2841d4270f7ae7aed803e896ace221a9a94615799d8/twine-3.7.0-py3-none-any.whl")
    version("3.6.0", sha256="916070f8ecbd1985ebed5dbb02b9bda9a092882a96d7069d542d4fc0bb5c673c", url="https://pypi.org/packages/a7/a5/3722f04d44bc47fd2850a2b5720f21ce808c965908a79235f32e2b3646c9/twine-3.6.0-py3-none-any.whl")
    version("3.5.0", sha256="3725b79a6f1cfe84a134544ae1894706e60719ab28547cb6c6de781b9f72706d", url="https://pypi.org/packages/3d/a5/a42d1fca138f96a4f36efc91277d87930e9c805eb8498c2beda7db475efe/twine-3.5.0-py3-none-any.whl")
    version("3.4.2", sha256="087328e9bb405e7ce18527a2dca4042a84c7918658f951110b38bc135acab218", url="https://pypi.org/packages/1d/f7/27bff231e6339189ca72bc9e08336995d86f7b0f36e44a2615823905f743/twine-3.4.2-py3-none-any.whl")
    version("2.0.0", sha256="5319dd3e02ac73fcddcd94f035b9631589ab5d23e1f4699d57365199d85261e1", url="https://pypi.org/packages/c4/43/b9c56d378f5d0b9bee7be564b5c5fb65c65e5da6e82a97b6f50c2769249a/twine-2.0.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-colorama@0.4.3:", when="@3.2:3")
        depends_on("py-importlib-metadata@3.6:", when="@3.4:")
        depends_on("py-keyring@15.1:", when="@3:")
        depends_on("py-pkginfo@1.8.1:", when="@3.7:")
        depends_on("py-pkginfo@1.4.2:", when="@1.11:3.6")
        depends_on("py-readme-renderer@35:", when="@4.0.1:")
        depends_on("py-readme-renderer@21:", when="@1.12:4.0.0")
        depends_on("py-requests@2.20:", when="@2:")
        depends_on("py-requests-toolbelt@0.8,0.9.1:", when="@1.13:")
        depends_on("py-rfc3986@1.4:", when="@3.2:")
        depends_on("py-rich@12.0.0:", when="@4:")
        depends_on("py-setuptools@0.7:", when="@1.6:3.3")
        depends_on("py-tqdm@4.14:", when="@1.10:3")
        depends_on("py-urllib3@1.26:", when="@3.8:")
    # END DEPENDENCIES

