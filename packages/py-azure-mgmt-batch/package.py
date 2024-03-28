# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtBatch(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("17.3.0", sha256="8cd70837831c2681a6fa2d0b3232bbec9df69627283c6abe1c336fd230249a12", url="https://pypi.org/packages/46/0d/f7d816ad7eb722c4be1a926cbc70d67a581914778918f04a4052834f94fe/azure_mgmt_batch-17.3.0-py3-none-any.whl")
    version("17.2.0", sha256="73e34bfd8cdf917b15119c6d043d223a0ba22d916d95510d582475a4694af479", url="https://pypi.org/packages/cf/8c/b46bf78e397b7261e8dc00513149818ede39600162354ea231b73441270c/azure_mgmt_batch-17.2.0-py3-none-any.whl")
    version("17.1.0", sha256="a987d44766b3ca09cb507a30b45c98bae08ecd86b53151e24e4f81a56cf45f9b", url="https://pypi.org/packages/6f/de/ad4f433c419340ab0d66e02d7e3ad904bb8d1d54d0de014085e3f84e8cce/azure_mgmt_batch-17.1.0-py3-none-any.whl")
    version("17.0.0", sha256="45480e4dbad82b27780c85643b73da5f0b84c8e12369c66f19a4536f296d9bd2", url="https://pypi.org/packages/4f/36/fa03d3bc0f073a57ccc7718eaacf60e5eeeadfb72c8ca253f2fa8a1d85ca/azure_mgmt_batch-17.0.0-py3-none-any.whl")
    version("16.2.0", sha256="b1307cbb79d23fbd53ea80b45cf4ff7653ed31a0e725f294c1202f304506ad1c", url="https://pypi.org/packages/b2/a8/17eb2b5e2956d4f027ed69a377e91d32e4f33f57edbe72405f56fa35259f/azure_mgmt_batch-16.2.0-py3-none-any.whl")
    version("16.1.0", sha256="6b39dab6f6c6e7845a9fbefa90f2dad0bddcf7b070c48cd6e4aa62979ce73049", url="https://pypi.org/packages/5a/94/4ada9399b91a5ca864068408892519f8c7f49c233b986e464493d50ac395/azure_mgmt_batch-16.1.0-py3-none-any.whl")
    version("16.0.0", sha256="71f914fe1d74f0c9134a8779a790cc5443a5051814ef0d87b097b16cc85d646b", url="https://pypi.org/packages/81/36/2320ff86113d4aa33b23b29b1c53938ddc17109652d0172ec521a065ca1d/azure_mgmt_batch-16.0.0-py2.py3-none-any.whl")
    version("15.0.0", sha256="25e534eaae5e848bffb978038cd412a6478cd3f08220d361aa1981b98cb39704", url="https://pypi.org/packages/bf/48/aa5b7c7172551c5d8ba186faf1490d307a584d62b9ab48c6c97e6b35b0b7/azure_mgmt_batch-15.0.0-py2.py3-none-any.whl")
    version("14.0.0", sha256="622a850d10623f8c58f44e85fb25d685e8b9d8bb0fc9664f1cf4272bacfccfb9", url="https://pypi.org/packages/b1/81/e104654bc6c9f10203d7011a3459355e604b7b1ce94fbf2596eabcf4812c/azure_mgmt_batch-14.0.0-py2.py3-none-any.whl")
    version("10.0.1", sha256="b8ce49f33561d150b3ed329ab3043e59a6bef7a2787244e65e5667aa495cfea0", url="https://pypi.org/packages/82/9e/cbdea6ccb90c02f86c68079d5b956200e97156babe4e6eca397e074665e7/azure_mgmt_batch-10.0.1-py2.py3-none-any.whl")
    version("9.0.0", sha256="79c2b46b88559e0b1d34e8d7e945608397202c8de2bfbfb89e8cfced84fb89e4", url="https://pypi.org/packages/47/6e/a1469a8ff5dd1043c2414450e1c9e6cdf13bebddc01c9bdbb58c3de60968/azure_mgmt_batch-9.0.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-common@1.1:", when="@5:")
        depends_on("py-azure-mgmt-core@1.3.2:", when="@17:")
        depends_on("py-azure-mgmt-core@1.3.0:", when="@16.1:16")
        depends_on("py-azure-mgmt-core@1.2:", when="@14:16.0")
        depends_on("py-isodate@0.6.1:", when="@17.1:")
        depends_on("py-msrest@0.7.1:", when="@17:17.0")
        depends_on("py-msrest@0.6.21:", when="@16")
        depends_on("py-msrest@0.5:", when="@6:15")
        depends_on("py-msrestazure@0.4.32:", when="@6:10")
    # END DEPENDENCIES

