# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyClick(PythonPackage):
    # BEGIN VERSIONS
    version("8.1.7", sha256="ae74fb96c20a0277a1d615f1e4d73c8414f5a98db8b799a7931d1582f3390c28", url="https://pypi.org/packages/00/2e/d53fa4befbf2cfa713304affc7ca780ce4fc1fd8710527771b58311a3229/click-8.1.7-py3-none-any.whl")
    version("8.1.6", sha256="fa244bb30b3b5ee2cae3da8f55c9e5e0c0e86093306301fb418eb9dc40fbded5", url="https://pypi.org/packages/1a/70/e63223f8116931d365993d4a6b7ef653a4d920b41d03de7c59499962821f/click-8.1.6-py3-none-any.whl")
    version("8.1.5", sha256="e576aa487d679441d7d30abb87e1b43d24fc53bffb8758443b1a9e1cee504548", url="https://pypi.org/packages/22/b3/1da4ea0efa2e5ae410a347be614162ca08bd24a84059938aa5122d1e751b/click-8.1.5-py3-none-any.whl")
    version("8.1.4", sha256="2739815aaa5d2c986a88f1e9230c55e17f0caad3d958a5e13ad0797c166db9e3", url="https://pypi.org/packages/f9/a6/dc327484918f1656cc9fcebebe77efcfc0ef0d447fa925a8760ee55abe0e/click-8.1.4-py3-none-any.whl")
    version("8.1.3", sha256="bb4d8133cb15a609f44e8213d9b391b0809795062913b383c62be0ee95b1db48", url="https://pypi.org/packages/c2/f1/df59e28c642d583f7dacffb1e0965d0e00b218e0186d7858ac5233dce840/click-8.1.3-py3-none-any.whl")
    version("8.1.2", sha256="24e1a4a9ec5bf6299411369b208c1df2188d9eb8d916302fe6bf03faed227f1e", url="https://pypi.org/packages/a0/66/c8196ad693d62384d8e800e5bd27434a64c0057fe169b61c69a73f1614a8/click-8.1.2-py3-none-any.whl")
    version("8.1.1", sha256="5e0d195c2067da3136efb897449ec1e9e6c98282fbf30d7f9e164af9be901a6b", url="https://pypi.org/packages/97/b2/59e9a416766a54e182ad4980c96b097bf1b9fb6dee5f2ffc5f4b3c5d9800/click-8.1.1-py3-none-any.whl")
    version("8.1.0", sha256="19a4baa64da924c5e0cd889aba8e947f280309f1a2ce0947a3e3a7bcb7cc72d6", url="https://pypi.org/packages/86/3e/3a523bdd24510288b1b850428e01172116a29268378b1da9a8d0b894a115/click-8.1.0-py3-none-any.whl")
    version("8.0.4", sha256="6a7a62563bbfabfda3a38f3023a1db4a35978c0abd76f6c9605ecd6554d6d9b1", url="https://pypi.org/packages/4a/a8/0b2ced25639fb20cc1c9784de90a8c25f9504a7f18cd8b5397bd61696d7d/click-8.0.4-py3-none-any.whl")
    version("8.0.3", sha256="353f466495adaeb40b6b5f592f9f91cb22372351c84caeb068132442a4518ef3", url="https://pypi.org/packages/48/58/c8aa6a8e62cc75f39fee1092c45d6b6ba684122697d7ce7d53f64f98a129/click-8.0.3-py3-none-any.whl")
    version("8.0.1", sha256="fba402a4a47334742d782209a7c79bc448911afe1149d07bdabdf480b3e2f4b6", url="https://pypi.org/packages/76/0a/b6c5f311e32aeb3b406e03c079ade51e905ea630fc19d1262a46249c1c86/click-8.0.1-py3-none-any.whl")
    version("7.1.2", sha256="dacca89f4bfadd5de3d7489b7c8a566eee0d3676333fbb50030263894c38c0dc", url="https://pypi.org/packages/d2/3d/fa76db83bf75c4f8d338c2fd15c8d33fdd7ad23a9b5e57eb6c5de26b430e/click-7.1.2-py2.py3-none-any.whl")
    version("7.1.1", sha256="e345d143d80bf5ee7534056164e5e112ea5e22716bbb1ce727941f4c8b471b9a", url="https://pypi.org/packages/dd/c0/4d8f43a9b16e289f36478422031b8a63b54b6ac3b1ba605d602f10dd54d6/click-7.1.1-py2.py3-none-any.whl")
    version("7.1", sha256="91eb2c43db0254aaf3b14a3c4e0db914a900aa09bbc33c6e87ede4a8f7c969dc", url="https://pypi.org/packages/cf/14/03d1edbed5fe8be89d0938f8bc015f97cc6ff47af55d1195ec0fab978e64/click-7.1-py2.py3-none-any.whl")
    version("7.0", sha256="2335065e6395b9e67ca716de5f7526736bfa6ceead690adf616d925bdc622b13", url="https://pypi.org/packages/fa/37/45185cb5abbc30d7257104c434fe0b07e5a195a6847506c074527aa599ec/Click-7.0-py2.py3-none-any.whl")
    version("6.7", sha256="29f99fc6125fbc931b758dc053b3114e55c77a6e4c6c3a2674a2dc986016381d", url="https://pypi.org/packages/34/c1/8806f99713ddb993c5366c362b2f908f18269f8d792aff1abfd700775a77/click-6.7-py2.py3-none-any.whl")
    version("6.7.dev0", sha256="71c6adabc8afbcce77d9449cd447adecf3b9256cb213e8d593e4ff83880c8a4a", url="https://pypi.org/packages/7e/16/5a3cc0022ac505131fba3c9ea6ae5178fbb6de3d53580301b59d76b22ae3/click-6.7.dev0.tar.gz")
    version("6.6", sha256="fcf697e1fd4b567d817c69dab10a4035937fe6af175c05fd6806b69f74cbc6c4", url="https://pypi.org/packages/1c/7c/10b4132dd952b6a04e37626258825b8aa8c1eb99545f2eb26a77c21efb55/click-6.6-py2.py3-none-any.whl")
    version("6.5", sha256="596b81cda1d84d8cb57ceefd17a78d084c60b134819067b0721a3b0f53dc3ad2", url="https://pypi.org/packages/c5/69/cfba82517e863d6403560e7a6e0085ea67d7fa1fd618938b0bb28a34a870/click-6.5.tar.gz")
    version("6.4", sha256="a5369d2fcd77dc47f2e4cf9eb7161ef526661de3e5dca88e629d6ec8d7103821", url="https://pypi.org/packages/3a/6a/e4602135faa87282dab2d432c7d2e8b0e7a2663e487b5b4a335bda9bc9d4/click-6.4-py2.py3-none-any.whl")
    version("6.3", sha256="2edb68d966802dd1b28a5f3403bcd7d2e3cc4218c8a9ef6b8d152daa753bf6ca", url="https://pypi.org/packages/29/29/cc644d46601e331d025feb51f9c3ac6c2b6ad0b2e4403199514ea394ea82/click-6.3-py2.py3-none-any.whl")
    version("6.2", sha256="bbb49b513a663b9d93139b1ddadfa866edb41982d8b1c7b79a81f47e279bdb72", url="https://pypi.org/packages/a0/90/0f5ea412a4d5b8e31cb514208e02824b45a8f4de52654733f0a862353fd9/click-6.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-colorama", when="@8.0.0-rc1: platform=windows")
    # END DEPENDENCIES

