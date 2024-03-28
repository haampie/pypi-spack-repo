# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPygraphviz(PythonPackage):
    # BEGIN VERSIONS
    version("1.12", sha256="8b0b9207954012f3b670e53b8f8f448a28d12bdbbcf69249313bd8dbe680152f", url="https://pypi.org/packages/f0/2a/3a7e5f6ba25c0a8998ded9234127c88c5c867bd03cfc3a7b18ef00876599/pygraphviz-1.12.tar.gz")
    version("1.12-rc3", sha256="a27fa60ae58914f5ec0c99379837da8a6c9f1cc1d36ad3744ad82fc65f43b2ac", url="https://pypi.org/packages/6e/86/a5aafca6f9404bbf58d9c1b55c31edc372d66541ec5ca7cbd5c6453b3760/pygraphviz-1.12rc3.tar.gz")
    version("1.11", sha256="a97eb5ced266f45053ebb1f2c6c6d29091690503e3a5c14be7f908b37b06f2d4", url="https://pypi.org/packages/19/db/cc09516573e79a35ac73f437bdcf27893939923d1d06b439897ffc7f3217/pygraphviz-1.11.zip")
    version("1.11-rc1", sha256="833145341147d191299e238ca45e9b41030cf8507e565906a1ce0ae23cc974f7", url="https://pypi.org/packages/53/75/729b6fed1e4246e6b6caebb5d4ff918349f7536d3ccfc5c8b686672d356b/pygraphviz-1.11rc1.zip")
    version("1.10", sha256="457e093a888128903251a266a8cc16b4ba93f3f6334b3ebfed92c7471a74d867", url="https://pypi.org/packages/ee/7e/7366c082f959db7ee18a16fc38dc594158ede65ca789bef87751ed5130c7/pygraphviz-1.10.zip")
    version("1.10-rc1", sha256="d9caf92b075938139fa6873320be17359485cd015182117152bc1caca71e4df5", url="https://pypi.org/packages/a1/69/cd2ceb0923bc3b3a2ed14af45d7f450508e6519594d05a0a2ba3ead29fdc/pygraphviz-1.10rc1.zip")
    version("1.9", sha256="fa18f7c6cea28341a4e466ed0cf05682b0a68288afe8dd7c9426782f7c1ae01c", url="https://pypi.org/packages/c7/21/063c3ec261904f3c67b7d8bb0033e4e53bbdacb17e6d27097239d50fb7ca/pygraphviz-1.9.zip")
    version("1.8", sha256="eb2e25a2c647044e7b66b5a159be64daaef24b549fcf535c241369d6e6e09c45", url="https://pypi.org/packages/01/8f/1538b3f3ad0441577d366ba3a96f7ccbe71356818fc4a54b2e7119a7794a/pygraphviz-1.8.zip")
    version("1.8-rc1", sha256="8b9e365b7c0e267d2d7e23145e5e369cbecfda915b76850b507e3c35736b30f1", url="https://pypi.org/packages/bf/43/e0bda9c82f25207f49ab1106407f887c32e27d5e14b717227ae941a7f8e7/pygraphviz-1.8rc1.zip")
    version("1.7", sha256="a7bec6609f37cf1e64898c59f075afd659106cf9356c5f387cecaa2e0cdb2304", url="https://pypi.org/packages/3a/d6/2c56f09ee83dbebb62c40487e4c972135661b9984fec9b30b77fb497090c/pygraphviz-1.7.zip")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.10:", when="@1.12-rc3:")
    # END DEPENDENCIES

