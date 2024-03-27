##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkPhase(PythonPackage):
    version("10.2", sha256="f29cd40e5be860758d8444e761d43f313915e2750b8b03b8a080dd86260f6f91", url="https://pypi.org/packages/0a/56/1ec5abb4316fa3984b487fd2c01d4bbb203995a021456954b2e24c9b6c61/pyobjc_framework_PHASE-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="329cd6dd040a7ef8091dda9d8e57d9613bc9c8edf3cfd3af549f5cd9d64a0941", url="https://pypi.org/packages/0a/53/14c78bc95e6a094848c56443e37e76fd292d087a7d661440600dc39e3416/pyobjc_framework_PHASE-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="d16c38d58065d22c9b688f0fa753fc0a32d9a24bcda23830dab7fd34105c5432", url="https://pypi.org/packages/ac/3f/22637fe5a23f0a0eef09cc69cafeb3ffb8ea5700cad28697195b40b2a34b/pyobjc_framework_PHASE-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="051b04401279f6885a88c74faead48db0f5f8fedd0496f3affca25970fc097d4", url="https://pypi.org/packages/73/59/edc37f7fa13c29d667011be34dabce6e7ce6fca14697c9a64b21c39f75df/pyobjc_framework_PHASE-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="7303ec167f26ab85cec46977d372017f1c6cb678b5e9e70d3c6b32801cbb1a4a", url="https://pypi.org/packages/3b/43/de06a0cae620136c06757f0d371719d189078a942d6e394e7a9c6b246644/pyobjc_framework_PHASE-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="88d699e504644297332a2955910b4c0ee8794b432a4ff75a0ef91bc48e88d4d2", url="https://pypi.org/packages/3d/47/713c9c3c61d5809a9d68bd599621c0d91c54ccfc37d56856019c37dad889/pyobjc_framework_PHASE-9.1-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-core@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-core@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-core@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-avfoundation@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-avfoundation@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-avfoundation@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-avfoundation@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-avfoundation@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-avfoundation@9.1:", when="@9.1:9.1.0")

