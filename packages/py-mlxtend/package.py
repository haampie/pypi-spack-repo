# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMlxtend(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.16.0", sha256="aa31f086a2af17425c0b149616b85523eaac6de79bc432abaf0782a70cc06dda", url="https://pypi.org/packages/c0/ca/54fe0ae783ce81a467710d1c5fb41cfca075121139b48327b807020dc40c/mlxtend-0.16.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-matplotlib@1.5.1:", when="@0.16")
        depends_on("py-numpy@1.10.4:", when="@0.16")
        depends_on("py-pandas@0.17.1:", when="@0.16")
        depends_on("py-scikit-learn@0.18:", when="@0.16")
        depends_on("py-scipy@0.17:", when="@0.16")
        depends_on("py-setuptools", when="@0.16:0.22")
    # END DEPENDENCIES

