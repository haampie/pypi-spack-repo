# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCheckmGenome(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.2.1", sha256="dcae47d7003dccf2f6d49cd7bfbdfa6d250550ef9164779522ac8e5f1158fe39", url="https://pypi.org/packages/b5/33/7d43376eb7b443dfbd88049178d2c7a9f3c638607eab957f98171ef3e3bf/checkm_genome-1.2.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-dendropy@4.5.2:", when="@1.1.11:")
        depends_on("py-matplotlib@3.5.1:", when="@1.1.11:")
        depends_on("py-numpy@1.21.3:", when="@1.1.11:")
        depends_on("py-pysam@0.19:", when="@1.1.11:")
        depends_on("py-scipy@1.7.3:", when="@1.1.11:")
        depends_on("py-setuptools", when="@1.1.4:")
    # END DEPENDENCIES

