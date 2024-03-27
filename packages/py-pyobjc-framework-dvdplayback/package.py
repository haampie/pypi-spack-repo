##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkDvdplayback(PythonPackage):
    version("10.2", sha256="f3fb90eb3d616290d2ab652214ce682130cd19d1fd3205def6ab0ba295535dd9", url="https://pypi.org/packages/56/2e/abf2c3205f50ea1eadd1d88da1631632612713fd0cf83dc3b6c1829c61cf/pyobjc_framework_DVDPlayback-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="bcbfb832a3f04e47aef03606a21fd58458bc28e25e1a444e7a9388bfee2f9dd3", url="https://pypi.org/packages/9d/4c/5227d0747050b4921b817e7dbc2bbcbbc1f66200dbaf49d4d29f1fc756dd/pyobjc_framework_DVDPlayback-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="ea31f045edf56abda6e1fc2aa9ff0bee267fd549b7787bbaf7e437e4fa58135e", url="https://pypi.org/packages/4e/53/6f915dbc55c2df55079e22f7fedf30a25085671d61c103befc5de60b6ef4/pyobjc_framework_DVDPlayback-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="ff3ab187941859d5ea4976cbef021ae3fcb38e5b60efb673ec3647c80f8df65e", url="https://pypi.org/packages/ff/1d/1ea1bbb0cdfb94579981a8cf0bf920add1416f78c59d9c1080027179ab04/pyobjc_framework_DVDPlayback-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="71869628467ab6786afddb785c9ee146ecf1969dc37816141779dfda84c67d01", url="https://pypi.org/packages/ba/fc/598cc15abc8136cc20769189dabeadfd00f12d621051073b47ac350108c4/pyobjc_framework_DVDPlayback-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="9f85b93d1fae16075ac6ac714fe56e25f744c1388dca5460d9477778c4203437", url="https://pypi.org/packages/33/bd/576161e3015ee1dab117c36cf32f4a9727c67eac02d4e1916c3f13d56a42/pyobjc_framework_DVDPlayback-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="c46e58f539659c3619fe66ed52cc3d7105149b83deee6a6360d3b12576cc9471", url="https://pypi.org/packages/27/98/5bb819e82f754b217f79acedeb57e6e2ecb50fbc418a3fcd691f58546e43/pyobjc_framework_DVDPlayback-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="80e07e8722804317bf6e959d70785111f965f8b95e6c3adacd0797da022f3ebe", url="https://pypi.org/packages/92/bc/a90e480543e7ca7009cd180c89b1ea871ba00861ea8ef7d9bef2d2dbbfbc/pyobjc_framework_DVDPlayback-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="906b065667636a365d02dcb89235417b296d6b4b5630d7ac7d040d8a9ff154c4", url="https://pypi.org/packages/fa/97/2b3b5fa079af67c465ceb851a8b3908c707cff33d2750df0c79785c63ac1/pyobjc_framework_DVDPlayback-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="7708ae636614f059a0c36f43e61727593bc31c119d4aaf0782603e38269b2e10", url="https://pypi.org/packages/b7/00/42a2557e470e08b69857eaf5746b7023fe4b52d034ce332cdd99c69e7ac8/pyobjc_framework_DVDPlayback-8.5-py2.py3-none-any.whl")

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

