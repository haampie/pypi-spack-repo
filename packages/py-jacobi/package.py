# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJacobi(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.9.2", sha256="7e57b2d9c62d47bce688ef4b3564adeb1def611cf5ed232ec39a6aa6083f7a8c", url="https://pypi.org/packages/b0/5c/2d6a44da539db44820b1c053958bfc4ee011e33f4f110175bfc712520440/jacobi-0.9.2-py3-none-any.whl")
    version("0.9.1", sha256="cfc2957b898a275201f010bd95d38698684ebfb5e89572552b527c2dd10ac99c", url="https://pypi.org/packages/0f/1d/13af5cb059e5143c8c4bee83cde39300847ab43c0f61191eb69291d3d351/jacobi-0.9.1-py3-none-any.whl")
    version("0.8.1", sha256="39ee015e8d163e6049a11c6cf3d789710c78818837fe9d24cf92797fbefbb891", url="https://pypi.org/packages/d9/e6/58c03059503dbc97e83eb7558662a9c0da6b4b661b6703529a7e27bd6857/jacobi-0.8.1-py3-none-any.whl")
    version("0.8.0", sha256="9fe822c2dc8de77d7107b58ca0682223b88f6cc1a2d034d17bd073dc2084cee8", url="https://pypi.org/packages/b2/60/df0848d1f774da7f22b5dbd15eddbe253b6f41bacca7778eb2d8e59dc812/jacobi-0.8.0-py3-none-any.whl")
    version("0.7.0", sha256="369c02bd99c8e658cbcd1673a537f87ae9e54e750c77e3a1da4c3322a71fad5b", url="https://pypi.org/packages/28/25/bb17f18c2ce2d5089a8d757e53eeb0c9d685f3197994b67fdb993bbb66b5/jacobi-0.7.0-py3-none-any.whl")
    version("0.6.0", sha256="464ca0f66e7f66f2d42d1af8b848b19aff82ebd56029a8b12475e01daf6eab48", url="https://pypi.org/packages/36/03/c48d148418a4013d005e2c8b36337a6457736ac693108813604aebe86c9a/jacobi-0.6.0-py3-none-any.whl")
    version("0.5.0", sha256="ac10ed23a8e1f820a7d662c940cd2ef58a682dd719094e64960da3e963d50245", url="https://pypi.org/packages/95/a0/92452e4767611e84b5c068ff48baf59c1db58263105b7635e9e0003578bf/jacobi-0.5.0-py3-none-any.whl")
    version("0.4.2", sha256="efe514d621b1974da67c6b3a050ca12b44c15ab71f0e4b8d9b57034fb50ca318", url="https://pypi.org/packages/77/8a/3dd5a3bdf5eb5ef7fd430fd805823421a9892b1993eddf9280b8f835e8c9/jacobi-0.4.2-py3-none-any.whl")
    version("0.4.0", sha256="c6e4c58fb058303d8079d7b58f0649c151734b0ca56d4e7791442aed48ecd1aa", url="https://pypi.org/packages/e8/80/a88385f1f7f5cd63a081d58e83d50822b602e67cd12db4c8fc7728c35d56/jacobi-0.4.0-py3-none-any.whl")
    version("0.3.0", sha256="0533f58343c5639adc1b0c7da1325cb44a45a961d9c7ead6528ae435404f773e", url="https://pypi.org/packages/7a/fa/85febc70890181fc1fa402b2964ef17533c33abc399fb6862143d7efaee6/jacobi-0.3.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@0.9.2:")
        depends_on("py-numpy@1.10:", when="@0.1:0.9.1")
    # END DEPENDENCIES

