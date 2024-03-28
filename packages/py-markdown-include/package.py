# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMarkdownInclude(PythonPackage):
    # BEGIN VERSIONS
    version("0.8.1", sha256="32f0635b9cfef46997b307e2430022852529f7a5b87c0075c504283e7cc7db53", url="https://pypi.org/packages/d7/e2/c4d20b21a05fe0fee571649cebc05f7f72e80b1a743f932e7326125e6c9e/markdown_include-0.8.1-py3-none-any.whl")
    version("0.8.0", sha256="d12fb51500c46334a53608635035c78b7d8ad7f772566f70b8a6a9b2ef2ddbf5", url="https://pypi.org/packages/14/cc/b58c19b6c7993a2f374740615defb420571dbce2cea0c0a644ed6c98261c/markdown_include-0.8.0-py3-none-any.whl")
    version("0.7.2", sha256="09ca3a7470b79d217be828a27c6808c24f4a8814cc422fca05be1bc3fd866907", url="https://pypi.org/packages/1d/e4/66a2397d9c494b04608dc901a414b562354f83abb37b86d7c8819796cf34/markdown_include-0.7.2-py3-none-any.whl")
    version("0.7.0", sha256="a06183b7c7225e73112737acdc6fe0ac0686c39457234eeb5ede23881fed001d", url="https://pypi.org/packages/ee/5a/388ea1dbaed7e51f8f6561267bd915cefc757eaa7e9f5f4fcdb2fbfd0d03/markdown_include-0.7.0-py3-none-any.whl")
    version("0.6.0", sha256="6f5d680e36f7780c7f0f61dca53ca581bd50d1b56137ddcd6353efafa0c3e4a2", url="https://pypi.org/packages/34/ce/289d5d459c274a59379f79af95f3f36ae29cb9d787206ad9b45dda48e3ce/markdown-include-0.6.0.tar.gz")
    version("0.5.1", sha256="72a45461b589489a088753893bc95c5fa5909936186485f4ed55caa57d10250f", url="https://pypi.org/packages/ef/44/eb6e9b4fa1110b719abb876c9b6dd8b46af886a94536ec4e9117fe5e7b97/markdown-include-0.5.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-markdown@3:", when="@0.7:")
    # END DEPENDENCIES

