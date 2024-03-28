# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySanic(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("23.12.1", sha256="e292293b2663a7afeb380bdc48ab93978468b27deae46ad9561513941eb0311f", url="https://pypi.org/packages/e2/68/07655bda3412fa86cb38d77ae14da231ac0724ebd08b72d905262b9fea3e/sanic-23.12.1-py3-none-any.whl")
    version("23.12.0", sha256="33a92c66c9a533065744fc20339a13974736d2f87d505813076d344b43ae9956", url="https://pypi.org/packages/ca/49/01434a2a88bb1acf912021db16de8d079d407e2ecb97b5c59c93334edaf6/sanic-23.12.0-py3-none-any.whl")
    version("23.6.0", sha256="35136e9cbac1250636f6523326506c4867cbc8635bd15087d3b38fcdbd0bd855", url="https://pypi.org/packages/f3/d7/98494dea060bb04da5c3f4ca3fc5c278391f01c65225546da6c60ee49586/sanic-23.6.0-py3-none-any.whl")
    version("23.3.0", sha256="7cafbd63da9c6c6d8aeb8cb4304addf8a274352ab812014386c63e55f474fbee", url="https://pypi.org/packages/4d/a6/e8c150347207fa5ba2aa728acd90aed66bc4c76a649ad5363b7419aeeb56/sanic-23.3.0-py3-none-any.whl")
    version("22.12.0", sha256="84edf46cc17d13264ccec0ae6622e43087498f95644dc336ade74a2d5e6c88cb", url="https://pypi.org/packages/80/5c/91c44dd9daf62f0068a372d9c3a12945bfcb36eb22aa1b1bfc81ecc0e6e1/sanic-22.12.0-py3-none-any.whl")
    version("22.9.1", sha256="d8905ee1c72759c7b37b1638c3b2b6656573d38156a82a85fd020532749029c1", url="https://pypi.org/packages/77/c7/8862b9953e92f3a4654f5828575f39f95a22e732c47f8775fc280538cd91/sanic-22.9.1-py3-none-any.whl")
    version("22.9.0", sha256="01932dc4cbcd312caf509cb9ffcee8bea4f22b497a5b0c2d4dd5794c4408737a", url="https://pypi.org/packages/ed/79/e08f51fc289ebd5ef289bc78e168a83fe74d67b8a1ce69192785fe536172/sanic-22.9.0-py3-none-any.whl")
    version("22.6.2", sha256="efc3e19eb8c43836ebfd424cb3efc762880b5e3f8fbc07bc125e6d469243a62c", url="https://pypi.org/packages/b1/28/9b6771a4ecf9202f37147a21ff101f658a7a55400ecbd96499e9b620e27f/sanic-22.6.2-py3-none-any.whl")
    version("22.6.1", sha256="a6d684ff572a4a8cdba66a28d128c9693b05dac07954d8dab9e7150eaa6714bc", url="https://pypi.org/packages/d3/c0/1f20e20c793f905c86228eb4c17feec64f2d2364939783a6ac9e593ab4c5/sanic-22.6.1-py3-none-any.whl")
    version("22.6.0", sha256="f6eb181e7a1b9a77a3b916de0f1413eddbe384c59487c2a4bff0c7a41e66e080", url="https://pypi.org/packages/89/f9/56ed8f4cc3f2ab329134117e274176ed77b2c289907fa2271617650be831/sanic-22.6.0-py3-none-any.whl")
    version("20.6.3", sha256="202b75fbf334140cffe559f18772c08263ad97e3534cda3597bc7c3446311526", url="https://pypi.org/packages/63/7c/df37dec6e44cee27f1d597833b1cb69d8bba3593ac2eae3e29ee4c17f1fb/sanic-20.6.3-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-aiofiles@0.6:", when="@20.12:")
        depends_on("py-aiofiles@0.3:", when="@0.5.4:20.9")
        depends_on("py-html5tagger@1.2.1:", when="@23:")
        depends_on("py-httptools@0.0.10:", when="@18:")
        depends_on("py-httpx@0.11.1:0.11", when="@20:20.6")
        depends_on("py-multidict@5:", when="@22:")
        depends_on("py-multidict@4", when="@0.8:19.12.2,20:20.9.0")
        depends_on("py-sanic-routing@23.12:", when="@23.12:")
        depends_on("py-sanic-routing@23:", when="@23.6")
        depends_on("py-sanic-routing@22.8:", when="@22.9:23.3")
        depends_on("py-sanic-routing@22:22.3", when="@22:22.6")
        depends_on("py-tracerite", when="@23:")
        depends_on("py-typing-extensions@4.4:", when="@23.6:")
        depends_on("py-ujson@1.35:", when="@0.8: platform=linux")
        depends_on("py-ujson@1.35:", when="@0.8: platform=freebsd")
        depends_on("py-ujson@1.35:", when="@0.8: platform=darwin")
        depends_on("py-ujson@1.35:", when="@0.8: platform=cray")
        depends_on("py-ujson@1.35:", when="@0.5.4:0.7")
        depends_on("py-uvloop@0.15:", when="@22.12: platform=linux")
        depends_on("py-uvloop@0.15:", when="@22.12: platform=freebsd")
        depends_on("py-uvloop@0.15:", when="@22.12: platform=darwin")
        depends_on("py-uvloop@0.15:", when="@22.12: platform=cray")
        depends_on("py-uvloop@0.5.3:", when="@0.8:19.12.4,20:20.12.1,20.12.4:22.9 platform=linux")
        depends_on("py-uvloop@0.5.3:", when="@0.8:19.12.4,20:20.12.1,20.12.4:22.9 platform=freebsd")
        depends_on("py-uvloop@0.5.3:", when="@0.8:19.12.4,20:20.12.1,20.12.4:22.9 platform=darwin")
        depends_on("py-uvloop@0.5.3:", when="@0.8:19.12.4,20:20.12.1,20.12.4:22.9 platform=cray")
        depends_on("py-uvloop@0.5.3:", when="@0.5.4:0.7")
        depends_on("py-websockets@10:", when="@21.9:")
        depends_on("py-websockets@8.1:8", when="@20.6:20.12.4,21:21.3")
    # END DEPENDENCIES

