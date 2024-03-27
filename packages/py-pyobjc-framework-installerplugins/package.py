##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkInstallerplugins(PythonPackage):
    version("10.2", sha256="754b8fdf462b6e568f30249255af50f9bd3ac90edacfe6e02d0fe77f276c049b", url="https://pypi.org/packages/97/43/c41047a64df64c30e2d835c608c18831540b3b82b658904d849d14f3c8e7/pyobjc_framework_InstallerPlugins-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="195e7d559421bf36479b085bf74d56f8549fff715596fc21e0e0c95989a3149a", url="https://pypi.org/packages/41/48/16218dbbeddfc604fd03866cd45e8b993d61c3f81ed82a8905f8c5ec4ff7/pyobjc_framework_InstallerPlugins-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="1dfee60017bdf9c2e1566dd26972a288f9f9ace878c25ab5681164b2221d1e70", url="https://pypi.org/packages/1f/c7/4b3a81980f8b315e3f2e3a58b7c94bf534a248a46259052cc920a0c28097/pyobjc_framework_InstallerPlugins-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="9d4b3c425e6d6180c528f3aa0510d86328d56c2b58e626d88961ffc4fddfa5f5", url="https://pypi.org/packages/a1/17/9f2384f7d381716684f99f775fd2d78395a9aa0afa545ba0638bd7e7b858/pyobjc_framework_InstallerPlugins-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="b9dc036bc48554cd9eb1846f1fc96476e8d7e875b12fc488f09367fc7018af21", url="https://pypi.org/packages/98/ad/a7ac8c6e0928aae0f903f3fd309bf846071ddf1da380fbc7225503836424/pyobjc_framework_InstallerPlugins-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="b2a97431bef823d127e303e968111239301edc088e13b5b9239c207a2e139ad2", url="https://pypi.org/packages/88/69/f518bed1152f73fc484546a86539503059e955d10889d277f326eb841dbc/pyobjc_framework_InstallerPlugins-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="77f0277eb9851df5d4c803c136d0d7abd52bd3c5208491ec6af67dd49b77165a", url="https://pypi.org/packages/e2/69/043189c2ebb324bc9a15cc6f4542b4fdc069a34f4beab4244eb11d7b84a0/pyobjc_framework_InstallerPlugins-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="07da692d9621a1d80f6af2471983711bba5bced5515fcb7d9dd24ed68bcab487", url="https://pypi.org/packages/b5/77/fa95d2bd26ad7ea1391e2eb65f0bbb50399fd672b9e50529033fc7a02324/pyobjc_framework_InstallerPlugins-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="6ba6221f879f3642eadca628db4fa989f984e5371741e905b8696a25d2b2bfe9", url="https://pypi.org/packages/87/52/72e9d6e436332b90965a58ee013b0f7c5f4c73187ff7afe9e00fefbaee03/pyobjc_framework_InstallerPlugins-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="b2de297cb2e07e971ec068fad1f4d492a42e2a0d0e42a52681fbce231c3f3930", url="https://pypi.org/packages/74/70/63dba575056a21ab9b083db9681f856779f9d62d0761728ba43d32815a20/pyobjc_framework_InstallerPlugins-8.5-py2.py3-none-any.whl")

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

