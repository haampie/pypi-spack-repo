##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonXlib(PythonPackage):
    version("0.30", sha256="c4c92cd47e07588b2cbc7d52de18407b2902c3812d7cdec39cd2177b060828e2", url="https://pypi.org/packages/54/c3/45ecfd3e6a541bb4b383fc320a32762703cfe28763c131d71f4183ace819/python_xlib-0.30-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-six@1.10:")

