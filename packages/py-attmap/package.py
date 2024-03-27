##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAttmap(PythonPackage):
    version("0.13.2", sha256="9c76af312c3678927a03ebb8fd2fa3a9cab37f7ce34f1dc574ea890c778f2f26", url="https://pypi.org/packages/2b/14/20b368acd5aacbd0f01004f7ac8b57ced1a961833795c053fd87774ce7e8/attmap-0.13.2-py3-none-any.whl")
    version("0.13.1", sha256="bcec0623a217d81b0700077bc8d769bb52e376d8c8cb5ef8470a56dba6b470d1", url="https://pypi.org/packages/2a/d6/aca2fe6162f4b0dd6bce1eeca8287990f07173d4e5d7cf0d6c369be3d3dd/attmap-0.13.1-py3-none-any.whl")
    version("0.13.0", sha256="768b4c2ac99cae9484edd88e8d7d701e26a24dd9ffb8daa937013d3153790b5b", url="https://pypi.org/packages/e1/f1/9c1efaba84658cd8116738b4b03f9cc8557e4d133ca270dc5981cf80b51b/attmap-0.13.0-py3-none-any.whl")
    version("0.12.11", sha256="95b1f7dbcdad7278a3702fa921be6271046c96e1c9ed9feb10e0d4c13092b0a0", url="https://pypi.org/packages/d0/d4/8b8fca155270a6675bac9a1e49b7c616ae763f66af7b836042ecfc805552/attmap-0.12.11.tar.gz")
    version("0.12.10", sha256="6f5e10688c29ba41d09108413d0419d37b573607f7eccee55d7153a0261e830e", url="https://pypi.org/packages/9d/36/d39343587a05904e601231370f54f67c34473c63a54bb30f2bf6e2c2ed91/attmap-0.12.10.tar.gz")
    version("0.12.9", sha256="5f8066a242d4cc8588dfa6b8f4d4a83587fc4c91f8b55eb7b04158d8eba76b48", url="https://pypi.org/packages/9c/b7/afa6cff15a9b3f67ae55d72ca8b6952c739a1a21314f937ef96749735df5/attmap-0.12.9.tar.gz")
    version("0.12.8", sha256="98eb09658ca917092bc62676b5a465c6634954cde5578d7be0e1ccd9e337fefa", url="https://pypi.org/packages/99/08/66c4e601cd0135622f606f32d5db6eb86bb3406ce7417f499349c401a53d/attmap-0.12.8.tar.gz")
    version("0.12.7", sha256="01af15824befed4c0ebfc3cc053bdeebf7ae4313b369068347c834ce1ca1898d", url="https://pypi.org/packages/85/07/9fc9235ca51f91ff1e3cb18b14aad3e3dcb54a799c958f89192315778816/attmap-0.12.7.tar.gz")
    version("0.12.6", sha256="2ef446738ae8dc30709d8073749672df6f18d1fb30186c96e3899f8891475f48", url="https://pypi.org/packages/2e/3d/9ddaeb284eddefab8107bb48a476e7adeec8ca71fa2292a9ed71e818a7b3/attmap-0.12.6.tar.gz")
    version("0.12.5", sha256="64336aaaaabf33b7b721c0a6057ba4ac15e17be3feabcf5898ab65a29a8202e3", url="https://pypi.org/packages/90/2b/dc7fca577bbd71a099ca90d517054b8f374812ff95e20b95b2915a853aa2/attmap-0.12.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-ubiquerg@0.2.1:", when="@0.13:")

