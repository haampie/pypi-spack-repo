# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkFsevents(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="3a75f38bb1d5d2cf6a0d3e92801b3510f32e96cf6443d81b9dd92a84d72eff0a", url="https://pypi.org/packages/6e/5b/42b1dcca24ebf2eebc29846a7779a9f7edc4104b6a2161a62532a7054023/pyobjc-framework-FSEvents-10.2.tar.gz")
    version("10.1", sha256="f5dee8cfbd878006814db264c5f70aeb1a43c06620e98f628ca6c0008beb1b1d", url="https://pypi.org/packages/a4/4f/505fe82b5b90a2f03046817298953b743870ccddea0ca426d658ebc5008e/pyobjc-framework-FSEvents-10.1.tar.gz")
    version("10.0", sha256="a462c1ad6d6c93d9542c9780b970915e5e9fa0f70391187f7145b5b1c64e57d5", url="https://pypi.org/packages/f7/f3/068f2523e564b39a30540e81d69f795330817b5b0b04e197199a5626ffd4/pyobjc-framework-FSEvents-10.0.tar.gz")
    version("9.2", sha256="910d3b3ae041a2a8f5bcb66749d705107ded384f9823ba44c54664a0c3ee9a65", url="https://pypi.org/packages/6e/95/77856ae09f6162e7ce670f2f8b7e2c7225365f16ca1ff5f29f60f9d4cf15/pyobjc-framework-FSEvents-9.2.tar.gz")
    version("9.1.1", sha256="c974a288f74cc5afc96d5d744fb8bf638d25f88be2ffcea92a1e74758978e3c2", url="https://pypi.org/packages/d6/2d/d813746f2c90a14dd47d570239e8e987870807dd15c794cf7dd6c977dce3/pyobjc-framework-FSEvents-9.1.1.tar.gz")
    version("9.1", sha256="d95362c4efc8cc838522c31fa0d2c869a016308d2826ff335dc4ae4a47c82574", url="https://pypi.org/packages/b2/bb/398102b7d9e3143050e592ec86cc474ad6caf4c0995354a3b8f28fcdba90/pyobjc-framework-FSEvents-9.1.tar.gz")
    version("9.0.1", sha256="31643db10d27f712a701ca0864adf78426b19d7b3c56dbf0053d13ab4f2f4ae6", url="https://pypi.org/packages/9b/30/62086854cee6e8cd6af3de4bffaedb5652a087d68edd9d2b160960365127/pyobjc-framework-FSEvents-9.0.1.tar.gz")
    version("9.0", sha256="3577e67ce41e9dae9eeb7b31c828b65a0234ab808f5b64779f27b0552ef5f265", url="https://pypi.org/packages/ed/b3/2635e51e733351246f8718585af0c6c3781df5df4cfa00118a3ec271498a/pyobjc-framework-FSEvents-9.0.tar.gz")
    version("8.5.1", sha256="c25ec45f6154ee2a42437a33bad6d1ada24f6791742f22d7ab632a524f4dc99f", url="https://pypi.org/packages/3f/0c/10ee54061aaa9e09c6675d9a698e26999d2338867023bfaeee32d982c569/pyobjc-framework-FSEvents-8.5.1.tar.gz")
    version("8.5", sha256="21928fd0d17ad69f45d41f89228b7446d8faf0d1bba0d71e8e23451196701004", url="https://pypi.org/packages/eb/c6/738e7a2197769e75f8b75618c765838a8c05e9f29b82b759944368f58905/pyobjc-framework-FSEvents-8.5.tar.gz")
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

