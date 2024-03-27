##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkDiscrecordingui(PythonPackage):
    version("10.2", sha256="e0423c548851cd9eb4ad7e9e085da4db2cde2420e1f3e05d46e649498edf97d8", url="https://pypi.org/packages/1c/1c/b316298dd8e426af04bca9dffb4760a753d0abe3b6206534cbfd971e0a53/pyobjc_framework_DiscRecordingUI-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="684925119e4c8f8ea43cfede1a3e39f785b5aa94a48f1aa7a98fd4cdc4c1d2e3", url="https://pypi.org/packages/4c/d9/b09df3dacdf58dc7352bdf784baca6f0bcc8816c5c754b5434b5d82bfa82/pyobjc_framework_DiscRecordingUI-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="c80135d65bb25f1d4c3c40af9a50c3b15125c54703d6e65cf4316fe3ed3bd0e7", url="https://pypi.org/packages/d5/9b/13d1ee1445a2f83c45bed45629f7b9c8f21cbee676c3e156322bd1540437/pyobjc_framework_DiscRecordingUI-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="c77836ce4f27eba9ff5ac0f1a5e01730765807dc60e0d6375e93780676b22725", url="https://pypi.org/packages/98/b1/afaee4ff4c48ddb6c96a14dc3feb457cb9b875f5cdd4cac8245def2d3ee3/pyobjc_framework_DiscRecordingUI-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="ca0cb22614effb4c1d521a8d57c343377dc029da3dc040b87bc23e29a2a5b1ea", url="https://pypi.org/packages/5f/36/b388a25fdf79bc76d529be1fc3f64e998ec4c81880b4a9927134f25151d7/pyobjc_framework_DiscRecordingUI-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="591fd8bd8947431706089fe212376741737b1fca864fbc5eb0c9a11b75ba7360", url="https://pypi.org/packages/8f/27/59b33ae39b833d81df358fff57e865ebfc3cec3960e55fce21b192068663/pyobjc_framework_DiscRecordingUI-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="e21443da92bd121ea63732ce0367760f422fe9e72a3c210a179b47e34ec6e09f", url="https://pypi.org/packages/0d/77/02a7df3743417facf9fcf1f5d8698133b880bb253bcd0ba57eac12e8fe8f/pyobjc_framework_DiscRecordingUI-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="9ba40eb285bf7a6c32cbdd7549aa9f122588269ab776cd2a3155a7c4987ff3d1", url="https://pypi.org/packages/9f/93/143ae73185ab399cecd91baa3e946b9db82c7253218e6fdbb9ae2b4a7af1/pyobjc_framework_DiscRecordingUI-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="a92d66f5565125054794004c45e47b6f8276608d1575af3a1d51458fb3d00ab7", url="https://pypi.org/packages/7b/2e/9f2cae2375feac755d765b13ead9c1ce1e066dd0d2aed7a399e1ae85ddaa/pyobjc_framework_DiscRecordingUI-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="821d6b7413ad4ba7770700c1dc7f6788b68bbc588619578798bbfe780a6b3a07", url="https://pypi.org/packages/04/de/58bb765ba0f1f48e6c540278a1b540ae833c9a4c49c2d9c3286e0a320800/pyobjc_framework_DiscRecordingUI-8.5-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-core@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-core@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-core@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-core@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-core@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-core@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-core@8.5:", when="@8.5:8.5.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-cocoa@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-cocoa@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-cocoa@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-cocoa@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-cocoa@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-cocoa@8.5:", when="@8.5:8.5.0")
        depends_on("py-pyobjc-framework-discrecording@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-discrecording@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-discrecording@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-discrecording@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-discrecording@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-discrecording@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-discrecording@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-discrecording@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-discrecording@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-discrecording@8.5:", when="@8.5:8.5.0")

