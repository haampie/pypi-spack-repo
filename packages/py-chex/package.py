# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyChex(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.1.86", sha256="251c20821092323a3d9c28e1cf80e4a58180978bec368f531949bd9847eee568", url="https://pypi.org/packages/e6/ed/625d545d08c6e258d2d63a93a0bf8ed8a296c09d254208e73f9d4fb0b746/chex-0.1.86-py3-none-any.whl")
    version("0.1.85", sha256="32c96719aa94045339174138a6aec14aed2630a8a17fb2633ad3eb868890551d", url="https://pypi.org/packages/9a/82/257141baabfaf8b0187521ddb83e996f2a71cdd4f7796d9599ca3e3ea4a9/chex-0.1.85-py3-none-any.whl")
    version("0.1.84", sha256="a41603ed1a3c1d59c15aa017238b36b2437c82ef0a69d5bc4b1140fb32610ea5", url="https://pypi.org/packages/41/ab/662e3961529746ea9410f25cbea3d1565bed16a5e94bfa3e8b906e8f5337/chex-0.1.84-py3-none-any.whl")
    version("0.1.83", sha256="d51485018b064c0cca2b9db8e96a74368ab4bea96f023fa95b916ada1ec27b0e", url="https://pypi.org/packages/8b/c5/ab99c61d1384f89fe0d89b4b105c1ad22dab98cfe8c78136fb8c3f75f75b/chex-0.1.83-py3-none-any.whl")
    version("0.1.82", sha256="4df8f087e30c3879c15d3765f9081d5996e57682fa1fbaa8a16a1eab6f6eb2d0", url="https://pypi.org/packages/84/c9/a2182cbf8bc066de9433930c41e76b7f4e904f155c5881235dbb54f8148b/chex-0.1.82-py3-none-any.whl")
    version("0.1.81", sha256="b78b60d440b9172cbf7a15f2c126eac21b3761752bc9f901ab4e3c63530e1554", url="https://pypi.org/packages/f4/c2/e66bf06bff9d2fad600b0daebf54ecb5d7e2c40eae25968773e3ce292814/chex-0.1.81-py3-none-any.whl")
    version("0.1.8", sha256="390321e6e3dd6923411029472c36fb809b04f3e2f5aab1605942b0853458883c", url="https://pypi.org/packages/c1/90/1eea87b796c8bef63de9d7e6a022a6fdffcec02d3f08339a3f5b36726d0b/chex-0.1.8-py3-none-any.whl")
    version("0.1.7", sha256="9f583015303b1205443843c0b55849bb287f1dfdbd22d9907b1ebb04f964d93e", url="https://pypi.org/packages/03/5f/3b0fd7ea23aa13a61430256234cf43895c29d6d0bbe7e98b68c6eaebbd48/chex-0.1.7-py3-none-any.whl")
    version("0.1.6", sha256="5e04a28fcab3c2c0fb05431c6e646e8e4889cacb3e1670369e556f12029cf785", url="https://pypi.org/packages/ff/32/23b2b468c7f85fc84ddcb73e5170f781477c30a4da5c13e882abe5506a9c/chex-0.1.6-py3-none-any.whl")
    version("0.1.5", sha256="b3321184850d5fc29b2eca63087cdbdd83a1b3e4f33c1314ff8b3b8bd67abbca", url="https://pypi.org/packages/38/ee/bce278eceda025e8f7d1939b5a5fd8ebfe4f3307fe33dab7c243b2bc3668/chex-0.1.5-py3-none-any.whl")
    version("0.1.0", sha256="7fd187a68285aae9a35e314817ba037b6e0996da782a40689cfafae1fe7d0536", url="https://pypi.org/packages/09/dc/c10c71ec92a4a0e31b4bb0b930389ad4f2c7ad82e7c74aca9bd5bcfc7842/chex-0.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.1.8:")
        depends_on("py-absl-py@0.9:")
        depends_on("py-dm-tree@0.1.5:", when="@0.0.3:0.1.81")
        depends_on("py-jax@0.4.16:", when="@0.1.83:")
        depends_on("py-jax@0.4.6:", when="@0.1.7:0.1.82")
        depends_on("py-jax@0.1.55:", when="@:0.1.6")
        depends_on("py-jaxlib@0.1.37:")
        depends_on("py-numpy@1.24.1:", when="@0.1.83:")
        depends_on("py-numpy@1.25.0:", when="@0.1.81:0.1.82")
        depends_on("py-numpy@1.18.0:", when="@:0.1.8")
        depends_on("py-setuptools", when="@0.1.85: ^python@3.12:")
        depends_on("py-toolz@0.9:")
        depends_on("py-typing-extensions@4.2:", when="@0.1.8:")
        depends_on("py-typing-extensions@4.2:", when="@0.1.6:0.1.7 ^python@:3.10")
    # END DEPENDENCIES

