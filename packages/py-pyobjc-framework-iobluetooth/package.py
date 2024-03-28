# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkIobluetooth(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="8c4d6a82d0f550c84dce72188369adb9347ad6ee1c8adef996ee1a8c376c51ee", url="https://pypi.org/packages/ce/ba/cfee8bc9d6df041c5955787feb343b736149e304ba13108bd197b8500d99/pyobjc-framework-IOBluetooth-10.2.tar.gz")
    version("10.1", sha256="9a30554f1c9229ba120b2626d420fb44059e4aa7013c11f36ab9637dc3aba21f", url="https://pypi.org/packages/df/5e/c59299b1653b76bb116e14501c5f0ae4f304075040ea6b35433ab6cc691b/pyobjc-framework-IOBluetooth-10.1.tar.gz")
    version("10.0", sha256="5e6ddcdb8132124fa18c2eb0d0dab9b51e32be14e7ab7a2df12daee3940ec431", url="https://pypi.org/packages/fe/29/a17c86ad9ac3d3d4aa8f10f1f754e93ad86d10b0458415284dad59b1eec6/pyobjc-framework-IOBluetooth-10.0.tar.gz")
    version("9.2", sha256="c0cf643059eac6c783d268f71bd43602c3b2ad714a0218bd2d6b8e10eea0a2b3", url="https://pypi.org/packages/a3/5f/2278fa36e3faac5b80d0691459fad1f5b36a449cc715054f30b7fc4b5e4d/pyobjc-framework-IOBluetooth-9.2.tar.gz")
    version("9.1.1", sha256="1051680e060ecfb489f6e0d6b56e82e3f51ebad22fabde81517e910f3ffe1f14", url="https://pypi.org/packages/7c/6e/b1eae3572ed9c175e94239a95b94fc35f035483d1d523143690292f9464e/pyobjc-framework-IOBluetooth-9.1.1.tar.gz")
    version("9.1", sha256="4cf83c7bbc8e00c42fb86917aadcef9edd269db3a91178e23f42baa13d4982fc", url="https://pypi.org/packages/7d/bf/c95c4ad83670975bc9388553689f67e8654334bd5cea1586922ad0901798/pyobjc-framework-IOBluetooth-9.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
    # END DEPENDENCIES

