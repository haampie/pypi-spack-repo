##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCycler(PythonPackage):
    version("0.12.1", sha256="85cef7cff222d8644161529808465972e51340599459b8ac3ccbac5a854e0d30", url="https://pypi.org/packages/e7/05/c19819d5e3d95294a6f5947fb9b9629efb316b96de511b418c53d245aae6/cycler-0.12.1-py3-none-any.whl")
    version("0.12.0", sha256="7896994252d006771357777d0251f3e34d266f4fa5f2c572247a80ab01440947", url="https://pypi.org/packages/2b/b3/70c33027c4918c10ccf176014b38f8b91cb18ac018a78854543a4fc72609/cycler-0.12.0-py3-none-any.whl")
    version("0.12.0-rc1", sha256="b6cde6f42951d145550a40e8ebc1985d2c8161e1ff3f419dc329a4c21920eca6", url="https://pypi.org/packages/ba/97/67c06c058c4afebeeef3a1857dc23bc35fa44f69b245b97fc1cbf116a101/cycler-0.12.0rc1-py3-none-any.whl")
    version("0.11.0", sha256="3a27e95f763a428a739d2add979fa7494c912a32c17c4c38c4d5f082cad165a3", url="https://pypi.org/packages/5c/f9/695d6bedebd747e5eb0fe8fad57b72fdf25411273a39791cde838d5a8f51/cycler-0.11.0-py3-none-any.whl")
    version("0.10.0", sha256="1d8a5ae1ff6c5cf9b93e8811e581232ad8920aeec647c37316ceac982b08cb2d", url="https://pypi.org/packages/f7/d2/e07d3ebb2bd7af696440ce7e754c59dd546ffe1bbe732c8ab68b9c834e61/cycler-0.10.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-six", when="@:0.10")

