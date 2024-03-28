# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkMetalkit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="42fc61371d49c2b86828d2a668b7badb2418c0ecce7595fce790830607bd8040", url="https://pypi.org/packages/08/d9/0c495e6c02c89b248cb0b762985a049d98c8d99cdd63742f67a66a665104/pyobjc-framework-MetalKit-10.2.tar.gz")
    version("10.1", sha256="da0357868824e6ec506ff92d18d729f8462c4c5ca8f26ecc86e8c031d78fa80d", url="https://pypi.org/packages/72/a6/6a2759fa4192f18a28d805049c3fe1833bdaad12c12ef7f494f75b954cc7/pyobjc-framework-MetalKit-10.1.tar.gz")
    version("10.0", sha256="a29951ae30dae738bb9d1bab5bcc6fa1150815f671923b6e6705a10d7bab2f8c", url="https://pypi.org/packages/cb/c3/e55f444b45b3929bbd60aada463e6a2325b4cb3edce2704118d3e33bdf2c/pyobjc-framework-MetalKit-10.0.tar.gz")
    version("9.2", sha256="7432069c1c9dbfe106a11744ace6d16a14170da20f1c1628adf45ad4c06e88d7", url="https://pypi.org/packages/78/7d/e0c9050b7b44a07e7f7af49b146685e622727feb88627f3752747fc1dd8a/pyobjc-framework-MetalKit-9.2.tar.gz")
    version("9.1.1", sha256="33143604eacb87fd3e6360d0ace2b12095a1010c3be30c8bc0105844104984f1", url="https://pypi.org/packages/5f/f7/f99f14eb96be285bf2474aa58dc33d6a7faaee5b50d42fe368f3e61d58d5/pyobjc-framework-MetalKit-9.1.1.tar.gz")
    version("9.1", sha256="32aaf4140c7629857a2676efcb32d5ae682ff57d5e4f387504b1ae0bafce2f35", url="https://pypi.org/packages/75/df/738440e6bf6de50cd6e39925f9cc1b4c7f26cef555d409738c295594572a/pyobjc-framework-MetalKit-9.1.tar.gz")
    version("9.0.1", sha256="dc6087557e83d67adb907976d8c22954c8e984488ceed773cecffc9cc04e897e", url="https://pypi.org/packages/08/48/b0b71b6eee25c0baa4199a6ac4f8e9fcbd0ad1abb4b28b85a394f237ac77/pyobjc-framework-MetalKit-9.0.1.tar.gz")
    version("9.0", sha256="55463080b6d4e59525c98a638fc9664070e32f2748049d7e4c27acc536d2bc69", url="https://pypi.org/packages/77/57/593d7dca94483a1cad33bd329c790633444da91f8c256590d25c983fdce1/pyobjc-framework-MetalKit-9.0.tar.gz")
    version("8.5.1", sha256="da129788c8de3ea908cab2bce3b6a6668fd94562547bbb4c532717bbfc9af611", url="https://pypi.org/packages/41/74/fdf5b8088fcfa79c80f44f099f669b74ba0ad1c8ae948d38bc9ebdb6b812/pyobjc-framework-MetalKit-8.5.1.tar.gz")
    version("8.5", sha256="95f373deadee11c2bf2e5fa37fee101c56b40cf8fe2f94bb6a4bb4065a3001ff", url="https://pypi.org/packages/b9/fd/99fad35a042f2cc09a23c124b763fdc34779a3e1d9ff8a0365a125c94b2c/pyobjc-framework-MetalKit-8.5.tar.gz")
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
        depends_on("py-pyobjc-framework-metal@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-metal@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-metal@10:", when="@10:10.0")
    # END DEPENDENCIES

