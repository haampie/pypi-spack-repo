# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyWhey(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.0.24", sha256="dfd55a3400ce0ab8004b8bcbf06e45f51db8eeb8b2cd7bdf05feeeebc398bd92", url="https://pypi.org/packages/2f/a8/dcc6640fd21781c9f5c2c71f6c589bb9453782826e8b89ec82f4cfb42b74/whey-0.0.24-py3-none-any.whl")
    version("0.0.23", sha256="d3d5c3aa5b5ddb49afcc7fe0447cc6a9ea339040f4a4e9acc948e4f5841422d0", url="https://pypi.org/packages/e3/e0/75fe8cbbb6c50fbed5aadd61be806d3728b244cb9b3d127dfbf87b2f4f5b/whey-0.0.23-py3-none-any.whl")
    version("0.0.22", sha256="4559a07fc45e14b96219a7175b6a5a5e4e505e8b913002bd780d023d85552acd", url="https://pypi.org/packages/df/2b/6188ecce3326d043fdc2140c61ac28e82bff04cb0c5808c068619a3032b1/whey-0.0.22-py3-none-any.whl")
    version("0.0.21", sha256="2a1809112135f610a4fed48e9544c210ad9e84adbd737c5ab618b30196635a62", url="https://pypi.org/packages/2c/13/c12bf5016ae5ea8e5f955f5df7f06ff8e0c0161ce658893166880ddb0678/whey-0.0.21-py3-none-any.whl")
    version("0.0.20", sha256="7cc5664d80847741ebe2655ced8d20903d759f4e0994e441ebb91a1d908a066a", url="https://pypi.org/packages/c6/c1/440b36715b33baace42cc643eca5be16c13fd588e2d585bb835d2f332010/whey-0.0.20-py3-none-any.whl")
    version("0.0.17", sha256="8d16172923d916d0109c11de8db0c8425b99b993b97bfe76da26bbfeb939aecc", url="https://pypi.org/packages/e4/40/094399239108e774aa0192e168ba34fab982202db86352b05fc1aeb71444/whey-0.0.17-py3-none-any.whl")
    version("0.0.16", sha256="9366991c00e94f5aeda2f7c1d60adaa87527f3a54805e1d06944eb646a58a640", url="https://pypi.org/packages/d7/88/5af7bf4b2c752f0883f9955683090fc597ef4ad2f0f46b363c270503a860/whey-0.0.16-py3-none-any.whl")
    version("0.0.15", sha256="0eaa5892fac75df23b2e540e6a256d4e9725f8f43b018530595a16b9d39253ed", url="https://pypi.org/packages/db/c2/5309f867ee491c78f2d622ed8d273fe7036afbf0726de38a3ceddbea565c/whey-0.0.15-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-click@7.1.2:")
        depends_on("py-consolekit@1.4.1:", when="@0.0.23:")
        depends_on("py-consolekit@1.2.2:", when="@0.0.16:0.0.22")
        depends_on("py-consolekit@1.2:", when="@0.0.14:0.0.15")
        depends_on("py-dist-meta", when="@0.0.20:")
        depends_on("py-dom-toml@0.4:", when="@0.0.16:")
        depends_on("py-dom-toml@0.3:", when="@0.0.8:0.0.15")
        depends_on("py-domdf-python-tools@2.8:", when="@0.0.16:")
        depends_on("py-domdf-python-tools@2.7:", when="@0.0.2:0.0.15")
        depends_on("py-first@2.0.2:", when="@:0.0.17")
        depends_on("py-handy-archives", when="@0.0.20:")
        depends_on("py-natsort@7.1.1:")
        depends_on("py-packaging@20.9:")
        depends_on("py-pyproject-parser@0.6.0:", when="@0.0.22:")
        depends_on("py-pyproject-parser@0.3:", when="@0.0.16:0.0.21")
        depends_on("py-pyproject-parser@0.2:", when="@0.0.14:0.0.15")
        depends_on("py-shippinglabel@0.16:", when="@0.0.17:")
        depends_on("py-shippinglabel@0.15:", when="@0.0.16")
        depends_on("py-shippinglabel@0.10:", when="@:0.0.15")
    # END DEPENDENCIES

