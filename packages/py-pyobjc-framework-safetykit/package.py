##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSafetykit(PythonPackage):
    version("10.2", sha256="b5822cda3b1dc0209fa58027551fa17457763275902c7d42fc23d5b13de9ee67", url="https://pypi.org/packages/cb/01/3f54482dd8e4660fd64e11fd1d807639f60b1493b4b79651d27464fed65d/pyobjc-framework-SafetyKit-10.2.tar.gz")
    version("10.1", sha256="f1ac7201d32129c9c1a200724a5d3e75c6da8793f9c8a628be206cdebcd548e5", url="https://pypi.org/packages/24/1d/1a92e8358c310196871d2c2ebcf0fb4285f58adabaf9fb607b2f86abf00b/pyobjc-framework-SafetyKit-10.1.tar.gz")
    version("10.0", sha256="8f6408bdd4ba749d1840700e1a7f1719a5068ae15a2dfdab9d533333b2adda20", url="https://pypi.org/packages/2e/55/5caac06411651b27492ccae3f3abd39aa9360034b6524b1cbd1530aea22d/pyobjc-framework-SafetyKit-10.0.tar.gz")
    version("9.2", sha256="5d64807eef60fc1fe1b88fa396feac8618ca57dd0746da7343681ec9beedb605", url="https://pypi.org/packages/4c/c4/92ca1ea64cb0bfd5b5960b38d1038cfe7b30c106af6f648c584a9d64ddc4/pyobjc-framework-SafetyKit-9.2.tar.gz")
    version("9.1.1", sha256="28ab486fc24f73fecbd627665ae01dd030c72b17f794f67fdf132b0f4bde7923", url="https://pypi.org/packages/fd/a1/39909365da264c7981fa997e530f5678cee4a8511cb100cd7c247093d7a7/pyobjc-framework-SafetyKit-9.1.1.tar.gz")
    version("9.1", sha256="d853d6c1e27e8c00e627376d202a1cdb1dac922481740b9cd48027092c325fdb", url="https://pypi.org/packages/16/bd/815bc38881f7a21ab574e02efb79d7136b5682d4a4d2acd9fa29e0140bb9/pyobjc-framework-SafetyKit-9.1.tar.gz")
    version("9.0.1", sha256="afa2b0012555c9f5b390d1fd8d4283bcb0ede09c9b109f5fdc4143e103a12627", url="https://pypi.org/packages/75/88/27f4a2659d72f4305bdedd9ffb363130dfc741e550932449ae1f4f642a89/pyobjc-framework-SafetyKit-9.0.1.tar.gz")
    version("9.0", sha256="aa6171bbfdc6817ade276eaffdca7dec5dafda1daae341b43a9bbf01211234df", url="https://pypi.org/packages/10/1d/2f303467f30254bf94c4b4504bdfb4208b2662006004a4f3a2f1703e3d0e/pyobjc-framework-SafetyKit-9.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-quartz@10:", when="@10:10.0")

