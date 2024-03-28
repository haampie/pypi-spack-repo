# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestDatadir(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.4.1", sha256="095f441782b1b907587eca7227fdbae94be43f1c96b4b2cbcc6801a4645be1af", url="https://pypi.org/packages/46/0f/063f1d9754258254a61d20926ef1a7635f72a42604b12c036e0fc77aa1be/pytest_datadir-1.4.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pytest@5:", when="@1.4:")
    # END DEPENDENCIES

