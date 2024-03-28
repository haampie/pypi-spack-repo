# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkMetalfx(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="d98a0fd1f0d2d3ea54efa768e6817a8773566c820ae7a3a23497e1c492e11da7", url="https://pypi.org/packages/69/96/dafa41327a9c0649c958829624690c9be055f156dc1623f956e6c31b6b7c/pyobjc-framework-MetalFX-10.2.tar.gz")
    version("10.1", sha256="64c96595c2489e41d93a1c75d1eace70619d973e5c9e90e7cfca29c934fc5d06", url="https://pypi.org/packages/b8/d7/733969db1088d0cd21ef5d956209ac5852e84794425e115c1fa994ce20d4/pyobjc-framework-MetalFX-10.1.tar.gz")
    version("10.0", sha256="79edcf90b59276023a143c637d37a1be563a921f5f73f526bb2d970fc08949a3", url="https://pypi.org/packages/7d/a1/df8885571882305350d2327ff7e5fe5fb085d275c599414742a5bc49c401/pyobjc-framework-MetalFX-10.0.tar.gz")
    version("9.2", sha256="c2b5f0c34cf307e1e1133e1a13c65abfdec36c34f1b086b7897fe66833e648a5", url="https://pypi.org/packages/41/c2/af5520aab53e62371f835d4aa041a097171ff94276c3d74b8cec69feb3c0/pyobjc-framework-MetalFX-9.2.tar.gz")
    version("9.1.1", sha256="edb47649d122afdf212811fb6d2a3c62304749d63629a7a93ed875a7e8dde496", url="https://pypi.org/packages/1e/24/dcd5885405512e94ccb120c8f459fd81e9b4c3934e2e0a188fd595b75f52/pyobjc-framework-MetalFX-9.1.1.tar.gz")
    version("9.1", sha256="95d4289616eabda8f9e061ae9356dcfee04bdfff0da52a8cc00ddaf7b2dd3459", url="https://pypi.org/packages/22/02/22f2f8fa6dea97ce7f54f64304c944ad6930e9b479303480bcbe3f615970/pyobjc-framework-MetalFX-9.1.tar.gz")
    version("9.0.1", sha256="4c3657c10054f882788c9f9ced2fb8a43501229b0ef4a77070f02f38b021d760", url="https://pypi.org/packages/37/df/67964ad749bf1e7ef0accaef660d76cf7a5a098f929d508f6ef9f037fc81/pyobjc-framework-MetalFX-9.0.1.tar.gz")
    version("9.0", sha256="ddcae78c1b5163bed10e4f72ef068d24e46d2df29646f6257f5b20b0936e4ff5", url="https://pypi.org/packages/c6/c1/c2f0f5cd00a49a4822bd3cd542c1bef1b6758b8300545581ad836ae7cd66/pyobjc-framework-MetalFX-9.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-metal@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-metal@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-metal@10:", when="@10:10.0")
    # END DEPENDENCIES

