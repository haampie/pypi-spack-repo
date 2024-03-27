##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkLibxpc(PythonPackage):
    version("10.2", sha256="04deac1f9dbd1c19c10d175846017f8e8e51d2b52a2674482638d6b289e883a6", url="https://pypi.org/packages/3b/3e/ccfc601a392fa62bf5dac0c13f4d2227fe8a13b66f07bcbd4e1705a89aab/pyobjc-framework-libxpc-10.2.tar.gz")
    version("10.1", sha256="8e768bb3052b30ef3938c41c9b9a52ad9d454c105d2011f5247f9ffb151e3702", url="https://pypi.org/packages/ac/20/f4875b1771007873e17af4eb3fa798488ce4431a8439b927f56b5cc99233/pyobjc-framework-libxpc-10.1.tar.gz")
    version("10.0", sha256="ece6fc3158f61c3f33a5ed0d767f2aeb64e4575f367716f3f1642cb80221b02c", url="https://pypi.org/packages/9f/8b/2049b3fc6f295c9a5828bcdc6cb2311c073c8f60d2c621aeccfba8fc7903/pyobjc-framework-libxpc-10.0.tar.gz")
    version("9.2", sha256="66a1bfa0196c0066538f809e94166205d1874c0456cb4cd23210143b29846601", url="https://pypi.org/packages/17/ae/e82b137ed19556c0e075a9c61ac316b8476abef6d965f87c0d24cb9fc0ed/pyobjc-framework-libxpc-9.2.tar.gz")
    version("9.1.1", sha256="39f702985f5a09f90fa157ce8c3c7d8ea44ee52c1bceb130ede60ad80f35154d", url="https://pypi.org/packages/fe/88/b9bc71489670805206d0742377b2a6246f69293cb919c26164a3723f5856/pyobjc-framework-libxpc-9.1.1.tar.gz")
    version("9.1", sha256="b0d431d03f360abe45bc26746d57e478405b77a26eaeb59bc8bd91cf1db366b8", url="https://pypi.org/packages/ac/29/4428ef4488616ad8af0ac54dc10f0645e5f5fb4a0ffc1bd58c527a3b3ac0/pyobjc-framework-libxpc-9.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")

