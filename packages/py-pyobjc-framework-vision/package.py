##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkVision(PythonPackage):
    version("10.2", sha256="722e0a6da64738b5fc3c763a102445cad5892c0af94597637e89455099da397e", url="https://pypi.org/packages/9e/ed/5a3de32f0f4d3695ce56de84670c2e02df2f148202874cb70447c8151fbd/pyobjc-framework-Vision-10.2.tar.gz")
    version("10.1", sha256="ff50fb7577be8d8862a076a6cde5ebdc9ef07d9045e2158faaf0f04b5b051208", url="https://pypi.org/packages/48/25/aeedf7fa5aae3082c0667ee1272b631a43b6e67c92445da80e696f53c6ed/pyobjc-framework-Vision-10.1.tar.gz")
    version("10.0", sha256="c78244e68b7601682f0940b3d205ca087db4177e3fcc17ee29ae6f0fa811f492", url="https://pypi.org/packages/72/e4/70263373da55492fa16d707080765baaaa628e62d402346907534885b11f/pyobjc-framework-Vision-10.0.tar.gz")
    version("9.2", sha256="648d2224e85d45068aa8aa80527f7ae8d9d0af3bcb2a2a6e555c58e2313b3753", url="https://pypi.org/packages/07/9b/f5a99e28dd81a717cc7735edd3c1ad45b7e196c449ba84201ab31b82235c/pyobjc-framework-Vision-9.2.tar.gz")
    version("9.1.1", sha256="9275988390a9db96ad5359ef7061570410826995716e4525e65ad476de9e40fa", url="https://pypi.org/packages/b4/eb/414c897a8251e2459624e5c21886e360904b547aac36d3a0411d2a873b13/pyobjc-framework-Vision-9.1.1.tar.gz")
    version("9.1", sha256="51c716f0a64daf080d844efdec622f3ecd9f5223d8968ce20299bd2bc7096946", url="https://pypi.org/packages/43/c9/abc914c5d055ade6a4f2c379898db8f6b23f4c95a1bf5e09b6ffea9e8d57/pyobjc-framework-Vision-9.1.tar.gz")
    version("9.0.1", sha256="0f5a6f56fd4a2d9ea340aeafe06479b500aebfcc2b81aa2a496d438a00598222", url="https://pypi.org/packages/24/68/17872bbfee580fd404e53e7a7fe0b4da06ccc374f20ac70c7b333c97090e/pyobjc-framework-Vision-9.0.1.tar.gz")
    version("9.0", sha256="f9a9e4433d06336fad3849faefb9ef5b5d25dd4e45ef9e49e93bbbb4ddbcc7ae", url="https://pypi.org/packages/7e/58/0d434adde75f9d274cedd5391c2dc5fc88efd798ed958e9498223a864030/pyobjc-framework-Vision-9.0.tar.gz")
    version("8.5.1", sha256="a8e33ea8fd693d4ebdc484e70e92d416607d15af2004ee19dd7b8372a1eecf45", url="https://pypi.org/packages/cc/4d/c7345694003a7643b8de83dff048fff832cbeed5c22649a1f9e92802d9d2/pyobjc-framework-Vision-8.5.1.tar.gz")
    version("8.5", sha256="0c05ffd6195a7ed0329f55feca2956fbeb60b4369b384f246c8673539abbebdc", url="https://pypi.org/packages/6b/9d/ddce5297177c99b3ff21d8f7f67252325a797841e4f23009e1a504e5a7e7/pyobjc-framework-Vision-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-coreml@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coreml@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-coreml@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-quartz@10:", when="@10:10.0")

