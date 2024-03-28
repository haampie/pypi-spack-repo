# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyEcos(PythonPackage):
    # BEGIN VERSIONS
    version("2.0.13", sha256="f2a9dc108ade7faf6f6f4fad245f4714b7293c8767d2a351ead59428a94a98b9", url="https://pypi.org/packages/4d/26/1494d3da76c1ebecdcb1f3028c77b50a272f07e9d34b8eca981a7b3f6267/ecos-2.0.13.tar.gz")
    version("2.0.12", sha256="f48816d73b87ae325556ea537b7c8743187311403c80e3832035224156337c4e", url="https://pypi.org/packages/04/da/aefd27c06a9179a7e5614d0d97c0384072d2d22800790690c661eb6f2f4a/ecos-2.0.12.tar.gz")
    version("2.0.11", sha256="97d8944cac7e88b6ebd7ebfc04eedf922f6641ea7ecadd2764fb7be4043f9056", url="https://pypi.org/packages/84/2a/1480b85692f349fd669655e020a1aafdd2b798eab69305d394989f1d2b64/ecos-2.0.11.tar.gz")
    version("2.0.10", sha256="9391a73fd25b2fc56b163a2a70c78973458bb194fe475b6c27672c0d980a47cf", url="https://pypi.org/packages/08/0c/a9195eb04d6b58572a4379d98661d138066da97fb8dbbdc4e104452e8377/ecos-2.0.10.tar.gz")
    version("2.0.9", sha256="87562479f4e3008ef83361f4581138b5c3ed13a4e4d39e8bc3db45ebc3b470f5", url="https://pypi.org/packages/6d/57/4e4a48d79747a837b148c1d32b7487407eeaa64a8996df59c84cdc0026ce/ecos-2.0.9.tar.gz")
    version("2.0.8", sha256="0b8e3f6468c15d62967bfa4f9ef5bbd62fd0b455d547eacc0afc15aceb65197b", url="https://pypi.org/packages/35/5c/6fda325368b9ff4d4dd971667e3bc5085cad9724ca852ae3f3062e45adf9/ecos-2.0.8.tar.gz")
    version("2.0.7.post1", sha256="83e90f42b3f32e2a93f255c3cfad2da78dbd859119e93844c45d2fca20bdc758", url="https://pypi.org/packages/b9/3a/59aa93b573a22fda44402383aeddcc2a081c31e61080af3da9d11855c77a/ecos-2.0.7.post1.tar.gz")
    version("2.0.5", sha256="5dbe53db1cad43f08ba91e98918314c2fc149a481a44af19133c60e436dc2eeb", url="https://pypi.org/packages/b6/b4/988b15513b13e8ea2eac65e97d84221ac515a735a93f046e2a2a3d7863fc/ecos-2.0.5.tar.gz")
    version("2.0.4", sha256="1733e2e5f0fe12389acfaab9aff613d0405855c7aa802c1ca624652168255187", url="https://pypi.org/packages/77/09/a310016980c7652e6470d5bf4938d792b5c99528b16d5c20ca5e3e377bf0/ecos-2.0.4.tar.gz")
    version("2.0.3", sha256="525b6149d6a1dff336508427c0d661a0e61a641aa9b9f99033fe8f330499ea08", url="https://pypi.org/packages/c3/98/78dbaa94e80e2ff69a02b232e38e5563a3f18aa54edc0b333c2cbe76a763/ecos-2.0.3.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.6:", when="@1.1:2.0.4,2.0.7.post:2.0.7")
        depends_on("py-scipy@0.9:", when="@1.1:2.0.4,2.0.7.post:2.0.7")
    # END DEPENDENCIES

