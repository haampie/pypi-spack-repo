##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNbstripout(PythonPackage):
    version("0.6.1", sha256="5ff6eb0debbcd656c4a64db8e082a24fabcfc753a9e8c9f6d786971e8f29e110", url="https://pypi.org/packages/85/bd/b008a9f66ce2537ff86fbcd3beaf5a6fd86ede0897b0b6e9e65c447bb84a/nbstripout-0.6.1-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-nbformat", when="@0.3.2:")

