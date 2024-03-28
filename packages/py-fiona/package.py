# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFiona(PythonPackage):
    # BEGIN VERSIONS
    version("1.9.6", sha256="791b3494f8b218c06ea56f892bd6ba893dfa23525347761d066fb7738acda3b1", url="https://pypi.org/packages/92/2c/2ab81e38aad8cf4f4e2a7b1c0488750ffc512c108fb244a8b4dd4f196cd3/fiona-1.9.6.tar.gz")
    version("1.9.5", sha256="99e2604332caa7692855c2ae6ed91e1fffdf9b59449aa8032dd18e070e59a2f7", url="https://pypi.org/packages/83/a0/6b870864ceebcd046d2e952b0d18932812ff7a48d3b05670af3f702d9c01/fiona-1.9.5.tar.gz")
    version("1.9.4", sha256="49f18cbcd3b1f97128c1bb038c3451b2e1be25baa52f02ce906c25cf75af95b6", url="https://pypi.org/packages/53/b6/84916103fe50d6876810687671d2b8814edd50250d117cf2f222679d899b/Fiona-1.9.4.tar.gz")
    version("1.9.3", sha256="60f3789ad9633c3a26acf7cbe39e82e3c7a12562c59af1d599fc3e4e8f7f8f25", url="https://pypi.org/packages/c2/e1/d854d283e8962f3d1b717983ab3dfe99f7447116e9475f1c4a3342095136/Fiona-1.9.3.tar.gz")
    version("1.9.2", sha256="f9263c5f97206bf2eb2c010d52e8ffc54e96886b0e698badde25ff109b32952a", url="https://pypi.org/packages/f1/57/61443cf8b58022cb117c26d8a25c8a1435b24de9dac5d7f848b94a2c584a/Fiona-1.9.2.tar.gz")
    version("1.9.1", sha256="3a3725e94840a387fef48726d60db6a6791563f366939d22378a4661f8941be7", url="https://pypi.org/packages/62/c4/05f25e319e1bffacaf521bf366c31b01acda7d1acf251d3e4f1f0d0270d3/Fiona-1.9.1.tar.gz")
    version("1.9.0", sha256="6e487cbfba5a849fbdf06e45169fd7e1f1662f44f3d717ab4b946046b2457eae", url="https://pypi.org/packages/2f/28/5ec9014f188f6f9ff8fff48f8df00ddf197a9f1cc6bf7629a3c052bf5080/Fiona-1.9.0.tar.gz")
    version("1.8.22", sha256="a82a99ce9b3e7825740157c45c9fb2259d4e92f0a886aaac25f0db40ffe1eea3", url="https://pypi.org/packages/b9/d7/48025179fbbb2e1bab698131246878df36fa9aa5bee0ba1c062cd8f2ef44/Fiona-1.8.22.tar.gz")
    version("1.8.21", sha256="3a0edca2a7a070db405d71187214a43d2333a57b4097544a3fcc282066a58bfc", url="https://pypi.org/packages/67/5c/4e028e84a1f0cb3f8a994217cf2366360ca984dfc1433f6171de527d0dca/Fiona-1.8.21.tar.gz")
    version("1.8.20", sha256="a70502d2857b82f749c09cb0dea3726787747933a2a1599b5ab787d74e3c143b", url="https://pypi.org/packages/ec/f7/093890341a7e8fbfcdfa04caf4dfb588ebab32c13ceaa6a3819da79ea106/Fiona-1.8.20.tar.gz")
    version("1.8.18", sha256="b732ece0ff8886a29c439723a3e1fc382718804bb057519d537a81308854967a", url="https://pypi.org/packages/9f/e8/401cdaa58d862a25c4b3365acf7d2bd7ac77191e3dc9acdcdac0eff20ff0/Fiona-1.8.18.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.10-alpha1:")
        depends_on("py-attrs@19.2:", when="@1.9.5:")
        depends_on("py-certifi", when="@1.9.5:")
        depends_on("py-click@8.0.0:", when="@1.9.5:")
        depends_on("py-click-plugins", when="@1.8-beta1:1.8.13,1.9.5:")
        depends_on("py-cligj@0.5:", when="@1.8-alpha3:1.8.13,1.9.5:")
        depends_on("py-importlib-metadata", when="@1.9.5: ^python@:3.9")
        depends_on("py-setuptools", when="@1.9.5")
        depends_on("py-six", when="@1.5:1.7.2,1.7.4:1.7.11.post1,1.8-alpha1,1.9.5:1.9")
    # END DEPENDENCIES

