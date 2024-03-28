# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyWhey(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.0.24", sha256="dfd55a3400ce0ab8004b8bcbf06e45f51db8eeb8b2cd7bdf05feeeebc398bd92", url="https://pypi.org/packages/2f/a8/dcc6640fd21781c9f5c2c71f6c589bb9453782826e8b89ec82f4cfb42b74/whey-0.0.24-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-click@7.1.2:")
        depends_on("py-consolekit@1.4.1:", when="@0.0.23:")
        depends_on("py-dist-meta", when="@0.0.20:")
        depends_on("py-dom-toml@0.4:", when="@0.0.16:")
        depends_on("py-domdf-python-tools@2.8:", when="@0.0.16:")
        depends_on("py-handy-archives", when="@0.0.20:")
        depends_on("py-natsort@7.1.1:")
        depends_on("py-packaging@20.9:")
        depends_on("py-pyproject-parser@0.6.0:", when="@0.0.22:")
        depends_on("py-shippinglabel@0.16:", when="@0.0.17:")
    # END DEPENDENCIES

