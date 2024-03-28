# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyYacman(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.9.3", sha256="d77a3a05a58a0bcc993efc64c6b57a2265c1d1f11f65a8e31c71a1e3b8f0e144", url="https://pypi.org/packages/07/ed/d477d1df9728ac9f1af7c912e14da681d5b912024b930139e5a15ac0773e/yacman-0.9.3-py3-none-any.whl")
    version("0.9.2", sha256="5ba2b84cef318febb9a85711c37382c01b85848bc8f53643ac8a61de3a5dd942", url="https://pypi.org/packages/06/34/f8c12705a8d1e8c1fca5958515bbbac79c24742c3b00aab8d3f630bf4d16/yacman-0.9.2-py3-none-any.whl")
    version("0.9.1", sha256="f97872ff6c74705611893133af0a74e47d7e6780b1baa9d4638406d835276dcb", url="https://pypi.org/packages/bb/a7/21ab046bb670d9f37f64f0f1ab41b90117ae194979740d5ad8244f91eee7/yacman-0.9.1-py3-none-any.whl")
    version("0.9.0", sha256="cbf326de789acecf90853ec536d3739330345a28cf5807ab8a48cc4678573f3d", url="https://pypi.org/packages/03/f1/354cb71a0f54b13a08088866f1eb3f20a641af631f08312392fb443d2868/yacman-0.9.0-py3-none-any.whl")
    version("0.8.4", sha256="0cc7aed9e400b9757f937eaf95b2257e822822cdf30626cb35ce7974b2446323", url="https://pypi.org/packages/7d/a6/ff07474f18e129fa1e034558f84391c665038f940cec89efc59e3b4a2b71/yacman-0.8.4-py3-none-any.whl")
    version("0.8.3", sha256="1825a7996febf85c93476c069220d53a195c1b724af6f6c695803775148d9178", url="https://pypi.org/packages/79/02/d4be5f2c4c5e8bed2ac5a917407937d02c3fd19181f3d4c3286a591ebbcd/yacman-0.8.3-py3-none-any.whl")
    version("0.8.2", sha256="96a3f46c35fdee850a03dbfa8220c4d87a3c6a2ca934e4f3a8bee61ae55a540d", url="https://pypi.org/packages/cf/7a/278802de6a06ab5bb206be70c9634ab3ed532e0cd93fb8bd02077403e5fd/yacman-0.8.2-py3-none-any.whl")
    version("0.8.1", sha256="9b5ec8d19771d1470e2f47e74cf4a95db8397bbe156cfbe62a470543d2de4b9a", url="https://pypi.org/packages/b3/69/46be85bafe651bd7c4ff204a30431489363c37fcc7520ed64192f9e1c2bd/yacman-0.8.1-py3-none-any.whl")
    version("0.8.0", sha256="eac7486e638d319c2ff571c5f2b2e01fa37ac88ac3bb70fbd27de0d7f11e679e", url="https://pypi.org/packages/05/8c/0b0e851efd3d3f29d95b7dbec677f6dafd142957fa57f334e764be301e7d/yacman-0.8.0-py3-none-any.whl")
    version("0.7.1", sha256="4030ea7e8e2711d82cfdb284a6a91184cb5b09ed6b44e10bec574b7b23cffbfe", url="https://pypi.org/packages/00/4d/22427ffbae81e0a2e237a6fb3012b7f76aec9b861b1400d66148d6499c6e/yacman-0.7.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-attmap@0.13:", when="@0.7.1:")
        depends_on("py-jsonschema@3.2:", when="@0.8:")
        depends_on("py-oyaml", when="@0.6:0.6.2,0.6.8:")
        depends_on("py-pyyaml@3.13:", when="@0.6:0.6.2,0.6.8:")
        depends_on("py-ubiquerg@0.7:", when="@0.9.3:")
        depends_on("py-ubiquerg@0.6.1:", when="@0.6.9:0.9.2")
    # END DEPENDENCIES

