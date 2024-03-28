# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRocrate(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.7.0", sha256="86443b621e4eb31eb501c202402ce0d8d8b0e9d5f8a446296d8df83ac21c0d53", url="https://pypi.org/packages/3b/b9/20dea9f6f79c4032fc2ab971bacfcd91a59e452d66cd3d04e6a1a3ef7a0f/rocrate-0.7.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-arcp@0.2.1:")
        depends_on("py-click", when="@0.4:")
        depends_on("py-galaxy2cwl")
        depends_on("py-jinja2")
        depends_on("py-python-dateutil", when="@0.2.3:")
        depends_on("py-requests", when="@0.3.1:")
    # END DEPENDENCIES

