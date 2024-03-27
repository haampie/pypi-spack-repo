##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySphinxcontribJquery(PythonPackage):
    version("4.1", sha256="f936030d7d0147dd026a4f2b5a57343d233f1fc7b363f68b3d4f1cb0993878ae", url="https://pypi.org/packages/76/85/749bd22d1a68db7291c89e2ebca53f4306c3f205853cf31e9de279034c3c/sphinxcontrib_jquery-4.1-py2.py3-none-any.whl")
    version("4.0", sha256="001c7901eebf8b41a99d70b1c0b5cacdd2ce43f5b397f6ce3c43f8a74e6b3708", url="https://pypi.org/packages/b7/b4/409cced59c8dfac0a92627b703c39c0eb9fa58becb32f4b88fcec53b53b9/sphinxcontrib_jquery-4.0-py2.py3-none-any.whl")
    version("2.0.0", sha256="ed47fa425c338ffebe3c37e1cdb56e30eb806116b85f01055b158c7057fdb995", url="https://pypi.org/packages/42/e0/c492f21bf39616ea34a83994c3add2132134f9803e3516d918ef0b6a2a45/sphinxcontrib_jquery-2.0.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-setuptools", when="@:3")
        depends_on("py-sphinx@1.8.0:", when="@4:")

