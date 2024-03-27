##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyjwt(PythonPackage):
    version("2.8.0", sha256="59127c392cc44c2da5bb3192169a91f429924e17aff6534d70fdc02ab3e04320", url="https://pypi.org/packages/2b/4f/e04a8067c7c96c364cef7ef73906504e2f40d690811c021e1a1901473a19/PyJWT-2.8.0-py3-none-any.whl")
    version("2.7.0", sha256="ba2b425b15ad5ef12f200dc67dd56af4e26de2331f965c5439994dad075876e1", url="https://pypi.org/packages/c7/e8/01b2e35d81e618a8212e651e10c91660bdfda49c1d15ce66f4ca1ff43649/PyJWT-2.7.0-py3-none-any.whl")
    version("2.6.0", sha256="d83c3d892a77bbb74d3e1a2cfa90afaadb60945205d1095d9221f04466f64c14", url="https://pypi.org/packages/40/46/505f0dd53c14096f01922bf93a7abb4e40e29a06f858abbaa791e6954324/PyJWT-2.6.0-py3-none-any.whl")
    version("2.5.0", sha256="8d82e7087868e94dd8d7d418e5088ce64f7daab4b36db654cbaedb46f9d1ca80", url="https://pypi.org/packages/37/82/43382713811f0ddd9fff1ed778af6818cc2080ccd425e3eba540be690fb6/PyJWT-2.5.0-py3-none-any.whl")
    version("2.4.0", sha256="72d1d253f32dbd4f5c88eaf1fdc62f3a19f676ccbadb9dbc5d07e951b2b26daf", url="https://pypi.org/packages/1c/fb/b82e9601b00d88cf8bbee1f39b855ae773f9d5bcbcedb3801b2f72460696/PyJWT-2.4.0-py3-none-any.whl")
    version("2.3.0", sha256="e0c4bb8d9f0af0c7f5b1ec4c5036309617d03d56932877f2f7a0beeb5318322f", url="https://pypi.org/packages/2a/4d/67cc66a0c49003dc216fc73db2d05a3b80c7193167fd113da1f2c678ac2a/PyJWT-2.3.0-py3-none-any.whl")
    version("2.2.0", sha256="b0ed5824c8ecc5362e540c65dc6247567db130c4226670bf7699aec92fb4dae1", url="https://pypi.org/packages/7d/5a/8ec21f8c4159708919b6cb5c203a1537349fd05265d2d88609493b462875/PyJWT-2.2.0-py3-none-any.whl")
    version("2.1.0", sha256="934d73fbba91b0483d3857d1aff50e96b2a892384ee2c17417ed3203f173fca1", url="https://pypi.org/packages/3f/32/d5d3cab27fee7f6b22d7cd7507547ae45d52e26030fa77d1f83d0526c6e5/PyJWT-2.1.0-py3-none-any.whl")
    version("2.0.1", sha256="b70b15f89dc69b993d8a8d32c299032d5355c82f9b5b7e851d1a6d706dffe847", url="https://pypi.org/packages/b4/9b/8850f99027ed029af6828199cc87179eaccbbf1f9e6e373e7f0177d32dad/PyJWT-2.0.1-py3-none-any.whl")
    version("2.0.0", sha256="5c2ff2eb27d7e342dfc3cafcc16412781f06db2690fbef81922b0172598f085b", url="https://pypi.org/packages/91/5f/5cff1c3696e0d574f5741396550c9a308dde40704d17e39e94b89c07d789/PyJWT-2.0.0-py3-none-any.whl")
    version("1.7.1", sha256="5c6eca3c2940464d106b99ba83b00c6add741c9becaec087fb7ccdefea71350e", url="https://pypi.org/packages/87/8b/6a9f14b5f781697e51259d81657e6048fd31a113229cf346880bb7545565/PyJWT-1.7.1-py2.py3-none-any.whl")
    version("1.7.0", sha256="00414bfef802aaecd8cc0d5258b6cb87bd8f553c2986c2c5f29b19dd5633aeb7", url="https://pypi.org/packages/02/9b/16c92330f1fb76e3f6372ba6f804d412ec894ee1d9ea31516269b5f6add4/PyJWT-1.7.0-py2.py3-none-any.whl")
    version("1.6.4", sha256="30b1380ff43b55441283cc2b2676b755cca45693ae3097325dea01f3d110628c", url="https://pypi.org/packages/93/d1/3378cc8184a6524dc92993090ee8b4c03847c567e298305d6cf86987e005/PyJWT-1.6.4-py2.py3-none-any.whl")
    version("1.6.3", sha256="d527c3330d83d7278a0a8ef570b7c9c39fbf2c0c1edbe564a1a8a02d5352322b", url="https://pypi.org/packages/77/11/4ccc1f4f8d812a6459e53f4f33107ae5d25babed9e6c1f0c6923b1fa8966/PyJWT-1.6.3-py2.py3-none-any.whl")
    version("1.6.1", sha256="bca523ef95586d3a8a5be2da766fe6f82754acba27689c984e28e77a12174593", url="https://pypi.org/packages/31/8f/19c302aa9a391dd1fbd249362b749021b88d40fb59af0363939a2250afed/PyJWT-1.6.1-py2.py3-none-any.whl")
    version("1.6.0", sha256="b752500cafd4df9f0dc6efe9063603e36a4e1a5c24fee48234d2949b6606aa59", url="https://pypi.org/packages/fc/fd/02c195aa48beef5e4b018259634dd885fa1a9df351c708a8486e7ddf2216/PyJWT-1.6.0-py2.py3-none-any.whl")
    version("1.5.3", sha256="a4e5f1441e3ca7b382fd0c0b416777ced1f97c64ef0c33bfa39daf38505cfd2f", url="https://pypi.org/packages/8a/a6/4d931a2c77a224d27c78382f4ce8ec07542d4426ea2793bea77a689273c2/PyJWT-1.5.3-py2.py3-none-any.whl")
    version("1.5.2", sha256="1179f0bff86463b5308ee5f7aff1c350e1f38139d62a723e16fb2c557d1c795f", url="https://pypi.org/packages/ac/b2/72a8bff872e6f8e2aed4f4210aa24ba9c9f4f03a67f34e2f867905122235/PyJWT-1.5.2.tar.gz")
    version("1.5.1", sha256="d6b363d2015c33afd63dfd961d38ae40e97f7abd3db50c87ac626238bc1039a0", url="https://pypi.org/packages/b2/b0/7fb49bcbc43f1ea70f1cb7c68e2d444295ec53dfd641f1d3600f44bbfc5b/PyJWT-1.5.1.tar.gz")
    version("1.5.0", sha256="fd182b728d13f04c289d9b2623d09256d356c9b4a6778018001454a954d7c54b", url="https://pypi.org/packages/53/d1/bc6a0296a4a63277c45ab22f4b4a58a0d2ada12d6d60905dbdc40989d8fd/PyJWT-1.5.0.tar.gz")

    variant("crypto", default=False)

    with default_args(type="run"):
        depends_on("py-cryptography@3.4:", when="@2.6:+crypto")
        depends_on("py-cryptography@3.3.1:", when="@2.2:2.5+crypto")
        depends_on("py-cryptography@3.3.1:3", when="@2.0.0:2.1+crypto")
        depends_on("py-cryptography@1.4:", when="@1.5.3:1+crypto")
        depends_on("py-types-cryptography@3.3.21:", when="@2.5+crypto")

