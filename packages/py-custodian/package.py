# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCustodian(PythonPackage):
    # BEGIN VERSIONS
    version("2022.5.26", sha256="92bdafa578c75f976176492e7bf3eb83abde97f112725e2e421633fa8954c6ef", url="https://pypi.org/packages/08/4b/879e76ee54aa3c9d3e0b2fccf1230ca9e5153a8867b1c79e1be9f94b9109/custodian-2022.5.26.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@2024:")
    # END DEPENDENCIES

