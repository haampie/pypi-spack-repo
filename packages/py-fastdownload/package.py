##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFastdownload(PythonPackage):
    version("0.0.7", sha256="b791fa3406a2da003ba64615f03c60e2ea041c3c555796450b9a9a601bc0bbac", url="https://pypi.org/packages/47/60/ed35253a05a70b63e4f52df1daa39a6a464a3e22b0bd060b77f63e2e2b6a/fastdownload-0.0.7-py3-none-any.whl")
    version("0.0.6", sha256="e9fe28616112195561fb368dd6ba6b25d74ba1c16ed52353a11991967183327c", url="https://pypi.org/packages/8f/96/37080956658b9d294fedb66a3e274a0ac5acd63de139c7371dfb0ae4894b/fastdownload-0.0.6-py3-none-any.whl")
    version("0.0.5", sha256="bf5c48fd415e01484307dd619ff01fc0747f22b0ee01cafd1b2b3b98d34f31f4", url="https://pypi.org/packages/4a/7d/d352ae8f0aa2170f9e0ae4676148675a738cf9fd0c034bd024b82f7df8ed/fastdownload-0.0.5-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-fastcore@1.3.26:", when="@0.0.5:")
        depends_on("py-fastprogress")

