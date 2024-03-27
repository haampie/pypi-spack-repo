##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHistoprint(PythonPackage):
    version("2.4.0", sha256="db5c07309ab12788c85ea2c679c47d49f1e961a5d4254270521c3e883256236a", url="https://pypi.org/packages/4b/f1/b8e4e56241f53f4db673d8927eb92b0a374f0ef57791764597b182cee1cd/histoprint-2.4.0-py3-none-any.whl")
    version("2.3.0", sha256="ac808ee80467afccdb777f928c3278cc359fb1540bce40203d9355e2c420ec31", url="https://pypi.org/packages/27/46/6799c7c4dc4c987ab40e81588199a642b4656ddd7c4ca22adb651d6ed01a/histoprint-2.3.0-py3-none-any.whl")
    version("2.2.1", sha256="b373df678bde3cc0328d048094618054ee4069351532f83591d5e7cbb6635915", url="https://pypi.org/packages/e4/42/da77a3f89756d2eb13bbd5d48edaca2caca176165ab9c7d43d1bde1abdc1/histoprint-2.2.1-py3-none-any.whl")
    version("2.2.0", sha256="bb2278172379b82aaa3b79e56896b51aad084902ddea7f076b5c4bf08c19ca6d", url="https://pypi.org/packages/a5/a7/435cd9b0955a20d96fbe56e175856ac4dbdb1eeadf717d7b653d431a63c9/histoprint-2.2.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-click@7:", when="@1.2:")
        depends_on("py-numpy", when="@2:")
        depends_on("py-uhi@0.2.1:", when="@2.2:")

