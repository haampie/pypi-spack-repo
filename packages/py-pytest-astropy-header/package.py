# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestAstropyHeader(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2.2", sha256="6088db080166d59f27c045247ad038ac8656f7c35d5c979cb87ed9a8f7efdee0", url="https://pypi.org/packages/10/db/3bde86b77504c01f8cc174ccce13029aa5e26daaae9fcdc08826f1f0c7a5/pytest_astropy_header-0.2.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@0.2:")
        depends_on("py-pytest@4.6:", when="@0.2:")
    # END DEPENDENCIES

