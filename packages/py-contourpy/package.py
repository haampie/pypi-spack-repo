# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyContourpy(PythonPackage):
    # BEGIN VERSIONS
    version("1.0.7", sha256="d8165a088d31798b59e91117d1f5fc3df8168d8b48c4acc10fc0df0d0bdbcc5e", url="https://pypi.org/packages/b4/9b/6edb9d3e334a70a212f66a844188fcb57ddbd528cbc3b1fe7abfc317ddd7/contourpy-1.0.7.tar.gz")
    version("1.0.5", sha256="896631cd40222aef3697e4e51177d14c3709fda49d30983269d584f034acc8a4", url="https://pypi.org/packages/38/b3/d6fd43ab2eadce72ac089328d80e9cdf274efdb79a9933aaf52ef1621e99/contourpy-1.0.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.2:")
    # END DEPENDENCIES

