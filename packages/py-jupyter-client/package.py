# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJupyterClient(PythonPackage):
    # BEGIN VERSIONS
    version("8.6.1", sha256="3b7bd22f058434e3b9a7ea4b1500ed47de2713872288c0d511d19926f99b459f", url="https://pypi.org/packages/75/6d/d7b55b9c1ac802ab066b3e5015e90faab1fffbbd67a2af498ffc6cc81c97/jupyter_client-8.6.1-py3-none-any.whl")
    version("8.6.0", sha256="909c474dbe62582ae62b758bca86d6518c85234bdee2d908c778db6d72f39d99", url="https://pypi.org/packages/43/ae/5f4f72980765e2e5e02b260f9c53bcc706cefa7ac9c8d7240225c55788d4/jupyter_client-8.6.0-py3-none-any.whl")
    version("8.5.0", sha256="c3877aac7257ec68d79b5c622ce986bd2a992ca42f6ddc9b4dd1da50e89f7028", url="https://pypi.org/packages/ab/1f/d93fd1d2bf75233134a4aa1f56186b3c1975932fbfb58322e8de2906ea3d/jupyter_client-8.5.0-py3-none-any.whl")
    version("8.4.0", sha256="6a2a950ec23a8f62f9e4c66acec7f0ea6c7d1f80ba0992e747b10c56ce2e6dbe", url="https://pypi.org/packages/dc/05/e91a1a935a25ca1b46c78260def39125b2cfca96c2adbc285d365af23e3f/jupyter_client-8.4.0-py3-none-any.whl")
    version("8.3.1", sha256="5eb9f55eb0650e81de6b7e34308d8b92d04fe4ec41cd8193a913979e33d8e1a5", url="https://pypi.org/packages/73/d4/3c13d6a300be9e894561aea0b81e7aed46e8f98029b7d9369d90b1fc7ac5/jupyter_client-8.3.1-py3-none-any.whl")
    version("8.3.0", sha256="7441af0c0672edc5d28035e92ba5e32fadcfa8a4e608a434c228836a89df6158", url="https://pypi.org/packages/29/24/0491f7837cedf39ae0f96d9b3e4db2fae31cc4dd5eac00a98ab0db996c9b/jupyter_client-8.3.0-py3-none-any.whl")
    version("8.2.0", sha256="b18219aa695d39e2ad570533e0d71fb7881d35a873051054a84ee2a17c4b7389", url="https://pypi.org/packages/07/37/4019d2c41ca333c08dfdfeb84c0fc0368c8defbbd3c8f0c9a530851e5813/jupyter_client-8.2.0-py3-none-any.whl")
    version("8.1.0", sha256="d5b8e739d7816944be50f81121a109788a3d92732ecf1ad1e4dadebc948818fe", url="https://pypi.org/packages/31/6c/96771d6b3ce94da927f7688be821899f169306f16023dd0af5ef55f71a52/jupyter_client-8.1.0-py3-none-any.whl")
    version("8.0.3", sha256="be48ac6bd659cbbddb7a674cf06b3b8afbf53f228253cf58bde604c03bd487b0", url="https://pypi.org/packages/78/11/562517956f801607c4f7855ebf8c545e9a9f62ef936f0da1bdec9cd1a7aa/jupyter_client-8.0.3-py3-none-any.whl")
    version("8.0.2", sha256="c53731eb590b68839b0ce04bf46ff8c4f03278f5d9fe5c3b0f268a57cc2bd97e", url="https://pypi.org/packages/1f/f6/2b63e6021171dc90517681537358313a58855d3bfbaafc7861d99134f959/jupyter_client-8.0.2-py3-none-any.whl")
    version("7.4.9", sha256="214668aaea208195f4c13d28eb272ba79f945fc0cf3f11c7092c20b2ca1980e7", url="https://pypi.org/packages/fd/a7/ef3b7c8b9d6730a21febdd0809084e4cea6d2a7e43892436adecdd0acbd4/jupyter_client-7.4.9-py3-none-any.whl")
    version("7.4.8", sha256="d4a67ae86ee014bcb96bd8190714f6af921f2b0f52f4208b086aa5acfd9f8d65", url="https://pypi.org/packages/00/e4/d6b3f0e3c00caf230ce117a096e057b536748747b1cfc74ec3d14c366a5b/jupyter_client-7.4.8-py3-none-any.whl")
    version("7.4.7", sha256="df56ae23b8e1da1b66f89dee1368e948b24a7f780fa822c5735187589fc4c157", url="https://pypi.org/packages/4b/b4/df6186d9d1c7e8d943febb8e1a17aedc031ab374924fd19193f9efb0fbb2/jupyter_client-7.4.7-py3-none-any.whl")
    version("7.4.6", sha256="540b6a5c9c2dc481c5dd54fd5acb260f03dfaaa7c5325b2ffb1f676710f8c7c4", url="https://pypi.org/packages/1b/8e/cea6d897f18b1c95ea63cde0717a4945fc95ea209e831d4ca406b45d3dba/jupyter_client-7.4.6-py3-none-any.whl")
    version("7.4.5", sha256="feaad9c04871254067d3b8c41192b7aba8e9bbbf9df9830ecf2673939510c5b7", url="https://pypi.org/packages/7c/2c/9a15fa5ea373c05a8deea126bac17043f33186e28db38a72291724f21b05/jupyter_client-7.4.5-py3-none-any.whl")
    version("7.4.4", sha256="1c1d418ef32a45a1fae0b243e6f01cc9bf65fa8ddbd491a034b9ba6ac6502951", url="https://pypi.org/packages/7b/31/2d74aee388c124b5b833f99817bf4b57784ea1b1a828a342c052c48a4f64/jupyter_client-7.4.4-py3-none-any.whl")
    version("7.4.3", sha256="8845e3f5a339734b1ecc21d2100638aa1c7a145e356a31845f155cda5b624b1c", url="https://pypi.org/packages/ce/fb/745c1bd05c748bcac98c7e7a013ed95b09927e14b2ca1da7a32cd6ededdb/jupyter_client-7.4.3-py3-none-any.whl")
    version("7.4.2", sha256="f8929321204d3f0b446401cfadc04ed8226e77002a9e379416df8c252607f695", url="https://pypi.org/packages/44/2a/e811114993bae45059fcf8242439b562bba8dfe6a92284cdccf2fde00d05/jupyter_client-7.4.2-py3-none-any.whl")
    version("7.4.1", sha256="bbf6404ef64afff3d4f583c90c6335545959657b7dec3a86c440d7b1368407ea", url="https://pypi.org/packages/3f/be/24df88324de68a80143b35cd11a6577bb2ba6b759057119a81e0a995a5c2/jupyter_client-7.4.1-py3-none-any.whl")
    version("7.4.0", sha256="b26e3e47df5b9fbc72cb0838c6cf378bbfdfb85a13983f742eae97188493cc20", url="https://pypi.org/packages/19/a4/af508f91ed5519f04d8f9ae21c299b60a7288f209933319cc4b89a89bb63/jupyter_client-7.4.0-py3-none-any.whl")
    version("7.3.5", sha256="b33222bdc9dd1714228bd286af006533a0abe2bbc093e8f3d29dc0b91bdc2be4", url="https://pypi.org/packages/35/af/66f66acacf1b22b1400cd46e1ac83810509511e7c75afbfbdd9155367a99/jupyter_client-7.3.5-py3-none-any.whl")
    version("7.1.2", sha256="d56f1c57bef42ff31e61b1185d3348a5b2bcde7c9a05523ae4dbe5ee0871797c", url="https://pypi.org/packages/56/a7/f4d3790ce7bb925d3ffe299244501a264f23ee7ec401914f7d788881ea31/jupyter_client-7.1.2-py3-none-any.whl")
    version("7.0.6", sha256="074bdeb1ffaef4a3095468ee16313938cfdc48fc65ca95cc18980b956c2e5d79", url="https://pypi.org/packages/3c/51/06efe08a819c36215e02750b50ac1e5e322303a8369ec1bc4e915d485ad4/jupyter_client-7.0.6-py3-none-any.whl")
    version("6.2.0", sha256="9715152067e3f7ea3b56f341c9a0f9715c8c7cc316ee0eb13c3c84f5ca0065f5", url="https://pypi.org/packages/88/4e/50fcf8b38d9c08d5b4839c1650e595f6bfa4fc9b419e2b800db8f14ee532/jupyter_client-6.2.0-py3-none-any.whl")
    version("6.1.13", sha256="1df17b0525b45cc03645fc9eeab023765882d3c18fb100f82499cf6a353b3941", url="https://pypi.org/packages/50/d0/9a6cef4d6471e482fbf8943242ddbe559d1f99761e85983c07d623f7b70c/jupyter_client-6.1.13-py3-none-any.whl")
    version("6.1.12", sha256="e053a2c44b6fa597feebe2b3ecb5eea3e03d1d91cc94351a52931ee1426aecfc", url="https://pypi.org/packages/77/e8/c3cf72a32a697256608d5fa96360c431adec6e1c6709ba7f13f99ff5ee04/jupyter_client-6.1.12-py3-none-any.whl")
    version("6.1.11", sha256="5eaaa41df449167ebba5e1cf6ca9b31f7fd4f71625069836e2e4fee07fe3cb13", url="https://pypi.org/packages/83/d6/30aed7ef13ff3f359e99626c1b0a32ebbc3bf9b9d5616ec46e9e245d5fa9/jupyter_client-6.1.11-py3-none-any.whl")
    version("6.1.10", sha256="2cd2f201d0b237a61bbbf2e772c12b9971e095eb283244a8dfd7148b8d8152a9", url="https://pypi.org/packages/99/a6/1d31bea9938db05a90cc7ab14159e89b49e4caec06e8e1d6f2ef27598262/jupyter_client-6.1.10-py3-none-any.whl")
    version("6.1.9", sha256="35123881e7c2f65fe3d05bcee972a50694f2931b4b7816781851987cbc36d6aa", url="https://pypi.org/packages/e4/47/34ebbe78517fbb464eed122c7f754e154e050d17c8493981dffcba84ac37/jupyter_client-6.1.9-py3-none-any.whl")
    version("6.1.8", sha256="d51ce4eb0d3c86a1139db3ce8273a7d91ebc2eb13fea350759b6a4884f24dc05", url="https://pypi.org/packages/0b/5d/ffb8e35d802c0cf91c195c46a02d95c063b6aec5202086ddce98050049f7/jupyter_client-6.1.8-py3-none-any.whl")
    version("6.1.7", sha256="c958d24d6eacb975c1acebb68ac9077da61b5f5c040f22f6849928ad7393b950", url="https://pypi.org/packages/dc/41/9fa443d5ae8907dd8f7d12146cb0092dc053afd67b5b57e7e8786a328547/jupyter_client-6.1.7-py3-none-any.whl")
    version("6.1.6", sha256="7ad9aa91505786420d77edc5f9fb170d51050c007338ba8d196f603223fd3b3a", url="https://pypi.org/packages/48/2e/6d48ae4ef0c9aa1383b3186349472a01bb38dacb2162a4a4370525d3f2a4/jupyter_client-6.1.6-py3-none-any.whl")
    version("6.1.5", sha256="9f0092a0951d878e7521924899e1fba6f689c7a99d43735a4c0bc05c6f311452", url="https://pypi.org/packages/93/4b/26eabcf24b3e7cfdf063858609af45eecea245cf64d82e2fc88d2ef57857/jupyter_client-6.1.5-py3-none-any.whl")
    version("5.3.4", sha256="d0c077c9aaa4432ad485e7733e4d91e48f87b4f4bab7d283d42bb24cbbba0a0f", url="https://pypi.org/packages/13/81/fe0eee1bcf949851a120254b1f530ae1e01bdde2d3ab9710c6ff81525061/jupyter_client-5.3.4-py2.py3-none-any.whl")
    version("5.2.4", sha256="c44411eb1463ed77548bc2d5ec0d744c9b81c4a542d9637c7a52824e2121b987", url="https://pypi.org/packages/3b/c3/3043fe9ffd140d03c9d091a056794ccdc427c56ec19b8eea74f9ea0a498f/jupyter_client-5.2.4-py2.py3-none-any.whl")
    version("4.4.0", sha256="8bb42fb013f3a70367ae4a8854d2cf90df6ba4c333731a98a717d9a4a10a01a5", url="https://pypi.org/packages/a7/a1/29d2284986596be9023ad6b6fe1de989318fb1526e7ec99a43519d69d709/jupyter_client-4.4.0-py2.py3-none-any.whl")
    version("4.3.0", sha256="e1450feb58aca6a9837a572d432735c54884e31de2ff477af7035238058be269", url="https://pypi.org/packages/bb/b0/6f33f2e88343a8fb04289de186320b1ddb165f1a646af41b07be14f78379/jupyter_client-4.3.0-py2.py3-none-any.whl")
    version("4.2.2", sha256="278d5870a0d2350b1fb7495fd70a86d90543c10eb0e5d3b7636e453f1347d4a6", url="https://pypi.org/packages/fd/7a/07ad70876fa3e6906440ff8bbecbb24d958d3547ca350544ac70fe2221bf/jupyter_client-4.2.2-py2.py3-none-any.whl")
    version("4.2.1", sha256="4596380adfa76d583cfa376ae21990b938443e938f8ec8b24adbea20a55efc04", url="https://pypi.org/packages/cc/c8/ab3b82f3436bef22b4e6a5bde26fce2d038362607ac0d0c4999bfa05a3cd/jupyter_client-4.2.1-py2.py3-none-any.whl")
    version("4.2.0", sha256="2cb24e9e760a7d512d57193d9740dee9f25bbc1502ac5f43251134988577eca7", url="https://pypi.org/packages/c3/4d/6431e0fbb301f8f6ebf52f4a4f5bb4cbf9f64d64e2e2c16c305b95b17e25/jupyter_client-4.2.0-py2.py3-none-any.whl")
    version("4.1.1", sha256="c1290dadbd215e12ef72b8350155538dd59dc462fe37d46d2a31be9359d5c31d", url="https://pypi.org/packages/b0/d5/418205a8c83cd34dc1e83b852936a6fe02e4ba3bdc420dc12a0a0ca7c3d8/jupyter_client-4.1.1-py2.py3-none-any.whl")
    version("4.1.0", sha256="969d01e95a8b092302901f936fc8b4c16e59197ab1825bd12aaaad1f88638d54", url="https://pypi.org/packages/ff/3f/9dbbe6fc01be4ac5b63b8becdda2408663492305763fd999a1616399e760/jupyter_client-4.1.0.zip")
    version("4.0.0", sha256="ca9e4bf694953a009e6dc7fd40300547f43abd846c70a995da74d19cbd013309", url="https://pypi.org/packages/39/bc/3679bee00a2958230a42e5d6b31bbea178119a7f167e233fdec67ebef3b2/jupyter_client-4.0.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-entrypoints", when="@7.0.0-alpha1:8.0.0-alpha2")
        depends_on("py-importlib-metadata@4.8.3:", when="@8.0.0-alpha3: ^python@:3.9")
        depends_on("py-jedi@:0.17", when="@6.1.9:6.1.10")
        depends_on("py-jupyter-core@4.12:4,5.1:", when="@8.0.0-beta2:")
        depends_on("py-jupyter-core@4.9.2:", when="@7.2:8.0.0-alpha4")
        depends_on("py-jupyter-core@4.6:", when="@5.3.4:7.1")
        depends_on("py-jupyter-core", when="@4.2:5.3.3")
        depends_on("py-nest-asyncio@1.5.4:", when="@7.2.1:7")
        depends_on("py-nest-asyncio@1.5:", when="@6.1.13:7.1")
        depends_on("py-pytest", when="@5.2:5.2.0")
        depends_on("py-python-dateutil@2.8.2:", when="@7.2.1:")
        depends_on("py-python-dateutil@2:", when="@5:7.2.0")
        depends_on("py-pywin32", when="@5.3.2:5 platform=windows")
        depends_on("py-pyzmq@23.0.0:", when="@7.3.2:")
        depends_on("py-pyzmq@13:", when="@4.2:7.1")
        depends_on("py-tornado@6.2:", when="@7.3.5:")
        depends_on("py-tornado@4.1:", when="@5.2.2:7.1")
        depends_on("py-traitlets@5.3:5.3.0.0,5.4:", when="@8.0.0-beta2:")
        depends_on("py-traitlets", when="@4.2:8.0.0-alpha4")
    # END DEPENDENCIES

