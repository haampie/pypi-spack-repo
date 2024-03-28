# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSearchkit(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="ddd9e2f207ae578f04ec2358fdf485f26978d6de4909640b58486a8a9e4e639c", url="https://pypi.org/packages/15/5a/d411aeadd0177beb5b3bd0afa8a4882342db31730332e2eb5b19749101e0/pyobjc_framework_SearchKit-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="2e42e7cacb0a7f9b327d1c770e52fe13dfaaac377cb4e413b609e478993552e0", url="https://pypi.org/packages/c4/d0/a387ef595d2ae8264d78bea9996cffeab4dc4f7c208f712f5747b038631c/pyobjc_framework_SearchKit-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="21921a722f3f1e3868ae38c4582c6d51bad35b13290e90cca62802a477d7f8d1", url="https://pypi.org/packages/ef/ba/289ced0e56bbbd9cf9c40f2e687e44813a9cacbcd461626173c3d3d7e438/pyobjc_framework_SearchKit-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="e7d7315475a791b5565aa0abb0deac1c0dbec48e8250f7075448ea9032f91dc5", url="https://pypi.org/packages/4c/db/2310882915e03177cb7de3affa80e0eb71f63d1a52697c16c2c2f7a74ac2/pyobjc_framework_SearchKit-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="9441700a817b25da33a53caf05526b2173c93e84cae30d873b034900c1e27c22", url="https://pypi.org/packages/41/76/eb79c39f9db17567c7cdb80580d94e456c7c111c5efb183dcbd247e667ad/pyobjc_framework_SearchKit-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="1941aaf141439f2e7d23cf7346af93b3be2bdd4bca1c127d6e9f9cde2151134d", url="https://pypi.org/packages/3f/88/f39f0423db1c61c020cba3b21654b53e5d9dcd57b844aa7c677f468e9aa6/pyobjc_framework_SearchKit-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="7ea06eed275da1faf4da352fdddf073ee15855b26019cc7b0641516a5399893b", url="https://pypi.org/packages/2f/9d/62b4471f4f88f84ea73b337122bee76d8c11825dbc09da260693e6494d54/pyobjc_framework_SearchKit-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="cd3992fbe0f0163a1638ff8ba54e969be18d8a125786400cd1145d92b3188029", url="https://pypi.org/packages/e9/cc/7aca914c804d5f5e1aa7e3874ede09cb7428f94ed92c2a7b25801f57c307/pyobjc_framework_SearchKit-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="e24aa73344639c2286aa016bdf60a7781d2aeae5f83440f1506eaef0294faf07", url="https://pypi.org/packages/63/40/90f5e9fc2ba2e65a3eaa2f1e98ef58377dddc39ef7a56863426d35a8b023/pyobjc_framework_SearchKit-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="f5e3cc43d5874c6b8abd8f82d9dba2d0f04ec2ed4998f973184202f3a85c399e", url="https://pypi.org/packages/90/44/4ee2cc51a711f28ed63c630c2df02cbf8e6dd5ab3885d7d6695c290e4327/pyobjc_framework_SearchKit-8.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
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
        depends_on("py-pyobjc-framework-coreservices@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coreservices@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-coreservices@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-coreservices@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-coreservices@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-coreservices@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-coreservices@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-coreservices@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-coreservices@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-coreservices@8.5:", when="@8.5:8.5.0")
    # END DEPENDENCIES

