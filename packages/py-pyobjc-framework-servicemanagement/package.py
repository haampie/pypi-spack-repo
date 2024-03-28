# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkServicemanagement(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="e5a1c1746788d0e125cc87cbe0749b2b824fb7a08bc4344c06c9ac6007859187", url="https://pypi.org/packages/89/06/3a51828dba366bba110f6a67d5561348aab96a55aa41ee618ee65a65b388/pyobjc_framework_ServiceManagement-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="d05289948558cf4c7fbc101946f6ccadcc33826b2056c14d5494a8ae7f136936", url="https://pypi.org/packages/13/e1/9f47cdd081efeadcaabb477d33f364f23a4cb2efda825f94a03d513d58a3/pyobjc_framework_ServiceManagement-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="a27685c393c1c91b42c5701e0e18326b58d50f0b0c2a194190bc3078d53b5df1", url="https://pypi.org/packages/fb/0d/a099e3d9cdb3957c31a65fcef17e146a838636f43e2a0b110ef71b7fd6d2/pyobjc_framework_ServiceManagement-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="ee102db9a6086bcd28f228bf427f630a9bd3920f73a94f8043db9b2a67119b22", url="https://pypi.org/packages/e2/64/7b7165a2cdcd287f5acb1f9627eb8e3d55324639cb25dfceedae05332145/pyobjc_framework_ServiceManagement-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="5e0709bbd23adaa801ed5fd618be7a25cd6c55b1cad9ab21b5e39166215c033b", url="https://pypi.org/packages/1f/a5/566458adcad2b4016eeba7c59f576a80593b82251663fa69c1e81a56ccfd/pyobjc_framework_ServiceManagement-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="06533aff41ac668d5bf7d9a0a862b8b081b5630e12c1de7121b1e769f964e36e", url="https://pypi.org/packages/2b/7c/b5fb132bbbf65975bc7f7cba2ee9179fc83e0064a9a902f04dc7f9d509d8/pyobjc_framework_ServiceManagement-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="a3c4ff85036f43c9f3ee41a81ae5d9f0ce75bb3f8b974bf8a613c2da6008f454", url="https://pypi.org/packages/46/10/d7cbd9cf8890c5da7547378c235f971412fc7503fe550d6cbd62fab0dc6d/pyobjc_framework_ServiceManagement-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="9a768f72314d9f7943396fe8075b6cc34fc7eaedb23a8c416937f3fba32ac024", url="https://pypi.org/packages/0b/f0/77b9a9d201f128aba788e4b99d5c6ac56724ae2b93b68a91cfa001f74f56/pyobjc_framework_ServiceManagement-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="cee84027054f945d5a5f0d377ca492dcf085b1f5874e313ac9e6369937053ceb", url="https://pypi.org/packages/70/6c/73e3cd05e6a100f53a3d6cd8ec609be493338eb05f8c63b8e28956aa165a/pyobjc_framework_ServiceManagement-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="b7e5013c23102c32eadb9117ef85c4438a78dd60c8cadbf63005e1f56ecfa023", url="https://pypi.org/packages/4f/9a/986113c386855271725977d1bc0b4b7ffc8203310dd16cd79d15a901ffaf/pyobjc_framework_ServiceManagement-8.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
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
    # END DEPENDENCIES

