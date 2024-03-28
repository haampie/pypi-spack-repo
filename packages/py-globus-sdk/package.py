# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGlobusSdk(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.39.0", sha256="5c9ed926c6b5195850ef631152454915b2e8f84c49a4241d90f7f0fa1e92c176", url="https://pypi.org/packages/25/d4/2e3be9304f7d73de4a21a7b73ebe1ed0f44701a0ecff07c0ae2ff54265fa/globus_sdk-3.39.0-py3-none-any.whl")
    version("3.38.0", sha256="00a7a9492614cdfe67258d3c81af26b31807f6910df54ccad6afad9a5ceb2bb2", url="https://pypi.org/packages/d5/3c/7b8e3aff2b982406b77f69ab619ad47ac8e383a45bd76f6c19e40fd29a24/globus_sdk-3.38.0-py3-none-any.whl")
    version("3.37.0", sha256="01c6a27ad4bb012181a714eb8abc29cb5e27875a753aa94c893259a0fe4a5edf", url="https://pypi.org/packages/7e/e9/3be8425b5ca91e43e93042bbb8e353750ab3f647602ede317bf197d9df83/globus_sdk-3.37.0-py3-none-any.whl")
    version("3.36.0", sha256="da0934375ab81122f4ddecb0967cb3e344fb853ff2606d616a4faaced74c3783", url="https://pypi.org/packages/27/67/1c88fb23f0863785e42afdf8bb063cb863e68f42b3239e96c12b6f930f3f/globus_sdk-3.36.0-py3-none-any.whl")
    version("3.35.0", sha256="0cf6a1b2f108de0ad4b01a091772e8f9f136793cf693fa656f582a02c2e85fa8", url="https://pypi.org/packages/0d/11/a58fdfce8ca2a47803462d068ec54ff3c71f021ee54ef2f1aa199ee2ec67/globus_sdk-3.35.0-py3-none-any.whl")
    version("3.34.0", sha256="c9b64627c9baac84c5ea8ef10a8f1abbd4db3fc34dd3ce06ecff02460c5e89ec", url="https://pypi.org/packages/e5/a7/afc2915817eae4e3b3789938d0a6f3e026e2bdaa76e88744b594067d0167/globus_sdk-3.34.0-py3-none-any.whl")
    version("3.33.0.post0", sha256="96d57f2c6d1968e7127a5fda8ea0d9d9512ec129bc384c1e027ce0f5b5a186c9", url="https://pypi.org/packages/d0/65/25004bd22cb78bae0d860290c00f2cbe9c96f2754c246a8c8850d1812773/globus_sdk-3.33.0.post0-py3-none-any.whl")
    version("3.33.0", sha256="f10402f8421dddfe591abd60b68b09e5435da2136d5a789f7c07fb094bbd7145", url="https://pypi.org/packages/bc/de/3f999057c27c11e60eb93c52fefc9027be9df92921a37b4508fbb6746d67/globus_sdk-3.33.0-py3-none-any.whl")
    version("3.32.0", sha256="ed00797c33212f56a3478f4393ddeb9cdb7fe4cc7ba05b41da0d08c625ae528b", url="https://pypi.org/packages/7d/8f/280423abf9dd78a7cf0e5ffed3ae0dc0c85be414bb261eef37c68e0f91a2/globus_sdk-3.32.0-py3-none-any.whl")
    version("3.31.0", sha256="4399e1515ea9e1284bf526a19fba53d3b0e0a397a1299dd3f473beb880448e8c", url="https://pypi.org/packages/24/9d/acbe95f5cbb174749cbcfbae951d5601b36febe4721ce1dba697a532610b/globus_sdk-3.31.0-py3-none-any.whl")
    version("3.10.1", sha256="e8073dd8db5bcd9c14d0f9dc5c543d4bfe25bfe96d6aab34a9c4961d985ed59f", url="https://pypi.org/packages/86/74/9dce30b2e12d8f26c4270667b09c5cd1ab0f3bada696ae65717893258a51/globus_sdk-3.10.1-py3-none-any.whl")
    version("3.10.0", sha256="f73d15cf88463aac9a9f77b8c4f601e11adfcbd4ecc77910a144dd251ed90551", url="https://pypi.org/packages/61/e2/a491b39a861df113d99f0ddd6e6f68aab416d6df7c9d52ed8cd98ab5389e/globus_sdk-3.10.0-py3-none-any.whl")
    version("3.9.0", sha256="a196070b549d6af534a7fa8a180eae6ab84c0745959d5ee2d3863705eef9c7fc", url="https://pypi.org/packages/a1/19/83dd4110d789eabeec942bfd39d992f037fb2875f50faf8c142dafa99b9a/globus_sdk-3.9.0-py3-none-any.whl")
    version("3.8.0", sha256="8ede91296c793eb2a1a9ec56c3660d257b31afb28bf49e402f3589df28f17afb", url="https://pypi.org/packages/af/18/8cbd7b20e660c29b79b86afaf282592ee382e3df5acaa25e588aa74bf2f5/globus_sdk-3.8.0-py3-none-any.whl")
    version("3.7.0", sha256="ba2d85b61374394a096814cbddee510b89883b68803e47e6cf4247324ea57fa6", url="https://pypi.org/packages/29/40/9041132e1b12577a79a13811f5f1da5de5c3728bf0f23c6c2ade21150894/globus_sdk-3.7.0-py3-none-any.whl")
    version("3.0.2", sha256="03b1a24fc0f9080163999bb651c8ce2a35a6c9fcdf7f57fe913978d2eed31557", url="https://pypi.org/packages/b2/bd/078c44638ae236c56c8a942de7743d0c44074933fe7426dff88f803777b0/globus_sdk-3.0.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cryptography@3.3.1:3.3,3.4.1:", when="@3.1:")
        depends_on("py-cryptography@2:3.3,3.4.1:3", when="@3.0.2:3.0")
        depends_on("py-pyjwt@2.0.0:+crypto", when="@3:")
        depends_on("py-requests@2.19.1:", when="@3.0.2:")
        depends_on("py-typing-extensions@4:", when="@3.4.1: ^python@:3.9")
        depends_on("py-typing-extensions", when="@3.3:3.4.0 ^python@:3.9")

        # marker: python_version < "3,8" and extra == "dev"
        # depends_on("py-typing-extensions", when="@3.0.0-beta3:3.0.0")
    # END DEPENDENCIES

