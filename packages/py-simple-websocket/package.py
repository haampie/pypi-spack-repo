# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySimpleWebsocket(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0.0", sha256="1d5bf585e415eaa2083e2bcf02a3ecf91f9712e7b3e6b9fa0b461ad04e0837bc", url="https://pypi.org/packages/6d/ea/288a8ac1d9551354488ff60c0ac6a76acc3b6b60f0460ac1944c75e240da/simple_websocket-1.0.0-py3-none-any.whl")
    version("0.10.1", sha256="62c36bacfd75cc867927bb39d91951342a7234bdfe20f41dd969a3b8bb1413b7", url="https://pypi.org/packages/f6/00/6583d44c59b765c01a14e69260d90c3ca489a47ac8ffc9f1ddf81f1d25f5/simple_websocket-0.10.1-py3-none-any.whl")
    version("0.10.0", sha256="fc1bc56c393a187e7268f8ab99da1a8e8da9b5dfb7769a2f3b8dada00067745b", url="https://pypi.org/packages/61/be/26306666c771f86304c0fc814530ddeabb324ff74ca39d95a638609e8d8d/simple_websocket-0.10.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-wsproto")
    # END DEPENDENCIES

