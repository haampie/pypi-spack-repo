##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPydot(PythonPackage):
    version("2.0.0", sha256="408a47913ea7bd5d2d34b274144880c1310c4aee901f353cf21fe2e526a4ea28", url="https://pypi.org/packages/7f/90/c9b51f3cdff89cd8f93382060330f43d1af098a6624cff439e700791e922/pydot-2.0.0-py3-none-any.whl")
    version("1.4.2", sha256="66c98190c65b8d2e2382a441b4c0edfdb4f4c025ef9cb9874de478fb0793a451", url="https://pypi.org/packages/ea/76/75b1bb82e9bad3e3d656556eaa353d8cd17c4254393b08ec9786ac8ed273/pydot-1.4.2-py2.py3-none-any.whl")
    version("1.4.1", sha256="67be714300c78fda5fd52f79ec994039e3f76f074948c67b5ff539b433ad354f", url="https://pypi.org/packages/33/d1/b1479a770f66d962f545c2101630ce1d5592d90cb4f083d38862e93d16d2/pydot-1.4.1-py2.py3-none-any.whl")
    version("1.4.0", sha256="caa91aacce405b2de17c9610c8d43873731239433080d9df5f5a4221baa007f7", url="https://pypi.org/packages/53/11/9db5c788f5ad05438b7c2a07fd7edd9820b7f3d95bb0690a16f7bf426204/pydot-1.4.0-py2.py3-none-any.whl")
    version("1.3.0", sha256="dbb8c123ea6ea6cf09eca2403e597244a960b31e70c2a5c8a2a8a2e2594ce191", url="https://pypi.org/packages/50/da/68cee64ad379462abb743ffb665fa34b214df85d263565ad2bd512c2d935/pydot-1.3.0-py2.py3-none-any.whl")
    version("1.2.4", sha256="92d2e2d15531d00710f2d6fb5540d2acabc5399d464f2f20d5d21073af241eb6", url="https://pypi.org/packages/c3/f1/e61d6dfe6c1768ed2529761a68f70939e2569da043e9f15a8d84bf56cadf/pydot-1.2.4.tar.gz")
    version("1.2.3", sha256="edb5d3f249f97fbd9c4bb16959e61bc32ecf40eee1a9f6d27abe8d01c0a73502", url="https://pypi.org/packages/ae/e6/2c0b7c142c18fb89b294734d45d4264a71269686090af69404df211754c3/pydot-1.2.3.tar.gz")
    version("1.2.2", sha256="04a97a885ed418dcc193135cc525fa356cad8b16719293295a149b30718ce400", url="https://pypi.org/packages/87/d0/3f3a3d2a57b2ca29ea37c93917a3b25858f4cccc5611767bcdef9770ccc7/pydot-1.2.2.tar.gz")
    version("1.1.0", sha256="469d2cf565994064236be24e87ab3571c1c1243fbc8d2ad836d16637d1a5049b", url="https://pypi.org/packages/da/9c/2ee9bed5653839c00252670b65b28c734803ff2d61e97e99ef58a4a4e715/pydot-1.1.0.tar.gz")
    version("1.0.29", sha256="3472c7fb21364c2f844477e0a6fc62424afbd12dbd593cfc96f6d7bbe44f1de9", url="https://pypi.org/packages/8d/ca/bed32e7ced110aeef48a223610e57382bc52a043e14de656de98a492546c/pydot-1.0.29.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyparsing@3.0.0:", when="@2:")
        depends_on("py-pyparsing@2.1.4:", when="@1.3:1")

