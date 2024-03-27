##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkNaturallanguage(PythonPackage):
    version("10.2", sha256="0165735973a720f09bd5a2333f32e16aac52332fb595425480d7a2215472d4fb", url="https://pypi.org/packages/14/d2/c82aca0db9492633be84c56c4b4c206cbff9ea762290c3850cade423c511/pyobjc_framework_NaturalLanguage-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="02bb4df955ecf329cf6da77ca6952777e5b2a10aee67452ea6314ec632cbc475", url="https://pypi.org/packages/bf/7a/38a136ed05f5de06675e69d6d1fb84e1b98cfb704fd0f3d5eaea232ea282/pyobjc_framework_NaturalLanguage-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="8924630ff802486dd16a426d75fddfc7e6cd917fecd5ff3902b84107051130cb", url="https://pypi.org/packages/7b/c5/c00240cda3096c6cc183419439d7332764a6a12311b5cba1e1c044f53b06/pyobjc_framework_NaturalLanguage-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="b81bdc87eaa153d58e2db5c503d73b221561f7b310f8f7b9d5ed16721eb724ec", url="https://pypi.org/packages/e1/38/da51494e0772e0506d4698927cd2ce01760cf10684adc5f1b877ca605286/pyobjc_framework_NaturalLanguage-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="c80391a2a65a2182cf09e0c2dde4428c16fbbfe7f237729471a5ff7ee4908e8f", url="https://pypi.org/packages/75/5d/7f7c7ff8875c8a4a3eeb61c1c13d9333d53c8acd65d3a28bef71c1b40252/pyobjc_framework_NaturalLanguage-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="27bd026c93959ed6cab56dd41b0afedf3bd91ec0f20d7788cfa022b2c86cc923", url="https://pypi.org/packages/a7/63/d8eb0aacc4a59832ba790a4ffd119b9ac67c17b84e666dbecee929b67005/pyobjc_framework_NaturalLanguage-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="6791885064044a769d0324c676e9e2c0e66bd8e13daef201ba06562077885082", url="https://pypi.org/packages/6a/97/09442466981220e98e9b6fdc44fab81ee121a4c20e12c7d17fee76569433/pyobjc_framework_NaturalLanguage-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="8f75657fc019c8517fe774f754dd73642ac1e37df2e5d35933da1f5df809989d", url="https://pypi.org/packages/80/6c/22a97b191aaaa6b6dcc26097a1400f9f1397b6630c1f0ee52b52c187f91a/pyobjc_framework_NaturalLanguage-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="f8039e8db941d07d989c7e7d0a44ce61a6aee6cea3b1d2178256e82dfcd289bd", url="https://pypi.org/packages/31/30/3e4df034c1eb1de3901b818505787bc0a694685106e9c92ed9b22700cfc9/pyobjc_framework_NaturalLanguage-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="89c01c581392deeda7f11fd9847d067621cd4104ac5c4ac0cab82f9b5784d811", url="https://pypi.org/packages/bd/07/2486c7e2da494aecdb17660dd44146fa638b62360f50c5de8003c2b90237/pyobjc_framework_NaturalLanguage-8.5-py2.py3-none-any.whl")

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

