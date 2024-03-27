##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkLatentsemanticmapping(PythonPackage):
    version("10.2", sha256="dadd4352b9af681dd85d04712a6cf1d2c574acbf0b8178c35f42231ec8c5a6d1", url="https://pypi.org/packages/5e/29/1eb7ceaff33e1aabb3559597578755d3c4c423adca8ae4f7425268588f9b/pyobjc_framework_LatentSemanticMapping-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="f0b14a1a2a6d6b25b902a2cc5949f0145926f0b0a3132d17210b1a580dc7f0f5", url="https://pypi.org/packages/70/8b/20b74fa79d2cb83e69525b60e375b9284f76579e2e8393f5e98ea054b729/pyobjc_framework_LatentSemanticMapping-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="01dc811aad11914c1e01daa018ef1833da144095f42ca2dfe810e4768a540a86", url="https://pypi.org/packages/bb/2e/8bc5e5ad439175e74dda5aace8bb1e6cdab84190c20b78bc3056aa09f7b5/pyobjc_framework_LatentSemanticMapping-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="bf68a732cec7d24a4e4fd5d96dce82cd37a765daa4f33e3a0d1190b9e4401bdf", url="https://pypi.org/packages/55/4d/20e0d143a0c283588600f77757f1e27b50f7e9cd7e91639e905901d47461/pyobjc_framework_LatentSemanticMapping-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="387f3c7ebb979651d7279e247df20a0e04eff824d536d21e0b507381d1f12c77", url="https://pypi.org/packages/06/94/109724fac8f6b28a5e96371eb43ccd15a2fd61660fa73e518862fc1bb839/pyobjc_framework_LatentSemanticMapping-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="eef67a90f870e816885b44352d610fd60f5304a609ad40c2c3d20741a3e0ad10", url="https://pypi.org/packages/18/06/5f52b7797e3cdba7515d37cca46b7e4350575bd9eeb102c4b29ab971fc03/pyobjc_framework_LatentSemanticMapping-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="04a77d254c3692984560455aa917caa813b8dd385114eff347d628a7ef39a5a0", url="https://pypi.org/packages/66/83/03aed3d2a9850f8c89c62c84bd718171afb1e3fa4291e4ae0beb01cca61d/pyobjc_framework_LatentSemanticMapping-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="c93d4f699c8501ae5658b578736689d6b446ff0c75de51ebbc1893280c189ba3", url="https://pypi.org/packages/ff/51/8a2179954ffaa8f8f1926aad0555ffa4c729252012085c311edb1e4ec0e7/pyobjc_framework_LatentSemanticMapping-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="14b0e828aebbb254a79c83532b64d62c7b4539208f3f10173267a2dd1645d8c5", url="https://pypi.org/packages/1e/25/a3974ee805189971e2c52f707f602cd8345fcd03084da2417714d456b7c3/pyobjc_framework_LatentSemanticMapping-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="3eb2cd0758b61f68cfe58f7ec05acc020c0a633735c0b604a8701929d20f6189", url="https://pypi.org/packages/1e/5d/41cd7654eaee87831f0187fde1dfcd98abab3d8b35d38814a337b090ea1b/pyobjc_framework_LatentSemanticMapping-8.5-py2.py3-none-any.whl")

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

