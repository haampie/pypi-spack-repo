# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyStratify(PythonPackage):
    # BEGIN VERSIONS
    version("0.1", sha256="5426f3b66e45e1010952d426e5a7be42cd45fe65f1cd73a98fee1eb7c110c6ee", url="https://pypi.org/packages/f9/a6/067946d74affbd4bb1130f157f7be6b9f8ce6be56d8eb694cffce9b53e19/stratify-0.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.3:")
    # END DEPENDENCIES

