##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMplhep(PythonPackage):
    version("0.3.26", sha256="1490d127e37f843579d0d5b643f053e6cf54d6966831211cd87246e3c532d70f", url="https://pypi.org/packages/94/08/99ac2ed8e6be593f8c3f2c593ed36db5c0f5acd27af2601f21fb7f309eb5/mplhep-0.3.26-py3-none-any.whl")
    version("0.3.15", sha256="d5719d19d247caa18916b93e4484cb1c519d8528fb09e1671094f947eaa407ab", url="https://pypi.org/packages/33/80/4888aa2686b6ef6de6b1275f442fd88f3ef2f6dba0cb21f452e605cb2f29/mplhep-0.3.15-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-matplotlib@3.4.0:", when="@0.3:")
        depends_on("py-mplhep-data", when="@0.3:")
        depends_on("py-numpy@1.16.0:", when="@0.0.26:")
        depends_on("py-packaging", when="@0.0.26:")
        depends_on("py-scipy@1.1.0:", when="@0.0.26:0.2")
        depends_on("py-uhi@0.2:", when="@0.3:")

