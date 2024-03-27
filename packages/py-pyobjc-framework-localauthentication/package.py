##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkLocalauthentication(PythonPackage):
    version("10.2", sha256="442f6cae70300f29c9133ed7f2e01c294976b9aae55fe180c64983d5dee62254", url="https://pypi.org/packages/b0/9a/3086be180e2afae66cb1c9c01c5d61650b423c09c849015646443c833564/pyobjc_framework_LocalAuthentication-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="3df6ac268f79f28e5b5e76b4fd6e095bdc9a200e1908f24cc33e805fa789f716", url="https://pypi.org/packages/a0/65/9b888ca21ce5bc1918ac731cb84c83baa0cbb1cb40c7687a85cdf06e2127/pyobjc_framework_LocalAuthentication-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="6d55c6df7a6337903b3a0c61e48c6e1fe7059005024885244ff8c937bf570aae", url="https://pypi.org/packages/06/88/d317091f5ca1351f689e9d7e6f2fd2c90e11a91506983e294e7276d4856b/pyobjc_framework_LocalAuthentication-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="ef4da0ba7d327622483eba06707d54665417219ced192916eda60b953053b49a", url="https://pypi.org/packages/8f/7c/d38935859e2d9d7f7cff171e43085fca07f71116e8684ce5f0141d9fc1c3/pyobjc_framework_LocalAuthentication-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="b659acdd9f2f0e2c3fc482bf28a063854ba229fb45c681b5bf546d94b58f288e", url="https://pypi.org/packages/8e/40/4b4415f217a34723a7d766ceeeaa433f450ce98809fc50b8b428af679c73/pyobjc_framework_LocalAuthentication-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="afbbb4584050f8437ae14c9ac5f47c6634db9b6325f95e3837f6f83e759f4f42", url="https://pypi.org/packages/dc/49/2b5da31de982387831bc0ac9abc19ea10cddfbcb96916450c4c263975339/pyobjc_framework_LocalAuthentication-9.1-py2.py3-none-any.whl")
    version("9.1-beta1", sha256="e830be26e615163f9f1ea46fd71cd67805485b8b858d9cd6eb051fa31f420797", url="https://pypi.org/packages/83/d1/015ae409a1db50fee921b18e904afdb123db8272764d98f20132bd221f87/pyobjc_framework_LocalAuthentication-9.1b1-py2.py3-none-any.whl")
    version("9.0.1", sha256="e9daac430507f2fc245a3b714810f52873284905bb8e2f4fb87980dbe659ec34", url="https://pypi.org/packages/a6/a4/37f03c7124daec35f88211fe7762c4d89fd670c1558ac2097300c544d984/pyobjc_framework_LocalAuthentication-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="b75feb493115dafa98a0494ec307703307ad19305872e40f85ed560e62fe03d8", url="https://pypi.org/packages/a7/c4/038e56a4ea2af249ab791cf28dacb46781c09724fe26b71b7988c646c81e/pyobjc_framework_LocalAuthentication-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="6e54e072602efb2d350d4f2dce6ddd1ef37f2e11de521fde1cb3fa349c973d3e", url="https://pypi.org/packages/97/ee/a5572a81f3d8de5d132f8db89c9781ea2e6123f53ece29eb933c4c0c1d37/pyobjc_framework_LocalAuthentication-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="ed996158246336b02e291f3bc797fded94a0d7c3ba4347fa2246d3b0dd08140a", url="https://pypi.org/packages/5a/46/89fe18fd22b14e4585abd5adad41b950c39d09c043e0092532adaaa03499/pyobjc_framework_LocalAuthentication-8.5-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-core@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-core@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-core@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-core@9.1-beta1:", when="@9.1-beta1")
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
        depends_on("py-pyobjc-framework-cocoa@9.1-beta1:", when="@9.1-beta1")
        depends_on("py-pyobjc-framework-cocoa@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-cocoa@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-cocoa@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-cocoa@8.5:", when="@8.5:8.5.0")
        depends_on("py-pyobjc-framework-security@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-security@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-security@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-security@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-security@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-security@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-security@9.1-beta1:", when="@9.1-beta1")
        depends_on("py-pyobjc-framework-security@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-security@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-security@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-security@8.5:", when="@8.5:8.5.0")

