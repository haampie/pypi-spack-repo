# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGoogleapisCommonProtos(PythonPackage):
    # BEGIN VERSIONS
    version("1.63.0", sha256="ae45f75702f7c08b541f750854a678bd8f534a1a6bace6afe975f1d0a82d6632", url="https://pypi.org/packages/dc/a6/12a0c976140511d8bc8a16ad15793b2aef29ac927baa0786ccb7ddbb6e1c/googleapis_common_protos-1.63.0-py2.py3-none-any.whl")
    version("1.62.0", sha256="4750113612205514f9f6aa4cb00d523a94f3e8c06c5ad2fee466387dc4875f07", url="https://pypi.org/packages/f0/43/c9d8f75ddf08e2a0a27db243c13a700c3cc7ec615b545b697cf6f715ad92/googleapis_common_protos-1.62.0-py2.py3-none-any.whl")
    version("1.61.0", sha256="22f1915393bb3245343f6efe87f6fe868532efc12aa26b391b15132e1279f1c0", url="https://pypi.org/packages/21/49/12996dc0238e017504dceea1d121a48bd49fb3f4416f40d59fc3e924b4f3/googleapis_common_protos-1.61.0-py2.py3-none-any.whl")
    version("1.60.0", sha256="69f9bbcc6acde92cab2db95ce30a70bd2b81d20b12eff3f1aabaffcbe8a93918", url="https://pypi.org/packages/a7/bc/416a1ffeba4dcd072bc10523dac9ed97f2e7fc4b760580e2bdbdc1e2afdd/googleapis_common_protos-1.60.0-py2.py3-none-any.whl")
    version("1.59.1", sha256="0cbedb6fb68f1c07e18eb4c48256320777707e7d0c55063ae56c15db3224a61e", url="https://pypi.org/packages/b3/b7/bbaa556e9ff0580f408c64ccf4db0c1414eec79e7151d33a10bc209ffb6d/googleapis_common_protos-1.59.1-py2.py3-none-any.whl")
    version("1.59.0", sha256="b287dc48449d1d41af0c69f4ea26242b5ae4c3d7249a38b0984c86a4caffff1f", url="https://pypi.org/packages/a7/8d/7ccf8f63ab0a768e13720262374c0d6a1489f7f23f1b89a16c92af452f09/googleapis_common_protos-1.59.0-py2.py3-none-any.whl")
    version("1.58.0", sha256="ca3befcd4580dab6ad49356b46bf165bb68ff4b32389f028f1abd7c10ab9519a", url="https://pypi.org/packages/32/4e/ed585842aaa704d87495a0e99317aaa44c5007a597c05b995fa8cfc4dfbe/googleapis_common_protos-1.58.0-py2.py3-none-any.whl")
    version("1.57.1", sha256="2672d6b3a7b6188b70a5a4c70def7ddbb9000852dfbf49daf52fc7306c09db0c", url="https://pypi.org/packages/76/b9/fc6a31a90e3c78cea00d209d48f1e5c6c9edc6b14f3039470c3f7fae60a1/googleapis_common_protos-1.57.1-py2.py3-none-any.whl")
    version("1.57.0", sha256="a9f4a1d7f6d9809657b7f1316a1aa527f6664891531bcfcc13b6696e685f443c", url="https://pypi.org/packages/f0/2a/25d8c1ceedc5af97de37434c9c5e38ce28aaa45960aa2bd7aa215fc420c0/googleapis_common_protos-1.57.0-py2.py3-none-any.whl")
    version("1.56.4", sha256="8eb2cbc91b69feaf23e32452a7ae60e791e09967d81d4fcc7fc388182d1bd394", url="https://pypi.org/packages/e2/fd/d9efa2085bd762fba3a637eb3e36d76d72eb6e083d170aeaca65a75f1f9c/googleapis_common_protos-1.56.4-py2.py3-none-any.whl")
    version("1.55.0", sha256="183bb0356bd614c4330ad5158bc1c1bcf9bcf7f5e7f911317559fe209496eeee", url="https://pypi.org/packages/50/a9/6c76954ad5ee88c749407b282e5dfa724e3bd3065a069bcbe6a3da08a3e3/googleapis_common_protos-1.55.0-py2.py3-none-any.whl")
    version("1.6.0", sha256="e61b8ed5e36b976b487c6e7b15f31bb10c7a0ca7bd5c0e837f4afab64b53a0c6", url="https://pypi.org/packages/eb/ee/e59e74ecac678a14d6abefb9054f0bbcb318a6452a30df3776f133886d7d/googleapis-common-protos-1.6.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("grpc", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-grpcio@1.44.0:", when="@1.57:1.61,1.62.0-rc2:+grpc")
        depends_on("py-grpcio@1.0.0:", when="@1.52:1.56+grpc")
        depends_on("py-protobuf@3.19.5:3.20.0-rc2,3.20.1-rc1,3.20.2:4.21.0,4.21.6:4", when="@1.57:")
        depends_on("py-protobuf@3.15.0:4", when="@1.56.2-beta1,1.56.3-beta1:1.56")
        depends_on("py-protobuf@3.12.0:", when="@1.53:1.56.0")
    # END DEPENDENCIES

