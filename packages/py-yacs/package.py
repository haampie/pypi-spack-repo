# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyYacs(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.1.8", sha256="99f893e30497a4b66842821bac316386f7bd5c4f47ad35c9073ef089aa33af32", url="https://pypi.org/packages/38/4f/fe9a4d472aa867878ce3bb7efb16654c5d63672b86dc0e6e953a67018433/yacs-0.1.8-py3-none-any.whl")
    version("0.1.7", sha256="c8e228c7c74298d0dcc820e217dc9a743b757e148a4a7abb9a1d831beb143caf", url="https://pypi.org/packages/81/3b/40e876afde9f5ffa1cfdce10565aba85b0dc2e067ed551dfb566cfee6d4d/yacs-0.1.7-py3-none-any.whl")
    version("0.1.6", sha256="77cb0f9a638dca68b0e9d49e3d51a986dc5741651316df8608d5127b92278e9a", url="https://pypi.org/packages/2f/51/9d613d67a8561a0cdf696c3909870f157ed85617fea3cff769bb7de09ef7/yacs-0.1.6-py3-none-any.whl")
    version("0.1.5", sha256="d420272bed407e3bd9b24f747dfc8b52268c34f565d1c996b42becb3f0e54b0b", url="https://pypi.org/packages/54/d4/7b12a88a06adef912f95d1e08edbdb70ee63e2160244bc311b6e51ef3842/yacs-0.1.5-py3-none-any.whl")
    version("0.1.4", sha256="eca099dcad2b97b383abfac5015cb10a0bc322403e223125756fda05abab03c8", url="https://pypi.org/packages/0a/b2/163054e1e789f6affb43761ccedac47cac3ae8e02944e514187f2c52628a/yacs-0.1.4-py3-none-any.whl")
    version("0.1.3", sha256="a4a8bdc15d758a04f5bb02244045578e2d6731b433b06791be820b96d76925df", url="https://pypi.org/packages/27/4e/7d1ea3d7c38a4e3ece12b879399234d87ee36137e32a5f202055ffd8574d/yacs-0.1.3-py3-none-any.whl")
    version("0.1.2", sha256="084fec88a895ed31537d83acff764d815fcda450874d297f08aa20c6f11c07cf", url="https://pypi.org/packages/09/51/a4b81c0cd3a4327665410bae9cd4497cd29a95b6cc35df9a64d892a25389/yacs-0.1.2-py3-none-any.whl")
    version("0.1.1", sha256="c09014e8a6028e09b01dd1d96070afe4796062a5b6d24fe6f3de15857eed0228", url="https://pypi.org/packages/38/7f/f25af268bbb25f810a4e741e6e5ddd742ebc1c62b93d090b2355d961577f/yacs-0.1.1-py3-none-any.whl")
    version("0.1.0", sha256="218098c073537591fca61de85e759bc971c789b8a9782d687a0fa8d16b5fb920", url="https://pypi.org/packages/ad/f1/17ef089734ed17c4bfa0112d7860a7be9eb6814b42f9fb0c91d2f4de3454/yacs-0.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyyaml", when="@0.1.2:")
    # END DEPENDENCIES

