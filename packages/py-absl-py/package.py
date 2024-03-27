##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAbslPy(PythonPackage):
    version("2.1.0", sha256="526a04eadab8b4ee719ce68f204172ead1027549089702d99b9059f129ff1308", url="https://pypi.org/packages/a2/ad/e0d3c824784ff121c03cc031f944bc7e139a8f1870ffd2845cc2dd76f6c4/absl_py-2.1.0-py3-none-any.whl")
    version("2.0.0", sha256="9a28abb62774ae4e8edbe2dd4c49ffcd45a6a848952a5eccc6a49f3f0fc1e2f3", url="https://pypi.org/packages/01/e4/dc0a1dcc4e74e08d7abedab278c795eef54a224363bb18f5692f416d834f/absl_py-2.0.0-py3-none-any.whl")
    version("1.4.0", sha256="0d3fe606adfa4f7db64792dd4c7aee4ee0c38ab75dfd353b7a83ed3e957fcb47", url="https://pypi.org/packages/dd/87/de5c32fa1b1c6c3305d576e299801d8655c175ca9557019906247b994331/absl_py-1.4.0-py3-none-any.whl")
    version("1.3.0", sha256="34995df9bd7a09b3b8749e230408f5a2a2dd7a68a0d33c12a3d0cb15a041a507", url="https://pypi.org/packages/2c/39/ba081c6f7837366a39c9286fa1bc9dbf217249df80e133f25c62b05d1a53/absl_py-1.3.0-py3-none-any.whl")
    version("1.2.0", sha256="5d15f85b8cc859c6245bc9886ba664460ed96a6fee895416caa37d669ee74a9a", url="https://pypi.org/packages/a5/b8/fc74a554a6fc7f26744c883ebfe405cf49c1f1320f13ee874aee47c70e1d/absl_py-1.2.0-py3-none-any.whl")
    version("1.1.0", sha256="db97287655e30336938f8058d2c81ed2be6af1d9b6ebbcd8df1080a6c7fcd24e", url="https://pypi.org/packages/11/8d/5fce604f03c8d30aa0d45451e67efe30d23e65eec7bbef9b9d341b86c0ef/absl_py-1.1.0-py3-none-any.whl")
    version("1.0.0", sha256="84e6dcdc69c947d0c13e5457d056bd43cade4c2393dce00d684aedea77ddc2a3", url="https://pypi.org/packages/2c/03/e3e19d3faf430ede32e41221b294e37952e06acc96781c417ac25d4a0324/absl_py-1.0.0-py3-none-any.whl")
    version("0.15.0", sha256="ea907384af023a7e681368bedb896159ab100c7db593efbbd5cde22af11270cd", url="https://pypi.org/packages/97/75/f5e61fb67ecbe45c31035b17562464e11b91a2b8a351bae5ca0db2969e3b/absl_py-0.15.0-py3-none-any.whl")
    version("0.14.1", sha256="565a2c1be855e466e697e1be6b9876c2435dda926954d1de4abf0d592561ece8", url="https://pypi.org/packages/a0/b3/dba58c285e9720979b55574496c819322653f8e6d1d6cf9101c187c7d972/absl_py-0.14.1-py3-none-any.whl")
    version("0.14.0", sha256="81409f8c5c1601f47d57eaa548a8516a967ab45a43ef75e5dfceab2ab4b69143", url="https://pypi.org/packages/6f/30/9447db7fb0ff3e56a3462cb1c005e44c8291bfcb58a0150e098d1f6d0ddd/absl_py-0.14.0-py3-none-any.whl")
    version("0.13.0", sha256="62bd4e248ddb19d81aec8f9446b407ff37c8175c2ba88266a7afa9b4ce4a333b", url="https://pypi.org/packages/23/47/835652c7e19530973c73c65e652fc53bd05725d5a7cf9bb8706777869c1e/absl_py-0.13.0-py3-none-any.whl")
    version("0.12.0", sha256="afe94e3c751ff81aad55d33ab6e630390da32780110b5af72ae81ecff8418d9e", url="https://pypi.org/packages/92/c9/ef0fae29182d7a867d203f0eff8296b60da92098cc41db33a434f4be84bf/absl_py-0.12.0-py3-none-any.whl")
    version("0.11.0", sha256="b3d9eb5119ff6e0a0125f6dabf2f9fae02f8acae7be70576002fac27235611c5", url="https://pypi.org/packages/bc/58/0aa6fb779dc69cfc811df3398fcbeaeefbf18561b6e36b185df0782781cc/absl_py-0.11.0-py3-none-any.whl")
    version("0.10.0", sha256="ea07d7d437798bffc14f39fccec3909d251a1e76e233205ded72b71c267e0178", url="https://pypi.org/packages/b9/07/f69dd3367368ad69f174bfe426a973651412ec11d48ec05c000f19fe0561/absl_py-0.10.0-py3-none-any.whl")
    version("0.9.0", sha256="75e737d6ce7723d9ff9b7aa1ba3233c34be62ef18d5859e706b8fdc828989830", url="https://pypi.org/packages/1a/53/9243c600e047bd4c3df9e69cfabc1e8004a82cac2e0c484580a78a94ba2a/absl-py-0.9.0.tar.gz")
    version("0.7.1", sha256="b943d1c567743ed0455878fcd60bc28ac9fae38d129d1ccfad58079da00b8951", url="https://pypi.org/packages/da/3f/9b0355080b81b15ba6a9ffcf1f5ea39e307a2778b2f2dc8694724e8abd5b/absl-py-0.7.1.tar.gz")
    version("0.7.0", sha256="8718189e4bd6013bf79910b9d1cb0a76aecad8ce664f78e1144980fabdd2cd23", url="https://pypi.org/packages/31/bc/ab68120d1d89ae23b694a55fe2aece2f91194313b71f9b05a80b32d3c24b/absl-py-0.7.0.tar.gz")
    version("0.1.6", sha256="02c577d618a8bc0a2a5d1a51f160d3649745d7a2516d87025322f46ac1391a22", url="https://pypi.org/packages/23/83/a8339834609941af26206d99ca19d499538f5ee28447e40889ca25241b56/absl-py-0.1.6.tar.gz")

    with default_args(type="run"):
        depends_on("py-six", when="@0.10:1.0")

