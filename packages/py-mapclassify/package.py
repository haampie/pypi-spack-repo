# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMapclassify(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.4.2", sha256="e2c9585bc0b17457d6b13bacaf1fc4222f7196408b6317e431b0397a03dad8c3", url="https://pypi.org/packages/22/8e/d968c0945d41bb02de0efaa92e31e43a817dc52d30e82b4dfdda407a1903/mapclassify-2.4.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-networkx", when="@2.3:2.6.0,23:")
        depends_on("py-numpy@1.3:", when="@2.3:2.6.0,23:")
        depends_on("py-pandas@1.0.0:", when="@2.3:2.6.0,23:")
        depends_on("py-scikit-learn", when="@2.3:2.6.0,23:")
        depends_on("py-scipy@1.0.0:", when="@2.3:2.6.0,23:")
    # END DEPENDENCIES

