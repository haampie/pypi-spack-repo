# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPydap(PythonPackage):
    # BEGIN VERSIONS
    version("3.4.1", sha256="a24cc3bc8c78089542699382bf650d57a055c82bb72c342fa7caa6618b9e4417", url="https://pypi.org/packages/37/e1/176f49111e96267d5b24107f03a9a84eaee1d2fe5922c489c6ba54bbcc51/pydap-3.4.1-py3-none-any.whl")
    version("3.4.0", sha256="0c2f2e674eed88286cee899d7512b601d6d8abb5118bb42263d2007bf5fa1c08", url="https://pypi.org/packages/3c/0f/1731635fa2d6f2ce319df536b6397f86da3246238feea34535fd66416ee2/pydap-3.4.0-py3-none-any.whl")
    version("3.2.2", sha256="9655711d8da71192bda78fed15cbf4fc7fb1decc661ea5022263c0143648cf63", url="https://pypi.org/packages/9e/ad/01367f79b24015e223dd7679e4c9b16a6792fe5a9772e45e5f81b2c4a021/Pydap-3.2.2-py3-none-any.whl")
    version("3.2.1", sha256="d2bba644ba5bac5e6570d0a42db4b908440d2d8ccaf6ffae1ae459c4c8a3244b", url="https://pypi.org/packages/64/14/5fb9e6ac4635aff2ffa2b879621c763d823de4de597db34f3646d5abb363/Pydap-3.2.1.tar.gz")
    version("3.2.0", sha256="86dca669f84eecba6ff67af7fa3332af24a0163a72991d02452f4ca1f4d3f99f", url="https://pypi.org/packages/c1/1d/727262a03998c7ea406d15301513d67f0815c95dac4cfbd5418d92911667/Pydap-3.2.0.tar.gz")
    version("3.1.1", sha256="31af591d244f3a9d379a0f0217524382d473fd24d2ef1173272f24f3a0df3511", url="https://pypi.org/packages/cd/da/577a2b6721e9b103f1671bd020f5553e582f2c509fe5cade636822b35351/Pydap-3.1.1.tar.gz")
    version("3.1", sha256="0e37ebb7755134689d34c7221a140b0b7fb8a76b213e3975e85fec3fe0c2d5f1", url="https://pypi.org/packages/7e/b9/71b3ffac9db66f337ead4b725a5b2d18af57ced48516c87d13601066a09b/Pydap-3.1.tar.gz")
    version("3.0.3", sha256="0a066ee92882b6b31fc255f73d4e5944d66a1a8c83950be02e824f068e68ff6b", url="https://pypi.org/packages/8d/e7/0fafb5f920640384eea9dbe1ea5dc8302f110f9522683f8cce7ba17193f8/Pydap-3.0.3.tar.gz")
    version("3.0.2", sha256="845dcfbc7ea68f9d9f867223fc540369c815d588657397fd83fe7adcd69ff32a", url="https://pypi.org/packages/a1/b0/5e2bbd5cb11d3c133bb9a170b0189766e2bd4d93f2a1eb820862b91f861b/Pydap-3.0.2.tar.gz")
    version("3.0.1", sha256="9a8398185a423a99392a423d1bf63a49c31e5fb24c9c365c566fc8257d2c12c6", url="https://pypi.org/packages/9b/ad/000ac383b505e81f7ce292afba1db785fb2375bf4b90b005483db7df812c/Pydap-3.0.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-beautifulsoup4", when="@3.2.2:")
        depends_on("py-docopt", when="@3.2.2:")
        depends_on("py-jinja2", when="@3.2.2:")
        depends_on("py-numpy", when="@3.2.2:")
        depends_on("py-requests", when="@3.4:")
        depends_on("py-six@1.4:", when="@3.2.2:")
        depends_on("py-webob", when="@3.2.2:")
    # END DEPENDENCIES

