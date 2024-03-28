# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySanic(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("20.6.3", sha256="202b75fbf334140cffe559f18772c08263ad97e3534cda3597bc7c3446311526", url="https://pypi.org/packages/63/7c/df37dec6e44cee27f1d597833b1cb69d8bba3593ac2eae3e29ee4c17f1fb/sanic-20.6.3-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-aiofiles@0.3:", when="@0.5.4:20.9")
        depends_on("py-httptools@0.0.10:", when="@18:")
        depends_on("py-httpx@0.11.1:0.11", when="@20:20.6")
        depends_on("py-multidict@4", when="@0.8:19.12.2,20:20.9.0")
        depends_on("py-ujson@1.35:", when="@0.8: platform=linux")
        depends_on("py-ujson@1.35:", when="@0.8: platform=freebsd")
        depends_on("py-ujson@1.35:", when="@0.8: platform=darwin")
        depends_on("py-ujson@1.35:", when="@0.8: platform=cray")
        depends_on("py-ujson@1.35:", when="@0.5.4:0.7")
        depends_on("py-uvloop@0.5.3:", when="@0.8:19.12.4,20:20.12.1,20.12.4:22.9 platform=linux")
        depends_on("py-uvloop@0.5.3:", when="@0.8:19.12.4,20:20.12.1,20.12.4:22.9 platform=freebsd")
        depends_on("py-uvloop@0.5.3:", when="@0.8:19.12.4,20:20.12.1,20.12.4:22.9 platform=darwin")
        depends_on("py-uvloop@0.5.3:", when="@0.8:19.12.4,20:20.12.1,20.12.4:22.9 platform=cray")
        depends_on("py-uvloop@0.5.3:", when="@0.5.4:0.7")
        depends_on("py-websockets@8.1:8", when="@20.6:20.12.4,21:21.3")
    # END DEPENDENCIES

