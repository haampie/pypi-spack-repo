# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBlinker(PythonPackage):
    # BEGIN VERSIONS
    version("1.6.2", sha256="c3d739772abb7bc2860abf5f2ec284223d9ad5c76da018234f6f50d6f31ab1f0", url="https://pypi.org/packages/0d/f1/5f39e771cd730d347539bb74c6d496737b9d5f0a53bc9fdbf3e170f1ee48/blinker-1.6.2-py3-none-any.whl")
    version("1.4", sha256="471aee25f3992bd325afa3772f1063dbdbbca947a041b8b89466dc00d606f8b6", url="https://pypi.org/packages/1b/51/e2a9f3b757eb802f61dc1f2b09c8c99f6eb01cf06416c0671253536517b6/blinker-1.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@1.6")
    # END DEPENDENCIES

