##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyS3transfer(PythonPackage):
    version("0.10.1", sha256="ceb252b11bcf87080fb7850a224fb6e05c8a776bab8f2b64b7f25b969464839d", url="https://pypi.org/packages/83/37/395cdb6ee92925fa211e55d8f07b9f93cf93f60d7d4ce5e66fd73f1ea986/s3transfer-0.10.1-py3-none-any.whl")
    version("0.10.0", sha256="3cdb40f5cfa6966e812209d0994f2a4709b561c88e90cf00c2696d2df4e56b2e", url="https://pypi.org/packages/12/bb/7e7912e18cd558e7880d9b58ffc57300b2c28ffba9882b3a54ba5ce3ebc4/s3transfer-0.10.0-py3-none-any.whl")
    version("0.9.0", sha256="01d4d2c35a016db8cb14f9a4d5e84c1f8c96e7ffc211422555eed45c11fa7eb1", url="https://pypi.org/packages/fd/fb/46eda754e80fa2efd82981e37cd75cabbecef71df63843e6e94e12fae9db/s3transfer-0.9.0-py3-none-any.whl")
    version("0.8.2", sha256="c9e56cbe88b28d8e197cf841f1f0c130f246595e77ae5b5a05b69fe7cb83de76", url="https://pypi.org/packages/75/ca/5399536cbd5889ca4532d4b8bbcd17efa0fe0be0da04e143667a4ff5644e/s3transfer-0.8.2-py3-none-any.whl")
    version("0.7.0", sha256="10d6923c6359175f264811ef4bf6161a3156ce8e350e705396a7557d6293c33a", url="https://pypi.org/packages/5a/4b/fec9ce18f8874a96c5061422625ba86c3ee1e6587ccd92ff9f5bf7bd91b2/s3transfer-0.7.0-py3-none-any.whl")
    version("0.6.2", sha256="b014be3a8a2aab98cfe1abc7229cc5a9a0cf05eb9c1f2b86b230fd8df3f78084", url="https://pypi.org/packages/d9/17/a3b666f5ef9543cfd3c661d39d1e193abb9649d0cfbbfee3cf3b51d5af02/s3transfer-0.6.2-py3-none-any.whl")
    version("0.6.1", sha256="3c0da2d074bf35d6870ef157158641178a4204a6e689e82546083e31e0311346", url="https://pypi.org/packages/ec/fa/9416461ee05efabe477d588288bdd88acb69a51ee4b31a9b73d3b5b716fc/s3transfer-0.6.1-py3-none-any.whl")
    version("0.6.0", sha256="06176b74f3a15f61f1b4f25a1fc29a4429040b7647133a463da8fa5bd28d5ecd", url="https://pypi.org/packages/5e/c6/af903b5fab3f9b5b1e883f49a770066314c6dcceb589cf938d48c89556c1/s3transfer-0.6.0-py3-none-any.whl")
    version("0.5.2", sha256="7a6f4c4d1fdb9a2b640244008e142cbc2cd3ae34b386584ef044dd0f27101971", url="https://pypi.org/packages/7b/9c/f51775ebe7df5a7aa4e7c79ed671bde94e154bd968aca8d65bb24aba0c8c/s3transfer-0.5.2-py3-none-any.whl")
    version("0.5.1", sha256="25c140f5c66aa79e1ac60be50dcd45ddc59e83895f062a3aab263b870102911f", url="https://pypi.org/packages/17/7c/4b60191e38bed78c65e817f7506ef1038a4246a703cb36fb5390a5eaf7ce/s3transfer-0.5.1-py3-none-any.whl")
    version("0.5.0", sha256="9c1dc369814391a6bda20ebbf4b70a0f34630592c9aa520856bf384916af2803", url="https://pypi.org/packages/ab/84/fc3717a7b7f0f6bb08af593127171f08e3e0087c197922da09c01bfe7c3a/s3transfer-0.5.0-py3-none-any.whl")
    version("0.4.2", sha256="9b3752887a2880690ce628bc263d6d13a3864083aeacff4890c1c9839a5eb0bc", url="https://pypi.org/packages/63/d0/693477c688348654ddc21dcdce0817653a294aa43f41771084c25e7ff9c7/s3transfer-0.4.2-py2.py3-none-any.whl")
    version("0.4.1", sha256="b5130849df909773254099d085790456665f8d7e0032bbef6e3407f28adb1ad9", url="https://pypi.org/packages/95/95/91a1b99e4ef46bb915167b04aa26aec74dad5356d13d487a90f7d22994ee/s3transfer-0.4.1-py2.py3-none-any.whl")
    version("0.4.0", sha256="af1af6384bd7fb8208b06480f9be73d0295d965c4c073a5c95ea5b6661dccc18", url="https://pypi.org/packages/3e/50/ac379fa31377f5d316cad8967db9f73c50cd61b80153269bfd7d8b964fc8/s3transfer-0.4.0-py2.py3-none-any.whl")
    version("0.3.7", sha256="efa5bd92a897b6a8d5c1383828dca3d52d0790e0756d49740563a3fb6ed03246", url="https://pypi.org/packages/00/89/0cb4e92c239e6425b9b0035227b8cdf9d3d098a5c9e95632c3815df63a09/s3transfer-0.3.7-py2.py3-none-any.whl")
    version("0.3.6", sha256="5d48b1fd2232141a9d5fb279709117aaba506cacea7f86f11bc392f06bfa8fc2", url="https://pypi.org/packages/98/14/0b4be62b65c52d6d1c442f24e02d2a9889a73d3c352002e14c70f84a679f/s3transfer-0.3.6-py2.py3-none-any.whl")
    version("0.3.5", sha256="2db91129803fa023bc71c16d106acac52c43409477a777910ae61a8279b4ee73", url="https://pypi.org/packages/6b/41/9e8a1a97a4cace08a904af1b781a8f1a463d821de2b1d6d896809c5b2dcd/s3transfer-0.3.5-py2.py3-none-any.whl")
    version("0.3.4", sha256="1e28620e5b444652ed752cf87c7e0cb15b0e578972568c6609f0f18212f259ed", url="https://pypi.org/packages/ea/43/4b4a1b26eb03a429a4c37ca7fdf369d938bd60018fc194e94b8379b0c77c/s3transfer-0.3.4-py2.py3-none-any.whl")
    version("0.3.3", sha256="2482b4259524933a022d59da830f51bd746db62f047d6eb213f2f8855dcb8a13", url="https://pypi.org/packages/69/79/e6afb3d8b0b4e96cefbdc690f741d7dd24547ff1f94240c997a26fa908d3/s3transfer-0.3.3-py2.py3-none-any.whl")
    version("0.3.2", sha256="2525bae2a530195576da53671bae8ca8c55ee8e33bc2225a65e804476611ea5a", url="https://pypi.org/packages/c7/48/a8252b6b3cd31774eab312b19d58a6ac55f296240c206617dcd38cd93bf8/s3transfer-0.3.2-py2.py3-none-any.whl")
    version("0.3.1", sha256="80ed96731b3bd77395cd6197246069092015e1124164b2c152c8f741a823dd04", url="https://pypi.org/packages/de/6d/27abf73e66a05726dd52fb3a6645417b5dc86d90488b59589296dafbf054/s3transfer-0.3.1-py2.py3-none-any.whl")
    version("0.3.0", sha256="2157640a47c8b8fa2071bdd7b0d57378ec8957eede3bd083949c2dcc4d9b0dd4", url="https://pypi.org/packages/d5/29/2a79d0223617d255eccac5fd9c147d65ee32f9aabe0e47ab75fd7568af24/s3transfer-0.3.0-py2.py3-none-any.whl")
    version("0.2.1", sha256="b780f2411b824cb541dbcd2c713d0cb61c7d1bcadae204cdddda2b35cef493ba", url="https://pypi.org/packages/16/8a/1fc3dba0c4923c2a76e1ff0d52b305c44606da63f718d14d3231e21c51b0/s3transfer-0.2.1-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-botocore@1.33.2:", when="@0.8.1:")
        depends_on("py-botocore@1.12.36:", when="@0.3.4:0.7")
        depends_on("py-futures@2.2:", when="@0.3.5")

