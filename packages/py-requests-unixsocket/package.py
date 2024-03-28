# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRequestsUnixsocket(PythonPackage):
    # BEGIN VERSIONS
    version("0.3.0", sha256="c685c680f0809e1b2955339b1e5afc3c0022b3066f4f7eb343f43a6065fc0e5d", url="https://pypi.org/packages/b3/63/e9e81d5e7370d46f08407c37399b507725125587b01fff46b4da5ddd3a4a/requests_unixsocket-0.3.0-py2.py3-none-any.whl")
    version("0.2.0", sha256="014d07bfb66dc805a011a8b4b306cf4ec96d2eddb589f6b2b5765e626f0dc0cc", url="https://pypi.org/packages/d0/63/97662a6f7175c08381447a09f6bc35464075f0ea6549cf6daf2668b51f04/requests_unixsocket-0.2.0-py2.py3-none-any.whl")
    version("0.1.5", sha256="a91bc0138f61fb3396de6358fa81e2cd069a150ade5111f869df01d8bc9d294c", url="https://pypi.org/packages/f3/94/67d781fb32afbee0fffa0ad9e16ad0491f1a9c303e14790ae4e18f11be19/requests-unixsocket-0.1.5.tar.gz")
    version("0.1.4", sha256="ba2c86a7e993ee8495f922a31d0cab6bc69f1ee33c5cca58e2ae85c2a6234368", url="https://pypi.org/packages/c4/0f/449d2d43016596ae3a30199b1d9b0373a30afb8d1a29d56a2a788c263ff7/requests-unixsocket-0.1.4.tar.gz")
    version("0.1.3", sha256="9a0f52c39b7df8e004b70077f3efd54062077e21063c9303e400a2d7ca6f1619", url="https://pypi.org/packages/83/dd/c8b731e0458ee311976cca9a64f32ddf20a4647e596e7b397f2ddf234325/requests-unixsocket-0.1.3.tar.gz")
    version("0.1.2", sha256="05744a17d59d9dd3632bc5ce342315a4df83d79e4c3fffa5214cd7df01046315", url="https://pypi.org/packages/0f/08/3f84dff1ff841ac5ea86af00c31dd08a877b14881a38dd7d3905c21898a0/requests-unixsocket-0.1.2.tar.gz")
    version("0.1.1", sha256="6d9dbd358e6ebe8df283abccd41f12185e170eedb0543265eeb3e70fbe6b22fa", url="https://pypi.org/packages/7c/b8/3789c2cc817d16ef1bd0441e26cbc3c3a49afe50d396d93cbf20b64b05f3/requests-unixsocket-0.1.1.tar.gz")
    version("0.1.0", sha256="aa2d4772e188b93da5d9b8f25c3bd92a8ed85afefb9bd8083f87580e2233def7", url="https://pypi.org/packages/af/0b/66d2c7cfd63f2b7032fc31fe1cf00785ad7f4ade55c853b7fe6abfe4fb33/requests-unixsocket-0.1.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-requests@1.1:", when="@0.2:")
        depends_on("py-urllib3@1.8:", when="@0.2")
    # END DEPENDENCIES

