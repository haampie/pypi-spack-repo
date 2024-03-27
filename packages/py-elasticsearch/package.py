##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyElasticsearch(PythonPackage):
    version("8.6.2", sha256="8ccbebd9a0f6f523c7db67bb54863dde8bdb93daae4ff97f7c814e0500a73e84", url="https://pypi.org/packages/f7/43/f73f5a5cc40b1943f90a895b248a4985a4b23aa25439d7919bc6ab147398/elasticsearch-8.6.2-py3-none-any.whl")
    version("7.17.9", sha256="0e2454645dc00517dee4c6de3863411a9c5f1955d013c5fefa29123dadc92f98", url="https://pypi.org/packages/9b/0a/5ad75e5379bf01c044aa00e0ea893eab630cb5339db87b84436f2b762ffd/elasticsearch-7.17.9-py2.py3-none-any.whl")
    version("7.17.8", sha256="f511ea92e96db09b0e96b0de5fbbb7aa5c3740b0c571a364a2c3a1cc7ec06203", url="https://pypi.org/packages/c3/41/98c17a30539c93cb1946cfc648f2600dc46ddb5ef8f61a6db74afd74ffa8/elasticsearch-7.17.8-py2.py3-none-any.whl")
    version("7.17.7", sha256="555170b4e13a823f4472bc12a148aef90febd5b90b16be83651d35524f34acb3", url="https://pypi.org/packages/4b/42/060e2d26d6b0f6f27c993002c6ceaddb9b0f30bf9f7c6fef8a62817485d5/elasticsearch-7.17.7-py2.py3-none-any.whl")
    version("7.17.6", sha256="2c3400c9e9c7fee46c4732fb32b933577aebb07b5e94df025f6ff1a30d2397d0", url="https://pypi.org/packages/42/05/eac555094ec3e94461661ddcf2d4bf98bbfadf44e38d65e4981aa3dc7984/elasticsearch-7.17.6-py2.py3-none-any.whl")
    version("7.17.5", sha256="1cca401df5ec5cf28c51dae21d11810e4f0289bd6e3985cbefe09c05e6428adb", url="https://pypi.org/packages/5e/2f/55b3da932a7aa844e9e790dc5d60c7bda4c6f0f0551802ea0dac54741ce4/elasticsearch-7.17.5-py2.py3-none-any.whl")
    version("7.17.4", sha256="81c1d15b0f9382b2dc40a896c634f8de09bfcd5079e19a8412940a9ddfbde64b", url="https://pypi.org/packages/f9/09/fa1d015066c3911f0b2f6959c78e7f72c8bd7687ba272de990a7e80d367d/elasticsearch-7.17.4-py2.py3-none-any.whl")
    version("7.17.3", sha256="e7a03ef9b37a569f4d228a583b8aad3cf99aaae72a53cfc7f1fee70c7fa05255", url="https://pypi.org/packages/38/ea/3bbadeaf3e3fa9cfee822f0d597bac7d691417e43b5953e6baaa8561f415/elasticsearch-7.17.3-py2.py3-none-any.whl")
    version("7.17.2", sha256="f49ebaf9e9652a468db4dce5eb8a6a7ea33594ab988f6dadebf36f99772ac809", url="https://pypi.org/packages/4a/e5/ba6af6d8bbf90abb4114c90fb7a9e19f15b38c31818f56443d6ff4a80615/elasticsearch-7.17.2-py2.py3-none-any.whl")
    version("7.17.1", sha256="8c79fe145f23826df144d1adc406a131e5cf3f41f302869fb5a1263b381e5ee2", url="https://pypi.org/packages/c9/08/ee5b3db444962cb1783df0bf74192ad1751038eb4cbb773bd963ee23814a/elasticsearch-7.17.1-py2.py3-none-any.whl")
    version("7.17.0", sha256="ccbf3d1651eb79798a55c1e84b8be850db3873f0329e74086a2cfba37e8c288c", url="https://pypi.org/packages/8b/ae/051943fc4dc456dfa7b87d462333edd31a19ecfab1c821a4cdf891ad4a45/elasticsearch-7.17.0-py2.py3-none-any.whl")
    version("7.6.0", sha256="f4bb05cfe55cf369bdcb4d86d0129d39d66a91fd9517b13cd4e4231fbfcf5c81", url="https://pypi.org/packages/cc/cf/7973ac58090b960857da04add0b345415bf1e1741beddf4cbe136b8ad174/elasticsearch-7.6.0-py2.py3-none-any.whl")
    version("7.5.1", sha256="2a0ca516378ae9b87ac840e7bb529ec508f3010360dd9feed605dff2a898aff5", url="https://pypi.org/packages/b8/02/97e33ea5dc350821b8df9784134188fd68819d6841b5fab4c68aab798500/elasticsearch-7.5.1.tar.gz")
    version("6.4.0", sha256="fb5ab15ee283f104b5a7a5695c7e879cb2927e4eb5aed9c530811590b41259ad", url="https://pypi.org/packages/9e/66/84914ae9483d03055c1245e7e26e095de413fa364c4cdb6e4f6e1a2ce210/elasticsearch-6.4.0.tar.gz")
    version("5.2.0", sha256="45d9f8fbe0878a1b7493afeb20f4f6677a43982776ed1a77d9373e9c5b9de966", url="https://pypi.org/packages/e7/b5/a77098b1f248dbc6407a53d51bf1980ab91718cd93c662cdb1ed529a1278/elasticsearch-5.2.0.tar.gz")
    version("2.3.0", sha256="be3080a2bf32dff0a9f9fcc1c087515a25a357645673a976d25ef77166134d81", url="https://pypi.org/packages/10/35/5fd52c5f0b0ee405ed4b5195e8bce44c5e041787680dc7b94b8071cac600/elasticsearch-2.3.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-certifi", when="@7.7:7")
        depends_on("py-elastic-transport@8.0.0:", when="@8.0.0:")
        depends_on("py-urllib3@1.21.1:1", when="@7.10:7")
        depends_on("py-urllib3@1.21.1:", when="@6.8:6,7.6:7.9")

