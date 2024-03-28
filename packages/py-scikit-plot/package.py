# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyScikitPlot(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.3.7", sha256="6b3d529800b32a899c54dc5761a93c63cbff482b1889a4afee57dd219f3ef0c3", url="https://pypi.org/packages/7c/47/32520e259340c140a4ad27c1b97050dd3254fdc517b1d59974d47037510e/scikit_plot-0.3.7-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-joblib@0.10:", when="@0.3.5:")
        depends_on("py-matplotlib@1.4:", when="@0.3.5:")
        depends_on("py-scikit-learn@0.18:", when="@0.3.5:")
        depends_on("py-scipy@0.9:", when="@0.3.5:")
    # END DEPENDENCIES

