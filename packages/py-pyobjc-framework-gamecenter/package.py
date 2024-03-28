# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkGamecenter(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="43341b428cad2e50710cb974728924280e520e04ae9f750bc7beda5006457ae3", url="https://pypi.org/packages/a3/13/a371d6aec4aa3da321f38554d7b994f83c0e61388d2c268cba5788f22730/pyobjc-framework-GameCenter-10.2.tar.gz")
    version("10.1", sha256="0d124b3f18bb1b3e134268c99bf92c29791e8c62a97095c1fb1eb912ebe495e0", url="https://pypi.org/packages/8e/24/aa87b6c80629e34f483de0fc279bf27238f3016f477cdadac2ab6ffeb0d2/pyobjc-framework-GameCenter-10.1.tar.gz")
    version("10.0", sha256="3157d1389bde7afd6fa7d5d1aa64578e99c5fd50a1400178b1f58443013d6669", url="https://pypi.org/packages/d2/28/f2c80079e2823cd02a34b0f1fe6e7af161dbaa71026f6c32c6ce644b72ab/pyobjc-framework-GameCenter-10.0.tar.gz")
    version("9.2", sha256="34ebacdde6d66113c7790717b3a6df8f691605c9c0f5f437b7d8a284cca6c1ad", url="https://pypi.org/packages/41/ac/fcba7225b4dd4d6665f33dae4f4ec7a6a5e63967f6a6b18c5897614433bc/pyobjc-framework-GameCenter-9.2.tar.gz")
    version("9.1.1", sha256="ad8753f72c7f48e72006d7f66e1485ef4d86a5ea66d2e8bbd6a1fac39dd45b9f", url="https://pypi.org/packages/51/25/b55a8de43aa3cfe30964dfa48e5028a785191a276a49dca47024bddc2ab4/pyobjc-framework-GameCenter-9.1.1.tar.gz")
    version("9.1", sha256="3c0632371227fa52b6d62b5ff1620e537f788c1fc6fdbfcbbeebe56d3ec16326", url="https://pypi.org/packages/f6/28/4d933787ab0d8a221096c17c8a6c7ed91634c4e7db685367a03b89d24195/pyobjc-framework-GameCenter-9.1.tar.gz")
    version("9.0.1", sha256="a3a4e7207bc63ec4a9f522781fe4081bff3d03ebc9d773d2b4f8da788ebb6068", url="https://pypi.org/packages/62/b3/f0124ea51dc629e493c83f8924f095e1d6ef8f0bc6fbdc142293b16a82be/pyobjc-framework-GameCenter-9.0.1.tar.gz")
    version("9.0", sha256="bc2818b21bc799c7a180c0c0c5e3cc3171aa58e6748e8d9a6eaade838e5b9838", url="https://pypi.org/packages/f4/25/dcf7785e6efe894ebe7a6b6f11e1d9428d25c540a6eb4e689644fc235fce/pyobjc-framework-GameCenter-9.0.tar.gz")
    version("8.5.1", sha256="46b4bad47684b2cca5b9d55e46b09db1fc1e4ba4120a37c1ffb3fbcd3cc93e0e", url="https://pypi.org/packages/e7/1a/b0afd464a5dc106b682a20755f534daef7fbce601eaaf098b72d7ab04a3b/pyobjc-framework-GameCenter-8.5.1.tar.gz")
    version("8.5", sha256="fd357cb824468ac0bc484cfa4110551378788cf411f24a8f942a9d33c8ba74f4", url="https://pypi.org/packages/39/be/af7b3a27865129be6014ecfc8c77dbe5e45d683684da4d307d4bb24a103a/pyobjc-framework-GameCenter-8.5.tar.gz")
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

