# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyVirtualenv(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("20.25.1", sha256="961c026ac520bac5f69acb8ea063e8a4f071bcc9457b9c1f28f6b085c511583a", url="https://pypi.org/packages/16/65/0d0bdfdac31e2db8c6d6c18fe1e00236f0dea279f9846f94a9aafa49cfc9/virtualenv-20.25.1-py3-none-any.whl")
    version("20.25.0", sha256="4238949c5ffe6876362d9c0180fc6c3a824a7b12b80604eeb8085f2ed7460de3", url="https://pypi.org/packages/83/22/54b1180756d2d6194bcafb7425d437c3034c4bff92129c3e1e633079e2c4/virtualenv-20.25.0-py3-none-any.whl")
    version("20.24.7", sha256="a18b3fd0314ca59a2e9f4b556819ed07183b3e9a3702ecfe213f593d44f7b3fd", url="https://pypi.org/packages/7f/1b/433ebb5530c48d70bebe1bf10ec7591af9f66847e34c4fcbca16d5eaaa0c/virtualenv-20.24.7-py3-none-any.whl")
    version("20.24.6", sha256="520d056652454c5098a00c0f073611ccbea4c79089331f60bf9d7ba247bb7381", url="https://pypi.org/packages/7f/19/1f0eddcb9acf00a95793ce83417f69e0fd106c192121360af499cd6fde39/virtualenv-20.24.6-py3-none-any.whl")
    version("20.24.5", sha256="b80039f280f4919c77b30f1c23294ae357c4c8701042086e3fc005963e4e537b", url="https://pypi.org/packages/4e/8b/f0d3a468c0186c603217a6656ea4f49259630e8ed99558501d92f6ff7dc3/virtualenv-20.24.5-py3-none-any.whl")
    version("20.24.4", sha256="29c70bb9b88510f6414ac3e55c8b413a1f96239b6b789ca123437d5e892190cb", url="https://pypi.org/packages/48/87/0ff871ebe003075d61e1abeab67c21d50edf44dbfdeabd107bef30a9e027/virtualenv-20.24.4-py3-none-any.whl")
    version("20.24.3", sha256="95a6e9398b4967fbcb5fef2acec5efaf9aa4972049d9ae41f95e0972a683fd02", url="https://pypi.org/packages/17/8d/6989e5dcd812520cbf9f31be2b08643ae3a895586601bbab501df8ed6e54/virtualenv-20.24.3-py3-none-any.whl")
    version("20.24.2", sha256="43a3052be36080548bdee0b42919c88072037d50d56c28bd3f853cbe92b953ff", url="https://pypi.org/packages/14/19/e266f07cf55155d5f45170bbe08c486d8a9a9ae17bc8983acb1c019a8dd4/virtualenv-20.24.2-py3-none-any.whl")
    version("20.24.1", sha256="01aacf8decd346cf9a865ae85c0cdc7f64c8caa07ff0d8b1dfc1733d10677442", url="https://pypi.org/packages/dd/af/4a7f56bb73ede17f6195aaf03353a1c1dd1381ba0aa2e3b786f7ec9fe8aa/virtualenv-20.24.1-py3-none-any.whl")
    version("20.24.0", sha256="18d1b37fc75cc2670625702d76849a91ebd383768b4e91382a8d51be3246049e", url="https://pypi.org/packages/c5/d5/f914b715f8b4c2ae8ca10112d389c04bed368ddd8888b70dafe740269bb5/virtualenv-20.24.0-py3-none-any.whl")
    version("20.22.0", sha256="48fd3b907b5149c5aab7c23d9790bea4cac6bc6b150af8635febc4cfeab1275a", url="https://pypi.org/packages/b9/dc/44f55e57b8c106391987b17fe17db0ef3cc6364a935d1691b89df0e149a7/virtualenv-20.22.0-py3-none-any.whl")
    version("20.17.1", sha256="ce3b1684d6e1a20a3e5ed36795a97dfc6af29bc3970ca8dab93e11ac6094b3c4", url="https://pypi.org/packages/18/a2/7931d40ecb02b5236a34ac53770f2f6931e3082b7a7dafe915d892d749d6/virtualenv-20.17.1-py3-none-any.whl")
    version("20.16.5", sha256="d07dfc5df5e4e0dbc92862350ad87a36ed505b978f6c39609dc489eadd5b0d27", url="https://pypi.org/packages/c1/23/9dc3c3fc959ad442397dd90cbc9ea2eca7c8a140d242c6e4222675ea9f86/virtualenv-20.16.5-py3-none-any.whl")
    version("20.16.4", sha256="035ed57acce4ac35c82c9d8802202b0e71adac011a511ff650cbcf9635006a22", url="https://pypi.org/packages/4f/8c/2f44bb00c152f24d980c91b95c0b0f38f814eb5b7a7da102467d23749ee3/virtualenv-20.16.4-py3-none-any.whl")
    version("20.16.3", sha256="4193b7bc8a6cd23e4eb251ac64f29b4398ab2c233531e66e40b19a6b7b0d30c1", url="https://pypi.org/packages/c2/d2/e80b6ad57bc0727fe0bbe7d9c496bde4ef3008e57f452ed1bfafe6618d04/virtualenv-20.16.3-py2.py3-none-any.whl")
    version("20.16.2", sha256="635b272a8e2f77cb051946f46c60a54ace3cb5e25568228bd6b57fc70eca9ff3", url="https://pypi.org/packages/f6/5e/1c73595c491b4cceffcb1aebf87eb54b9a5d48cc5226409ccf0ea96aeb91/virtualenv-20.16.2-py2.py3-none-any.whl")
    version("20.16.1", sha256="bde925b831f36053a0fa7a468ca337dee26851c9f0bfc3d72a79d534703102d2", url="https://pypi.org/packages/fb/21/6f2cac444cfafeb82868e2955191da8b780552f0f8bc846aba8f03332b66/virtualenv-20.16.1-py2.py3-none-any.whl")
    version("20.16.0", sha256="2202dbc33c4f9aaa13289d244d64f2ade8b0169e88d0213b505099b384c5ae04", url="https://pypi.org/packages/b3/73/ee968859e261c92cd1502c7197a35e42e0ccefa90c7502898a63e93631f0/virtualenv-20.16.0-py2.py3-none-any.whl")
    version("20.15.1", sha256="b30aefac647e86af6d82bfc944c556f8f1a9c90427b2fb4e3bfbf338cb82becf", url="https://pypi.org/packages/6f/43/df7c7b1b7a5ac4e41fac24c3682c1cc32f2c1d683d308bba2500338d1e3e/virtualenv-20.15.1-py2.py3-none-any.whl")
    version("20.15.0", sha256="804cce4de5b8a322f099897e308eecc8f6e2951f1a8e7e2b3598dff865f01336", url="https://pypi.org/packages/0a/d7/8f8f84aa834d9afde02055b6d11e0a0f2f35435b2ccf1a1aca4cf9046105/virtualenv-20.15.0-py2.py3-none-any.whl")
    version("20.14.1", sha256="e617f16e25b42eb4f6e74096b9c9e37713cf10bf30168fb4a739f3fa8f898a3a", url="https://pypi.org/packages/9e/34/e86fc6a8f84329b49321a532b3c1fef103c67765df957fbb3852eea39d00/virtualenv-20.14.1-py2.py3-none-any.whl")
    version("20.14.0", sha256="1e8588f35e8b42c6ec6841a13c5e88239de1e6e4e4cedfd3916b306dc826ec66", url="https://pypi.org/packages/37/71/59f8e6d2673c6137139588df2bc2c326895637c2ae43e8777c02e99e2462/virtualenv-20.14.0-py2.py3-none-any.whl")
    version("20.10.0", sha256="4b02e52a624336eece99c96e3ab7111f469c24ba226a53ec474e8e787b365814", url="https://pypi.org/packages/ac/8a/05e8d8a3ac88a3c4ebec1fe2b1b4730e6e6ebdddb52cfd6cea6803de4624/virtualenv-20.10.0-py2.py3-none-any.whl")
    version("16.7.6", sha256="3e3597e89c73df9313f5566e8fc582bd7037938d15b05329c232ec57a11a7ad5", url="https://pypi.org/packages/89/66/786e0d6f61bd0612f431e19b016d1ae46f1cb8d21a80352cc6774ec876e3/virtualenv-16.7.6-py2.py3-none-any.whl")
    version("16.4.1", sha256="dffd40d19ab0168c02cf936de59590a3c0f2c8c4a36f363fcf3dae18728dc94e", url="https://pypi.org/packages/88/b6/9f2e13a71e5a7cd458dcf4f24540a4bd39206cc6290e8393a48d8b95c11e/virtualenv-16.4.1-py2.py3-none-any.whl")
    version("16.0.0", sha256="2ce32cd126117ce2c539f0134eb89de91a8413a29baac49cbab3eb50e2026669", url="https://pypi.org/packages/b6/30/96a02b2287098b23b875bc8c2f58071c35d2efe84f747b64d523721dc2b5/virtualenv-16.0.0-py2.py3-none-any.whl")
    version("15.1.0", sha256="39d88b533b422825d644087a21e78c45cf5af0ef7a99a1fc9fbb7b481e5c85b0", url="https://pypi.org/packages/6f/86/3dc328ee7b1a6419ebfac7896d882fba83c48e3561d22ddddf38294d3e83/virtualenv-15.1.0-py2.py3-none-any.whl")
    version("15.0.1", sha256="13ce1079910a6bc60e2ce1d79813a99f30b2fd1e571427fcde1fabb0ff4c436c", url="https://pypi.org/packages/bb/83/1aa921ab8c7d017e4098582acbc422a30485f820290577b361c8fc407d53/virtualenv-15.0.1-py2.py3-none-any.whl")
    version("13.0.1", sha256="da85f7ea539cfec9437f4d87d12f95d34d92a6d30485e85a4bc434bcdff7c6c3", url="https://pypi.org/packages/3f/21/8503e2592183d552c6e47fc431b3976c7b53256b1d1c50eb1f12ada2238c/virtualenv-13.0.1-py2.py3-none-any.whl")
    version("1.11.6", sha256="a8e07085d85c637c463ae23dc0911f32c871eddef69765ff9fa26cac9f2c5053", url="https://pypi.org/packages/c6/e3/f1eaf5a62fb7df7d98f39e7f45521f562bed2b6ab405a81d678e844a4ef2/virtualenv-1.11.6-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-backports-entry-points-selectable@1.0.4:", when="@20.5:20.10")
        depends_on("py-distlib@0.3.7:", when="@20.24.2:")
        depends_on("py-distlib@0.3.6:", when="@20.16.6:20.24.1")
        depends_on("py-distlib@0.3.5:", when="@20.16.3:20.16.5")
        depends_on("py-distlib@0.3.1:", when="@20.0.26:20.16.2")
        depends_on("py-filelock@3.12.2:", when="@20.24.2:")
        depends_on("py-filelock@3.12:", when="@20.23.1:20.24.1")
        depends_on("py-filelock@3.11:", when="@20.22:20.23.0")
        depends_on("py-filelock@3.4.1:", when="@20.16.3:20.21")
        depends_on("py-filelock@3.2:", when="@20.9:20.16.2")
        depends_on("py-platformdirs@3.9.1:", when="@20.24.7:")
        depends_on("py-platformdirs@3.9.1:3", when="@20.24.2:20.24.6")
        depends_on("py-platformdirs@3.5.1:3", when="@20.23.1:20.24.1")
        depends_on("py-platformdirs@3.2:3", when="@20.22:20.23.0")
        depends_on("py-platformdirs@2.4:2", when="@20.16.3:20.18")
        depends_on("py-platformdirs@2.0.0:2", when="@20.5:20.16.2")
        depends_on("py-six@1.9:", when="@20.0.4:20.15")
    # END DEPENDENCIES

