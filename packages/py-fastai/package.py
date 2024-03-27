##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFastai(PythonPackage):
    version("2.5.3", sha256="b6df7ae938a0fc587c89c350c1b3d8afba88f6ca7a722f7d367f95a3683cb5b0", url="https://pypi.org/packages/73/9a/661a804675d913535159d8de99e008d730382802dff12a3e990917aaebbb/fastai-2.5.3-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-fastcore@1.3.22:1.3", when="@2.5.3")
        depends_on("py-fastdownload@0.0.5:", when="@2.5.1:")
        depends_on("py-fastprogress@0.2.4:", when="@2:")
        depends_on("py-ipywidgets", when="@0.7:0")
        depends_on("py-matplotlib", when="@0.7:1.0.58,1.0.60:")
        depends_on("py-opencv-python", when="@0.7:0")
        depends_on("py-packaging", when="@1.0.38:1.0.58,1.0.60:")
        depends_on("py-pandas", when="@0.7:1.0.58,1.0.60:")
        depends_on("py-pillow@6.1:", when="@2.1.9:2.7.12")
        depends_on("py-pip", when="@2:")
        depends_on("py-pyyaml", when="@0.7:0,1.0.10:1.0.58,1.0.60:")
        depends_on("py-requests", when="@1:1.0.58,1.0.60:")
        depends_on("py-scikit-learn", when="@2:")
        depends_on("py-scipy", when="@0.7:1.0.58,1.0.60:")
        depends_on("py-spacy@:3", when="@2.3.1:")
        depends_on("py-torch@1.7:1.10", when="@2.5.3:2.5.5")
        depends_on("py-torchvision@0.8.2:", when="@2.3.1:2.7.12")

