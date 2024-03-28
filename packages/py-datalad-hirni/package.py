# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDataladHirni(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.0.8", sha256="75566a377a79792cb4b6fb939b79f30ad18bef56ae207752cc0c3728607820fe", url="https://pypi.org/packages/49/e9/390e456a99be0f6f1f9ea00d06f5046a4b789fd7302217145af76821589d/datalad_hirni-0.0.8-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-datalad@0.14.0:+full", when="@0.0.8:")
        depends_on("py-datalad-container@1.1.2:", when="@0.0.8:")
        depends_on("py-datalad-metalad@0.2:", when="@0.0.4:")
        depends_on("py-datalad-neuroimaging@0.3.1:", when="@0.0.7:")
        depends_on("py-datalad-webapp@0.3:", when="@0.0.6:")
    # END DEPENDENCIES

