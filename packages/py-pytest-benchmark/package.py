##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestBenchmark(PythonPackage):
    version("4.0.0", sha256="fdb7db64e31c8b277dff9850d2a2556d8b60bcb0ea6524e36e28ffd7c87f71d6", url="https://pypi.org/packages/4d/a1/3b70862b5b3f830f0422844f25a823d0470739d994466be9dbbbb414d85a/pytest_benchmark-4.0.0-py3-none-any.whl")
    version("3.4.1", sha256="36d2b08c4882f6f997fd3126a3d6dfd70f3249cde178ed8bbc0b73db7c20f809", url="https://pypi.org/packages/2c/60/423a63fb190a0483d049786a121bd3dfd7d93bb5ff1bb5b5cd13e5df99a7/pytest_benchmark-3.4.1-py2.py3-none-any.whl")
    version("3.4.0", sha256="52c67dac5e6ce8fce9ee801daad0bcedc43a489e9eb25fdc29ca600b96f790a6", url="https://pypi.org/packages/97/90/5e80677335cd092ba37aaf8325811e923b04b44ba39abfe61aeab79443d7/pytest_benchmark-3.4.0-py2.py3-none-any.whl")
    version("3.2.3", sha256="01f79d38d506f5a3a0a9ada22ded714537bbdfc8147a881a35c1655db07289d9", url="https://pypi.org/packages/e7/1e/180579ad3bc53fe3181ef3843f0602f4db77f3609e5e5069a0ec194ff213/pytest_benchmark-3.2.3-py2.py3-none-any.whl")
    version("3.2.2", sha256="ab851115ce022639173b9497d4a4183a1d8fe9cdcf8fab9d8a57607008aedd3d", url="https://pypi.org/packages/ab/0f/8488bebc18924bbf5ed9eff3d3cecd0287446c88962f10e99fa727a3d2d7/pytest_benchmark-3.2.2-py2.py3-none-any.whl")
    version("3.2.1", sha256="f7fe3d6574595503c0c8c6a53018c5e5e7d1fb460bbf806766ffcc285cd0ec11", url="https://pypi.org/packages/78/3f/8f23288b2ac33f3bfce329fdc4fb71e94e52830a292d5dfc064bdca98c37/pytest_benchmark-3.2.1-py2.py3-none-any.whl")
    version("3.2.0", sha256="6543b24f1431fd8a81bfb191929e87efccaa6891aaa3fe99ca55e145d4661a32", url="https://pypi.org/packages/ae/a3/faf4e4e06ce6199768f05e0b971133fd3ed73d6655fe6ebf4b24d7658f20/pytest_benchmark-3.2.0-py2.py3-none-any.whl")
    version("3.1.1", sha256="3549545f1a051a789d956a4a9b176583cd6b847e621b788471e6c04b7d8d0e3c", url="https://pypi.org/packages/05/5e/c837bf9e3f060ecdd29c7e8f4648571094868dda0945b27d1c5fa595625e/pytest_benchmark-3.1.1-py2.py3-none-any.whl")
    version("3.1.0", sha256="b9be8dbbf5f95aee2fd63a711b92f84bf1bade5501141cd30f7284d20ef45aa5", url="https://pypi.org/packages/36/b9/82bd5260a0f99d0b535162ad97e56746b231807c63e2c32dce75a39825df/pytest_benchmark-3.1.0-py2.py3-none-any.whl")
    version("3.0.0", sha256="3560274259a43a6aa55a29932b28c5fd47e6d34dfeb83aa59f4f51d206b014c0", url="https://pypi.org/packages/80/a7/0e7d4940d00883c8a6e6084519f8bbd6c53e645fc6579ac35f5b676b55e3/pytest_benchmark-3.0.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-py-cpuinfo", when="@3.1.0-alpha2:")
        depends_on("py-pytest@3.8:", when="@3.2.1:")
        depends_on("py-pytest@3.6:", when="@3.2:3.2.0")
        depends_on("py-pytest@2.8:", when="@3.1")
        depends_on("py-pytest@2.6:", when="@2.5:3.0")

