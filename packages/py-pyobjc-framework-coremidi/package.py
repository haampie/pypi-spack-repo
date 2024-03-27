##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCoremidi(PythonPackage):
    version("10.2", sha256="8168cb1e57e5dbc31648cd68d9afe3306cd2751de03275ef5f7f9b6483f17c07", url="https://pypi.org/packages/1d/cd/ff309706091fcfdc10fe6732ce4830b0fdeccfd3c2a1450ac4cf8b4df175/pyobjc-framework-CoreMIDI-10.2.tar.gz")
    version("10.1", sha256="e2e407dcb9d5ed53e0a8ed4622429a56c9770c26e2e4455dcb76a6620a12eba6", url="https://pypi.org/packages/53/b8/9b1a24a0d473be3a351fb3f29dddc07655d3898cc514a3495d0ad7783b02/pyobjc-framework-CoreMIDI-10.1.tar.gz")
    version("10.0", sha256="7e464775fb6bd77148394b5f53caa61c36e3426f61cc621f299bca91931eb3a4", url="https://pypi.org/packages/e3/70/9b17a38752943b56b66069988f7515682547acc0988cb398e1808245efae/pyobjc-framework-CoreMIDI-10.0.tar.gz")
    version("9.2", sha256="205650cbbd96f2b98abaad56b99840dabb7a9bf760aa105726af125934d90b26", url="https://pypi.org/packages/7c/49/0de8a2a39342b67f60b252e012098ef6578c55a0895f5f8d6cb21fabd9e1/pyobjc-framework-CoreMIDI-9.2.tar.gz")
    version("9.1.1", sha256="faa1ca641d15d7bcdd48edf14b8f621155760d3d5d117e5088899108528f17ec", url="https://pypi.org/packages/73/18/f376edd50fa1e05ea47bbb20657e7ed5218b2c53f3f708fb3119d027f179/pyobjc-framework-CoreMIDI-9.1.1.tar.gz")
    version("9.1", sha256="f50bcff4eea892b33b06cedc6f01141dcc07a232d90610f9a3cd10e4f01803da", url="https://pypi.org/packages/23/44/b22940e931cb53be6671f6b748eea6871990eca9cc3041b4a13c505cc3db/pyobjc-framework-CoreMIDI-9.1.tar.gz")
    version("9.0.1", sha256="b0294311db2f9421cfad4aafaa925c1e649faf3847fb3c6c9cd9892e094783c3", url="https://pypi.org/packages/fb/af/939feb398377c8b14f71a331d66cfe57c44d20d090a7e4c1fe4a65260289/pyobjc-framework-CoreMIDI-9.0.1.tar.gz")
    version("9.0", sha256="9de32bc8de9d6d11eea3724093ac4ac2ac6c6ffaba81a6970d58399552f9ffcd", url="https://pypi.org/packages/48/ec/3f3f697728909cf4fa63d562e9e958e9e11b8085e5842323b4cc08eb1c72/pyobjc-framework-CoreMIDI-9.0.tar.gz")
    version("8.5.1", sha256="efff3099eb444ae6863a4abf43e6020c892252de716d0b3457539bf4f1d31a42", url="https://pypi.org/packages/12/09/17a14207e543909b47ad7bcbbbaff72f0078e61e367b375f67d711d6f0a0/pyobjc-framework-CoreMIDI-8.5.1.tar.gz")
    version("8.5", sha256="c82821e753f62c2301b64c5b9efa9e5c5177b33f2560c2f39b52638d7e39a5ae", url="https://pypi.org/packages/33/be/cf5f0cd41b3ccba7ec76437f9019a0b456e4d22edbdd3ffac12ef53bd333/pyobjc-framework-CoreMIDI-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")

