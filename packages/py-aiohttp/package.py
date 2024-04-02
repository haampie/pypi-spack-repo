# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAiohttp(PythonPackage):
    # BEGIN VERSIONS
    version("3.8.4", sha256="bf2e1a9162c1e441bf805a1fd166e249d574ca04e03b34f97e2928769e91ab5c", url="https://pypi.org/packages/c2/fd/1ff4da09ca29d8933fda3f3514980357e25419ce5e0f689041edb8f17dab/aiohttp-3.8.4.tar.gz")
    version("3.8.1", sha256="fc5471e1a54de15ef71c1bc6ebe80d4dc681ea600e68bfd1cbce40427f0b7578", url="https://pypi.org/packages/5a/86/5f63de7a202550269a617a5d57859a2961f3396ecd1739a70b92224766bc/aiohttp-3.8.1.tar.gz")
    version("3.8.0", sha256="d3b19d8d183bcfd68b25beebab8dc3308282fe2ca3d6ea3cb4cd101b3c279f8d", url="https://pypi.org/packages/48/1a/ba9542a545aed4b0b6ef128561f68dd3c2812ff5abfa9ed5b96547a728ea/aiohttp-3.8.0.tar.gz")
    version("3.7.4", sha256="5d84ecc73141d0a0d61ece0742bb7ff5751b0657dab8405f899d3ceb104cc7de", url="https://pypi.org/packages/7a/95/eb60aaad7943e18c9d091de93c9b0b5ed40aa67c7d5e3c5ee9b36f100a38/aiohttp-3.7.4.tar.gz")
    version("3.6.2", sha256="259ab809ff0727d0e834ac5e8a283dc5e3e0ecc30c4d80b3cd17a4139ce1f326", url="https://pypi.org/packages/00/94/f9fa18e8d7124d7850a5715a0b9c0584f7b9375d331d35e157cee50f27cc/aiohttp-3.6.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-async-timeout@3", when="@:3.6.2,4:")
        depends_on("py-attrs@17.3:", when="@:3.6.2,3.8.6:")
        depends_on("py-chardet@2:3", when="@:3.6.2,4:")
        depends_on("py-idna-ssl@1:", when="@:3.6.2,3.8.6:3.8,4: ^python@:3.6")
        depends_on("py-multidict@4.5:4", when="@3.6.1-beta3:3.6.2,4.0.0-alpha1:")
        depends_on("py-typing-extensions@3.6.5:", when="@:3.6.2,4:4.0.0-alpha0 ^python@:3.6")
        depends_on("py-yarl@1:", when="@:3.6.2,3.8.6:")
    # END DEPENDENCIES

