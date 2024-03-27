##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAlembic(PythonPackage):
    version("1.13.1", sha256="2edcc97bed0bd3272611ce3a98d98279e9c209e7186e43e75bbb1b2bdfdbcc43", url="https://pypi.org/packages/7f/50/9fb3a5c80df6eb6516693270621676980acd6d5a9a7efdbfa273f8d616c7/alembic-1.13.1-py3-none-any.whl")
    version("1.13.0", sha256="a23974ea301c3ee52705db809c7413cecd165290c6679b9998dd6c74342ca23a", url="https://pypi.org/packages/d5/d8/fc331ad9aa5f2a551042582c3ededd70ee4e72b032089b1784150a5704ac/alembic-1.13.0-py3-none-any.whl")
    version("1.12.1", sha256="47d52e3dfb03666ed945becb723d6482e52190917fdb47071440cfdba05d92cb", url="https://pypi.org/packages/34/47/95d8f99c9f4a57079dfbcff5e023c5d81bde092d1c2354156340a56b3a1a/alembic-1.12.1-py3-none-any.whl")
    version("1.12.0", sha256="03226222f1cf943deee6c85d9464261a6c710cd19b4fe867a3ad1f25afda610f", url="https://pypi.org/packages/a2/8b/46919127496036c8e990b2b236454a0d8655fd46e1df2fd35610a9cbc842/alembic-1.12.0-py3-none-any.whl")
    version("1.11.3", sha256="d6c96c2482740592777c400550a523bc7a9aada4e210cae2e733354ddae6f6f8", url="https://pypi.org/packages/ab/7d/b572fc6a51bc430b1fa0ef59591db32b14105093324d472eed8ea296d2df/alembic-1.11.3-py3-none-any.whl")
    version("1.11.2", sha256="7981ab0c4fad4fe1be0cf183aae17689fe394ff874fd2464adb774396faf0796", url="https://pypi.org/packages/34/fe/eebb260c86c71d9ed861aa1434fc50601df657425b18329994af8c0bd789/alembic-1.11.2-py3-none-any.whl")
    version("1.11.1", sha256="dc871798a601fab38332e38d6ddb38d5e734f60034baeb8e2db5b642fccd8ab8", url="https://pypi.org/packages/11/00/46a4f66ad54c661350a1cd5daae4b4ab2232486c55635ee12ff12958b03f/alembic-1.11.1-py3-none-any.whl")
    version("1.11.0", sha256="f0e74af5a6ade86b72770790188aaf64122c9cba64efd1d7ff3323ac3fdb75e0", url="https://pypi.org/packages/59/4d/28b13ff3a9c26988f8c32f460cc34ee806ac46038232ee493b9baaaf6164/alembic-1.11.0-py3-none-any.whl")
    version("1.10.4", sha256="43942c3d4bf2620c466b91c0f4fca136fe51ae972394a0cc8b90810d664e4f5c", url="https://pypi.org/packages/83/64/3d091f50da38aca0774e30053db2bd3483ba6358674a60d82fd6dd6248b6/alembic-1.10.4-py3-none-any.whl")
    version("1.10.3", sha256="b2e0a6cfd3a8ce936a1168320bcbe94aefa3f4463cd773a968a55071beb3cd37", url="https://pypi.org/packages/1d/f3/bf536ece9c30b82f1cd193f36dff69a718138c443a1f2d41d3430fa467fd/alembic-1.10.3-py3-none-any.whl")
    version("1.5.5", sha256="65b64087cc47bcf2d7ee127698919976223a1e6fa36c7094f15be4fe55c8d788", url="https://pypi.org/packages/15/9f/b281de89dde4e26111bbc7d852322a79040eef42692d8772cb46f58303a6/alembic-1.5.5-py2.py3-none-any.whl")
    version("1.4.1", sha256="791a5686953c4b366d3228c5377196db2f534475bb38d26f70eb69668efd9028", url="https://pypi.org/packages/e0/e9/359dbb77c35c419df0aedeb1d53e71e7e3f438ff64a8fdb048c907404de3/alembic-1.4.1.tar.gz")
    version("1.4.0", sha256="2df2519a5b002f881517693b95626905a39c5faf4b5a1f94de4f1441095d1d26", url="https://pypi.org/packages/be/4e/9a6044bb78e8cb6d5846c07f8d3e976b7d5db845e5bd8c82c57f3ca91b0e/alembic-1.4.0.tar.gz")
    version("1.3.3", sha256="d412982920653db6e5a44bfd13b1d0db5685cbaaccaf226195749c706e1e862a", url="https://pypi.org/packages/9d/c9/d4aa3be3511dfd6d86f8f483ce0d9f120258be4aceadc17601843593e2ec/alembic-1.3.3.tar.gz")
    version("1.3.2", sha256="3b0cb1948833e062f4048992fbc97ecfaaaac24aaa0d83a1202a99fb58af8c6d", url="https://pypi.org/packages/dc/6d/3c1411dfdcf089ec89ce5e2222deb2292f39b6b1a5911222e15af9fe5a92/alembic-1.3.2.tar.gz")
    version("1.3.1", sha256="49277bb7242192bbb9eac58fed4fe02ec6c3a2a4b4345d2171197459266482b2", url="https://pypi.org/packages/84/64/493c45119dce700a4b9eeecc436ef9e8835ab67bae6414f040cdc7b58f4b/alembic-1.3.1.tar.gz")
    version("1.3.0", sha256="e6c6a4243e89c8d3e2342a1562b2388f3b524c9cac2fccc4d2c461a1320cc1c1", url="https://pypi.org/packages/70/3d/d5ed7a71fe84f9ed0a69e91232a40b0b148b151524dc5bb1c8e4211eb117/alembic-1.3.0.tar.gz")
    version("1.2.1", sha256="9f907d7e8b286a1cfb22db9084f9ce4fde7ad7956bb496dc7c952e10ac90e36a", url="https://pypi.org/packages/6f/42/48447bf41287bc577e4f340e7c28578e322567f5622a915bdfa01c83dc76/alembic-1.2.1.tar.gz")
    version("1.2.0", sha256="5609afbb2ab142a991b15ae436347c475f8a517f1610f2fd1b09cdca7c311f3f", url="https://pypi.org/packages/12/0a/b882c547f9955b8bff9ffabdf131a3cc69d9385a18d074dd4362bd5d3b24/alembic-1.2.0.tar.gz")
    version("1.1.0", sha256="4a4811119efbdc5259d1f4c8f6de977b36ad3bcc919f59a29c2960c5ef9149e4", url="https://pypi.org/packages/9a/0f/a5e8997d58882da8ecd288360dddf133a83145de6480216774923b393422/alembic-1.1.0.tar.gz")
    version("1.0.11", sha256="cdb7d98bd5cbf65acd38d70b1c05573c432e6473a82f955cdea541b5c153b0cc", url="https://pypi.org/packages/7b/8b/0c98c378d93165d9809193f274c3c6e2151120d955b752419c7d43e4d857/alembic-1.0.11.tar.gz")
    version("1.0.7", sha256="16505782b229007ae905ef9e0ae6e880fddafa406f086ac7d442c1aaf712f8c2", url="https://pypi.org/packages/a4/06/f1ae8393463c26f3dafa21eebac611088da02a26e1f1e23bd75fee2dbffe/alembic-1.0.7.tar.gz")

    with default_args(type="run"):
        depends_on("py-importlib-metadata", when="@1.7.4: ^python@:3.8")
        depends_on("py-importlib-resources", when="@1.7: ^python@:3.8")
        depends_on("py-mako", when="@1:1.0.0,1.4.3:1.4,1.5.1:1.6.1,1.6.3:")
        depends_on("py-python-dateutil", when="@1:1.0.0,1.4.3:1.4,1.5.1:1.6.1,1.6.3:1.6")
        depends_on("py-python-editor@0.3:", when="@1:1.0.0,1.4.3:1.4,1.5.1:1.6.1,1.6.3:1.6")
        depends_on("py-sqlalchemy@1.3.0:", when="@1.5.1:1.6.1,1.6.3:")
        depends_on("py-typing-extensions@4:", when="@1.10:")

