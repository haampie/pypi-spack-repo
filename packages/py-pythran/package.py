##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythran(PythonPackage):
    version("0.12.2", sha256="06ce86851b17384bced121beacae3a99705d2477e6ca67ae243b73912b9287f1", url="https://pypi.org/packages/21/5b/0ac28c9cdddbd262a5a14e3d6bcff662b967ea678a3638cb79e153b93843/pythran-0.12.2-py3-none-any.whl")
    version("0.12.0", sha256="f06c23e1045030a29cabe07161b61c511edf662cd0cd0b439ecde24a50e28eb5", url="https://pypi.org/packages/f4/1a/71f510d40adfefa5369388c0fe186981821cfb34bc4de2e6729b03363ea9/pythran-0.12.0-py3-none-any.whl")
    version("0.11.0", sha256="8fea162e6096c6a3d45613a9a5389db739bf78805e713f853c9fcc7113ab9369", url="https://pypi.org/packages/ae/5a/2fc283c873b9d3f5a612238165756b9e75ac345250f6c1511e0c60c181b5/pythran-0.11.0-py3-none-any.whl")
    version("0.10.0", sha256="cf798c838daba8cffd65549bdb3f79fe12bc2aef18d49bb14284d2b1058ea08e", url="https://pypi.org/packages/0a/c4/187ae2c4d39fabb8e0bb75521a00b04ba51bf37622ab799d5fc28182ea5d/pythran-0.10.0-py3-none-any.whl")
    version("0.9.12", sha256="b25c6f6c708c3b9a2c360f42e33e5f5f33e96b95c3799c729a638004633f078a", url="https://pypi.org/packages/eb/12/321a3e6bb9f903ba34929554f043b40446f596f5e7f04cc9b32d619f913e/pythran-0.9.12-py3-none-any.whl")
    version("0.9.11", sha256="d28e6651f6006c3fc2ca9701f0da33d91abb13fc198d0e9d0003d8d39d02f37e", url="https://pypi.org/packages/cf/15/4eeb85ed6aeaf13569a029c15143d8d550a6ae215dba57c267924bfdaf14/pythran-0.9.11-py3-none-any.whl")
    version("0.9.10", sha256="84b0bda5821048c556be368bdb6b4dd26a6bd88950331ddd9abbe16cae6567b6", url="https://pypi.org/packages/8b/31/931987bf2c151adc38a860938f0acabdc719a5aaa01edcde7dfbc8295723/pythran-0.9.10-py3-none-any.whl")
    version("0.9.9", sha256="39256c01dd27dffb35a2c9dfc01003f2118237f016f47a033f11c581954670ee", url="https://pypi.org/packages/b4/0a/78dc4ac761aaecc27323956f9bf69cc692fa721d9d62a2dbeff8de43bebf/pythran-0.9.9-py3-none-any.whl")
    version("0.9.8", sha256="d509d7b18557fc6d29778832863c137dbd55210c017114ad6ccdb49dbbce66f0", url="https://pypi.org/packages/8e/6b/cd2d8a0af48600fe3d9507f5fb6e5952a8d74507bcfd3f84bab3801eb5ca/pythran-0.9.8-py3-none-any.whl")
    version("0.9.7", sha256="b5f433d06e930efe7ba69ec0c50e7e19e9050c56b618787840f540cc38387aba", url="https://pypi.org/packages/26/3d/2efc9dd28984bf59176d592ea52bbcb79bcaaada3294601959ec8db5d03c/pythran-0.9.7-py3-none-any.whl")
    version("0.9.6", sha256="2af4f0d15916fe8d621a23e8dbfb16920dd3bfd07e63aca07e79ff223019e621", url="https://pypi.org/packages/73/81/e87e9c4e3571ff89242434e8e8ee46f4e162a776246c93fd691f27d62fbe/pythran-0.9.6-py3-none-any.whl")
    version("0.9.5", sha256="815a778d6889593c0b8ddf08052cff36a504ce4cc8bd8d7bfb856a212f91486e", url="https://pypi.org/packages/6f/df/d4f805e04d1b26900e284de27c900867ff9acefe67c452aa8ae9bedeb405/pythran-0.9.5.tar.gz")
    version("0.9.4", sha256="ec9c91f5331454263b064027292556a184a9f55a50f8615e09b08f57a4909855", url="https://pypi.org/packages/89/66/610a3cdd0ca916e2e82098d4f8b6a9ffb320c7bbf39b872c15910ea95f28/pythran-0.9.4.tar.gz")
    version("0.9.3", sha256="217427a8225a331fdc8f3efe57871aed775cdf2c6e847a0a83df0aaae4b02493", url="https://pypi.org/packages/01/4d/6af15b6deeff16cbde453a08137c87dee6290a2cca8fd73c534400314224/pythran-0.9.3.tar.gz")

    with default_args(type="run"):
        depends_on("py-beniget@0.4:", when="@0.9.12:")
        depends_on("py-beniget@0.3", when="@0.9.7:0.9.11")
        depends_on("py-beniget@0.2.1:0.2", when="@0.9.6")
        depends_on("py-decorator", when="@0.9.6:0.9.11")
        depends_on("py-gast@:0.5.3", when="@0.12.2:0.12")
        depends_on("py-gast@0.5:", when="@0.9.12:0.12.1,0.13:")
        depends_on("py-gast@0.4", when="@0.9.7:0.9.11")
        depends_on("py-gast@0.3.3:0.3", when="@0.9.6")
        depends_on("py-networkx@2:", when="@0.9.6:0.9.11")
        depends_on("py-numpy", when="@0.9.6:")
        depends_on("py-ply", when="@0.9.6:")
        depends_on("py-six", when="@0.9.6:0.9.11")

