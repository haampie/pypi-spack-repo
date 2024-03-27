##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPot(PythonPackage):
    version("0.9.3", sha256="eecf2394390a73472e727ef75f7c801fc47509039f00c40f8fc64fdeea617c86", url="https://pypi.org/packages/02/5a/10886cb742919dc83ebd55486b6c1c1455a1ff268a8ef1bfca9424aae70d/POT-0.9.3.tar.gz")
    version("0.9.2", sha256="8b1ac1fca71dee525b62fd3407f296aa3cdb2b825ad751e00eb945845538084e", url="https://pypi.org/packages/e0/40/4ba3b77183b6dc017bda3d0ddf16900810c41ad25a5247087c920fb69f3c/POT-0.9.2.tar.gz")
    version("0.9.1", sha256="81c25327a00197ff11c1fe5221cf181ad1dffe615644152e2e115ddddf5e591b", url="https://pypi.org/packages/b2/ce/e26a1bd731c089249d32af1f422f0d420e0f0ff6856575fce3b98403da04/POT-0.9.1.tar.gz")
    version("0.9.0", sha256="300864ae2b469a7b66155fc610a134961d9d46f1ecde0d85e484d14acd06b215", url="https://pypi.org/packages/4a/90/86ec09ac19eb438915e2b253b9bfc8922fc753b3da871d407497e00b0ff4/POT-0.9.0.tar.gz")
    version("0.8.2", sha256="3ca9ae3c8f370cfcbb4643a01c73dd3c9273e4d4ff7e9af5db70154f34cbc204", url="https://pypi.org/packages/1c/0d/aee391eac05f0ba1a6d29cbb3eacb79bfd80cc8da52c9bf964115fcf8334/POT-0.8.2.tar.gz")
    version("0.8.1", sha256="ecf270b60759996958c6bf8a7211e6d40cfd0c054a7175400249fd30fda4c94b", url="https://pypi.org/packages/32/03/a360be6b316bae6f63e5287dd4da764891c96c555924038b5f211b1e2937/POT-0.8.1.tar.gz")
    version("0.8.0", sha256="a70e092ddc5a29a4b526192750604a634dfc2faa1641664b4c2c1c00b3cd63cf", url="https://pypi.org/packages/6b/0c/f4d5cb879c2be8742f363ea6461713a0f83c3599ecd44843a2913923b4bd/POT-0.8.0.tar.gz")
    version("0.7.0.post1", sha256="5dc9aa40a75af8dfd3dc24772ce3349e204a2e1ceefc4d99ea2f06994bc976a2", url="https://pypi.org/packages/87/e1/958578fbbdf734dcfb21cd2c7386fff6bb63839fb2a00a980dad3f929de4/POT-0.7.0.post1.tar.gz")
    version("0.7.0", sha256="d4ac2bc8791f049a3166820d51e218d6c299885449b735eafef8d18c76d4ad06", url="https://pypi.org/packages/a8/5d/e7525ff865040845bfacbca4416610761a07db67ba77f6be4e26dd2583bf/POT-0.7.0.tar.gz")
    version("0.6.0", sha256="a0c254825b65bdfb2b9a4594d1876bdb3bd2564caf0bd86401b440e64c0806c0", url="https://pypi.org/packages/4e/23/8aba82a55d40ac8c5f4313c1c51804dcb239ee3761b9789db1b621e43c87/POT-0.6.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-cython@0.23:", when="@0.7:0.7.0.0")
        depends_on("py-cython", when="@0.6")
        depends_on("py-numpy@1.16.0:", when="@0.7:0.7.0.0")
        depends_on("py-numpy", when="@0.6")
        depends_on("py-scipy@1.0.0:", when="@0.7:0.7.0.0")
        depends_on("py-scipy", when="@0.6")

