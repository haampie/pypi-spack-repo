# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySnakemakeInterfaceExecutorPlugins(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("9.1.0", sha256="102d06304bc0b63bc1dcdf0e1b07692e6da197607483243245e21a1cbe15b5f0", url="https://pypi.org/packages/64/df/eefd7d59ffc8741eb6988a0c3a7ad5c2f90cb9efcf259a861e60ad641d5b/snakemake_interface_executor_plugins-9.1.0-py3-none-any.whl")
    version("9.0.2", sha256="19831d18cd32a356626a3a47e8adafa7caf0ac5bc9762a8ce948c30ad5fd13c0", url="https://pypi.org/packages/de/8f/6b04b1edbce85c3844287f481c7e3e78018ab6dbd313229209a8fefcc0fd/snakemake_interface_executor_plugins-9.0.2-py3-none-any.whl")
    version("9.0.1", sha256="13f5077c7808d335f257ea13225a5de8af82cf20f28f4aefa256520fd818c74d", url="https://pypi.org/packages/b5/bf/cc0190e195b7eae6cae902d72ac8af0d257c11af1acfade0424f2143c0c6/snakemake_interface_executor_plugins-9.0.1-py3-none-any.whl")
    version("9.0.0", sha256="54e703c14852eb86e6e38e21c5d66af6ff684f6c164d714d5748cfd431bccc6e", url="https://pypi.org/packages/df/87/c8e11d12cbf89609c05dbeedc1540db64cecb09bdf1874c4c2401330bd84/snakemake_interface_executor_plugins-9.0.0-py3-none-any.whl")
    version("8.2.0", sha256="b5d7f83b699492648bd44fc601736f15c86a2aa7ba8e5e011282e83a38b0e05f", url="https://pypi.org/packages/48/da/bd3caeb1de705bf3d1ff072b6788ef3189f784990bf027957f835eecf4dc/snakemake_interface_executor_plugins-8.2.0-py3-none-any.whl")
    version("8.1.3", sha256="cf057f29f5ce9141aebd460c0ac7072dbfd4b58050607d5bbf3a8ce1f95de92f", url="https://pypi.org/packages/cc/81/f2f8d302dc6a6e4fbf7b3bbb9e31271859f55e08d3505356304277dcb3e6/snakemake_interface_executor_plugins-8.1.3-py3-none-any.whl")
    version("8.1.2", sha256="c7c2e4c1a5a108622002015202b5d68f1773276ebce8b77fc1eef4fe06de2d82", url="https://pypi.org/packages/c9/4f/966610e214c5699eb66d39a5ffa04390a8df9295b2395cb5aa70cc8a3c27/snakemake_interface_executor_plugins-8.1.2-py3-none-any.whl")
    version("8.1.1", sha256="c39ba893b21425a9322f4055c89cb1219e03acfb57210d9a82265f5376769632", url="https://pypi.org/packages/40/a9/b433960d08f43b7bd4d2d411a567fc63cdbeb2f6585fc1e2714b52360223/snakemake_interface_executor_plugins-8.1.1-py3-none-any.whl")
    version("8.1.0", sha256="180da92e8ff10ed05c26eb2ddb66fd1083a29c0fca72916d9edef578f8406e6b", url="https://pypi.org/packages/40/66/07f339d806c125b19f1cc65ab8aaac6463aa1449b105c2f0ee2c16a61f58/snakemake_interface_executor_plugins-8.1.0-py3-none-any.whl")
    version("8.0.2", sha256="630666bfd907287d0952db6470951626b28f2802654fb6df9a6bd59225651add", url="https://pypi.org/packages/0f/25/1ab127419d7cad9263bdd8cb704346488f462fabfe44c6b2de266ab2f9e1/snakemake_interface_executor_plugins-8.0.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.11:", when="@7:")
        depends_on("python@3.9:", when="@:6")
        depends_on("py-argparse-dataclass@2:")
        depends_on("py-snakemake-interface-common@1.12:", when="@6:")
        depends_on("py-throttler@1.2.2:")
    # END DEPENDENCIES

