# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJupyterClient(PythonPackage):
    # BEGIN VERSIONS
    version("8.2.0", sha256="b18219aa695d39e2ad570533e0d71fb7881d35a873051054a84ee2a17c4b7389", url="https://pypi.org/packages/07/37/4019d2c41ca333c08dfdfeb84c0fc0368c8defbbd3c8f0c9a530851e5813/jupyter_client-8.2.0-py3-none-any.whl")
    version("8.1.0", sha256="d5b8e739d7816944be50f81121a109788a3d92732ecf1ad1e4dadebc948818fe", url="https://pypi.org/packages/31/6c/96771d6b3ce94da927f7688be821899f169306f16023dd0af5ef55f71a52/jupyter_client-8.1.0-py3-none-any.whl")
    version("7.3.5", sha256="b33222bdc9dd1714228bd286af006533a0abe2bbc093e8f3d29dc0b91bdc2be4", url="https://pypi.org/packages/35/af/66f66acacf1b22b1400cd46e1ac83810509511e7c75afbfbdd9155367a99/jupyter_client-7.3.5-py3-none-any.whl")
    version("7.1.2", sha256="d56f1c57bef42ff31e61b1185d3348a5b2bcde7c9a05523ae4dbe5ee0871797c", url="https://pypi.org/packages/56/a7/f4d3790ce7bb925d3ffe299244501a264f23ee7ec401914f7d788881ea31/jupyter_client-7.1.2-py3-none-any.whl")
    version("7.0.6", sha256="074bdeb1ffaef4a3095468ee16313938cfdc48fc65ca95cc18980b956c2e5d79", url="https://pypi.org/packages/3c/51/06efe08a819c36215e02750b50ac1e5e322303a8369ec1bc4e915d485ad4/jupyter_client-7.0.6-py3-none-any.whl")
    version("6.1.12", sha256="e053a2c44b6fa597feebe2b3ecb5eea3e03d1d91cc94351a52931ee1426aecfc", url="https://pypi.org/packages/77/e8/c3cf72a32a697256608d5fa96360c431adec6e1c6709ba7f13f99ff5ee04/jupyter_client-6.1.12-py3-none-any.whl")
    version("6.1.7", sha256="c958d24d6eacb975c1acebb68ac9077da61b5f5c040f22f6849928ad7393b950", url="https://pypi.org/packages/dc/41/9fa443d5ae8907dd8f7d12146cb0092dc053afd67b5b57e7e8786a328547/jupyter_client-6.1.7-py3-none-any.whl")
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

