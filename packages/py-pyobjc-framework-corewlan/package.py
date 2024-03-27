##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCorewlan(PythonPackage):
    version("10.2", sha256="f47dcf735145eb2f817db5c2134321a7cfb9274a634161ff3069617fd2afff42", url="https://pypi.org/packages/38/b4/c3c3fe7624d7b9840e38769dcdf8fc25d6eab3498418303e23c5e6578019/pyobjc-framework-CoreWLAN-10.2.tar.gz")
    version("10.1", sha256="a4316e992521878fb75ccff6bd633ee9c9a9bf72d5e2741e8804b43e8eeef8ac", url="https://pypi.org/packages/7a/67/c049ad264519c848f5c9108f368a6fbfb1aa6a54f19693a465473fd72a6e/pyobjc-framework-CoreWLAN-10.1.tar.gz")
    version("10.0", sha256="f71594ca1d2741f5979688d6d3880237c469943b49a030de131102357cdccb2a", url="https://pypi.org/packages/6d/3d/a1fa1dc1eabcc8419ce3540f6b623552ee4dd2d78b7f52507a7733137491/pyobjc-framework-CoreWLAN-10.0.tar.gz")
    version("9.2", sha256="4969e1416727e9683b30d0ebf37be6fde94e1577d25e6adee2a6018844888161", url="https://pypi.org/packages/66/a5/a00162dff83a80c6c4b6543958f35db6a7fd76ca0374ea3431bc740b029c/pyobjc-framework-CoreWLAN-9.2.tar.gz")
    version("9.1.1", sha256="1297f8dd653a5a22a972012bdaf5a0b9cd39ff8fc7255b37c1de6bb35ace4cf5", url="https://pypi.org/packages/17/1a/fb2a62d3e7ec943ae09df0574786337c07df3a7365edda6c920d13f1756b/pyobjc-framework-CoreWLAN-9.1.1.tar.gz")
    version("9.1", sha256="cd0344680af6f80a58a156ead6eeed89c23012f6c08c3887928130f7a2739192", url="https://pypi.org/packages/65/c4/959d98cd376d4ac582b85ad2bc99c9cce1bfecfc60698837d19dce429340/pyobjc-framework-CoreWLAN-9.1.tar.gz")
    version("9.0.1", sha256="1193f2d06c92ec8afe7438c3110957f599ee39d2ccdfc2fcabb749306faacbae", url="https://pypi.org/packages/b3/3d/9a2c66601ee55f56c7588a885acbc9f74e5394a3930d5bb258a035236806/pyobjc-framework-CoreWLAN-9.0.1.tar.gz")
    version("9.0", sha256="364d1db52976d6c9aeef64ba7bf8ce6e74baadfb7438a0849102c144249baaae", url="https://pypi.org/packages/f9/ac/5f7aa73821f2bd1685a5b63b4a7206e8d2ec6ff042f823e4f7d293150218/pyobjc-framework-CoreWLAN-9.0.tar.gz")
    version("8.5.1", sha256="9e8de627a3cb93661504c5be49fe0523388fd478e9406048cd662c04be9e7dc1", url="https://pypi.org/packages/1d/40/fb5b0a0d3f3eceeb91bf9236038f5248aef9f3c64955ed43d49daa7b2486/pyobjc-framework-CoreWLAN-8.5.1.tar.gz")
    version("8.5", sha256="c2713d772ac0d0b0f1c5b596057b4fb4da90c2aadd2d2515153ebd618cbec42d", url="https://pypi.org/packages/ff/07/a160e609895edf5322450f6270b24c61572af0e895c8694bc8cb55ca25ce/pyobjc-framework-CoreWLAN-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")

