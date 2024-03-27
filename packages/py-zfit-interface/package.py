##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyZfitInterface(PythonPackage):
    version("0.0.3", sha256="c41cf79f1da4150b9a60bb1e8cab15df895b6ff4b753e2306494a7abda4150d0", url="https://pypi.org/packages/61/ce/07d8fa63a501dc3af9639595e486be0a18de00726b54a7dc88a5ada235d8/zfit_interface-0.0.3-py2.py3-none-any.whl")
    version("0.0.1", sha256="a67273e379f2af0ee0fdeb80de50f1e4cdaeb66ac114fdd93780513c26a84fc3", url="https://pypi.org/packages/df/6f/69fbadc5807978368d3facf16bea9f19c16225d3145ce194df30096725a6/zfit-interface-0.0.1.linux-x86_64.tar.gz")

    with default_args(type="run"):
        depends_on("py-numpy", when="@0.0.3:")
        depends_on("py-typing-extensions", when="@0.0.3:")
        depends_on("py-uhi", when="@0.0.3:")

