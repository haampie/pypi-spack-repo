##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySpatialist(PythonPackage):
    version("0.4", sha256="a98c7345f588c1b7aad187ba7a4eb16ba2399512d6ac625cfe01134731f3326a", url="https://pypi.org/packages/b5/1c/fc55798cab73ac7dbb5f24ab55e24cc0f64d2996f5941dcdb43bcf7e7754/spatialist-0.4-py3-none-any.whl")
    version("0.2.8", sha256="97de7f9c0fbf28497ef28970bdf8093a152e691a783e7edad22998cb235154c6", url="https://pypi.org/packages/32/ef/a6f1f20c1741f8d181d2c6b3a9690e3fb998a67a47391f866f27c1c74bce/spatialist-0.2.8.tar.gz")

    with default_args(type="run"):
        depends_on("py-ipython", when="@:0.2.0,0.2.5:0.2.7,0.2.9:0.6")
        depends_on("py-ipywidgets", when="@:0.2.0,0.2.5:0.2.7,0.2.9:0.6")
        depends_on("py-jupyter", when="@:0.2.0,0.2.5:0.2.7,0.2.9:0.6")
        depends_on("py-matplotlib", when="@:0.2.0,0.2.5:0.2.7,0.2.9:")
        depends_on("py-numpy", when="@:0.2.0,0.2.5:0.2.7,0.2.9:")
        depends_on("py-pathos@0.2:", when="@:0.2.0,0.2.5:0.2.7,0.2.9:")
        depends_on("py-progressbar2", when="@:0.2.0,0.2.5:0.2.7,0.2.9:")
        depends_on("py-prompt-toolkit@2.0.10:2", when="@0.4")
        depends_on("py-pyyaml", when="@0.3:")
        depends_on("py-scoop", when="@:0.2.0,0.2.5:0.2.7,0.2.9:0.5")
        depends_on("py-tblib", when="@0.2.9:")

