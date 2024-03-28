# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBxPython(PythonPackage):
    # BEGIN VERSIONS
    version("0.11.0", sha256="2cf8872572817e0d36145cc2711889df5729987ffed4e51280da1e3c2ccb9429", url="https://pypi.org/packages/00/55/edbf83af071f44259d0d1f476e216f8e25dda802cc0d2911608e7f927695/bx-python-0.11.0.tar.gz")
    version("0.10.0", sha256="bfe9541d7b18a98e907b085e31f58d3989fbca4dc667c4ae48c33b753e0e2da8", url="https://pypi.org/packages/31/0a/dc1d064bb81c1f88a42d6b68d82ec9525289f0944def525714f195a4da19/bx-python-0.10.0.tar.gz")
    version("0.9.0", sha256="fe545c44d2ea74b239d41e9090618aaf6a859d1a1f64b4a21b133cb602dfdb49", url="https://pypi.org/packages/b1/79/6159768ef08fc5d037c184bc964d7a79984ac99d0c076b70251c89964550/bx-python-0.9.0.tar.gz")
    version("0.8.13", sha256="5989170d13367e9f811014803bafdbcc893024d63e98b66f734511e4f9e90c7d", url="https://pypi.org/packages/3b/57/f2602114260bd51004c6025f24db811ddd2077c72fc7b62da3b1d1750268/bx-python-0.8.13.tar.gz")
    version("0.8.12", sha256="60234745e6a38268d2bda242ade3b8a518848e3e642ad3bfb67f0ce7cda81f48", url="https://pypi.org/packages/27/03/bc0552367cab2da0e2634e8150373ea12b6bc497afdb849eea7ad1b7b645/bx-python-0.8.12.tar.gz")
    version("0.8.11", sha256="7f26c2a5516b999f4330887f2b126608b4d96ed0f1de6e62ee59f3d066586974", url="https://pypi.org/packages/09/06/34d30efc7ee4f94945335a1aa4c5fc461e406f3c9f9f73f6102d26bf1932/bx-python-0.8.11.tar.gz")
    version("0.8.10", sha256="f1e17b85ee5830b6e634d3f7e7f95adab8b713b9d10511feca4d8bd921c27304", url="https://pypi.org/packages/e9/0d/cdde9b57ae1f62da0302b73e3e7983723f081b8098f745a9115af3bc89ab/bx-python-0.8.10.tar.gz")
    version("0.8.9", sha256="7a6c8d41daf81c92601f00c0065c1b018a0b4e349abf78d662d4191a51ac8588", url="https://pypi.org/packages/01/d1/7c8a1b1a46e5c0a7875d02bbc8087755edc72ffbe5adb20551c40c7b5e71/bx-python-0.8.9.tar.gz")
    version("0.8.8", sha256="ad0808ab19c007e8beebadc31827e0d7560ac0e935f1100fb8cc93607400bb47", url="https://pypi.org/packages/5c/7f/03375de727d21c5aecd4ee210ce458a045203e723999f706325e06a81c4f/bx-python-0.8.8.tar.gz")
    version("0.8.7", sha256="10756beaf214146ed422db4bca3d56523680123105f5e0e6aab23a3786124e3b", url="https://pypi.org/packages/68/90/d0e158fa1a50bd4907aeefcab424cc2acd6a46c2aafe78bad39cd2c6bdda/bx-python-0.8.7.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@0.8.3:0.8.9,0.11:")
        depends_on("py-six@1.13:", when="@0.8.9")
        depends_on("py-six", when="@0.8.3:0.8.8")
    # END DEPENDENCIES

