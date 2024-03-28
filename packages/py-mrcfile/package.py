# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMrcfile(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.4.3", sha256="798fa12f2861e74d627546bd1989836857b10090fa2a148913ea468bbbb27e80", url="https://pypi.org/packages/09/b5/c1a218305dfb1165a5d058373d57c64b9dac0def8bcca3f31f1376b72ada/mrcfile-1.4.3-py2.py3-none-any.whl")
    version("1.3.0", sha256="4eeaed257eee22dbe142481c35498244d190e4ca10a2daf2ba3749db6822fd41", url="https://pypi.org/packages/7d/b3/6d35d37e5f51ebb1a6ed4c5178206705bcaf8848c853db790254a15039be/mrcfile-1.3.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.16.0:", when="@1.4:")
        depends_on("py-numpy@1.12.0:", when="@0.2:0.2.3,1.2:1.3")
    # END DEPENDENCIES

