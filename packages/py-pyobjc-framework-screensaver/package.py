##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkScreensaver(PythonPackage):
    version("10.2", sha256="00c6a312467abb516fd2f19e3166c4609eed939edc0f2c888ccd8c9f0fdd30f1", url="https://pypi.org/packages/21/95/ceab6db3dd4ffd801f927e071be8cc62215de566ed45f59707b80e096aab/pyobjc-framework-ScreenSaver-10.2.tar.gz")
    version("10.1", sha256="d1b890c7cae9e5c43582fe834aebcb6a1ecf52467a8ed7a28ba9d873bbf582d5", url="https://pypi.org/packages/57/f6/809407db2ccd7216a4d8da1015f37d9f5d74d26cffb8f4b20f4563e4c7f9/pyobjc-framework-ScreenSaver-10.1.tar.gz")
    version("10.0", sha256="84b658c81469305f29aaad61ac29aaad4db27ef9e9b8a13568ddb3a6bfbb902d", url="https://pypi.org/packages/a9/49/d51c483177837692faa8f83a64ef8e90cf46938592c60f99c4265f191c49/pyobjc-framework-ScreenSaver-10.0.tar.gz")
    version("9.2", sha256="6146baeee38d7d4852b4a7cb3a77c75c5bf2d68f198515df3ce78a45dc4ca3fa", url="https://pypi.org/packages/3c/50/c846094aa2d73f24fe1e8c57b8cbdef9de1d5f88df695c236a7a58687677/pyobjc-framework-ScreenSaver-9.2.tar.gz")
    version("9.1.1", sha256="4109f55b3fa157c03191ddc7cbf1217a285f69dccef433847a6042f2bc0f9de1", url="https://pypi.org/packages/48/28/b9efbdadba1420d2102ac0d5ec289775eb53de35fb1cecf76a879d229457/pyobjc-framework-ScreenSaver-9.1.1.tar.gz")
    version("9.1", sha256="e495f48bd47a5bb1400020f613672a0386bc0b7da97d9bff903aaf5cb7b2de09", url="https://pypi.org/packages/c0/a9/862966d054acce4dc073f7c22cf10179d0bf31d528df75a3ad2808be9413/pyobjc-framework-ScreenSaver-9.1.tar.gz")
    version("9.0.1", sha256="632a1fb94105554d53a2b329fdf47f9fd1ccfe6401d40d7be4b87312f3ec1f94", url="https://pypi.org/packages/e5/3f/00c4fcc0d9e3ccb91f2d8aa674291e9b634c2477daf8e4ae91e0fb8c2d34/pyobjc-framework-ScreenSaver-9.0.1.tar.gz")
    version("9.0", sha256="f171eb308d7dfeaf0ef3cf10bc7d50c391cc5a64b5341cc1ca38cb0fe63f0185", url="https://pypi.org/packages/cf/dd/17f008a8ab9e1bd82787c4d1300c6239347e552d447d2dcfba6649363434/pyobjc-framework-ScreenSaver-9.0.tar.gz")
    version("8.5.1", sha256="8f8978371536e0b8f068d8158562ef2a0cb07d94a652bf53172f5e555f9fd489", url="https://pypi.org/packages/03/2b/5c631307d9f20b7caa52d366757f0b0358fad5a8788c802457d6b5b328ae/pyobjc-framework-ScreenSaver-8.5.1.tar.gz")
    version("8.5", sha256="ee52cb4d7081faba606368c294baccbccb8e616bd2d2510b85101c8333032a1b", url="https://pypi.org/packages/9c/cc/9c53010d376267b895d767018e72bf95e1f420968b85f913470c2cb1709a/pyobjc-framework-ScreenSaver-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")

