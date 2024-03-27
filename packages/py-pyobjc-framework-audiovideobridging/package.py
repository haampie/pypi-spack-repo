##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkAudiovideobridging(PythonPackage):
    version("10.2", sha256="94d77284aae3a151124aa170074c2902537f540debb076376d49f5ee54fb9ce1", url="https://pypi.org/packages/35/d9/12788ed1536442af93b252d5ad2cce6dbfe888256fb4bebc69f0c215539b/pyobjc-framework-AudioVideoBridging-10.2.tar.gz")
    version("10.1", sha256="73d049a9d203541c12a672af37676c8dddf68217a3e9212510544cb457e77db0", url="https://pypi.org/packages/76/fd/8a7a1d8437395514007c41dee1d64aa4999f090f519202c35020bb3d5a28/pyobjc-framework-AudioVideoBridging-10.1.tar.gz")
    version("10.0", sha256="979081558ec3a8cd875515120027448fbe24fa0605b96cf13c7541bffab281bc", url="https://pypi.org/packages/83/a6/9b57e2f0375278fbbd274f02521dc241089ee7b6da843cbc7608f17c7382/pyobjc_framework_AudioVideoBridging-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="5a1dfc5bed7f8b9e1d82371889301d44c7488ed0ade5b7844c1f847769de7d6e", url="https://pypi.org/packages/5d/39/952f4c2de9e322cc6c9a4955fe1868fee72908a4738caa7b8ec511d4819c/pyobjc_framework_AudioVideoBridging-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="b9129a59cbaa57a445822f0abea283bbe52a7553a1fb668ce4746927ad5ab888", url="https://pypi.org/packages/3e/3d/00bb3c77a9386a8c8fb7352c26320333b227ee8ae8e92e8481ec821ba263/pyobjc_framework_AudioVideoBridging-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="21fc5849593f08d68dee91b99c028243c7eba69ded8b498390fb4dd452d71078", url="https://pypi.org/packages/22/60/2b06b9f7e2621ea995f0efceca6329aca99a7811b5bc859e28162219706c/pyobjc_framework_AudioVideoBridging-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="1f9b94380bbfa7cc82a82cdc078f8d78a572a5debefe7343571fdd4050c2e6eb", url="https://pypi.org/packages/2c/a3/094025ace0a3845bb41e47f5f5b38c75ceec45fbc4f9b5f88302b18549b8/pyobjc_framework_AudioVideoBridging-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="af442713b8c7042c46e665d416de05574e68530c87b238215de2e1dc2682b622", url="https://pypi.org/packages/ea/35/4d0b525a9875014013c0da989793d05515ab77f4ab641b8235bdbb6bde6e/pyobjc_framework_AudioVideoBridging-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="2ae8e4ad8852bb39638af656d183216282fa448a1b6c81c7109b7909247b1847", url="https://pypi.org/packages/b3/55/198d567d3cb890081529d692dbf965f115bd8759a31fe66227dc46cdd7a0/pyobjc_framework_AudioVideoBridging-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="d2a0cf6bb696a385722cfb7d33afa5bd08c79e231fba22879cb743236e63b63d", url="https://pypi.org/packages/b5/7c/2460156aa0656cfe39af4ea9d26357e611f8b46e5f2e9e6ffccf7cbbb23a/pyobjc_framework_AudioVideoBridging-8.5-py2.py3-none-any.whl")

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

