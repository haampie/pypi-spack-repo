##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkMlcompute(PythonPackage):
    version("10.2", sha256="a191abf1c6aef061b4eab1aa8d4cf886fd6c98e53f6fedcd738ddd904571b933", url="https://pypi.org/packages/65/f3/06c02e1955a9068d5a43920ffe49a1016f3037cfce0aba1fc559cc7822fb/pyobjc_framework_MLCompute-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="25ed4d3002bd33c039f4ad9bf05b4830d53f67282a8399df7c65bd1430a01183", url="https://pypi.org/packages/00/e5/00450d67931fc87aa7bcdc2a9abc65de200ac14ac9e09ed27d1b3ca263c2/pyobjc_framework_MLCompute-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="8ba3eba33549a22acfdf589818ede36f65031425c6968eb193a9dad143d3cc64", url="https://pypi.org/packages/99/c0/550cb28761bf213eea52164c858f1d03e434eed62b5dd0d0fb53c82933d3/pyobjc_framework_MLCompute-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="702beaf4e449a96bc841fb99205ea4f5f1f70aa8e184984d91f8be0da3b1b72c", url="https://pypi.org/packages/02/1c/b52f9ed7f7e666a83dae827017a1100eb3ebed0555468b2d69885ebf8b5c/pyobjc_framework_MLCompute-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="c4100b5bc89b968db5c411143a59fffb0f76491827ee92987005e1ac82fa99cf", url="https://pypi.org/packages/04/02/91ee1a2fde66727f9e59d55e806e56cfc15351fba0e9b1982b749d91a959/pyobjc_framework_MLCompute-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="a2ce269ff3583228547af2dfe3afee6a703881c69db1a22b5b26d8146f4c2e90", url="https://pypi.org/packages/41/ec/5e68e00ef68e18f6d1e4f5ea1c13d219f284ed8a7e4018bff6e884e16496/pyobjc_framework_MLCompute-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="e1f37f7486e63dfbcdc3059bd52654e29ec3497e89e023eeba517d7c3b6dca1c", url="https://pypi.org/packages/cb/ad/fd63fcb24400e79bcc60cb8859187c3a8d65014be79cd9b56912ed1758e3/pyobjc_framework_MLCompute-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="f6fa1821c6c44515f9ec7fbcdfb7320e0c03666a052e8ea65f2d758530e1dc05", url="https://pypi.org/packages/e3/4a/7ab300d8ba2b38f395478922244db33c81489aa9d8bc26ec8c7ad2b8b411/pyobjc_framework_MLCompute-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="897539d254811b4f9d3ba614b2dc9213c5da86f2bc52dbd932ad2ae86f1388a9", url="https://pypi.org/packages/e3/f2/df2022265ecc58511fe7030c6bf56426735d9b3dc5e9d714beb7d3ed8278/pyobjc_framework_MLCompute-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="0b7d365f1a36913a1a1b02a5bae34bc4ace0d2adc950d3e0f0c0d07e21d9bb20", url="https://pypi.org/packages/57/ee/ef5665053327466688eb900ce66813f5d598dc887454d2657e958b60c45c/pyobjc_framework_MLCompute-8.5-py2.py3-none-any.whl")

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

