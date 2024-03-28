# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGoogleApiCore(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.18.0", sha256="5a63aa102e0049abe85b5b88cb9409234c1f70afcda21ce1e40b285b9629c1d6", url="https://pypi.org/packages/86/75/59a3ad90d9b4ff5b3e0537611dbe885aeb96124521c9d35aa079f1e0f2c9/google_api_core-2.18.0-py3-none-any.whl")
    version("2.18.0-rc0", sha256="d785ba174593d89483b07116dd809ae7ac46f0173ab13c780be361618755ccc7", url="https://pypi.org/packages/5d/aa/95763e643e307f56dc2745ee4cb258d3decac507a6bf5dfb9e16e2cabd16/google_api_core-2.18.0rc0-py3-none-any.whl")
    version("2.17.1", sha256="610c5b90092c360736baccf17bd3efbcb30dd380e7a6dc28a71059edb8bd0d8e", url="https://pypi.org/packages/0f/87/373ab788a4682adc1a6900e54d54c750b7bd4be456d75b8bf64eccc23ef9/google_api_core-2.17.1-py3-none-any.whl")
    version("2.17.1-rc1", sha256="050af319ff2eda4c4fbe03e422816bf024920eea943ca4b121d4bd09f576f71a", url="https://pypi.org/packages/ee/29/da5c38cfe95882949581ab608f9a6c5f5b233ced097030128366b3763393/google_api_core-2.17.1rc1-py3-none-any.whl")
    version("2.17.0", sha256="08ed79ed8e93e329de5e3e7452746b734e6bf8438d8d64dd3319d21d3164890c", url="https://pypi.org/packages/60/51/2054dfc08dda9a3add0d715cee98d6f8211c99bd6e5bff0ff1bdd3cf3384/google_api_core-2.17.0-py3-none-any.whl")
    version("2.17.0-rc0", sha256="888dd224be53b6d41a80a763358df2deb80fe370fe6dbbf5a5fe6dbc53cad315", url="https://pypi.org/packages/1e/bf/3766f90b8521afe353e4e87c5a6b289057b96739c627ceb12855851ac41a/google_api_core-2.17.0rc0-py3-none-any.whl")
    version("2.16.2", sha256="449ca0e3f14c179b4165b664256066c7861610f70b6ffe54bb01a04e9b466929", url="https://pypi.org/packages/29/37/f7d78e23eb97c1c1753163d5c0734ae8a412d829dbe6e1527f486664f483/google_api_core-2.16.2-py3-none-any.whl")
    version("2.16.1", sha256="257e9e152cd18da0c6701113c122ade04dca04731e179fc5c7dca48e1396ec4c", url="https://pypi.org/packages/e7/b5/b93e0041c7132032fd3bd273aef334cf587c5b9c1056897728069b90968f/google_api_core-2.16.1-py3-none-any.whl")
    version("2.16.0", sha256="c424f9f271c7f55366254708e0d0383963a72376286018af0a04f322be843400", url="https://pypi.org/packages/60/69/5182c52db38323a6c9e64ffb9346879db1a0f003897b5e8710045943b38a/google_api_core-2.16.0-py3-none-any.whl")
    version("2.15.0", sha256="2aa56d2be495551e66bbff7f729b790546f87d5c90e74781aa77233bcb395a8a", url="https://pypi.org/packages/d6/c9/0462f037b62796fbda4801be62d0ae3147eaeb99e2939661580c98abe3eb/google_api_core-2.15.0-py3-none-any.whl")
    version("2.14.0", sha256="de2fb50ed34d47ddbb2bd2dcf680ee8fead46279f4ed6b16de362aca23a18952", url="https://pypi.org/packages/c4/1e/924dcad4725d2e697888e044edf7a433db84bf9a3e40d3efa38ba859d0ce/google_api_core-2.14.0-py3-none-any.whl")
    version("2.13.1", sha256="e24c3a20799df3ee08a10d1d44d7df2d2ef2bc986cca80edfd982f3e415edd20", url="https://pypi.org/packages/94/a1/ab9fcb5a6a3e6dc36345f21ebebb4a6d4679e9e270661e93c3a6e9eabdfe/google_api_core-2.13.1-py3-none-any.whl")
    version("2.13.0", sha256="44ed591f6c3a0c1ac7a91867d2b3841f92839f860f3d3fe26c464dbd50f97094", url="https://pypi.org/packages/b5/ae/9d4efb12f13bab90689994334717c8ffdbfc9a66f5138261093fd4e4b91b/google_api_core-2.13.0-py3-none-any.whl")
    version("2.12.0", sha256="ec6054f7d64ad13b41e43d96f735acbd763b0f3b695dabaa2d579673f6a6e160", url="https://pypi.org/packages/4d/ce/4fd62ea66b3508debc795e475336ce915929765870f0ad52328426ba016e/google_api_core-2.12.0-py3-none-any.whl")
    version("2.11.1", sha256="d92a5a92dc36dd4f4b9ee4e55528a90e432b059f93aee6ad857f9de8cc7ae94a", url="https://pypi.org/packages/6e/c4/c3cd048b6cbeba8d9ae50dd7643ac065b85237338aa7501b0efae91eb4d9/google_api_core-2.11.1-py3-none-any.whl")
    version("2.11.0", sha256="ce222e27b0de0d7bc63eb043b956996d6dccab14cc3b690aaea91c9cc99dc16e", url="https://pypi.org/packages/f7/24/a17e75c733609dce285a2dae6f56837d69a9566963c9d1cab96d788546c8/google_api_core-2.11.0-py3-none-any.whl")
    version("1.34.1", sha256="52bcc9d9937735f8a3986fa0bbf9135ae9cf5393a722387e5eced520e39c774a", url="https://pypi.org/packages/11/51/1d325e9b7358f15dca82e1ed91413c5cecb9d4665da6c44cb8dd348deeaa/google_api_core-1.34.1-py3-none-any.whl")
    version("1.34.0", sha256="7421474c39d396a74dfa317dddbc69188f2336835f526087c7648f91105e32ff", url="https://pypi.org/packages/c7/ca/bf63a592b6db1b7a899d05a046955db2ea3cb5cff5eb899f421f3f97fc48/google_api_core-1.34.0-py3-none-any.whl")
    version("1.33.2", sha256="3b21d4488a898963df91ded12b3125ff0a87ab2af0b658944fad8e9636dd01d8", url="https://pypi.org/packages/09/d4/8f1e3f5e6650da1686901306ca560d3290367e9fa38b3ff9da3b05e97d4b/google_api_core-1.33.2-py3-none-any.whl")
    version("1.33.1", sha256="0cbf03aa67e6f4eb9f1ce1a81f4208c850bc7623bd7460e4b3c4a350d0fdf327", url="https://pypi.org/packages/fb/d4/c5328241bf434a05df092f1e23da7a43de2f0216bb7c368b3b3012487c98/google_api_core-1.33.1-py3-none-any.whl")
    version("1.33.0", sha256="ed50660aba0cbeef424d0684fc01c5ef2c05b349ec960f27ea95087a47e5da6b", url="https://pypi.org/packages/f1/e8/0b7562be1791f7ffd7d5a8a698e23768e175c51b829431f38ee00409e658/google_api_core-1.33.0-py3-none-any.whl")
    version("1.32.0", sha256="ead664143b52dccb4f9c8ba865e38d316c5e1c2f8dc1ff5791908c3e0c17ad3f", url="https://pypi.org/packages/9f/35/4177a49a54f3d4040ca7eb53094ab6d789a9688aba4c24be4e5291035f49/google_api_core-1.32.0-py2.py3-none-any.whl")
    version("1.31.6", sha256="29d01d0599da4188331b9afd7c1b03ce155ad5047e461cf9ce3223a873fec729", url="https://pypi.org/packages/32/6c/ef2b36484d46a6a8815b880163eb2c088fb53df534b3c93efc6043aa6a3c/google_api_core-1.31.6-py2.py3-none-any.whl")
    version("1.31.5", sha256="6815207a8b422e9da42c200681603f304b25f98c98b675a9db9fdc3717e44280", url="https://pypi.org/packages/5f/7e/43c73760cd58a480eba5c80810c146a2c15532f12ab72c94d0cadeb85f88/google_api_core-1.31.5-py2.py3-none-any.whl")
    version("1.31.4", sha256="ed59c6a695a81f601e4ba0f37ca9dbde3c43b3309e161a1a8946f266db4a0c4e", url="https://pypi.org/packages/ab/a5/4c97704976f1cba8a2e8a1afb2026f56f34cf76ab8788b3bf6ddc6ba0679/google_api_core-1.31.4-py2.py3-none-any.whl")
    version("1.31.3", sha256="f52c708ab9fd958862dea9ac94d9db1a065608073fe583c3b9c18537b177f59a", url="https://pypi.org/packages/bc/06/93572c5216b9b7a49468f1b185dcbeb83704b6aad8286ab23078fddd7cb2/google_api_core-1.31.3-py2.py3-none-any.whl")
    version("1.14.2", sha256="b2b91107bcc3b981633c89602b46451f6474973089febab3ee51c49cb7ae6a1f", url="https://pypi.org/packages/71/e5/7059475b3013a3c75abe35015c5761735ab224eb1b129fee7c8e376e7805/google_api_core-1.14.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("grpc", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-google-auth@2.14.1:", when="@2.11:")
        depends_on("py-google-auth@1.25:", when="@1.33:2.10")
        depends_on("py-google-auth@1.25:1", when="@1.28:1.32")
        depends_on("py-google-auth@0.4:1", when="@:1.16")
        depends_on("py-googleapis-common-protos@1.56.2:", when="@1.33:1,2.8.1:")
        depends_on("py-googleapis-common-protos@1.6.0:", when="@1.14:1.32,2:2.1")
        depends_on("py-grpcio@1.49.1:", when="@2.11:+grpc ^python@3.11:")
        depends_on("py-grpcio@1.33.2:", when="@1.33:1,2.0.0:+grpc")
        depends_on("py-grpcio@1.29:", when="@1.19.1:1.32,2:2.0.0-beta1+grpc")
        depends_on("py-grpcio@1.8.2:", when="@1.11.1:1.19.0+grpc")
        depends_on("py-grpcio-status@1.49.1:", when="@2.11:+grpc ^python@3.11:")
        depends_on("py-grpcio-status@1.33.2:", when="@1.33:1,2.2:+grpc")
        depends_on("py-packaging@14.3:", when="@1.26:1.26.0.0,1.26.1:1.32")
        depends_on("py-proto-plus@1.22.3:", when="@2.18:")
        depends_on("py-protobuf@3.19.5:3.20.0-rc2,3.20.1-rc1,3.20.2:4.21.0-rc2,4.21.6:4", when="@2.10.2:")
        depends_on("py-protobuf@3.19.5:3.20.0-rc2,3.20.1-rc1,3.20.2:3", when="@1.33.2:1")
        depends_on("py-protobuf@3.20.1:3", when="@1.33:1.33.1")
        depends_on("py-protobuf@3.12.0:3", when="@1.31.6:1.32")
        depends_on("py-protobuf@3.12.0:3.17", when="@1.31.3")
        depends_on("py-protobuf@3.12.0:", when="@1.20.1:1.31.2,1.31.4:1.31.5,2:2.8.0")
        depends_on("py-protobuf@3.4:", when="@1.4.1:1.20.0")
        depends_on("py-pytz", when="@0.1.2:1.32")
        depends_on("py-requests@2.18:")
        depends_on("py-setuptools@40.3:", when="@1.25:1.32,2:2.4")
        depends_on("py-setuptools@34:", when="@:1.24")
        depends_on("py-six@1.13:", when="@1.22.3:1.32")
        depends_on("py-six@1.10:", when="@:1.22.2")
    # END DEPENDENCIES

