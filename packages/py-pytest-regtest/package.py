# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestRegtest(PythonPackage):
    # BEGIN VERSIONS
    version("2.1.1", sha256="bd08a6161832378b59ecd4f5815fbe26af7cd091db4a1e710e30476d5f3b8832", url="https://pypi.org/packages/7f/14/5930d9175f3a1cfbe6ab12519b8d1522ac039b2a8f3de6855580a8c2cfab/pytest_regtest-2.1.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pytest@7.2.1:", when="@2:")
    # END DEPENDENCIES

