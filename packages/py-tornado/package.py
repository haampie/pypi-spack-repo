# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTornado(PythonPackage):
    # BEGIN VERSIONS
    version("6.4", sha256="72291fa6e6bc84e626589f1c29d90a5a6d593ef5ae68052ee2ef000dfd273dee", url="https://pypi.org/packages/bd/a2/ea124343e3b8dd7712561fe56c4f92eda26865f5e1040b289203729186f2/tornado-6.4.tar.gz")
    version("6.4-beta1", sha256="40954904d2c9d3a2c0b76e27b854247995e3f320ba4d535be84d765c34187fd2", url="https://pypi.org/packages/3b/94/1bd544570c0ebaaebfd2640cf217336a651b41be307294b54ad531b3cbf7/tornado-6.4b1.tar.gz")
    version("6.3.3", sha256="e7d8db41c0181c80d76c982aacc442c0783a2c54d6400fe028954201a2e032fe", url="https://pypi.org/packages/48/64/679260ca0c3742e2236c693dc6c34fb8b153c14c21d2aa2077c5a01924d6/tornado-6.3.3.tar.gz")
    version("6.3.2", sha256="4b927c4f19b71e627b13f3db2324e4ae660527143f9e1f2e2fb404f3a187e2ba", url="https://pypi.org/packages/30/f0/6e5d85d422a26fd696a1f2613ab8119495c1ebb8f49e29f428d15daf79cc/tornado-6.3.2.tar.gz")
    version("6.3.1", sha256="5e2f49ad371595957c50e42dd7e5c14d64a6843a3cf27352b69c706d1b5918af", url="https://pypi.org/packages/1c/1d/89cb7050dbd009db3cb69ca74c1f0a3f5c36405f887c2d2371d9ebfe0cd5/tornado-6.3.1.tar.gz")
    version("6.3", sha256="d68f3192936ff2c4add04dc21a436a43b4408d466746b78bb2b9d0a53a18683f", url="https://pypi.org/packages/15/e6/88afe8318b6aaff1e6c60b3d4b94c9b68708cc0a5ba2f6dae5cbc288ce69/tornado-6.3.tar.gz")
    version("6.3-beta1", sha256="de62a482ebe12d3c6b8c55fa6fa655ccd73bceab342ea597da779ca3b5e62ddf", url="https://pypi.org/packages/41/2c/ebb4c417eb82d1d9b9666875d051a9fce6ff1e0fe5d3e93019b94c61d29d/tornado-6.3b1.tar.gz")
    version("6.2", sha256="9b630419bde84ec666bfd7ea0a4cb2a8a651c2d5cccdbdd1972a0c859dfc3c13", url="https://pypi.org/packages/f3/9e/225a41452f2d9418d89be5e32cf824c84fe1e639d350d6e8d49db5b7f73a/tornado-6.2.tar.gz")
    version("6.2-beta2", sha256="a48eb59baa3ef83dd7e69c6692488cb81ff8f7b67749f732850065ef3924fd96", url="https://pypi.org/packages/62/94/bc31a73a9c09815e2b5d9dbe391ab01f0d14b3d39449ec09cfecda5ee630/tornado-6.2b2.tar.gz")
    version("6.1", sha256="33c6e81d7bd55b468d2e793517c909b139960b6c790a60b7991b9b6b76fb9791", url="https://pypi.org/packages/cf/44/cc9590db23758ee7906d40cacff06c02a21c2a6166602e095a56cbf2f6f6/tornado-6.1.tar.gz")
    version("6.1-beta2", sha256="803b3498a0d80190991bde5c0369c66b363632ad9206b558fd009a0e077aea32", url="https://pypi.org/packages/d8/fb/bfab79be6ea40a8df5aba81381a9f8c4ae58e4a406aca85701f25a114839/tornado-6.1b2.tar.gz")
    version("6.1-beta1", sha256="58444df74c89f67aa04c52f8912c9a87548c52d1bdf08c0e6b9e728e3637ec07", url="https://pypi.org/packages/1b/51/2c4e177ea1d38422bdd08e624169aa0657a575ff51ef7a1edcd8cae8023f/tornado-6.1b1.tar.gz")
    version("6.0.4", sha256="0fe2d45ba43b00a41cd73f8be321a44936dc1aba233dee979f17a042b83eb6dc", url="https://pypi.org/packages/95/84/119a46d494f008969bf0c775cb2c6b3579d3c4cc1bb1b41a022aa93ee242/tornado-6.0.4.tar.gz")
    version("6.0.3", sha256="c845db36ba616912074c5b1ee897f8e0124df269468f25e4fe21fe72f6edd7a9", url="https://pypi.org/packages/30/78/2d2823598496127b21423baffaa186b668f73cd91887fcef78b6eade136b/tornado-6.0.3.tar.gz")
    version("6.0.2", sha256="457fcbee4df737d2defc181b9073758d73f54a6cfc1f280533ff48831b39f4a8", url="https://pypi.org/packages/03/3f/5f89d99fca3c0100c8cede4f53f660b126d39e0d6a1e943e95cc3ed386fb/tornado-6.0.2.tar.gz")
    version("5.1.1", sha256="4e5158d97583502a7e2739951553cbd88a72076f152b4b11b64b9a10c4c49409", url="https://pypi.org/packages/e6/78/6e7b5af12c12bdf38ca9bfe863fcaf53dc10430a312d0324e76c1e5ca426/tornado-5.1.1.tar.gz")
    version("4.4", sha256="3176545b6cb2966870db4def4f646da6ab7a0c19400576969c57279a7561ab02", url="https://pypi.org/packages/8b/01/e7b4bcee946b356060639582fa71946130b5fe5ab0d0557c4340275f2dff/tornado-4.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

