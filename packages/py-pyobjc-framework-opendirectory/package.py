##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkOpendirectory(PythonPackage):
    version("10.2", sha256="7996985a746f4cceee72233eb5671983e9ee9c9bce3fa9c2fd03d65e766a4efd", url="https://pypi.org/packages/cd/1b/b84a059865b2f711a269a42b6742823b27f840fbdd35a73869b9110fc0b4/pyobjc_framework_OpenDirectory-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="83601f3b5694b1087616566019c300aa38b2a15b59d215e96c5dae18430e8c96", url="https://pypi.org/packages/f6/ae/bfcc1144cd3d228cae963fe5ed7e561cfd7ff13475dfa4e27160fe8461f4/pyobjc_framework_OpenDirectory-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="a58211a1cecb4e1d52377dfe60eecdd4579a3dfc44ff50b92cc3bb123a413189", url="https://pypi.org/packages/58/b2/a5cda8c527ad8883e829c5b862ab50c6cbd72695a0f8387f2131d429ea13/pyobjc_framework_OpenDirectory-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="3f6f18c83cc0e98959d2d568abcaab123f3881766ae2ac32f24b6a1d71ab4792", url="https://pypi.org/packages/31/21/b25a42053b781d0851180d6a3f9a3cde03618a948e781521b880b765c1cd/pyobjc_framework_OpenDirectory-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="5413e21190c47439c5fe48ba3e58f6fbf9045f820de5959d319e24e5fe194800", url="https://pypi.org/packages/53/58/8a0c328244c3cc44a44bdcd15276563b0db146e85e2aae65663224b0e9e4/pyobjc_framework_OpenDirectory-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="e6f65929581126eaefb484c94d0de1d903357d7bfe4665e55ba3b1b0a4542d72", url="https://pypi.org/packages/b7/8a/c35282089b0b26cd558af28a647095e0886da668a98e285afbde5bdf4ed3/pyobjc_framework_OpenDirectory-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="2235245f1bf157cc956c1e88fdff6906ff7568c2f7d91622b2e2ab66a8c5c81f", url="https://pypi.org/packages/cf/e1/21656eb8ac51afcd885451e5a2a756a0853108d313172628dbc1eb5508ec/pyobjc_framework_OpenDirectory-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="a7fa1f684e20f9bdc075658842921c656d9aebdadd6edbdcff7c8b3b9b2fad6e", url="https://pypi.org/packages/ab/f0/7a7185b661ffeec75eebeca6934ad4fa7447ed1191230799f9c22567853c/pyobjc_framework_OpenDirectory-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="706d80347f06c374b341ebd501dcbd5a277f05c91da0504c5ca774cf4e7a9b23", url="https://pypi.org/packages/1f/34/1e40576b92c650c7afb0c5bc40fb6e77af89aafc057f248c9e6332ad9846/pyobjc_framework_OpenDirectory-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="5fcdab699dab2577f700ee4a4435520723db89faaa985ad4630ba67dfca21df8", url="https://pypi.org/packages/f9/d5/3e2a366350c655053dc004436db0b033ae85f80f0db8642f8957d9202f65/pyobjc_framework_OpenDirectory-8.5-py2.py3-none-any.whl")

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

