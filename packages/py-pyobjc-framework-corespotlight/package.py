# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCorespotlight(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="bc4ac490953db29f6a58bc6fca6f819f8a810d0bb15d5f067451b3a8cad1cb50", url="https://pypi.org/packages/8d/94/867b96e673a466f43ad4d9e9ec3b10f904e5d5689e59b0c9b5ee3c45f609/pyobjc-framework-CoreSpotlight-10.2.tar.gz")
    version("10.1", sha256="b50e13d55d90b88800c2cc2955c000ea6b1de6481ff6e0092c7b7bf94fceea69", url="https://pypi.org/packages/3a/56/1467e214c9f7b17160215d85b0208e3d2fbadff04762da1a945ad7ca1265/pyobjc-framework-CoreSpotlight-10.1.tar.gz")
    version("10.0", sha256="393767c63f2513ab4056c688aecdaf1ae67357f8d99fa963d765cfbdc9ccba47", url="https://pypi.org/packages/48/ef/21e68d69cb7d5f7a601c26189e8d0aaaedb8e965337df4954edd2565b8b6/pyobjc-framework-CoreSpotlight-10.0.tar.gz")
    version("9.2", sha256="eb369dc792fd61dadd7322cf146750252a08a1961742169e0d9a10c303fc9c06", url="https://pypi.org/packages/b8/fe/70ab30eabbc22baaa49e3f34f3a03d6b280454a812305a9f292a0b7525c4/pyobjc-framework-CoreSpotlight-9.2.tar.gz")
    version("9.1.1", sha256="2b51eaef0429e5879fa74d7476d9ea727b31ea636a4b15f171e9af2768a04868", url="https://pypi.org/packages/b2/21/d790f4554fe7a776dfbb88bf1b71372642fea23879c5ab616076f1587c5f/pyobjc-framework-CoreSpotlight-9.1.1.tar.gz")
    version("9.1", sha256="b30437607a62fda367d898302a7c53ba15f8000f881bd37ff3ebcf00793351f7", url="https://pypi.org/packages/82/06/4f2bc885234e0078f11d34fc79654d345c34f0f2f79fc5d473aaf0c4c497/pyobjc-framework-CoreSpotlight-9.1.tar.gz")
    version("9.0.1", sha256="c436faf70d29f0eabb22b0c3f96189bc1168dc8ab6f1872b0618e3c7accbcfeb", url="https://pypi.org/packages/3d/01/70340bdd55a34b6bbf6edae1969c76cfb2d0edc279640270f3d908f6ae58/pyobjc-framework-CoreSpotlight-9.0.1.tar.gz")
    version("9.0", sha256="af30d4cecd4e5ff5852e15ed19e4f0c85f4c73471f57888b91dae7d5205e9d17", url="https://pypi.org/packages/59/94/6a8da57cf5a1b1776d833e0ef515377b487861427a67c9bdde2e7cb05607/pyobjc-framework-CoreSpotlight-9.0.tar.gz")
    version("8.5.1", sha256="698d79f2a2aec3082e441c6e746225eaf72560ad7b501619ee9ea38a1ffd9e29", url="https://pypi.org/packages/63/04/6804248156353029ea8f3cc62dcec08dec5d4b17bb09c3253042cf0f9460/pyobjc-framework-CoreSpotlight-8.5.1.tar.gz")
    version("8.5", sha256="ab90c64c38d8c3c6945c6db4ffd93333854a992fcca4ac5d9ece98ad575a9254", url="https://pypi.org/packages/03/0d/1184fc143ea975b527c66ff2befbe840f769af8acd041ecbba949bff860d/pyobjc-framework-CoreSpotlight-8.5.tar.gz")
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

