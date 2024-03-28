# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySphinxBasicNg(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0.0-beta2", sha256="eb09aedbabfb650607e9b4b68c9d240b90b1e1be221d6ad71d61c52e29f7932b", url="https://pypi.org/packages/3c/dd/018ce05c532a22007ac58d4f45232514cd9d6dd0ee1dc374e309db830983/sphinx_basic_ng-1.0.0b2-py3-none-any.whl")
    version("1.0.0-beta1", sha256="ade597a3029c7865b24ad0eda88318766bcc2f9f4cef60df7e28126fde94db2a", url="https://pypi.org/packages/76/aa/eb38c4ad0a46e9fe45604bde48fee569c1954929edb7c3f1d8a3a86fca71/sphinx_basic_ng-1.0.0b1-py3-none-any.whl")
    version("0.0.1-alpha12", sha256="e8b6efd2c5ece014156de76065eda01ddfca0fee465aa020b1e3c12f84570bbe", url="https://pypi.org/packages/61/a8/61c562fdb3114ee16efb95b56ebea69ef5e0d9e1d7bd0bfd815dc034afd1/sphinx_basic_ng-0.0.1a12-py3-none-any.whl")
    version("0.0.1-alpha11", sha256="9aecb5345816998789ef76658a83e3c0a12aafa14b17d40e28cd4aaeb94d1517", url="https://pypi.org/packages/4f/dd/e34062bbf353e51d0a1dbf1cb6a59d9a3f0af16cb258b18170317efe6f02/sphinx_basic_ng-0.0.1a11-py3-none-any.whl")
    version("0.0.1-alpha10", sha256="1c54414336fc80884816cad16379eb4614e59a222f5f76af5302f0d260ec9842", url="https://pypi.org/packages/19/c8/c86924fd108663c6c26aa7821009c21c543a61bb364456514f3b968e119b/sphinx_basic_ng-0.0.1a10-py3-none-any.whl")
    version("0.0.1-alpha9", sha256="533a793e7582418255d81f7495929210d7d18d66783aff32520f03c56adb790e", url="https://pypi.org/packages/a6/18/f21c2b9e7d05a2fedac70e05b809f8149010c07f8862ad9edcbb31042ef3/sphinx_basic_ng-0.0.1a9-py3-none-any.whl")
    version("0.0.1-alpha8", sha256="ae09dd73eecccea6e0f51472b5853447667e44dd8400367043939780cd6845fb", url="https://pypi.org/packages/06/f4/72dc61890ee7e91c73e2193471960e109e97ddeb5d06f6a593ea10804af1/sphinx_basic_ng-0.0.1a8-py3-none-any.whl")
    version("0.0.1-alpha7", sha256="3825763e77a991cc9cf806e0add60a54dc884d6b4f1b31b1c229fe0b0d51c32b", url="https://pypi.org/packages/a2/68/807166af8d2424b9387b1becb2a6177f87b4054a5342c8f09e0a61894a71/sphinx_basic_ng-0.0.1a7-py3-none-any.whl")
    version("0.0.1-alpha6", sha256="f16fa0f1017689ef64c43dbfd16785117f5f8d3fb78d91908b7b9b50a86b4d12", url="https://pypi.org/packages/3d/9c/3ba1fec0cc2de40a0c7d3e048ddbfed6f3d351f4ea7a83fe1d2c0924ad82/sphinx_basic_ng-0.0.1a6-py3-none-any.whl")
    version("0.0.1-alpha5", sha256="f5ad0eeff975ed32ca3373dffa24ec71a9b92af1a35f9ad2244169692139f321", url="https://pypi.org/packages/f2/2d/30a06fa53910c50ca01e30024c674a07cf77437e0f90ecf2d5a018445c32/sphinx_basic_ng-0.0.1a5-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-sphinx@4.0.0:", when="@1:")
        depends_on("py-sphinx@4.0.0:5", when="@0.0.1-alpha11:0")
        depends_on("py-sphinx@4.0.0:4", when="@0.0.1-alpha6:0.0.1-alpha10")
        depends_on("py-sphinx@3.0.0:3", when="@:0.0.1-alpha5")
    # END DEPENDENCIES

