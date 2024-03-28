# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyQuerystringParser(PythonPackage):
    # BEGIN VERSIONS
    version("1.2.4", sha256="d2fa90765eaf0de96c8b087872991a10238e89ba015ae59fedfed6bd61c242a0", url="https://pypi.org/packages/88/6b/572b2590fd55114118bf08bde63c0a421dcc82d593700f3e2ad89908a8a9/querystring_parser-1.2.4-py2.py3-none-any.whl")
    version("1.2.3", sha256="4c31b547c77b927a8aceccd6fa37f8152aa92fe5654a43d7363fcee8cf6d8aea", url="https://pypi.org/packages/57/64/3086a9a991ff3aca7b769f5b0b51ff8445a06337ae2c58f215bcee48f527/querystring_parser-1.2.3.tar.gz")
    version("1.2.2", sha256="eacf69c5f327269d527fa99050efbacb39197b13054975e59d83306543952e84", url="https://pypi.org/packages/1c/d1/c219f89c17bf7c9ab2456e07357d5a8d84b017af1f88b60ab9712b125d41/querystring_parser-1.2.2.tar.gz")
    version("1.2.1", sha256="a003150824656c7ac315071eab17e67c7c8f7b6edcefd23ba81dcd28577be4e7", url="https://pypi.org/packages/5d/5b/49d906b20a6c1f89311fc68a37c00c88ea38b8a538cbfc97f2fffe02f519/querystring_parser-1.2.1.tar.gz")
    version("1.2.0", sha256="722d60d0be7872f83fd7484f0aba854ad5ae2239b0be2794ecc6d85ddd8bea99", url="https://pypi.org/packages/3b/76/99c792dfd19ba803a4c0c68ec8dbde6d408be2250a50f20eac0b1c8d0c36/querystring_parser-1.2.0.tar.gz")
    version("1.1", sha256="aa2e97d9124319fca22e224ffe706b1cea90eb3de8331a987a36f66c5ab4afee", url="https://pypi.org/packages/1f/7c/8eda7f170d0ac68489ff2dbca44999725c8950daa6e73e5846c0069c32bd/querystring_parser-1.1.tar.gz")
    version("1.0", sha256="ba081dd8db740ae5444360d1a4fd9fb04f7d3d2fdab8c41069d08fbd6f23f8e7", url="https://pypi.org/packages/df/65/80b432031378b37e2f854a1473c520d83471d16cf838e83cca8f6eef5d15/querystring_parser-1.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six", when="@1.2.4:")
    # END DEPENDENCIES

