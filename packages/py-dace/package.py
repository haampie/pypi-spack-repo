##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDace(PythonPackage):
    version("0.15.1", sha256="69bfdbbd5c7177f2926a874f5fa82fcdef61fc532c022b4bc12e1e9218724093", url="https://pypi.org/packages/33/8d/35a67fbc5c92751498d017bc7229ecfe6b595167c09989a85b404a4c4eda/dace-0.15.1.tar.gz")

    with default_args(type="run"):
        depends_on("python@:3.12", when="@0.15:")
        depends_on("python@:3.11", when="@0.14.4:0.14")
        depends_on("python@:3.10", when="@0.11.4:0.14.3")
        depends_on("python@:3.9", when="@0.11:0.11.3")
        depends_on("python@:3.8", when="@0.10.8:0.10")
        depends_on("py-absl-py", when="@:0.9")
        depends_on("py-aenum@3.1:", when="@0.15:")
        depends_on("py-astunparse", when="@:0.10,0.15:")
        depends_on("py-dill", when="@0.10.8:0.10,0.15:")
        depends_on("py-flask", when="@:0.10,0.15:")
        depends_on("py-fparser@0.1.3:", when="@0.15:")
        depends_on("py-networkx@2.5:", when="@0.15:")
        depends_on("py-numpy", when="@:0.10,0.15:")
        depends_on("py-ply", when="@:0.10,0.15:")
        depends_on("py-pyreadline", when="@0.15: platform=windows")
        depends_on("py-pyreadline", when="@0.10.8:0.10")
        depends_on("py-pyyaml", when="@:0.10,0.15:")
        depends_on("py-requests", when="@:0.10,0.15:")
        depends_on("py-scipy", when="@:0.9")
        depends_on("py-sympy@:1.9", when="@0.15:")
        depends_on("py-websockets", when="@:0.10,0.15:")

