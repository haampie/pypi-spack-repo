# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPydot(PythonPackage):
    # BEGIN VERSIONS
    version("1.4.2", sha256="66c98190c65b8d2e2382a441b4c0edfdb4f4c025ef9cb9874de478fb0793a451", url="https://pypi.org/packages/ea/76/75b1bb82e9bad3e3d656556eaa353d8cd17c4254393b08ec9786ac8ed273/pydot-1.4.2-py2.py3-none-any.whl")
    version("1.4.1", sha256="67be714300c78fda5fd52f79ec994039e3f76f074948c67b5ff539b433ad354f", url="https://pypi.org/packages/33/d1/b1479a770f66d962f545c2101630ce1d5592d90cb4f083d38862e93d16d2/pydot-1.4.1-py2.py3-none-any.whl")
    version("1.2.3", sha256="edb5d3f249f97fbd9c4bb16959e61bc32ecf40eee1a9f6d27abe8d01c0a73502", url="https://pypi.org/packages/ae/e6/2c0b7c142c18fb89b294734d45d4264a71269686090af69404df211754c3/pydot-1.2.3.tar.gz")
    version("1.2.2", sha256="04a97a885ed418dcc193135cc525fa356cad8b16719293295a149b30718ce400", url="https://pypi.org/packages/87/d0/3f3a3d2a57b2ca29ea37c93917a3b25858f4cccc5611767bcdef9770ccc7/pydot-1.2.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyparsing@2.1.4:", when="@1.3:1")
    # END DEPENDENCIES

