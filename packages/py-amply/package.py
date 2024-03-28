# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAmply(PythonPackage):
    # BEGIN VERSIONS
    version("0.1.6", sha256="44c372cf60dbdfda06e80cbf201a28d1e6384485b6a2386ca21160dccd0e82a8", url="https://pypi.org/packages/43/b1/5ff785027761a1d29d6fabbad15fe5d9327a38bc2a1eb753f9d467bbbb5d/amply-0.1.6-py3-none-any.whl")
    version("0.1.5", sha256="57a1141b2591614c69df35f1df2f7913b8f5d5330aae92ce1b4b73ae8905fe6a", url="https://pypi.org/packages/eb/97/c7e61ca87316e5e498066c53681a4586f9666ef32f027e58b7c2b755fa68/amply-0.1.5-py3-none-any.whl")
    version("0.1.4", sha256="f8a846a544750493f45e75e9b44c393144be5728701df4f596b1fa5595d263fd", url="https://pypi.org/packages/f3/c5/dfa09dd2595a2ab2ab4e6fa7bebef9565812722e1980d04b0edce5032066/amply-0.1.4-py3-none-any.whl")
    version("0.1.2", sha256="6e5d53af62772790ba82a989a3de72b8ce5c1cd809613c06f7cb061f7ec34dc8", url="https://pypi.org/packages/7f/11/33cb09557ac838d9488779b79e05a2a3c1f3ce9747cd242ba68332736778/amply-0.1.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-docutils", when="@0.1.4:")
        depends_on("py-pyparsing", when="@0.1.4:")
    # END DEPENDENCIES

