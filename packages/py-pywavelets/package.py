# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPywavelets(PythonPackage):
    # BEGIN VERSIONS
    version("1.4.1", sha256="6437af3ddf083118c26d8f97ab43b0724b956c9f958e9ea788659f6a2834ba93", url="https://pypi.org/packages/6e/d4/008dceeb95fafcf141f39393bdfc10921d0b62a325c2794ac533195a1eb3/PyWavelets-1.4.1.tar.gz")
    version("1.1.1", sha256="1a64b40f6acb4ffbaccce0545d7fc641744f95351f62e4c6aaa40549326008c9", url="https://pypi.org/packages/17/6b/ef989cfb3acff2ea966c5f28a7443ccaec2ee136675dfa0366db2635f78a/PyWavelets-1.1.1.tar.gz")
    version("0.5.2", sha256="ce36e2f0648ea1781490b09515363f1f64446b0eac524603e5db5e180113bed9", url="https://pypi.org/packages/4b/df/3fff2a8b96ef7df6e4e8642fb7569c3717ae562dd76afe0f96525c0af784/PyWavelets-0.5.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@1.4.1:1.4")
        depends_on("py-numpy@1.13.3:", when="@1.1")
    # END DEPENDENCIES

