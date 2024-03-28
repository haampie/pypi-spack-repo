# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMaturin(PythonPackage):
    # BEGIN VERSIONS
    version("1.4.0", sha256="ed12e1768094a7adeafc3a74ebdb8dc2201fa64c4e7e31f14cfc70378bf93790", url="https://pypi.org/packages/20/90/43a3aa35f037e91582ec7516a92084a71f84e89e39ef580813bed072b154/maturin-1.4.0.tar.gz")
    version("1.1.0", sha256="4650aeaa8debd004b55aae7afb75248cbd4d61cd7da2dcf4ead8b22b58cecae0", url="https://pypi.org/packages/7b/78/2814bc0e46a96861aab337fd0404e7937acdb4ce187da239224ab4560d35/maturin-1.1.0.tar.gz")
    version("0.14.17", sha256="fb4e3311e8ce707843235fbe8748a05a3ae166c3efd6d2aa335b53dfc2bd3b88", url="https://pypi.org/packages/e4/83/8d43216b175e5840802af49d530761bce3176f0b502c561d1735eab82b57/maturin-0.14.17.tar.gz")
    version("0.13.7", sha256="c0a77aa0c57f945649ca711c806203a1b6888ad49c2b8b85196ffdcf0421db77", url="https://pypi.org/packages/4f/19/6f982e341612ab442f90ba1a047a4188d48473ad0d1dbfb3dffdaa20e095/maturin-0.13.7.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-tomli@1.1:", when="@0.12.10-beta4: ^python@:3.10")
    # END DEPENDENCIES

