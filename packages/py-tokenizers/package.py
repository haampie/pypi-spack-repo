# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTokenizers(PythonPackage):
    # BEGIN VERSIONS
    version("0.15.2", sha256="e6e9c6e019dd5484be5beafc775ae6c925f4c69a3487040ed09b45e13df2cb91", url="https://pypi.org/packages/c0/44/625db94e91c6196b6574359fa70bfe28e8eabf57a1b894f8f0ec69727fd1/tokenizers-0.15.2.tar.gz")
    version("0.15.2-rc1", sha256="1530c1480158827377cd3d219eea527844a9eccf54ded86e15dc1bf3ca5fedf2", url="https://pypi.org/packages/1d/1e/9fa9dbc127579fe210c5655040d86ea487a6b43a0049f47a31773e9037a6/tokenizers-0.15.2rc1.tar.gz")
    version("0.15.1", sha256="c0a331d6d5a3d6e97b7f99f562cee8d56797180797bc55f12070e495e717c980", url="https://pypi.org/packages/c9/90/06bd4bd6c33b9a8d4b4a184e2e575906234d3ba0d6f9e48890b6aa06d13b/tokenizers-0.15.1.tar.gz")
    version("0.15.1-rc1", sha256="e4f73a6b4503088e2b08ea6a62fc01df95c8351773bbbe5ce43dc8535b5f8988", url="https://pypi.org/packages/dc/21/302aad5066448ef1b230d31e61280656cc4b913d4202a0e51bf729b11d46/tokenizers-0.15.1rc1.tar.gz")
    version("0.15.1-rc0", sha256="3e8558b881f359c1f63c68547f8f7a25f804f7e8fa9a46d1f5bf749cf367eb53", url="https://pypi.org/packages/01/6a/b0553443d19f0275ed6525e7c9a98669c3381a6edbc3867bda1f3dfa181e/tokenizers-0.15.1rc0.tar.gz")
    version("0.15.0", sha256="10c7e6e7b4cabd757da59e93f5f8d1126291d16f8b54f28510825ef56a3e5d0e", url="https://pypi.org/packages/9f/17/1df113d77dab378cb02fcee438893610e055621d3994b51d5ffe315170e4/tokenizers-0.15.0.tar.gz")
    version("0.15.0-rc1", sha256="d91ff70866641dde8f27fee8407a10c0dba505352e75e67f9e5312bbc9ac148a", url="https://pypi.org/packages/ca/dd/bcc2b7573ba311f9194081e8dcd5b5737f0f85555e94d6a99eec2ad09df4/tokenizers-0.15.0rc1.tar.gz")
    version("0.14.1", sha256="ea3b3f8908a9a5b9d6fc632b5f012ece7240031c44c6d4764809f33736534166", url="https://pypi.org/packages/b2/b9/bf025d763bbdd333cb88bedb23426f932c5b4a6ce6f033c498517fad5b90/tokenizers-0.14.1.tar.gz")
    version("0.14.1-rc1", sha256="a481450e3d21026f79008b5f05294db3684127d5efeeef509e861368b314ede6", url="https://pypi.org/packages/d5/60/f7b66ad6041d064936749a0fc6e4b72a9a444499104943347f4b88babef8/tokenizers-0.14.1rc1.tar.gz")
    version("0.14.0", sha256="a06efa1f19dcc0e9bd0f4ffbf963cb0217af92a9694f68fe7eee5e1c6ddc4bde", url="https://pypi.org/packages/ce/e9/8dbbc014c48d73ca8eb86bccec15f857ad2e86f9d16a44b7d11ec145c0c2/tokenizers-0.14.0.tar.gz")
    version("0.13.3", sha256="2e546dbb68b623008a5442353137fbb0123d311a6d7ba52f2667c8862a75af2e", url="https://pypi.org/packages/29/9c/936ebad6dd963616189d6362f4c2c03a0314cf2a221ba15e48dd714d29cf/tokenizers-0.13.3.tar.gz")
    version("0.13.2", sha256="f9525375582fd1912ac3caa2f727d36c86ff8c0c6de45ae1aaff90f87f33b907", url="https://pypi.org/packages/4a/d9/af2821b5934ed871f716eb65fb3bd43e7bc70b99191ec08f20cfd642d0a1/tokenizers-0.13.2.tar.gz")
    version("0.13.1", sha256="3333d1cee5c8f47c96362ea0abc1f81c77c9b92c6c3d11cbf1d01985f0d5cf1d", url="https://pypi.org/packages/3d/66/5296f3610be7a4aaefa0b602351f63115f3945f725b5e37c2634c578a293/tokenizers-0.13.1.tar.gz")
    version("0.13.0", sha256="e49a137bd9321905bd37abcc77d34b7d9d6d11e09da3a901bd127e640be55985", url="https://pypi.org/packages/44/4b/323787e105caddf5ace40c4007e0745abf97e00ef21554e268c6d266d64d/tokenizers-0.13.0.tar.gz")
    version("0.12.1", sha256="070746f86efa6c873db341e55cf17bb5e7bdd5450330ca8eca542f5c3dab2c66", url="https://pypi.org/packages/12/57/da0cb8e40437f88630769164a66afec8af294ff686661497b6c88bc08556/tokenizers-0.12.1.tar.gz")
    version("0.12.0", sha256="81e2b69005d717c2856995979fe1f17646eec8e1bb974852a10b2195b3f7a64e", url="https://pypi.org/packages/25/39/3db82f83e42e95e6949d2f196ee08bb6f3e651d8eced80f1d2dde9fbbdc0/tokenizers-0.12.0.tar.gz")
    version("0.11.6", sha256="562b2022faf0882586c915385620d1f11798fc1b32bac55353a530132369a6d0", url="https://pypi.org/packages/c6/ad/f1d539784a41747e76f3d543bedcb3b255ff677b4f113e362743ede6384f/tokenizers-0.11.6.tar.gz")
    version("0.11.5", sha256="8ec3f22c0bcad5d2cfe295adff70981b7a3c09bbd577f467718f2edaf0f391c9", url="https://pypi.org/packages/67/64/79189b3d1d91211fd966561aa73cff186c3217a7c65b4bc460fe1a7276d3/tokenizers-0.11.5.tar.gz")
    version("0.11.4", sha256="62bfccd1de58d1372d3789f7ba2bbd5cd99cb5e799d5a70ffa8248d0fe4f7d81", url="https://pypi.org/packages/e2/8f/1caad5d4652335da37cd9e19d1db17647156b79c67c78df06ac77664e127/tokenizers-0.11.4.tar.gz")
    version("0.11.2", sha256="15f078682d29d0de1ae3a40c553acd6e3a8152174ea4705f6c72ea8f25cdec8e", url="https://pypi.org/packages/88/a4/8affb56f536185767491675b307fdde10cf51420559a41464a4171c8287f/tokenizers-0.11.2.tar.gz")
    version("0.10.3", sha256="1a5d3b596c6d3a237e1ad7f46c472d467b0246be7fd1a364f12576eb8db8f7e6", url="https://pypi.org/packages/48/2b/b99184cacb1a743edc18290e9127d1b0e658c0c46f2ab5290b27fe865ff4/tokenizers-0.10.3.tar.gz")
    version("0.10.2", sha256="cf7f1aad957fed36e4a90fc094e3adc03fdd45fbb058c1cde25721e3e66235f8", url="https://pypi.org/packages/05/96/d8f7a202cd46ac646b0aca2f3a7902bfefc70e9bd980e0371dba7fe7db85/tokenizers-0.10.2.tar.gz")
    version("0.10.1", sha256="81c35b4bc9238c0b5d0af91a719e732a60ee0d87d8bf76615bfec8f3e3ba8f15", url="https://pypi.org/packages/01/ee/206ac679a6e0e5d8fd685d9a16e8f23229b39a3733c57ec0851efe65f2c6/tokenizers-0.10.1.tar.gz")
    version("0.6.0", sha256="1da11fbfb4f73be695bed0d655576097d09a137a16dceab2f66399716afaffac", url="https://pypi.org/packages/42/82/71bbc4eff999a3e397373b9ccb43f82dad7d6d0865f2ce858d09add2dca6/tokenizers-0.6.0.tar.gz")
    version("0.5.2", sha256="b5a235f9c71d04d4925df6c4fa13b13f1d03f9b7ac302b89f8120790c4f742bc", url="https://pypi.org/packages/f5/d7/a3882b2d36991f613b749fc5e305cccc345ec9d6ab0621ad7e7bf1be8691/tokenizers-0.5.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-huggingface-hub@0.16.4:", when="@0.15:")
        depends_on("py-huggingface-hub@0.16.4:0.17", when="@0.14.1-rc1:0.14")
        depends_on("py-huggingface-hub@0.16.4:0.16", when="@0.14:0.14.0")
    # END DEPENDENCIES

