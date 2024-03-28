# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGeopy(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.4.1", sha256="ae8b4bc5c1131820f4d75fce9d4aaaca0c85189b3aa5d64c3dcaf5e3b7b882a7", url="https://pypi.org/packages/e5/15/cf2a69ade4b194aa524ac75112d5caac37414b20a3a03e6865dfe0bd1539/geopy-2.4.1-py3-none-any.whl")
    version("2.4.0", sha256="d2639a46d0ce4c091e9688b750ba94348a14b898a1e55c68f4b4a07e7d1afa20", url="https://pypi.org/packages/e1/58/9289c6a03116025cdb61461d99b2493daa4967a80b13755463d71a0affeb/geopy-2.4.0-py3-none-any.whl")
    version("2.3.0", sha256="4a29a16d41d8e56ba8e07310802a1cbdf098eeb6069cc3d6d3068fc770629ffc", url="https://pypi.org/packages/e4/00/6313c0ffdd230164890f433019749189e0b884562bdc170e9c3a3454b3a6/geopy-2.3.0-py3-none-any.whl")
    version("2.2.0", sha256="8f1f949082b964385de61fcc3a667a6a9a6e242beb1ae8972449f164b2ba0e89", url="https://pypi.org/packages/e1/e1/45f25e3d3acf26782888f847de7c958a2807a039210fb1016cc3fb9555c4/geopy-2.2.0-py3-none-any.whl")
    version("2.1.0", sha256="4db8a2b79a2b3358a7d020ea195be639251a831a1b429c0d1b20c9f00c67c788", url="https://pypi.org/packages/0c/67/915668d0e286caa21a1da82a85ffe3d20528ec7212777b43ccd027d94023/geopy-2.1.0-py3-none-any.whl")
    version("2.0.0", sha256="fdc596bab67d9f4828f43bf9e97c4e0a1d1518b7c2357485cef0e1c3cf470220", url="https://pypi.org/packages/07/e1/9c72de674d5c2b8fcb0738a5ceeb5424941fefa080bfe4e240d0bacb5a38/geopy-2.0.0-py3-none-any.whl")
    version("1.23.0", sha256="5dee9af0d1ad7019d2483a5f519ba415eaebc4010f271651790876d911a542f2", url="https://pypi.org/packages/41/4e/a3eb6ac14a9c4344d6f5e66a9457d82cf124daf5c8176cec0a49677b0e03/geopy-1.23.0-py2.py3-none-any.whl")
    version("1.22.0", sha256="d0adba79a4c50a0e253d4a9d2d86aea4a3c1c2ec0889c5c61500ea914dafb9a5", url="https://pypi.org/packages/ab/97/25def417bf5db4cc6b89b47a56961b893d4ee4fec0c335f5b9476a8ff153/geopy-1.22.0-py2.py3-none-any.whl")
    version("1.21.0", sha256="5de6fed0ee982e43a8e4243410477567cfccac22f8530edffc422761adf4e612", url="https://pypi.org/packages/53/fc/3d1b47e8e82ea12c25203929efb1b964918a77067a874b2c7631e2ec35ec/geopy-1.21.0-py2.py3-none-any.whl")
    version("1.20.0", sha256="6239cbf4d8e8a10460c10cf2ae1949c9e9d011e9f25c4e49202734455cc5e884", url="https://pypi.org/packages/80/93/d384479da0ead712bdaf697a8399c13a9a89bd856ada5a27d462fb45e47b/geopy-1.20.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-geographiclib@1.52:", when="@2.3:")
        depends_on("py-geographiclib@1.49:1", when="@1.13:2.2")
    # END DEPENDENCIES

