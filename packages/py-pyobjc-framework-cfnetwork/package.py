##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCfnetwork(PythonPackage):
    version("10.2", sha256="18ebd22c645b5b77c1df6d973a91cc035ddd4666346912b2a0c847803c23f4d4", url="https://pypi.org/packages/8c/cf/f7f8e8e91f6fa62b9bd774f9f64e3efa32b075423ad3c9ca37f55558a36c/pyobjc-framework-CFNetwork-10.2.tar.gz")
    version("10.1", sha256="898fa3ec863b9d72b3262135e1b0a24bc73879b65c69a2a7b213fe840e2a11de", url="https://pypi.org/packages/31/fd/d31594eeb11208dd1c182b7310f37454de7322046f7bbed4d9f33ecca869/pyobjc-framework-CFNetwork-10.1.tar.gz")
    version("10.0", sha256="18118d62e05e37692e3cfa5b1ab8c0b82079aad72240bcb6d626740aa4405480", url="https://pypi.org/packages/a7/76/92a099fe82b4f20e54ae848a26b5613ad4dd67ab0fa02fcbf15152860067/pyobjc-framework-CFNetwork-10.0.tar.gz")
    version("9.2", sha256="05baad07bcb8167cedb1a6a6f7bb7bdf0a568b71c1c814fa8b8cba7e64598b15", url="https://pypi.org/packages/7b/2a/6131c7151b7176f8a841bb4676299288fe4d51adeabe61775379a160921f/pyobjc-framework-CFNetwork-9.2.tar.gz")
    version("9.1.1", sha256="58614b1263f47ce87d7a4e8b9f3a798e99168b14fbaf028ec22fa9cddb1f04d5", url="https://pypi.org/packages/24/17/548c1247267c6eab4ffa28be647b9bb49c2e5b4f3218182bff6f27fba230/pyobjc-framework-CFNetwork-9.1.1.tar.gz")
    version("9.1", sha256="a673ee3a2467db66b4b112dd2eb8bf126555f6951b45fcc2d3473b3c5e9f5aa3", url="https://pypi.org/packages/cc/b9/183038476800b52e1ff8a1e4c3c8079b240b534882bfd0db07f65e16f062/pyobjc-framework-CFNetwork-9.1.tar.gz")
    version("9.0.1", sha256="7f0c05d1575bbf2de31fe38ee8ff18840640463ad530827af88cfbca817e130b", url="https://pypi.org/packages/4e/7d/d5d6c0706d70ca858908ed41a44ea3655477b9862afee6300e14d376a067/pyobjc-framework-CFNetwork-9.0.1.tar.gz")
    version("9.0", sha256="5173487185c0343af8c98ba58456bfbbbb56a5de2c3aa65be9090cf1be7bc604", url="https://pypi.org/packages/b8/cd/0597dcaddade02254cd7853ac338434fd33bae3a1c7f9d43a6056484f2ab/pyobjc-framework-CFNetwork-9.0.tar.gz")
    version("8.5.1", sha256="9a3759111ea2c3b8bb956a9f0af8f1c8d0b08a5f2ccd23b6d49ccd8e43079e43", url="https://pypi.org/packages/5d/46/b1c40bcc86aea61679b70c8adf49934b8c3e9e45ae8e90a7991aaf477e0f/pyobjc-framework-CFNetwork-8.5.1.tar.gz")
    version("8.5", sha256="6c588d1846faa623b4611a1a22132c1d794330b90190b3ff1ab14fdb6d884c34", url="https://pypi.org/packages/c4/f5/374ea435c7338ed67a9be1e384e0ecab0dfbcd52d60edea7a8e95b1a808f/pyobjc-framework-CFNetwork-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")

