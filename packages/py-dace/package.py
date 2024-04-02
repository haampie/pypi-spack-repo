# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDace(PythonPackage):
    # BEGIN VERSIONS
    version("0.15.1", sha256="69bfdbbd5c7177f2926a874f5fa82fcdef61fc532c022b4bc12e1e9218724093", url="https://pypi.org/packages/33/8d/35a67fbc5c92751498d017bc7229ecfe6b595167c09989a85b404a4c4eda/dace-0.15.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("counters", default=False, description="counters")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@:3.12", when="@0.15:")
        depends_on("py-aenum@3.1:", when="@0.15:")
        depends_on("py-astunparse", when="@0.15:")
        depends_on("py-dataclasses", when="@0.15: ^python@:3.6")
        depends_on("py-dill", when="@0.15:")
        depends_on("py-flask", when="@0.15:")
        depends_on("py-fparser@0.1.3:", when="@0.15:")
        depends_on("py-networkx@2.5:", when="@0.15:")
        depends_on("py-numpy", when="@0.15:")
        depends_on("py-ply", when="@0.15:")
        depends_on("py-pyreadline", when="@0.15: platform=windows")
        depends_on("py-pyyaml", when="@0.15:")
        depends_on("py-requests", when="@0.15:")
        depends_on("py-sympy@:1.9", when="@0.15:")
        depends_on("py-typing-compat", when="@0.15: ^python@:3.7")
        depends_on("py-websockets", when="@0.15:")
    # END DEPENDENCIES

