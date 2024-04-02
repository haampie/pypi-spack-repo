# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTikzplotlib(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.9.8", sha256="e9c33fa35d7ec3024674207469f86bd9a29128783b55fc6b3bee968e8e28a8db", url="https://pypi.org/packages/e7/92/8c988a21d71cc773a63d5d25814cbdce16bf064899242d14e03d6a4f5df3/tikzplotlib-0.9.8-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-importlib-metadata", when="@0.9.3:0.9 ^python@:3.7")
        depends_on("py-matplotlib@1.4:")
        depends_on("py-numpy")
        depends_on("py-pillow")
    # END DEPENDENCIES

