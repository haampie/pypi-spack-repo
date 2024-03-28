# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCryptography(PythonPackage):
    # BEGIN VERSIONS
    version("41.0.3", sha256="6d192741113ef5e30d89dcb5b956ef4e1578f304708701b8b73d38e3e1461f34", url="https://pypi.org/packages/8e/5d/2bf54672898375d081cb24b30baeb7793568ae5d958ef781349e9635d1c8/cryptography-41.0.3.tar.gz")
    version("40.0.2", sha256="c33c0d32b8594fa647d2e01dbccc303478e16fdd7cf98652d5b3ed11aa5e5c99", url="https://pypi.org/packages/f7/80/04cc7637238b78f8e7354900817135c5a23cf66dfb3f3a216c6d630d6833/cryptography-40.0.2.tar.gz")
    version("38.0.1", sha256="1db3d807a14931fa317f96435695d9ec386be7b84b618cc61cfa5d08b0ae33d7", url="https://pypi.org/packages/6d/0c/5e67831007ba6cd7e52c4095f053cf45c357739b0a7c46a45ddd50049019/cryptography-38.0.1.tar.gz")
    version("37.0.4", sha256="63f9c17c0e2474ccbebc9302ce2f07b55b3b3fcb211ded18a42d5764f5c10a82", url="https://pypi.org/packages/89/d9/5fcd312d5cce0b4d7ee8b551a0ea99e4ea9db0fdbf6dd455a19042e3370b/cryptography-37.0.4.tar.gz")
    version("36.0.1", sha256="53e5c1dc3d7a953de055d77bef2ff607ceef7a2aac0353b5d630ab67f7423638", url="https://pypi.org/packages/f9/4b/1cf8e281f7ae4046a59e5e39dd7471d46db9f61bb564fddbff9084c4334f/cryptography-36.0.1.tar.gz")
    version("35.0.0", sha256="9933f28f70d0517686bd7de36166dda42094eac49415459d9bdf5e7df3e0086d", url="https://pypi.org/packages/10/91/90b8d4cd611ac2aa526290ae4b4285aa5ea57ee191c63c2f3d04170d7683/cryptography-35.0.0.tar.gz")
    version("3.4.8", sha256="94cc5ed4ceaefcbe5bf38c8fba6a21fc1d365bb8fb826ea1688e3370b2e24a1c", url="https://pypi.org/packages/cc/98/8a258ab4787e6f835d350639792527d2eb7946ff9fc0caca9c3f4cf5dcfe/cryptography-3.4.8.tar.gz")
    version("3.4.7", sha256="3d10de8116d25649631977cb37da6cbdd2d6fa0e0281d014a5b7d337255ca713", url="https://pypi.org/packages/9b/77/461087a514d2e8ece1c975d8216bc03f7048e6090c5166bc34115afdaa53/cryptography-3.4.7.tar.gz")
    version("3.3.2", sha256="5a60d3780149e13b7a6ff7ad6526b38846354d11a15e21068e57073e29e19bed", url="https://pypi.org/packages/d4/85/38715448253404186029c575d559879912eb8a1c5d16ad9f25d35f7c4f4c/cryptography-3.3.2.tar.gz")
    version("3.2.1", sha256="d3d5e10be0cf2a12214ddee45c6bd203dab435e3d83b4560c03066eda600bfe3", url="https://pypi.org/packages/94/5c/42de91c7fbdb817b2d9a4e64b067946eb38a4eb36c1a09c96c87a0f86a82/cryptography-3.2.1.tar.gz")
    version("2.8", sha256="3cda1f0ed8747339bbdf71b9f38ca74c7b592f24f65cdb3ab3765e4b02871651", url="https://pypi.org/packages/be/60/da377e1bed002716fb2d5d1d1cab720f298cb33ecff7bf7adea72788e4e4/cryptography-2.8.tar.gz")
    version("2.7", sha256="e6347742ac8f35ded4a46ff835c60e68c22a536a8ae5c4422966d06946b6d4c6", url="https://pypi.org/packages/c2/95/f43d02315f4ec074219c6e3124a87eba1d2d12196c2767fadfdc07a83884/cryptography-2.7.tar.gz")
    version("2.3.1", sha256="8d10113ca826a4c29d5b85b2c4e045ffa8bad74fb525ee0eceb1d38d4c70dfd6", url="https://pypi.org/packages/22/21/233e38f74188db94e8451ef6385754a98f3cad9b59bedf3a8e8b14988be4/cryptography-2.3.1.tar.gz")
    version("1.8.1", sha256="323524312bb467565ebca7e50c8ae5e9674e544951d28a2904a50012a8828190", url="https://pypi.org/packages/ec/5f/d5bc241d06665eed93cd8d3aa7198024ce7833af7a67f6dc92df94e00588/cryptography-1.8.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("idna", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

