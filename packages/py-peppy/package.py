# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPeppy(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.40.1", sha256="33cfa369e26cb785d3a7e6d6a6036fe7d1d29b53073f2d497cd269c6fa7945fb", url="https://pypi.org/packages/00/4f/1f284acbe44d319d9c79dfd862ea01ee25f31f6fd3568ec89a83176d3c8b/peppy-0.40.1-py3-none-any.whl")
    version("0.40.0", sha256="965d86a0c38d231527ad419424c4375471722f05c06b9c99823b397f85a36a66", url="https://pypi.org/packages/2e/a9/c5c7e5b39e776cf0fe0140f9157498acab5d174f0152a76a61e884119573/peppy-0.40.0-py3-none-any.whl")
    version("0.40.0-alpha5", sha256="af53570649f18236cc2d760ba299f4ae1e340efd48fb5bde1eb3605c585ac90d", url="https://pypi.org/packages/21/d6/19311ef5fbfa80f88a8744fdb38a6ed39008925fd261cae5455f5d92de4a/peppy-0.40.0a5-py3-none-any.whl")
    version("0.40.0-alpha4", sha256="c1ce297f8ef02288851502b98b7f6e5eba9dc10028b8afc5da76a251a60135b6", url="https://pypi.org/packages/65/f6/658ad4242df9c11ba02c1313ff6f1fcbc246011fc1b1acdec63af82bb3b9/peppy-0.40.0a4-py3-none-any.whl")
    version("0.40.0-alpha3", sha256="f2ff1a36fd2f6b728c62ac456afea95f444b550ce09b6fb347e36f75c2c24d07", url="https://pypi.org/packages/67/cb/4b0c806d5aa79f8c1766d7e2fc07f9e0981222bebe3cbd09750b16a2b3af/peppy-0.40.0a3-py3-none-any.whl")
    version("0.40.0-alpha2", sha256="23f98dbfca87fa27421d4af52c12e93e57378a8a288118b3dfd68d7a7603aa42", url="https://pypi.org/packages/6b/e6/8ceded98a2f5d2b192b3e8a709e2444ec48f58c79bba6122d4cff48d4392/peppy-0.40.0a2-py3-none-any.whl")
    version("0.40.0-alpha1", sha256="a46b4630e70ec30af490f7f727e9b5d1e2d564510863c62d2ee750e5a377609a", url="https://pypi.org/packages/6d/bb/a9967ebffcd10ac6594eb2602d340eabb9720ec2b68ec6e6fd149854c7d5/peppy-0.40.0a1-py3-none-any.whl")
    version("0.35.7", sha256="b675df5027160b98fd87e5a3ba7ac65b90cf9aafa8acfa678006c74bcb1b39ef", url="https://pypi.org/packages/a4/39/22b984ff419fafd3315dbc0c23c12099d15dd8e0e7099c337f8097e5d4ec/peppy-0.35.7-py3-none-any.whl")
    version("0.35.6", sha256="654637c37e0185879dfcb51c013324d07b9e612d5920f5692d08407b77a3c592", url="https://pypi.org/packages/e6/cc/e51d0acdafb9f2c124a636345dd9762c8123f41870d5f7a68568b91b3d9c/peppy-0.35.6-py3-none-any.whl")
    version("0.35.5", sha256="1e9b14c9182c2d1fd90fda832347ddbe6ccaa6a0db087a01be12e5aedc62e4f8", url="https://pypi.org/packages/14/28/75f98028431c9988eb1e2bf742eaeb35bd771917ba70f36a0bb9b78f8962/peppy-0.35.5-py3-none-any.whl")
    version("0.35.4", sha256="88c0e3e450b1a5ce96f6dd7b39be25749e4742dd45a34488841d64abd03f666f", url="https://pypi.org/packages/c4/60/a1d3a437f8cd69432b214cd8cd67b296ff29ad2680e27834a41d75eaaed6/peppy-0.35.4-py3-none-any.whl")
    version("0.35.3", sha256="63a832e113d9ad3f09cc086e3ad1fe041cbf88a30b91ecbfb19175c49a4797de", url="https://pypi.org/packages/49/f1/8fa700079393cdba4f6d76743017b704420abf8d2a7ce352efa9987b895c/peppy-0.35.3-py3-none-any.whl")
    version("0.35.2", sha256="b1f993358eb4c4b4e317cf41142f0db24a8743afcf48e8294acfec739d925687", url="https://pypi.org/packages/52/fe/79c3fc6608227e37e0cb01ac5cf62b5931a37910a5c42f8aa61c58d7d85f/peppy-0.35.2-py3-none-any.whl")
    version("0.35.1", sha256="dd9e99930773f5c7c6ddbc3de7f1a7f9387627be8bd80e255d6158fb63781f1a", url="https://pypi.org/packages/80/af/47beaf531e269e1be1ab4bc1d52c3cc1f009822f26fd54452768334ee951/peppy-0.35.1-py3-none-any.whl")
    version("0.35.0", sha256="13efe8df44606256819a6190c7fa6398bca9c32c966c7ddf49bf792c8a364deb", url="https://pypi.org/packages/1b/9b/81e31c2d1c72e3107acd50702ff5389ff47740ac9e32a08724dea4137651/peppy-0.35.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-attmap@0.13.2:", when="@0.31.2:0.35")
        depends_on("py-logmuse@0.2:", when="@0.30.2:0.35.4")
        depends_on("py-numpy", when="@0.40.0:")
        depends_on("py-pandas@0.24.2:", when="@0.30.2:")
        depends_on("py-pyyaml", when="@0.31.1:")
        depends_on("py-rich@10.3:", when="@0.32:")
        depends_on("py-ubiquerg@0.6.2:", when="@0.31.2:")
        depends_on("py-yacman@0.9:", when="@0.40:0.40.0-alpha5")
    # END DEPENDENCIES

