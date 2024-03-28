# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyInflect(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("7.0.0", sha256="9544afed6182176e43955c44b1acdaed30f9b2b56c16d1fc5b222d98218b546e", url="https://pypi.org/packages/fb/c6/d9feb758be584f729424390af24687d3a4363d968164f94079f83cd536b4/inflect-7.0.0-py3-none-any.whl")
    version("6.2.0", sha256="5a005e0c9afe152cc95d552a59b8b0c19efc51823405b43d89e984f0c33bc243", url="https://pypi.org/packages/6a/e1/79603e4ae91b38a91dfd855f92321afb65e7f3d0192ac831d00bc9c45cca/inflect-6.2.0-py3-none-any.whl")
    version("6.1.1", sha256="b63199be340df9dc4c08eefca88e533f1f47f8eab360df3e468ddf3d6c8681a7", url="https://pypi.org/packages/c6/d5/f8fa4cc77e5137c949d7b98690e880cd7f3bc74793454834847657102dc1/inflect-6.1.1-py3-none-any.whl")
    version("6.1.0", sha256="5c0a218e66cb7a06ec4d416887175e97c6cdffcbbf8891f47b1ae2cbd8f6b7ab", url="https://pypi.org/packages/c3/dc/5150ca1063fd879419db6d0fc1f1f10736c93b0255008ed935529c70834b/inflect-6.1.0-py3-none-any.whl")
    version("6.0.5", sha256="88973e0dce35a9c34f073f0f983ee33ec5c798cc93512fa04bc35a7bb88b9d87", url="https://pypi.org/packages/a2/73/17b439e7f18b84ca63e4b85160e9305898b778dc94ef746e33557e2de902/inflect-6.0.5-py3-none-any.whl")
    version("6.0.4", sha256="2d592e7e4eafb6e51f9c626c5dd4288f5ce55981eaac9b342e868ead95ead5c3", url="https://pypi.org/packages/7e/87/3931f9438eb95902539b746c3846f2f16fe91d2093d5592ba84e164a5f8a/inflect-6.0.4-py3-none-any.whl")
    version("6.0.3", sha256="4b53e8db54d2feb286e658b5c7094b45dae6ba7e991795f1d3c4845bfcb3adb7", url="https://pypi.org/packages/50/ea/b22e11aac8419f735fbf16da21cb0e76ffe2187d4ffda98ede858be0a97b/inflect-6.0.3-py3-none-any.whl")
    version("6.0.2", sha256="182741ec7e9e4c8f7f55b01fa6d80bcd3c4a183d349dfa6d9abbff0a1279e98f", url="https://pypi.org/packages/67/e2/bcd7099b31d6a1f7be358f7ef7cf6fc97cc5a66353784fdfa4867e4243fb/inflect-6.0.2-py3-none-any.whl")
    version("6.0.1", sha256="27164f5627eb2753c55a0b09c615919d535001ba8c44d94dfc1ce5ea2664d91b", url="https://pypi.org/packages/84/3b/eab2a8afb639ab4cba4f3975b830340037800881afef434e3a6e82b77d7f/inflect-6.0.1-py3-none-any.whl")
    version("6.0.0", sha256="e3b85d65a296843268f35f4136283ad7c012a129375db1529d49b4b01ecb400b", url="https://pypi.org/packages/d3/0f/c51780fb99b156e998a8bcbc418aea9179ccd301f8c2a8c1bb255c294af6/inflect-6.0.0-py3-none-any.whl")
    version("5.0.2", sha256="f125f678288f4830f0ee4a4f51e088ff869ac44451a5717627a4ed38d734144c", url="https://pypi.org/packages/a8/d7/9ee314763935ce36e3023103ea2c689e6026147230037503a7772cdad6c1/inflect-5.0.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pydantic@1.9.1:1", when="@6.0.5:6.1")
        depends_on("py-pydantic@1.9.1:", when="@6.0.2:6.0.4,6.2:")
        depends_on("py-pydantic", when="@6:6.0.1")
        depends_on("py-typing-extensions", when="@6.2:")
    # END DEPENDENCIES

