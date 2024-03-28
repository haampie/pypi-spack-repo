# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAbslPy(PythonPackage):
    # BEGIN VERSIONS
    version("1.4.0", sha256="0d3fe606adfa4f7db64792dd4c7aee4ee0c38ab75dfd353b7a83ed3e957fcb47", url="https://pypi.org/packages/dd/87/de5c32fa1b1c6c3305d576e299801d8655c175ca9557019906247b994331/absl_py-1.4.0-py3-none-any.whl")
    version("1.2.0", sha256="5d15f85b8cc859c6245bc9886ba664460ed96a6fee895416caa37d669ee74a9a", url="https://pypi.org/packages/a5/b8/fc74a554a6fc7f26744c883ebfe405cf49c1f1320f13ee874aee47c70e1d/absl_py-1.2.0-py3-none-any.whl")
    version("1.1.0", sha256="db97287655e30336938f8058d2c81ed2be6af1d9b6ebbcd8df1080a6c7fcd24e", url="https://pypi.org/packages/11/8d/5fce604f03c8d30aa0d45451e67efe30d23e65eec7bbef9b9d341b86c0ef/absl_py-1.1.0-py3-none-any.whl")
    version("0.13.0", sha256="62bd4e248ddb19d81aec8f9446b407ff37c8175c2ba88266a7afa9b4ce4a333b", url="https://pypi.org/packages/23/47/835652c7e19530973c73c65e652fc53bd05725d5a7cf9bb8706777869c1e/absl_py-0.13.0-py3-none-any.whl")
    version("0.12.0", sha256="afe94e3c751ff81aad55d33ab6e630390da32780110b5af72ae81ecff8418d9e", url="https://pypi.org/packages/92/c9/ef0fae29182d7a867d203f0eff8296b60da92098cc41db33a434f4be84bf/absl_py-0.12.0-py3-none-any.whl")
    version("0.11.0", sha256="b3d9eb5119ff6e0a0125f6dabf2f9fae02f8acae7be70576002fac27235611c5", url="https://pypi.org/packages/bc/58/0aa6fb779dc69cfc811df3398fcbeaeefbf18561b6e36b185df0782781cc/absl_py-0.11.0-py3-none-any.whl")
    version("0.10.0", sha256="ea07d7d437798bffc14f39fccec3909d251a1e76e233205ded72b71c267e0178", url="https://pypi.org/packages/b9/07/f69dd3367368ad69f174bfe426a973651412ec11d48ec05c000f19fe0561/absl_py-0.10.0-py3-none-any.whl")
    version("0.7.1", sha256="b943d1c567743ed0455878fcd60bc28ac9fae38d129d1ccfad58079da00b8951", url="https://pypi.org/packages/da/3f/9b0355080b81b15ba6a9ffcf1f5ea39e307a2778b2f2dc8694724e8abd5b/absl-py-0.7.1.tar.gz")
    version("0.7.0", sha256="8718189e4bd6013bf79910b9d1cb0a76aecad8ce664f78e1144980fabdd2cd23", url="https://pypi.org/packages/31/bc/ab68120d1d89ae23b694a55fe2aece2f91194313b71f9b05a80b32d3c24b/absl-py-0.7.0.tar.gz")
    version("0.1.6", sha256="02c577d618a8bc0a2a5d1a51f160d3649745d7a2516d87025322f46ac1391a22", url="https://pypi.org/packages/23/83/a8339834609941af26206d99ca19d499538f5ee28447e40889ca25241b56/absl-py-0.1.6.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six", when="@0.10:1.0")
    # END DEPENDENCIES

