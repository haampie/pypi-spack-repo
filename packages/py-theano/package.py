# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTheano(PythonPackage):
    # BEGIN VERSIONS
    version("1.0.5", sha256="6e9439dd53ba995fcae27bf20626074bfc2fff446899dc5c53cb28c1f9202e89", url="https://pypi.org/packages/6b/97/bcd5654ba60f35f180931afabbd3b4c46c0379852f961c7a2819ff897f5d/Theano-1.0.5.tar.gz")
    version("1.0.4", sha256="35c9bbef56b61ffa299265a42a4e8f8cb5a07b2997dabaef0f8830b397086913", url="https://pypi.org/packages/7d/c4/6341148ad458b6cd8361b774d7ee6895c38eab88f05331f22304c484ed5d/Theano-1.0.4.tar.gz")
    version("1.0.3", sha256="637f3b34d40ef5e0d54dd4c40618475aaa085c26d2491e925c98e2ad4bc2115a", url="https://pypi.org/packages/4d/b1/d490d88ab47f01f367f413bd2e47d86acf92c84157c5172c23903798bd70/Theano-1.0.3.tar.gz")
    version("1.0.2", sha256="6768e003d328a17011e6fca9126fbb8a6ffd3bb13cb21c450f3e724cca29abde", url="https://pypi.org/packages/99/dd/e43e3da5dd52f1468def552ed3e752bfd6958369478cc906ff07b21af92e/Theano-1.0.2.tar.gz")
    version("1.0.1", sha256="88d8aba1fe2b6b75eacf455d01bc7e31e838c5a0fb8c13dde2d9472495ff4662", url="https://pypi.org/packages/62/da/ab486aae8e538d8ae91fa0e6ab26d3a454d7c5c7a66541f40300e58a3314/Theano-1.0.1.tar.gz")
    version("0.8.2", sha256="7463c8f7ed1a787bf881f36d38a38607150186697e7ce7e78bfb94b7c6af8930", url="https://pypi.org/packages/30/3d/2354fac96ca9594b755ec22d91133522a7db0caa0877165a522337d0ed73/Theano-0.8.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("cuda", default=False)
    variant("cuda_arch", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

