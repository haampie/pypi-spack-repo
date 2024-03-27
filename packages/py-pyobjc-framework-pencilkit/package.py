##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkPencilkit(PythonPackage):
    version("10.2", sha256="d3e605f104548f26c708957ab7939a64147c422c35d45c4ff4c8d01b5c248c4d", url="https://pypi.org/packages/21/ca/9c817b4956e90886d867a25608756e5c8ed05281fb7e8933cefa9872a551/pyobjc_framework_PencilKit-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="baf856d274653d74d66099ae81005ddb3923f7128d36d2f87100481cbb8b2b27", url="https://pypi.org/packages/a9/c6/439500193eebfc0c408cccb265c13984a9d186cda86ef0d93cd4332c0edb/pyobjc_framework_PencilKit-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="162bd4797749247e34414ddfb91336b97ff8c31fa79abe27a2885188cbe3fed8", url="https://pypi.org/packages/e7/36/02f71ac6ff4313efe3b91d31e56e4aa8b875a9924e4a3cce6afb9fa9d5bf/pyobjc_framework_PencilKit-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="c0920c3a9ecf1cc6e3b67b5e928aa23d5f61ce4218440c167df86989a2b01291", url="https://pypi.org/packages/74/de/11fb292985f38760a49969cc6e5f98a919ac81b438238124e8bf9ad8a34b/pyobjc_framework_PencilKit-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="1639404afa1f9422a3f48914d24aa6d7b6c436eb1c437eac4820cd2c530fdd43", url="https://pypi.org/packages/bd/bf/1934ed831e01bf2556f0c49372716cf824ff0c658b82347b331ed433f564/pyobjc_framework_PencilKit-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="194398b1d80cfc458bf5fbb4346a06b3d19101447f4613266fe1dd40fbb25ada", url="https://pypi.org/packages/00/ee/9b4d1a6d34b02d085101bf6436d367192525ac127467a1cb6b4377ceaee2/pyobjc_framework_PencilKit-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="d5d96757ca9170a373af4e5cc52d791aefe3a4f9e6d09034459d684e61aadf37", url="https://pypi.org/packages/6b/27/82fd7e150dc1bc89762bc50c9ea0943775504b0445bec0c597ae42016e56/pyobjc_framework_PencilKit-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="41643e6a233213adede31f1dd3bff128de087b077a7b31b5395e6ab6458133da", url="https://pypi.org/packages/5e/13/bba57cbda3eec82a89077ee483fe222a6ecc9c0f24e368e00a8fab3be77d/pyobjc_framework_PencilKit-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="a8bf72c5db694e737a94062826486c1cbb5f074a54b2d7d6795d3ffc1b879d43", url="https://pypi.org/packages/b7/c6/e9cab84597cc3885b031c8d072eb6e9e3720b6c67b6670e1124c7f792cf8/pyobjc_framework_PencilKit-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="9a2eb68a4ce3d2e627516373ab4c282e94bb0dd9530c11947a538ca0fb9b04ed", url="https://pypi.org/packages/34/bf/6b019fea18d31a60ba7c3805feeb3cbdca1c017d975304588b074f70d2c4/pyobjc_framework_PencilKit-8.5-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-core@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-core@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-core@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-core@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-core@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-core@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-core@8.5:", when="@8.5:8.5.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-cocoa@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-cocoa@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-cocoa@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-cocoa@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-cocoa@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-cocoa@8.5:", when="@8.5:8.5.0")

