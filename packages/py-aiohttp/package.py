##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAiohttp(PythonPackage):
    version("3.9.3", sha256="90842933e5d1ff760fae6caca4b2b3edba53ba8f4b71e95dacf2818a2aca06f7", url="https://pypi.org/packages/18/93/1f005bbe044471a0444a82cdd7356f5120b9cf94fe2c50c0cdbf28f1258b/aiohttp-3.9.3.tar.gz")
    version("3.9.2", sha256="b0ad0a5e86ce73f5368a164c10ada10504bf91869c05ab75d982c6048217fbf7", url="https://pypi.org/packages/07/2f/27c9ae85646de72784529a86d2a98c7cfae4ff9eab0004becf47da66c7ec/aiohttp-3.9.2.tar.gz")
    version("3.9.1", sha256="8fc49a87ac269d4529da45871e2ffb6874e87779c3d0e2ccd813c0899221239d", url="https://pypi.org/packages/54/07/9467d3f8dae29b14f423b414d9e67512a76743c5bb7686fb05fe10c9cc3e/aiohttp-3.9.1.tar.gz")
    version("3.9.0", sha256="09f23292d29135025e19e8ff4f0a68df078fe4ee013bca0105b2e803989de92d", url="https://pypi.org/packages/71/80/68f3bd93240efd92e9397947301efb76461db48c5ac80be2423ffa9c20a3/aiohttp-3.9.0.tar.gz")
    version("3.8.6", sha256="b0cf2a4501bff9330a8a5248b4ce951851e415bdcce9dc158e76cfd55e15085c", url="https://pypi.org/packages/fd/01/f180d31923751fd20185c96938994823f00918ee5ac7b058edc005382406/aiohttp-3.8.6.tar.gz")
    version("3.8.5", sha256="b9552ec52cc147dbf1944ac7ac98af7602e51ea2dcd076ed194ca3c0d1c7d0bc", url="https://pypi.org/packages/d6/12/6fc7c7dcc84e263940e87cbafca17c1ef28f39dae6c0b10f51e4ccc764ee/aiohttp-3.8.5.tar.gz")
    version("3.8.4", sha256="bf2e1a9162c1e441bf805a1fd166e249d574ca04e03b34f97e2928769e91ab5c", url="https://pypi.org/packages/c2/fd/1ff4da09ca29d8933fda3f3514980357e25419ce5e0f689041edb8f17dab/aiohttp-3.8.4.tar.gz")
    version("3.8.3", sha256="3828fb41b7203176b82fe5d699e0d845435f2374750a44b480ea6b930f6be269", url="https://pypi.org/packages/ff/4f/62d9859b7d4e6dc32feda67815c5f5ab4421e6909e48cbc970b6a40d60b7/aiohttp-3.8.3.tar.gz")
    version("3.8.2", sha256="599aa2ce967bea2580588833bf08d2df5930cd2ccb618e8d96dd67dbe063b692", url="https://pypi.org/packages/1a/0c/caa046ebcaa23d655ec0dce108ef25348dd6b7c63aaedc8cb182658e6947/aiohttp-3.8.2.tar.gz")
    version("3.8.1", sha256="fc5471e1a54de15ef71c1bc6ebe80d4dc681ea600e68bfd1cbce40427f0b7578", url="https://pypi.org/packages/5a/86/5f63de7a202550269a617a5d57859a2961f3396ecd1739a70b92224766bc/aiohttp-3.8.1.tar.gz")
    version("3.8.0", sha256="d3b19d8d183bcfd68b25beebab8dc3308282fe2ca3d6ea3cb4cd101b3c279f8d", url="https://pypi.org/packages/48/1a/ba9542a545aed4b0b6ef128561f68dd3c2812ff5abfa9ed5b96547a728ea/aiohttp-3.8.0.tar.gz")
    version("3.7.4", sha256="5d84ecc73141d0a0d61ece0742bb7ff5751b0657dab8405f899d3ceb104cc7de", url="https://pypi.org/packages/7a/95/eb60aaad7943e18c9d091de93c9b0b5ed40aa67c7d5e3c5ee9b36f100a38/aiohttp-3.7.4.tar.gz")
    version("3.6.2", sha256="259ab809ff0727d0e834ac5e8a283dc5e3e0ecc30c4d80b3cd17a4139ce1f326", url="https://pypi.org/packages/00/94/f9fa18e8d7124d7850a5715a0b9c0584f7b9375d331d35e157cee50f27cc/aiohttp-3.6.2.tar.gz")

    with default_args(type="run"):
        depends_on("py-aiosignal@1.1.2:", when="@3.8.6:3")
        depends_on("py-async-timeout@4.0.0:", when="@3.9:3 ^python@:3.10")
        depends_on("py-async-timeout@4.0.0-alpha3:", when="@3.8.6:3.8")
        depends_on("py-async-timeout@3", when="@3.2:3.6.2,4:")
        depends_on("py-attrs@17.3:", when="@3.0.3:3.6.2,3.8.6:")
        depends_on("py-chardet@2:3", when="@3.0.0:3.6.2,4:")
        depends_on("py-charset-normalizer@2:", when="@3.8.6:3.8")
        depends_on("py-frozenlist@1.1.1:", when="@3.8.6:3")
        depends_on("py-multidict@4.5:", when="@3.8.6:3")
        depends_on("py-multidict@4.5:4", when="@3.6.1-beta3:3.6.2,4.0.0-alpha1:")
        depends_on("py-yarl@1:", when="@3.0.0:3.6.2,3.8.6:")

