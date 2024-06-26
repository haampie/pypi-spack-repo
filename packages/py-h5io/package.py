# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyH5io(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.1.7", sha256="a6af826cea2da19901ca39a8a6212522c151cdf1fc171c4a381e3f7f25bb737e", url="https://pypi.org/packages/07/da/9a458c143ee79d7b340e2ac1301de14a9558336bdb07bfbd97f8e9252637/h5io-0.1.7-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@0.1.4:")
        depends_on("py-h5py", when="@0.1.7:")
        depends_on("py-numpy", when="@0.1.6:")
    # END DEPENDENCIES

