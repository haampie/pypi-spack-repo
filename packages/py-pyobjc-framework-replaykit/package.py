# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkReplaykit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="12544028e59ef25ea5c96ebd451cee70d1833d6b5991d3a1b324c6d81ecfb49e", url="https://pypi.org/packages/69/0e/b618ccb5ffb028ea72d3fd0374d52c24cbbd1540d1a02ffdf8b4272890ed/pyobjc-framework-ReplayKit-10.2.tar.gz")
    version("10.1", sha256="c74d092afd8da7448e3b96a28d9cde09ad11269b345a5df21ce971c87671e421", url="https://pypi.org/packages/2f/40/3abd5a1275f8b309b43c1640f9a26edb0c13f7ff022d7ef18a7893e7f14b/pyobjc-framework-ReplayKit-10.1.tar.gz")
    version("10.0", sha256="83a95c5c95d1a1af731fc9fba71e194d13ceded46799422908d8f95376a4a5ac", url="https://pypi.org/packages/12/40/37a8c88e07a6aed1c24d55d7c120504010d9a24786860f69c06e74f86582/pyobjc-framework-ReplayKit-10.0.tar.gz")
    version("9.2", sha256="bda42b68771c28846f90f5ae82d6418040a99a7dba8e59a465a26aa0b7c768f1", url="https://pypi.org/packages/9f/5a/d21d4a8d331aa3ca4615f7242acf9b2e63d234d5193030b1b90be815b04d/pyobjc-framework-ReplayKit-9.2.tar.gz")
    version("9.1.1", sha256="c0213a9e8e6227833726729c4d5c1523bc084acc16868713319a3b5a019d258e", url="https://pypi.org/packages/e9/28/2dcac6b53c2925adbb2797834b1a715fcff4d3db1fd521d2d68fa7461d78/pyobjc-framework-ReplayKit-9.1.1.tar.gz")
    version("9.1", sha256="646f7f0341c28c42d10a41758dc3bb8a9b3b99d75baf710e1c3722e77368f549", url="https://pypi.org/packages/9c/60/3849c610566c56121cb15c782f5efb36f4e6095d07f55f8d10ee593d8490/pyobjc-framework-ReplayKit-9.1.tar.gz")
    version("9.0.1", sha256="6242ca6f61458f5d0aea53a8d0ec5dc1bf32bce018a169b8293c17a0b7ba0e6b", url="https://pypi.org/packages/e0/bd/69da81077a11acbebf2f45a02d62578c7d76ffefc5ebba607ae7931daaa3/pyobjc-framework-ReplayKit-9.0.1.tar.gz")
    version("9.0", sha256="2d12d1c843e706570f78fc27a0a6498dd5dc2b29382764237638954d3744c3c3", url="https://pypi.org/packages/ad/62/5553a526e071d39ee447bb3dbad7c62e4b85e70f04f5331ace795bd7a7d9/pyobjc-framework-ReplayKit-9.0.tar.gz")
    version("8.5.1", sha256="d8efbd92e885b277e6cae341a45a7decafe5f728ab44d3c4d5088148c3997230", url="https://pypi.org/packages/cb/b1/76430850a36ef33f7287d408afe9621296bcaf37a8ef88c65b5bf3ee18f3/pyobjc-framework-ReplayKit-8.5.1.tar.gz")
    version("8.5", sha256="94cd956a3ee4a8d46a89f042645d34f30514ead22728efe9296cab2187b54a17", url="https://pypi.org/packages/01/24/1469363514a59bd9f52473d2e3cc9d7c8f4632e0ed82f6c8ad95568a29ab/pyobjc-framework-ReplayKit-8.5.tar.gz")
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
    # END DEPENDENCIES

