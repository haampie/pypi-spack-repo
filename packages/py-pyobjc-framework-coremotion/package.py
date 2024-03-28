# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCoremotion(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="1e1827f2f811ada123dd42809bc86f04a4c1ae3cec619ccf0f05a9387412bec1", url="https://pypi.org/packages/48/b1/addac94215e42ae1cd1cf50a1b8418d04dc02a172487ae3fa4666dc3c698/pyobjc-framework-CoreMotion-10.2.tar.gz")
    version("10.1", sha256="907a2f6da592f61d49f06559b34fc5addd8c0f2b85f9f277c5e4ea5d95247b67", url="https://pypi.org/packages/25/58/7eb6a88b690e30c5a107e46108e6d99d92a6d50d2bd877205dbb80f1dea4/pyobjc-framework-CoreMotion-10.1.tar.gz")
    version("10.0", sha256="d735668ffe028450c09499bca57467dbf77e0360b6f0623f1e054b2fe723fffb", url="https://pypi.org/packages/93/18/d8010043670fcd41f57cb5e9d7116bfa72dcf09d417f931332a089c04ee6/pyobjc-framework-CoreMotion-10.0.tar.gz")
    version("9.2", sha256="63ba5b6aee65619c4bdd2d375db7ede1b5b97887d46408ea88477fa3be9fca60", url="https://pypi.org/packages/34/27/2fd4c951ed6a9932238b2d320891b893c036481daf397d7a32ea7e275b46/pyobjc-framework-CoreMotion-9.2.tar.gz")
    version("9.1.1", sha256="33fb505ea23f9b9a830a97c722ca983b8ae2a748b3b875aeb178e4f3e35d1752", url="https://pypi.org/packages/1d/26/80026663441e6228a0399661f498505530298d8eef1cbd0bc3dba765cfe7/pyobjc-framework-CoreMotion-9.1.1.tar.gz")
    version("9.1", sha256="f0c74affb502cb559f4f9fc32c7024d5314d2a07a4579a26a4cbe777ba132f72", url="https://pypi.org/packages/5e/4e/e31ad3b74623eb894dd5d6ad9b999caf4ba74b6bf63a7bb4992b4615166b/pyobjc-framework-CoreMotion-9.1.tar.gz")
    version("9.0.1", sha256="7a5d2e9e2134779902dbfee8f1d8d9b3920f7399a85b5f8c91079600788423f6", url="https://pypi.org/packages/ad/a7/662ebdfe7747afb2a49c0f232e94243f67127171e45bacfc96add9638686/pyobjc-framework-CoreMotion-9.0.1.tar.gz")
    version("9.0", sha256="4d89e80571a8a924d909ad52e6821f74282c2fdf345f39a5d1832ccd4ddbd53e", url="https://pypi.org/packages/a2/74/740b20bd95b4f87c8a30e116ffb781f5ef9234591bc168eea4a1984d97c1/pyobjc-framework-CoreMotion-9.0.tar.gz")
    version("8.5.1", sha256="69dd1c6f05b8b1f860ad40ea1dcfedf2cc1f8f7d63ca334c48cfe043386b9eba", url="https://pypi.org/packages/0b/47/9b7926075a75493be5dd82dfb0254a9da156a7e1a175cbce45d71558eb61/pyobjc_framework_CoreMotion-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="d3c24dbf01309b69ac75e24f7368e8a52a5d8d84beaa064c459ae88b4575ba55", url="https://pypi.org/packages/67/be/44a203d51e5451643accd5ad35c946a6597ecbea9a6507af35c2ef9fe292/pyobjc_framework_CoreMotion-8.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-core@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-core@8.5:", when="@8.5:8.5.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-cocoa@8.5:", when="@8.5:8.5.0")
    # END DEPENDENCIES

