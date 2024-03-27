##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCffi(PythonPackage):
    version("1.16.0", sha256="bcb3ef43e58665bbda2fb198698fcae6776483e0c4a631aa5647806c25e02cc0", url="https://pypi.org/packages/68/ce/95b0bae7968c65473e1298efb042e10cafc7bafc14d9e4f154008241c91d/cffi-1.16.0.tar.gz")
    version("1.15.1", sha256="d400bfb9a37b1351253cb402671cea7e89bdecc294e8016a707f6d1d8ac934f9", url="https://pypi.org/packages/2b/a8/050ab4f0c3d4c1b8aaa805f70e26e84d0e27004907c5b8ecc1d31815f92a/cffi-1.15.1.tar.gz")
    version("1.15.0", sha256="920f0d66a896c2d99f0adbb391f990a84091179542c205fa53ce5787aff87954", url="https://pypi.org/packages/00/9e/92de7e1217ccc3d5f352ba21e52398372525765b2e0c4530e6eb2ba9282a/cffi-1.15.0.tar.gz")
    version("1.14.6", sha256="c9a875ce9d7fe32887784274dd533c57909b7b1dcadcc128a2ac21331a9765dd", url="https://pypi.org/packages/2e/92/87bb61538d7e60da8a7ec247dc048f7671afe17016cd0008b3b710012804/cffi-1.14.6.tar.gz")
    version("1.14.5", sha256="fd78e5fee591709f32ef6edb9a015b4aa1a5022598e36227500c8f4e02328d9c", url="https://pypi.org/packages/a8/20/025f59f929bbcaa579704f443a438135918484fffaacfaddba776b374563/cffi-1.14.5.tar.gz")
    version("1.14.4", sha256="1a465cbe98a7fd391d47dce4b8f7e5b921e6cd805ef421d04f5f66ba8f06086c", url="https://pypi.org/packages/66/6a/98e023b3d11537a5521902ac6b50db470c826c682be6a8c661549cb7717a/cffi-1.14.4.tar.gz")
    version("1.14.3", sha256="f92f789e4f9241cd262ad7a555ca2c648a98178a953af117ef7fad46aa1d5591", url="https://pypi.org/packages/cb/ae/380e33d621ae301770358eb11a896a34c34f30db188847a561e8e39ee866/cffi-1.14.3.tar.gz")
    version("1.14.2", sha256="ae8f34d50af2c2154035984b8b5fc5d9ed63f32fe615646ab435b05b132ca91b", url="https://pypi.org/packages/f7/09/88bbe20b76ca76be052c366fe77aa5e3cd6e5f932766e5597fecdd95b2a8/cffi-1.14.2.tar.gz")
    version("1.14.1", sha256="b2a2b0d276a136146e012154baefaea2758ef1f56ae9f4e01c612b0831e0bd2f", url="https://pypi.org/packages/54/1d/15eae71ab444bd88a1d69f19592dcf32b9e3166ecf427dd9243ef0d3b7bc/cffi-1.14.1.tar.gz")
    version("1.14.0", sha256="2d384f4a127a15ba701207f7639d94106693b6cd64173d6c8988e2c25f3ac2b6", url="https://pypi.org/packages/05/54/3324b0c46340c31b909fcec598696aaec7ddc8c18a63f2db352562d3354c/cffi-1.14.0.tar.gz")
    version("1.13.0", sha256="8fe230f612c18af1df6f348d02d682fe2c28ca0a6c3856c99599cdacae7cf226", url="https://pypi.org/packages/d6/cf/ba7e2df852a2fc807d48b3f7bea46f741830be4f047a0712e6de3e95fb6a/cffi-1.13.0.tar.gz")
    version("1.12.2", sha256="e113878a446c6228669144ae8a56e268c91b7f1fafae927adc4879d9849e0ea7", url="https://pypi.org/packages/64/7c/27367b38e6cc3e1f49f193deb761fe75cda9f95da37b67b422e62281fcac/cffi-1.12.2.tar.gz")
    version("1.11.5", sha256="e90f17980e6ab0f3c2f3730e56d1fe9bcba1891eeea58966e89d352492cc74f4", url="https://pypi.org/packages/e7/a7/4cd50e57cc6f436f1cc3a7e8fa700ff9b8b4d471620629074913e3735fb2/cffi-1.11.5.tar.gz")
    version("1.10.0", sha256="b3b02911eb1f6ada203b0763ba924234629b51586f72a21faacc638269f4ced5", url="https://pypi.org/packages/5b/b9/790f8eafcdab455bcd3bd908161f802c9ce5adbf702a83aa7712fcc345b7/cffi-1.10.0.tar.gz")
    version("1.1.2", sha256="390970b602708c91ddc73953bb6929e56291c18a4d80f360afa00fad8b6f3339", url="https://pypi.org/packages/a0/f2/b9ea4dd14dd586b8cc5c70f8b505cee7e03851e514ceb00f7406a498a6a2/cffi-1.1.2.tar.gz")

    with default_args(type="run"):
        depends_on("py-pycparser", when="@1.13.1,1.16:")

