# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFastcore(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.5.29", sha256="a7d7e89faf968f2d8584df2deca344c3974f6cf476e1299cd3c067d8fa7440e9", url="https://pypi.org/packages/39/b8/3059245adb5e4421222aab3852ac7f47d68eba82c8c62b88928ec1c69431/fastcore-1.5.29-py3-none-any.whl")
    version("1.5.28", sha256="8547b108a348d705ce04949bd327d9ad7871aacf35bce44f20bc475d1d9fa124", url="https://pypi.org/packages/51/88/488fc7f9a051e9681a7f9c0f89f20fcf58ab9413e8aa2f272c785179c872/fastcore-1.5.28-py3-none-any.whl")
    version("1.5.27", sha256="79dffaa3de96066e4d7f2b8793f1a8a9468c82bc97d3d48ec002de34097b2a9f", url="https://pypi.org/packages/a6/f7/d622436fb6dce10dce17c348ea3b5bc1fd389b507039174be2a7967e1895/fastcore-1.5.27-py3-none-any.whl")
    version("1.5.26", sha256="0d665fa5f5d6fbf9ff1eb861edada64c7c2876f7e5c1a51d2eadb3b97679136e", url="https://pypi.org/packages/e2/11/e3c6c1f54885030813f2288b04f0c28bea17be9515060008d86baa734575/fastcore-1.5.26-py3-none-any.whl")
    version("1.5.25", sha256="b92c2186534f17021a9dd95e003189f4bd995bc7a05b4d7970172c9eba103fd6", url="https://pypi.org/packages/1c/06/f397636a315522c65696534bd5fceb0631e3d65d44ff0bf94ec096927db9/fastcore-1.5.25-py3-none-any.whl")
    version("1.5.24", sha256="84980893bd2e79e0cae0bcd483e9163177361d909591e64bcf59016bffc3fac6", url="https://pypi.org/packages/4e/de/b51ab622c66fc1f9334e3fccf32bb2d67266f5a96eb94a89f170d5d24b93/fastcore-1.5.24-py3-none-any.whl")
    version("1.5.23", sha256="bd59b8106810c7545a674b8005522f2a4f00d29e07c98017ce6cb40f27d134e3", url="https://pypi.org/packages/bf/4e/6ce42187e42614ba6c22791aa101fcb7e3cab62108d2e0f9da0b2dbbef56/fastcore-1.5.23-py3-none-any.whl")
    version("1.5.22", sha256="96ec9b23cd95f969a3bd0a118aed92a60c7da80d89716ac3585cacc9b26a708a", url="https://pypi.org/packages/7b/41/372884bfd2c305c44dbb629348adbf9de9fbce876475691f50f3ea9b7272/fastcore-1.5.22-py3-none-any.whl")
    version("1.5.21", sha256="882ca33c93734dc5025fa6b2c82f002725d7cc7564427e76a562ded3e66d44d8", url="https://pypi.org/packages/d5/84/809d6bad9ae8db5b1189977a78ee7f4e5f149eb9c0bc259af8516c7aa14b/fastcore-1.5.21-py3-none-any.whl")
    version("1.5.20", sha256="2f4c110401ce2f54c3d2d1a5d698b14a3ce7d6205c8964fd12eb2e94405eee6d", url="https://pypi.org/packages/01/e0/d14bac8ac4abe5743be788e90ce0c29bff8cb9e5ea0a0040aae800a199ec/fastcore-1.5.20-py3-none-any.whl")
    version("1.3.29", sha256="6aac9db4df6dd30ab240d46943ce5ee0407e006769399dade6f12896e5623d06", url="https://pypi.org/packages/d2/d8/cd1569e4316ffc8dfe46bd07134aec17225698d21d2bcf5aae8e329d8d3f/fastcore-1.3.29-py3-none-any.whl")
    version("1.3.28", sha256="8132ba425d9bfa7082c97eb85716eafdd3a60e1145c46933ed53484cbbfa3b3f", url="https://pypi.org/packages/2a/05/90cf66d968ebf2f2c8713877fb132eb5b6653ff4867b805bf42eb7305aa8/fastcore-1.3.28-py3-none-any.whl")
    version("1.3.27", sha256="03c6c93f2c769fdd611e32a7cc1433db5a82f67146d9e2f88e03107db203f6de", url="https://pypi.org/packages/50/2b/832378cc02c608798fe13baec2709e70e3796459e6936c4bd3ee7edc4345/fastcore-1.3.27-py3-none-any.whl")
    version("1.3.26", sha256="39d85ec9728dfc4423495a37e06adb8744e8896cca435f39a4e8ffa12a41c8ef", url="https://pypi.org/packages/17/58/6c3d0426a58677eddaec505587d6ef68f4338668e962eedd8cc1372b62f2/fastcore-1.3.26-py3-none-any.whl")
    version("1.3.25", sha256="8d7c1b1fcedba36b46b10e5ee91cd64d21caf98e34ac5fb17bec116883438dc8", url="https://pypi.org/packages/cd/4b/08ba27dcbf3c702dd04220c654214b46fc449aca4553160de4a9e19d4292/fastcore-1.3.25-py3-none-any.whl")
    version("1.3.24", sha256="cd5bde119e84bc598139d574579e6299d3fed33ed9c608f0ed051152ab579a3e", url="https://pypi.org/packages/b3/b8/d2ad78881d2843bd8cdcb6e6b79fcb37c1b984f8d1622a2b1d494f177413/fastcore-1.3.24-py3-none-any.whl")
    version("1.3.23", sha256="269755ed1ec9992cc2a0be34cc48169f37afbfeb21d02aad19bc7dcd7932093a", url="https://pypi.org/packages/1a/55/594e1cafccd18e890cbbba9b8f9652781612bfcb7fc81d3f06d1325377d6/fastcore-1.3.23-py3-none-any.whl")
    version("1.3.22", sha256="7fab78762a5425ecdc332daba1645c08ed5cb6c5b5d912c285f0de6d38784cf0", url="https://pypi.org/packages/82/3f/665013950d6d7ab514a561a615b7dc647b6d54d904469e15f78e55bce7b2/fastcore-1.3.22-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-matplotlib", when="@:0.0.1")
        depends_on("py-numpy", when="@:1.0.4")
        depends_on("py-packaging", when="@0.1.25:")
        depends_on("py-pandas", when="@:0.1.5")
        depends_on("py-pip", when="@0.1.25:")
    # END DEPENDENCIES

