# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJupyterServer(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.13.0", sha256="77b2b49c3831fbbfbdb5048cef4350d12946191f833a24e5f83e5f8f4803e97b", url="https://pypi.org/packages/95/85/483b8e09a897d1bc2194646d30d4ce6ae166106e91ecbd11d6b6d9ccfc36/jupyter_server-2.13.0-py3-none-any.whl")
    version("2.12.5", sha256="184a0f82809a8522777cfb6b760ab6f4b1bb398664c5860a27cec696cb884923", url="https://pypi.org/packages/25/d6/6ee093c967d11144aeb1b0b4952d30e51da8eb2737837ab612084c783a58/jupyter_server-2.12.5-py3-none-any.whl")
    version("2.12.4", sha256="a125ae18a60de568f78f55c84dd58759901a18ef279abf0418ac220653ca1320", url="https://pypi.org/packages/f9/12/92ddd4af39e6c994722f6a016602647dbab74c3a2ff661b257e44f3ce27d/jupyter_server-2.12.4-py3-none-any.whl")
    version("2.12.3", sha256="6f85310ea5e6068568a521f079fba99d8d17e4884dd1d602ab0f43b3115204a8", url="https://pypi.org/packages/3d/02/48d2c610c3485069ea0ce4b6b255486483bb89ac4d46a72bb6baedbcb596/jupyter_server-2.12.3-py3-none-any.whl")
    version("2.12.2", sha256="abcfa33f98a959f908c8733aa2d9fa0101d26941cbd49b148f4cef4d3046fc61", url="https://pypi.org/packages/0c/3b/24a511c81b580a038aca06c91fc89df0464815903044bae1c85145cdf03c/jupyter_server-2.12.2-py3-none-any.whl")
    version("2.12.1", sha256="fd030dd7be1ca572e4598203f718df6630c12bd28a599d7f1791c4d7938e1010", url="https://pypi.org/packages/ed/20/2437a3865083360103b0218e82a910c4c35f3bf7248c5cdae6934ba4d01c/jupyter_server-2.12.1-py3-none-any.whl")
    version("2.12.0", sha256="3482912efa4387bb1edc23ba60531796aff3b6d6a6e93a5810f5719e2bdb48b7", url="https://pypi.org/packages/09/58/bac23f86dc66ea469c6eb8c953a7aea3a2c807f5988c43d2c5dccb106bd7/jupyter_server-2.12.0-py3-none-any.whl")
    version("2.11.2", sha256="0c548151b54bcb516ca466ec628f7f021545be137d01b5467877e87f6fff4374", url="https://pypi.org/packages/8c/57/bdbc3e5b5f796b599bb45f82ba11eec014bdf07946cbc0caaa10d991fd28/jupyter_server-2.11.2-py3-none-any.whl")
    version("2.11.1", sha256="4b3a16e3ed16fd202588890f10b8ca589bd3e29405d128beb95935f059441373", url="https://pypi.org/packages/3b/c8/2f997f763abafbed76fdb2534aa150939f2882f0ea88cd084a8b8a8f0e4d/jupyter_server-2.11.1-py3-none-any.whl")
    version("2.11.0", sha256="c9bd6e6d71dc5a2a25df167dc323422997f14682b008bfecb5d7920a55020ea7", url="https://pypi.org/packages/6e/79/178c7a551d50734a779b1fb7688089e46c6141d8b108b2c9cbb028c27437/jupyter_server-2.11.0-py3-none-any.whl")
    version("2.6.0", sha256="19525a1515b5999618a91b3e99ec9f6869aa8c5ba73e0b6279fcda918b54ba36", url="https://pypi.org/packages/6f/04/b2e87b4ee96a2219df7666706b28c9ebffd9895fc98fe4b5c56b8b6931ce/jupyter_server-2.6.0-py3-none-any.whl")
    version("1.24.0", sha256="c88ddbe862966ea1aea8c3ccb89a5903abd8fbcfe5cd14090ef549d403332c37", url="https://pypi.org/packages/5b/ce/142bcb35ffe215d8880e968689ab733bd7976a6c20dae24b6782cce2219a/jupyter_server-1.24.0-py3-none-any.whl")
    version("1.23.6", sha256="ede3a5c09b075541d960bb02854b617c0ffa58706c37de92e2d1c5acdc359c20", url="https://pypi.org/packages/1d/c4/2c22ebce27b5b51b19c09fd99a027eefb2bf72184afea58e7ccfbfd46166/jupyter_server-1.23.6-py3-none-any.whl")
    version("1.23.5", sha256="d42e520af98af9fbb7f0fb0d069991054d88e4d2ee051eb7110aef35f3756cef", url="https://pypi.org/packages/77/d0/41f8ac982b49456fe93bd0b00efb49c2df1ac2bada8c92c3d4e702f80477/jupyter_server-1.23.5-py3-none-any.whl")
    version("1.23.4", sha256="aa3398aeb5249d470ea53abcf81fca8a6876bb9dbdc652822e5bbbb0574a6e83", url="https://pypi.org/packages/af/f9/1bfd4c40903b0ac671781c9d85698fcb77404b41e5a432dbe590c710daaf/jupyter_server-1.23.4-py3-none-any.whl")
    version("1.23.3", sha256="438496cac509709cc85e60172e5538ca45b4c8a0862bb97cd73e49f2ace419cb", url="https://pypi.org/packages/2e/5e/70394c2d1b17b7c93308fcb6e9f9b27ac6812f2e88dff081a4773b3559b3/jupyter_server-1.23.3-py3-none-any.whl")
    version("1.23.2", sha256="c01d0e84c22a14dd6b0e7d8ce4105b08a3426b46582668e28046a64c07311a4f", url="https://pypi.org/packages/ed/a5/4d8db973e07b8ccf4fda0c1e116a39588a1495d30ae694e802fcb5d8e7f2/jupyter_server-1.23.2-py3-none-any.whl")
    version("1.23.1", sha256="4bdcde2aa576b05da5cf89f33b7d97adcaea5cad4f5863a0db09dcc9eecd66bf", url="https://pypi.org/packages/2a/3a/09dc05bd5b3a4ccbc406a0031cd7c8210149d4eb24a0e9ab9127f13cb580/jupyter_server-1.23.1-py3-none-any.whl")
    version("1.23.0", sha256="0adbb94fc41bc5d7217a17c51003fea7d0defb87d8a6aff4b95fa45fa029e129", url="https://pypi.org/packages/f0/e6/db3d6a52475296a3acafd657be7f2e995b1e7d90b280e822d7028519552d/jupyter_server-1.23.0-py3-none-any.whl")
    version("1.21.0", sha256="992531008544d77e05a16251cdfbd0bdff1b1efa14760c79b9cc776ac9214cf1", url="https://pypi.org/packages/0a/87/13dda7b92c48931b9fc006801edc3590b72502ffd95ccc6397c0a64edb91/jupyter_server-1.21.0-py3-none-any.whl")
    version("1.19.1", sha256="ea3587840f2a906883c9eecb6bc85ef87ba1b7ba4cb6eafbacfac4a568862106", url="https://pypi.org/packages/9e/e7/acb4e261277e0d6a366943075a92b6c19953901fc3a55fa97b668e00bfbc/jupyter_server-1.19.1-py3-none-any.whl")
    version("1.18.1", sha256="022759b09c96a4e2feb95de59ce4283e04e17782efe197b91d23a47521609b77", url="https://pypi.org/packages/36/6c/fe8c416a9f1a64b9296918e9096b68da81fc50e5fefba8077841c22d6691/jupyter_server-1.18.1-py3-none-any.whl")
    version("1.17.0", sha256="5aa5e0945e3dbf29390cfe9c418a9af245d812ce282932ae97d0671e10c147a0", url="https://pypi.org/packages/24/93/bf76a457fbe3adc4000c039013e6d1715ae2972eb3f341bb50a1712f8105/jupyter_server-1.17.0-py3-none-any.whl")
    version("1.13.5", sha256="a3eb9d397df2de26134cb24fe7cb5da60ec28b4f8b292e0bdefd450b1f062dd3", url="https://pypi.org/packages/02/8b/f7ad0a54cdd07b819dc768eb39cf5f09f522b48ff1d5171551358fffd497/jupyter_server-1.13.5-py3-none-any.whl")
    version("1.11.2", sha256="eb247b555f5bdfb4a219d78e86bc8769456a1a712d8e30a4dbe06e3fe7e8a278", url="https://pypi.org/packages/42/72/692f8b573af200fad3f5020ec485e41baa28eeb3446bc58307651f40df0f/jupyter_server-1.11.2-py3-none-any.whl")
    version("1.11.1", sha256="618aba127b1ff35f50e274b6055dfeff006a6008e94d4e9511c251a2d99131e5", url="https://pypi.org/packages/c2/5d/38eacdd6a5d250a64458b55044a873ac25c0f1cc85a3ed0401a8384d31fe/jupyter_server-1.11.1-py3-none-any.whl")
    version("1.11.0", sha256="827c134da7a9e09136c2dc2fd16743350970105247f085abfc6ce0432d0c979e", url="https://pypi.org/packages/99/1b/6cb192774cac40926f71069073d187e727c3bbc276d2a310ca352755455e/jupyter_server-1.11.0-py3-none-any.whl")
    version("1.10.2", sha256="491c920013144a2d6f5286ab4038df6a081b32352c9c8b928ec8af17eb2a5e10", url="https://pypi.org/packages/b0/3b/fc133648ef2f296e87ea13dd4709b0ac057fe9abb34c6e9e13731953f25f/jupyter_server-1.10.2-py3-none-any.whl")
    version("1.9.0", sha256="1a6bfcf4cd58a84dfe9d3060a76bf98428c08b8a177202fc0cadcec5f7d74090", url="https://pypi.org/packages/29/b7/7377d007118f7798b21362a6c0a0bf20c93cdc19345105276a862e1263d6/jupyter_server-1.9.0-py3-none-any.whl")
    version("1.6.1", sha256="ce7609d75c624d2e6b6eb9159ef019a0320cc55c3b77795ee295c3eb72a08425", url="https://pypi.org/packages/c8/12/05d6ec3576611696acc736dc80f0254f5b98cc19a38449a09f05b5517b52/jupyter_server-1.6.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("typescript", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-anyio@3.1:", when="@1.15:1.16,2.2.1:")
        depends_on("py-anyio@3.1:3", when="@1.8:1.13,1.17:2.2.0")
        depends_on("py-anyio@2.0.2:", when="@1.1:1.6.2")
        depends_on("py-argon2-cffi", when="@1.5:")
        depends_on("py-ipykernel", when="@:1.0.0-rc0")
        depends_on("py-ipython-genutils", when="@:1.15.2")
        depends_on("py-jinja2")
        depends_on("py-jupyter-client@7.4.4:", when="@2.0.0-rc4:")
        depends_on("py-jupyter-client@6.1.12:", when="@1.16:2.0.0-rc3")
        depends_on("py-jupyter-client@6.1.1:", when="@0.3:1.15")
        depends_on("py-jupyter-core@4.12:4,5.1:", when="@1.23.5:1,2.0.1:")
        depends_on("py-jupyter-core@4.7.0:", when="@1.16:1.23.4,2:2.0.0-rc3")
        depends_on("py-jupyter-core@4.6:", when="@1.7.0-alpha2:1.15")
        depends_on("py-jupyter-core@4.4:", when="@:1.7.0-alpha1")
        depends_on("py-jupyter-events@0.9:", when="@2.10.1:")
        depends_on("py-jupyter-events@0.6:", when="@2.6:2.10.0")
        depends_on("py-jupyter-server-terminals", when="@2:")
        depends_on("py-nbconvert@6.4.4:", when="@1.16:")
        depends_on("py-nbconvert", when="@:0.1,0.3:1.15")
        depends_on("py-nbformat@5.3.0:", when="@2.0.0-rc8:")
        depends_on("py-nbformat@5.2:", when="@1.15:2.0.0-rc7")
        depends_on("py-nbformat", when="@:1.13")
        depends_on("py-overrides", when="@2.6:")
        depends_on("py-packaging", when="@1.13.2:")
        depends_on("py-prometheus-client")
        depends_on("py-pywin32", when="@0.2:1.7.0-alpha2 platform=windows")
        depends_on("py-pyzmq@24:", when="@2.0.0-rc4:")
        depends_on("py-pyzmq@17.0.0:", when="@:2.0.0-rc3")
        depends_on("py-requests-unixsocket", when="@1.9:1.11.1")
        depends_on("py-send2trash@1.8.2:", when="@2.7.1:")
        depends_on("py-send2trash", when="@:2.7.0")
        depends_on("py-terminado@0.8.3:", when="@0.3:")
        depends_on("py-tornado@6.2:", when="@2.0.0-rc4:")
        depends_on("py-tornado@6.1:", when="@1.0.9:2.0.0-rc3")
        depends_on("py-traitlets@5.6:", when="@2.0.1:")
        depends_on("py-traitlets@5.1:", when="@1.16:2.0.0-rc4")
        depends_on("py-traitlets@5.0.0:", when="@1.13.3:1.15")
        depends_on("py-traitlets@4.2.1:", when="@:1.13.2")
        depends_on("py-websocket-client", when="@1.7:")

        # marker: os_name == "nt"
        # depends_on("py-pywinpty", when="@1.15:")
        # depends_on("py-pywinpty@:1", when="@1.13.5:1.13")
    # END DEPENDENCIES

