# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureCosmos(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("4.0.0", sha256="2dbcb33e091b6c3284026472cf3fc3d3ca3cc8bfdc200d469dbd9089f8ba0e54", url="https://pypi.org/packages/af/42/f9df4e1cba74ee5058782ef838b0f6caa0c271670e054c263d69702884e2/azure_cosmos-4.0.0-py2.py3-none-any.whl")
    version("3.2.0", sha256="313e766bcf5a1779802c274dec94d5b9cc0e4d0d269489c56606fd2464070fad", url="https://pypi.org/packages/4a/4f/23ffc8e870df94ea6def08121245301e763eaee7236fb8c3d02d5ff66687/azure_cosmos-3.2.0-py2.py3-none-any.whl")
    version("3.1.2", sha256="bac7de8fa84a3e34b6814cdadbb5ce99653874c27180f5fa596363a8dc1945db", url="https://pypi.org/packages/7a/c4/a4aa7dad65c1a55bf1a5794c897e7e5a2ab3260e6c76afb01e5ffb3e1307/azure_cosmos-3.1.2-py3-none-any.whl")
    version("3.1.1", sha256="3061e081150320a8aba5bf0204fa1c26329478bd9f00af1c1a64e0ebf53dae48", url="https://pypi.org/packages/1e/ab/7bce6265918d91325537f188869b901fb25d652e2c02ba3c2d0342d95114/azure_cosmos-3.1.1-py3-none-any.whl")
    version("3.1.0", sha256="f4e8c207e74296644ae2cb9816084562d8471f9b27c3f5533d048e87aa711a13", url="https://pypi.org/packages/d5/ef/87bd5c7ea5fd448501fe74dd54fd4e148cb52423e681026390b72d1f49df/azure_cosmos-3.1.0-py3-none-any.whl")
    version("3.0.2", sha256="12dac400ddebc72f9cff2dd152cd6cbd861d3dc11530e07c5aecd5a81a1b49d6", url="https://pypi.org/packages/a0/63/921bda96c1cf5cee4777a69fc0c13b44ff11a656dd8b88eb38818dc835d3/azure_cosmos-3.0.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-core@1.0.0:", when="@4.0.0-beta5:4.3.0-beta1")
        depends_on("py-requests@2.10:", when="@:3.1.1,3.2:4.0.0-alpha2")
        depends_on("py-six@1.6:", when="@:3.1.1,3.2:4.2")
    # END DEPENDENCIES

