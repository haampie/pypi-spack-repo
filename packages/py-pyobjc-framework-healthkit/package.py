##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkHealthkit(PythonPackage):
    version("10.2", sha256="abcc4e6bd0e11eace7257887958b6cc5332f8aad4efa6b94e930425016540789", url="https://pypi.org/packages/03/46/b3e68efd4912aca0b99944c0f75d1c6f0d2b2ef6573d84cd165dd3a54007/pyobjc-framework-HealthKit-10.2.tar.gz")
    version("10.1", sha256="9479c467514c506f9083889f11da6b8f34d705f716ffe9cbbb5a3157000d24de", url="https://pypi.org/packages/87/36/dda66c692ce007f72b67781066a7a87767486b1350e503485d8dfcbb10cd/pyobjc-framework-HealthKit-10.1.tar.gz")
    version("10.0", sha256="0abe3e003927998728db217d2a023f59d9e8f52072e81cc01469888731b7ebf5", url="https://pypi.org/packages/22/f1/ba2b8aabd0e2db641c16f8f04795728c2b7e606569191fd047a4c430b6dd/pyobjc-framework-HealthKit-10.0.tar.gz")
    version("9.2", sha256="69ad4ce21bce790e2aa16571cd59ba429f3c40dfb40d6eaef77ec9d7797524ac", url="https://pypi.org/packages/75/ea/ef58633e833774a9853ae1e28fff1a4f3eea8e8cbd305feb22938e14942c/pyobjc-framework-HealthKit-9.2.tar.gz")
    version("9.1.1", sha256="fca40953777512837cd03fab07cdfbaf048bdd51d29b8cc3bab1e26c0ec64158", url="https://pypi.org/packages/a5/be/3aebe9c1d596621dc217a56569c8f6213efdd73f20f2c33472ab839b168c/pyobjc-framework-HealthKit-9.1.1.tar.gz")
    version("9.1", sha256="d8a269e067bb9ef80c56fd9c86eba352a64d621f34a707b98f4cc61da1941ef1", url="https://pypi.org/packages/36/8c/d2e7daa9b030db3f21eb3ea6e69e52fd34c246454127dc75434276f55c15/pyobjc-framework-HealthKit-9.1.tar.gz")
    version("9.0.1", sha256="b8cc849bbdfff195472775be6872ee630e764fa34a362b8ee1ddfe78c4201099", url="https://pypi.org/packages/8d/ca/a3c8949da967e3eab5550d003aab60e63fbf5d380276a33ff73f4c2b5690/pyobjc-framework-HealthKit-9.0.1.tar.gz")
    version("9.0", sha256="11e92fdb00a40617febea3bacd8c8f4e2b2dee7b7a010f0618b98525d41e2c27", url="https://pypi.org/packages/80/63/6cb06ad13360a3f3834849b8b25901527576d88502f7622da382fd9693e0/pyobjc-framework-HealthKit-9.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")

