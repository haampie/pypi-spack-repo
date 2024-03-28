# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTiktoken(PythonPackage):
    # BEGIN VERSIONS
    version("0.4.0", sha256="59b20a819969735b48161ced9b92f05dc4519c17be4015cfb73b65270a243620", url="https://pypi.org/packages/9f/88/77a86f915a81449156375b7538c94105a34bebf00838462c9d3fced490e9/tiktoken-0.4.0.tar.gz")
    version("0.3.1", sha256="8295912429374f5f3c6c6bf053a091ce1de8c1792a62e3b30d4ad36f47fa8b52", url="https://pypi.org/packages/fb/d9/c38fee002c5979f29c182aee8e28c31538eabf40022e304f97ff82324199/tiktoken-0.3.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.1.1")
    # END DEPENDENCIES

