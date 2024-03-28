# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMkdocstrings(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.24.1", sha256="b4206f9a2ca8a648e222d5a0ca1d36ba7dee53c88732818de183b536f9042b5d", url="https://pypi.org/packages/d3/53/941fc52aa984f6f03b4f7473d7ec787b22076794eda40701a705cab1ab01/mkdocstrings-0.24.1-py3-none-any.whl")
    version("0.24.0", sha256="f4908560c10f587326d8f5165d1908817b2e280bbf707607f601c996366a2264", url="https://pypi.org/packages/26/1d/8e196854491b8bebe8be4f170734f9c33891da9294f7036896e434ae0d49/mkdocstrings-0.24.0-py3-none-any.whl")
    version("0.23.0", sha256="051fa4014dfcd9ed90254ae91de2dbb4f24e166347dae7be9a997fe16316c65e", url="https://pypi.org/packages/64/2f/6b72f8f8bf168a5820c6c38bffe54d25cfdafd9b4be6fbb335a9a57dd7c9/mkdocstrings-0.23.0-py3-none-any.whl")
    version("0.22.0", sha256="2d4095d461554ff6a778fdabdca3c00c468c2f1459d469f7a7f622a2b23212ba", url="https://pypi.org/packages/b6/26/5816407b5dd51821a3d23f53bdbd013ab1878b6246e520dc014d200ee1d2/mkdocstrings-0.22.0-py3-none-any.whl")
    version("0.21.2", sha256="949ef8da92df9d692ca07be50616459a6b536083a25520fd54b00e8814ce019b", url="https://pypi.org/packages/04/ca/7630aa270d8af95eadccc13836e5471a0d639d41555ec894e78a83d1a4cd/mkdocstrings-0.21.2-py3-none-any.whl")
    version("0.21.1", sha256="cf5a2d50bb0ee9c008e714a55ecce5acb7fa1ec9add5d8ad5bc2df6b2cdd3e21", url="https://pypi.org/packages/de/66/79a681e6e7649c09274d032f29f6d8054f227171a8b371ddeb26d32d90dd/mkdocstrings-0.21.1-py3-none-any.whl")
    version("0.21.0", sha256="05c52573366f0a32536f7bf0258f2a8ad180836058bb024b252b8a61a25452b3", url="https://pypi.org/packages/f8/81/562645a79ece59a6d2dc3716fbea7916443a8464c320009f7a2c98387f8e/mkdocstrings-0.21.0-py3-none-any.whl")
    version("0.20.0", sha256="f17fc2c4f760ec302b069075ef9e31045aa6372ca91d2f35ded3adba8e25a472", url="https://pypi.org/packages/22/08/dd06d533879ba4694bb31b0f4b8d8ec3b50ed51d8717083bdf6a8a0bd065/mkdocstrings-0.20.0-py3-none-any.whl")
    version("0.19.1", sha256="32a38d88f67f65b264184ea71290f9332db750d189dea4200cbbe408d304c261", url="https://pypi.org/packages/f1/b3/67004de33f860586d27301fc12d949f56026a5fc42f8004566e454659985/mkdocstrings-0.19.1-py3-none-any.whl")
    version("0.19.0", sha256="3217d510d385c961f69385a670b2677e68e07b5fea4a504d86bf54c006c87c7d", url="https://pypi.org/packages/60/53/eedad37654a74f969d297e0dec67db17e7e013266cc6e3ea61c7568a01c8/mkdocstrings-0.19.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-click@7:", when="@0.24:")
        depends_on("py-importlib-metadata@4.6:", when="@0.22: ^python@:3.9")
        depends_on("py-jinja2@2.11.1:", when="@0.17:")
        depends_on("py-markdown@3.3:", when="@0.17:")
        depends_on("py-markupsafe@1.1:", when="@0.17:")
        depends_on("py-mkdocs@1.4:", when="@0.24:")
        depends_on("py-mkdocs@1.2:", when="@0.17:0.23")
        depends_on("py-mkdocs-autorefs@0.3.1:", when="@0.18:")
        depends_on("py-platformdirs@2.2:", when="@0.24:")
        depends_on("py-pymdown-extensions@6.3:", when="@0.17:")
        depends_on("py-typing-extensions@4.1:", when="@0.21.1: ^python@:3.9")
    # END DEPENDENCIES

