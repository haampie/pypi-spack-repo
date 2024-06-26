# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBagitProfile(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.3.1", sha256="7565a95902cbdc9a646eece0939cfec025d77b00764d10538fd3d5962fa1c2b7", url="https://pypi.org/packages/a6/8e/a780f9d13ecfcd69e22cd6ba4497248abf82463386f616330f03da2b8a37/bagit_profile-1.3.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-bagit", when="@1.2:")
        depends_on("py-requests", when="@1.2:")
    # END DEPENDENCIES

