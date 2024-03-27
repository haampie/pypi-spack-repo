##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkBackgroundassets(PythonPackage):
    version("10.2", sha256="97ad7b0c693e406950c0c4af2edc9320eac9aef7fdf33274903f526b4682fcb7", url="https://pypi.org/packages/4e/b0/d8400cf00af060d0ad5163ed423aaba15779276a557f29099814f68d9c5c/pyobjc-framework-BackgroundAssets-10.2.tar.gz")
    version("10.1", sha256="0a770f77f7fe6d715cf02e95a5efb70895ee19736cf0fa0ecbb3c320f4fa3430", url="https://pypi.org/packages/7e/5e/388a0d89c3c483549c7a1b7dbaf00abdc49855a6570b300533fd04731da5/pyobjc-framework-BackgroundAssets-10.1.tar.gz")
    version("10.0", sha256="d2b9a7a46a632d0adeaa6ba411ddb829d8efa3273a93d7918cc143dfe9dfb54b", url="https://pypi.org/packages/49/52/06996f40c7c119a8fcc849d0b1df92f29555efd1bc60de5b1af61f921bb0/pyobjc-framework-BackgroundAssets-10.0.tar.gz")
    version("9.2", sha256="087b77a31d7c5cd4ce9f8c4a130c7cefda78fdf7a703609bc2554e3cf44aed9c", url="https://pypi.org/packages/76/9d/a58c2c921721ba26aabf791cb14429cb7a71a72cc5fb7a77e03ce210e3aa/pyobjc-framework-BackgroundAssets-9.2.tar.gz")
    version("9.1.1", sha256="382e0f74a98012c3efb6ed7bab829db77f8c99ad6aaf567e7dc9f37f8715d4f9", url="https://pypi.org/packages/d5/df/4bd6aff654f642b886034f0e4842eef7d7efc9b95c68b9dac28d059f1e38/pyobjc-framework-BackgroundAssets-9.1.1.tar.gz")
    version("9.1", sha256="18e0fd156eb75d87ee87b701649a8aae0ae1e4f6fe7457fe982b2ec7cc37d66f", url="https://pypi.org/packages/cd/62/979705479806c58320908647525fd5e3040e2245cfc0084581831105b19a/pyobjc-framework-BackgroundAssets-9.1.tar.gz")
    version("9.0.1", sha256="354c3602e55f93fd7bb08bf6468db62972c02da8b05bfa3e41dd0aa532e085ce", url="https://pypi.org/packages/af/4b/171ec6383c5e17cce4fee6c47b8ca69b7ce90bf412ae8232573a3709b224/pyobjc-framework-BackgroundAssets-9.0.1.tar.gz")
    version("9.0", sha256="52a37e47fac775e63c80df57bdf1a0c2ce248ec8b7a617a3278f5997ae4bbb6b", url="https://pypi.org/packages/9f/4b/132a40f18f13cd82c0ccb7cec7a0564e903bc2186961977d7ec6814d91d3/pyobjc-framework-BackgroundAssets-9.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")

