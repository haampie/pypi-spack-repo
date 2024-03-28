# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkEventkit(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="c9afa63fc2924281fdf1ef6c86cc2ba01b7b84a8545a826ddd89e4abd7077e81", url="https://pypi.org/packages/3f/44/91d97119ed7286cfbbfbb5918a28e6087abb1b9152a12bf8a230a9cf94b4/pyobjc_framework_EventKit-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="3265ef0bfab38508c50febfa922b4abf6ebc55a44f105d499e19231c225a027c", url="https://pypi.org/packages/32/f7/5fc7b983e03b68315e7150d5dab72ca0ac7a020e309561a780f5a8edda60/pyobjc_framework_EventKit-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="48d65edd47efd0864d93e5bbe3f05121c413d4006b7c0f0a3f0592b58d80a0db", url="https://pypi.org/packages/62/c4/1e6e78f4f554a85ef4c261315dd2e3a5551c28054da1cdd8868dd7bd5f04/pyobjc_framework_EventKit-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="8dda19382d18cccafa2c97eac0e4602546e7d9277787a359eeaddd83582cc365", url="https://pypi.org/packages/33/ee/aee0b942fa0590d2fffae822e4494feecac460aca0e8de7d6725feeb0749/pyobjc_framework_EventKit-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="768389131e4e48b859654a14b6b4650e413677a85bc794b327296b7e92b9d129", url="https://pypi.org/packages/a9/31/bb95685ceeb3d4b2338490d61bb96f76d66d530aa4e7e3ebe1152278e7eb/pyobjc_framework_EventKit-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="252c91b3b80438bd1baf9e7cb00544a1ff8c7b1551629c2f9b117eabe6997647", url="https://pypi.org/packages/85/82/7da87d49ff47946730f6b620787fe6258e7e34cecb66ca3ef2ef3c6c1e2b/pyobjc_framework_EventKit-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="714c35bd2dfc3b7ef55ac1d9339cec80762572f064f54a2fbc2d49a7c009692d", url="https://pypi.org/packages/ff/1b/f42f280a091e81a59c9de256988021d62c390a91fd2294455c2a116d7ae5/pyobjc_framework_EventKit-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="64375d523a369453ab0120bbb7140790904c950ac05bf9bbed1ac62ffb8fd0ee", url="https://pypi.org/packages/2d/1c/7d03480804e177c7f2e482030632698d36f25c998fc8a4bbd0e7a17d3000/pyobjc_framework_EventKit-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="ab801ce0aed58e3a989539d540ea7af8474ca69e01b2abf69d7ed7dde54750b6", url="https://pypi.org/packages/fc/83/1f0cd7ddad6db11735b97fe440739a499162691130038ac7628aca6b0937/pyobjc_framework_EventKit-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="6c77880ec39c47a8c016735f60d830324df65ddcbbd63cb106fed82f4fed0522", url="https://pypi.org/packages/c0/ea/55905ee3a867adad2e25078ffbfd65ff8d922bc4b3a20ad70b25cd9fa262/pyobjc_framework_EventKit-8.5-py2.py3-none-any.whl")
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
    # END DEPENDENCIES

