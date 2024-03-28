# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTifffile(PythonPackage):
    # BEGIN VERSIONS
    version("2024.2.12", sha256="870998f82fbc94ff7c3528884c1b0ae54863504ff51dbebea431ac3fa8fb7c21", url="https://pypi.org/packages/cd/0b/33610b4d0d1bb83a6bfd20ed838f52e02a44e9b439116cd4f3d424e81a80/tifffile-2024.2.12-py3-none-any.whl")
    version("2024.1.30", sha256="40cb48f661acdfea16cb00dc8941bd642b8eb5c59bca6de6a54091bee9ee2699", url="https://pypi.org/packages/16/09/b9f5e4f9448fd39b7c0c9cbb592409ab28e90a1913795260b975d8424cde/tifffile-2024.1.30-py3-none-any.whl")
    version("2023.12.9", sha256="9b066e4b1a900891ea42ffd33dab8ba34c537935618b9893ddef42d7d422692f", url="https://pypi.org/packages/54/a4/569fc717831969cf48bced350bdaf070cdeab06918d179429899e144358d/tifffile-2023.12.9-py3-none-any.whl")
    version("2023.9.26", sha256="1de47fa945fddaade256e25ad4f375ae65547f3c1354063aded881c32a64cf89", url="https://pypi.org/packages/f5/72/68ea763b5f3e3d9871492683059ed4724fd700dbe54aa03cdda7a9692129/tifffile-2023.9.26-py3-none-any.whl")
    version("2023.9.18", sha256="03574dc63a333111227c7710b52033def22db0072f9b49fdb25c9eea8249b026", url="https://pypi.org/packages/36/06/b5408ce5edf09a3ee0ee531dadb2afc85ffb7624515b223b226b4a45a1d2/tifffile-2023.9.18-py3-none-any.whl")
    version("2023.8.30", sha256="62364eef35a6fdcc7bc2ad6f97dd270f577efb01b31260ff800af76a66c1e145", url="https://pypi.org/packages/12/3e/89513f44a10c625121b7d5bc54390d7ac7f2c92a19755c052888febf9730/tifffile-2023.8.30-py3-none-any.whl")
    version("2023.8.25", sha256="40318485b59e9acb62e7139f22bd46e6760f92daea562b79900bfce3ee2613b7", url="https://pypi.org/packages/71/44/bc173b3b38adf96bfcc33864f1ac8016d3c03269754b6f1deebba635e952/tifffile-2023.8.25-py3-none-any.whl")
    version("2023.8.12", sha256="d1ef06461a947a6800ba6121b330b54a57fb9cbf7e5bc0adab8307081297d66b", url="https://pypi.org/packages/74/68/19989a1009f68ed777ea5d2624c2996bab0890a31ce7d4b2a7ae4e1c0cfe/tifffile-2023.8.12-py3-none-any.whl")
    version("2023.7.18", sha256="a9449ab688b82b69f3ddf80e4e0b4de7b5b02549974a56e112061b816b3c5585", url="https://pypi.org/packages/2d/e5/cc8a8ca43685006bb3ca56fab60707f3f74700844b18634db0b1e8b4b93f/tifffile-2023.7.18-py3-none-any.whl")
    version("2023.7.10", sha256="94dfdec321ace96abbfe872a66cfd824800c099a2db558443453eebc2c11b304", url="https://pypi.org/packages/06/a3/68d17088a4f09565bc7341fd20490da8191ec4cddde479daaabbe07bb603/tifffile-2023.7.10-py3-none-any.whl")
    version("2022.10.10", sha256="87f3aee8a0d06b74655269a105de75c1958a24653e1930d523eb516100043503", url="https://pypi.org/packages/d2/cb/1ecf9f39113a7ad0529a0441a16982791e7b37a4efdba2f89a687fdf15c9/tifffile-2022.10.10-py3-none-any.whl")
    version("2021.11.2", sha256="2e0066f90e2dbeb3e6a287cfd78bafbd2f142fabbca4a76a8ff809573baf5ad5", url="https://pypi.org/packages/d8/38/85ae5ed77598ca90558c17a2f79ddaba33173b31cf8d8f545d34d9134f0d/tifffile-2021.11.2-py3-none-any.whl")
    version("2020.10.1", sha256="9611ac348b4db6844b6555db2b5f8f2be1715728a0011352acb55e0171ee2949", url="https://pypi.org/packages/e8/8c/166c88fcbe3b3632dcf93a106f6d13892b1a2b822b61eb7cd9a5ab68b259/tifffile-2020.10.1-py3-none-any.whl")
    version("0.12.1", sha256="802367effe86b0d1e64cb5c2ed886771f677fa63260b945e51a27acccdc08fa1", url="https://pypi.org/packages/41/d2/086654909995176e34228ed0e5673fed505651083f0d8b277867fb4d9f3a/tifffile-0.12.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@2023.7.18:")
        depends_on("py-numpy", when="@2023:")
        depends_on("py-numpy@1.19.2:", when="@2022")
        depends_on("py-numpy@1.15.1:", when="@2020:2021")
    # END DEPENDENCIES

