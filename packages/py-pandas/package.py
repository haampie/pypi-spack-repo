# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPandas(PythonPackage):
    # BEGIN VERSIONS
    version("2.2.1", sha256="0ab90f87093c13f3e8fa45b48ba9f39181046e8f3317d3aadb2fffbb1b978572", url="https://pypi.org/packages/3d/59/2afa81b9fb300c90531803c0fd43ff4548074fa3e8d0f747ef63b3b5e77a/pandas-2.2.1.tar.gz")
    version("2.2.0", sha256="30b83f7c3eb217fb4d1b494a57a2fda5444f17834f5df2de6b2ffff68dc3c8e2", url="https://pypi.org/packages/03/d2/6fb05f20ee1b3961c7b283c1f8bafc6de752155d075c5db61c173de0de62/pandas-2.2.0.tar.gz")
    version("2.2.0-rc0", sha256="f864d8a5080e3f284b46eb26c7cb102a39b9bd6ac9a4d97d7a24d86fd3c0e656", url="https://pypi.org/packages/27/23/fef34c4746e5a228441c614174614714dc8aaec3646ccd53566d97a77fb8/pandas-2.2.0rc0.tar.gz")
    version("2.1.4", sha256="fcb68203c833cc735321512e13861358079a96c174a61f5116a1de89c58c0ef7", url="https://pypi.org/packages/6f/41/eb562668eaf93790762f600536b28c97b45803cba9253cd8e436cda96aef/pandas-2.1.4.tar.gz")
    version("2.1.3", sha256="22929f84bca106921917eb73c1521317ddd0a4c71b395bcf767a106e3494209f", url="https://pypi.org/packages/86/ff/662dde2193fc93b8547b073db20472b9676f944d907247a46c9c5bc45bfc/pandas-2.1.3.tar.gz")
    version("2.1.2", sha256="52897edc2774d2779fbeb6880d2cfb305daa0b1a29c16b91f531a18918a6e0f3", url="https://pypi.org/packages/3a/6e/6c9c197ec2da861ea8c9c6848f0f887b7563f16e607bc6a35506af677f30/pandas-2.1.2.tar.gz")
    version("2.1.1", sha256="fecb198dc389429be557cde50a2d46da8434a17fe37d7d41ff102e3987fd947b", url="https://pypi.org/packages/3d/0e/2c225d7a5de6ca0ec7d729aff6ef560544596f3a9bfed77f6dbc1713dbb5/pandas-2.1.1.tar.gz")
    version("2.1.0", sha256="62c24c7fc59e42b775ce0679cfa7b14a5f9bfb7643cfbe708c960699e05fb918", url="https://pypi.org/packages/6f/31/a4a8e7367856d9584d0332793edfe631182a9cca885f12dbe2dd77c10c4a/pandas-2.1.0.tar.gz")
    version("2.1.0-rc0", sha256="e6967a82ee26997ab5ef52907064ca21eed5e51089dc2131a252a26d67d88b36", url="https://pypi.org/packages/a9/ec/e531733ff7f955e58ac45089cf72d085e587a731778b9dac1b82878815e9/pandas-2.1.0rc0.tar.gz")
    version("2.0.3", sha256="c02f372a88e0d17f36d3093a644c73cfc1788e876a7c4bcb4020a77512e2043c", url="https://pypi.org/packages/b1/a7/824332581e258b5aa4f3763ecb2a797e5f9a54269044ba2e50ac19936b32/pandas-2.0.3.tar.gz")
    version("2.0.2", sha256="dd5476b6c3fe410ee95926873f377b856dbc4e81a9c605a0dc05aaccc6a7c6c6", url="https://pypi.org/packages/fb/88/d04926998a33223dbee6856970c5a7fd3cc83ded1f8782ccea8741ebd659/pandas-2.0.2.tar.gz")
    version("2.0.1", sha256="19b8e5270da32b41ebf12f0e7165efa7024492e9513fb46fb631c5022ae5709d", url="https://pypi.org/packages/6c/e0/73987b6ecc7246e02ab557240843f93fd5adf45d1355abb458aa1f2a0932/pandas-2.0.1.tar.gz")
    version("2.0.0", sha256="cda9789e61b44463c1c4fe17ef755de77bcd13b09ba31c940d20f193d63a5dc8", url="https://pypi.org/packages/9f/12/0b6bdd627b99cb10816956c1047b0733ef33b61a84e3420faf4d3202df06/pandas-2.0.0.tar.gz")
    version("1.5.3", sha256="74a3fd7e5a7ec052f183273dc7b0acd3a863edf7520f5d3a1765c04ffdb3b0b1", url="https://pypi.org/packages/74/ee/146cab1ff6d575b54ace8a6a5994048380dc94879b0125b25e62edcb9e52/pandas-1.5.3.tar.gz")
    version("1.5.2", sha256="220b98d15cee0b2cd839a6358bd1f273d0356bf964c1a1aeb32d47db0215488b", url="https://pypi.org/packages/4d/07/c4d69e1acb7723ca49d24fc60a89aa07a914dfb8e7a07fdbb9d8646630cd/pandas-1.5.2.tar.gz")
    version("1.5.1", sha256="249cec5f2a5b22096440bd85c33106b6102e0672204abd2d5c014106459804ee", url="https://pypi.org/packages/d7/4e/bc3163c2f0b2f0728c398cad15e082efaa27e40fa579a0523e98caf10fdf/pandas-1.5.1.tar.gz")
    version("1.5.0", sha256="3ee61b881d2f64dd90c356eb4a4a4de75376586cd3c9341c6c0fcaae18d52977", url="https://pypi.org/packages/2a/24/f5042daa59b91e94e6ea41edbb28d2b7e3712d0cf54a76f9ffde394efbe7/pandas-1.5.0.tar.gz")
    version("1.4.4", sha256="ab6c0d738617b675183e5f28db32b5148b694ad9bba0a40c3ea26d96b431db67", url="https://pypi.org/packages/1a/3f/bba4f9e41fff332415cdb08063b78a53c813aba1ac02887944657bb30911/pandas-1.4.4.tar.gz")
    version("1.4.3", sha256="2ff7788468e75917574f080cd4681b27e1a7bf36461fe968b49a87b5a54d007c", url="https://pypi.org/packages/f4/00/2de395c769335956b8650f990ef2a15e860be83b544c408ff95713446329/pandas-1.4.3.tar.gz")
    version("1.4.2", sha256="92bc1fc585f1463ca827b45535957815b7deb218c549b7c18402c322c7549a12", url="https://pypi.org/packages/5a/ac/b3b9aa2318de52e40c26ae7b9ce6d4e9d1bcdaf5da0899a691642117cf60/pandas-1.4.2.tar.gz")
    version("1.4.1", sha256="8db93ec98ac7cb5f8ac1420c10f5e3c43533153f253fe7fb6d891cf5aa2b80d2", url="https://pypi.org/packages/c4/eb/cfa96ba42695b3c28d4864a796d492f188471dd536df7e5e5e0c54b629a6/pandas-1.4.1.tar.gz")
    version("1.4.0", sha256="cdd76254c7f0a1583bd4e4781fb450d0ebf392e10d3f12e92c95575942e37df5", url="https://pypi.org/packages/4d/aa/e7078569d20f45e8cf6512a24bf2945698f13a7975650773c01366ea96dc/pandas-1.4.0.tar.gz")
    version("1.3.5", sha256="1e4285f5de1012de20ca46b188ccf33521bff61ba5c5ebd78b4fb28e5416a9f1", url="https://pypi.org/packages/99/f0/f99700ef327e51d291efdf4a6de29e685c4d198cbf8531541fc84d169e0e/pandas-1.3.5.tar.gz")
    version("1.3.4", sha256="a2aa18d3f0b7d538e21932f637fbfe8518d085238b429e4790a35e1e44a96ffc", url="https://pypi.org/packages/58/58/b729eda34f78060e14cb430c91d4f7ba3cf1e34797976877a3a1125ea5b2/pandas-1.3.4.tar.gz")
    version("1.3.3", sha256="272c8cb14aa9793eada6b1ebe81994616e647b5892a370c7135efb2924b701df", url="https://pypi.org/packages/71/65/3ab03ef46613e66880dba5b2c2cb5836938f0219389a11c10cfdc617e836/pandas-1.3.3.tar.gz")
    version("1.3.2", sha256="cbcb84d63867af3411fa063af3de64902665bb5b3d40b25b2059e40603594e87", url="https://pypi.org/packages/cf/f7/6c0dd488b5f5f1c0c1a48637df45046334d0be684faaf3536429f14aa9de/pandas-1.3.2.tar.gz")
    version("1.3.1", sha256="341935a594db24f3ff07d1b34d1d231786aa9adfa84b76eab10bf42907c8aed3", url="https://pypi.org/packages/12/01/360d7f444f910ae16496c07e3f003cb8c641b4ca6c033408a4469a904df3/pandas-1.3.1.tar.gz")
    version("1.3.0", sha256="c554e6c9cf2d5ea1aba5979cc837b3649539ced0e18ece186f055450c86622e2", url="https://pypi.org/packages/53/05/bf382e8bc60731906a2e7261648bcea3a6b309ad2b9952010737a1b9413e/pandas-1.3.0.tar.gz")
    version("1.2.5", sha256="14abb8ea73fce8aebbb1fb44bec809163f1c55241bcc1db91c2c780e97265033", url="https://pypi.org/packages/ab/5c/b38226740306fd73d0fea979d10ef0eda2c7956f4b59ada8675ec62edba7/pandas-1.2.5.tar.gz")
    version("1.2.4", sha256="649ecab692fade3cbfcf967ff936496b0cfba0af00a55dfaacd82bdda5cb2279", url="https://pypi.org/packages/e8/81/f7be049fe887865200a0450b137f2c574647b9154503865502cfd720ab5d/pandas-1.2.4.tar.gz")
    version("1.2.3", sha256="df6f10b85aef7a5bb25259ad651ad1cc1d6bb09000595cab47e718cbac250b1d", url="https://pypi.org/packages/8a/6f/7fcef020b5b305862cacf376183eaa0f907f2fa42f0b687b2a9a2c6cda4d/pandas-1.2.3.tar.gz")
    version("1.2.2", sha256="14ed84b463e9b84c8ff9308a79b04bf591ae3122a376ee0f62c68a1bd917a773", url="https://pypi.org/packages/78/e4/a935f1701fac697c6c5458f86968bec5d2b4cb66e7f738225216ebaa20b4/pandas-1.2.2.tar.gz")
    version("1.2.1", sha256="5527c5475d955c0bc9689c56865aaa2a7b13c504d6c44f0aadbf57b565af5ebd", url="https://pypi.org/packages/11/1c/b0bc154996617eae877ff267fcf84e55e6c6808dbade0da206f0419dd483/pandas-1.2.1.tar.gz")
    version("1.2.0", sha256="e03386615b970b8b41da6a68afe717626741bb2431cec993640685614c0680e4", url="https://pypi.org/packages/75/bc/abf2e8cc6a9d918008774b958613cfdbd3a8c135cffb0757f78fabd8268f/pandas-1.2.0.tar.gz")
    version("1.1.5", sha256="f10fc41ee3c75a474d3bdf68d396f10782d013d7f67db99c0efbfd0acb99701b", url="https://pypi.org/packages/fb/e4/828bb9c2474ff6016e5ce96a78220d485436d5468c23068f4f6c2eb9cff8/pandas-1.1.5.tar.gz")
    version("1.1.4", sha256="a979d0404b135c63954dea79e6246c45dd45371a88631cdbb4877d844e6de3b6", url="https://pypi.org/packages/09/39/fb93ed98962d032963418cd1ea5927b9e11c4c80cb1e0b45dea769d8f9a5/pandas-1.1.4.tar.gz")
    version("1.1.3", sha256="babbeda2f83b0686c9ad38d93b10516e68cdcd5771007eb80a763e98aaf44613", url="https://pypi.org/packages/1b/e5/552ba65835ab43e12b299458fea94ee23886125b8b8aabc91edb03f2ba65/pandas-1.1.3.tar.gz")
    version("1.1.2", sha256="b64ffd87a2cfd31b40acd4b92cb72ea9a52a48165aec4c140e78fd69c45d1444", url="https://pypi.org/packages/64/f1/8fdbd74edfc31625d597717be8c155c6226fc72a7c954c52583ab81a8614/pandas-1.1.2.tar.gz")
    version("1.1.1", sha256="53328284a7bb046e2e885fd1b8c078bd896d7fc4575b915d4936f54984a2ba67", url="https://pypi.org/packages/b1/1f/afb5cad013e8888053f6524849cc3df4bb83dfcab59485f10bf50016d4f8/pandas-1.1.1.tar.gz")
    version("1.1.0", sha256="b39508562ad0bb3f384b0db24da7d68a2608b9ddc85b1d931ccaaa92d5e45273", url="https://pypi.org/packages/6f/29/32ff85413724ffa7cc8d52373f93c2ef1cb197ffd0c7b1b10d36452dd0ca/pandas-1.1.0.tar.gz")
    version("1.0.5", sha256="69c5d920a0b2a9838e677f78f4dde506b95ea8e4d30da25859db6469ded84fa8", url="https://pypi.org/packages/31/29/ede692aa6547dfc1f07a4d69e8411b35225218bcfbe9787e78b67a35d103/pandas-1.0.5.tar.gz")
    version("1.0.4", sha256="b35d625282baa7b51e82e52622c300a1ca9f786711b2af7cbe64f1e6831f4126", url="https://pypi.org/packages/53/87/6438c197fc70ca6b3056cfb60b3dfedca25bedb631bce1f72d6a10502d15/pandas-1.0.4.tar.gz")
    version("1.0.3", sha256="32f42e322fb903d0e189a4c10b75ba70d90958cc4f66a1781ed027f1a1d14586", url="https://pypi.org/packages/2f/79/f236ab1cfde94bac03d7b58f3f2ab0b1cc71d6a8bda3b25ce370a9fe4ab1/pandas-1.0.3.tar.gz")
    version("1.0.2", sha256="76334ba36aa42f93b6b47b79cbc32187d3a178a4ab1c3a478c8f4198bcd93a73", url="https://pypi.org/packages/d2/08/61e6f33ef99999893f7840b368b06ddd6be11d1a2d5354667fed5f41c1e0/pandas-1.0.2.tar.gz")
    version("1.0.1", sha256="3c07765308f091d81b6735d4f2242bb43c332cc3461cae60543df6b10967fe27", url="https://pypi.org/packages/02/c3/e8c56de02d6c52f8541feca2fd77117e8ae4956f7b3e5cdbed726624039b/pandas-1.0.1.tar.gz")
    version("1.0.0", sha256="3ea6cc86931f57f18b1240572216f09922d91b19ab8a01cf24734394a3db3bec", url="https://pypi.org/packages/26/c4/b3cd1c8928a496e27a8604160a4b6c672bda76cc215130848f68f01e0213/pandas-1.0.0.tar.gz")
    version("0.25.3", sha256="52da74df8a9c9a103af0a72c9d5fdc8e0183a90884278db7f386b5692a2220a4", url="https://pypi.org/packages/b7/93/b544dd08092b457d88e10fc1e0989d9397fd32ca936fdfcbb2584178dd2b/pandas-0.25.3.tar.gz")
    version("0.25.2", sha256="ca91a19d1f0a280874a24dca44aadce42da7f3a7edb7e9ab7c7baad8febee2be", url="https://pypi.org/packages/42/cb/e3b69df7d3e6095a5e86fbe930e57f3f0a440fb73f350ab253efe2c7b924/pandas-0.25.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("excel", default=False)
    variant("performance", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@2.1:")
        depends_on("py-bottleneck@1.3.6:", when="@2.2:+performance")
        depends_on("py-bottleneck@1.3.4:", when="@2.1+performance")
        depends_on("py-numba@0.56.4:", when="@2.2:+performance")
        depends_on("py-numba@0.55.2:", when="@2.1+performance")
        depends_on("py-numexpr@2.8.4:", when="@2.2:+performance")
        depends_on("py-numexpr@2.8:", when="@2.1+performance")
        depends_on("py-numpy@1.26.0:1", when="@2.1.2:2.1,2.2.0: ^python@3.12:")
        depends_on("py-numpy@1.22.4:1", when="@2.1.2:2.1,2.2.0: ^python@:3.10")
        depends_on("py-numpy@1.23.2:1", when="@2.1.2:2.1,2.2.0: ^python@3.11:3.11.0")
        depends_on("py-numpy@1.26.0:", when="@2.1.1,2.2:2.2.0-rc0 ^python@3.12:")
        depends_on("py-numpy@1.23.2:", when="@2.1.1,2.2:2.2.0-rc0 ^python@3.11:3.11.0")
        depends_on("py-numpy@1.22.4:", when="@2.1:2.1.1,2.2:2.2.0-rc0 ^python@:3.10")
        depends_on("py-numpy@1.23.2:", when="@2.1:2.1.0 ^python@3.11:")
        depends_on("py-numpy@1.13.3:", when="@0.25:1.0")
        depends_on("py-odfpy@1.4.1:", when="@2.1:+excel")
        depends_on("py-openpyxl@3.1:", when="@2.2:+excel")
        depends_on("py-openpyxl@3.0.10:", when="@2.1+excel")
        depends_on("py-python-calamine@0.1.7:", when="@2.2:+excel")
        depends_on("py-python-dateutil@2.8.2:", when="@2.1:")
        depends_on("py-python-dateutil@2.6.1:", when="@0.25:1.0")
        depends_on("py-pytz@2020:", when="@2.1:")
        depends_on("py-pytz@2017:", when="@0.25:1.1.0-rc0")
        depends_on("py-pyxlsb@1.0.10:", when="@2.2:+excel")
        depends_on("py-pyxlsb@1.0.9:", when="@2.1+excel")
        depends_on("py-tzdata@2022.7:", when="@2.2:")
        depends_on("py-tzdata@2022:", when="@2.1")
        depends_on("py-xlrd@2.0.1:", when="@2.1:+excel")
        depends_on("py-xlsxwriter@3.0.5:", when="@2.2:+excel")
        depends_on("py-xlsxwriter@3.0.3:", when="@2.1+excel")
    # END DEPENDENCIES

