# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestWorkflow(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.6.0", sha256="bb1f1dbc2cfa4d4a9af45e7764fb8e65d8baa59cb0db72cf88ff0ad1590887e6", url="https://pypi.org/packages/09/3e/af45083f33ce8d4a412f9f7264254b689e6182c85619219fb8086294f158/pytest_workflow-1.6.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-jsonschema")
        depends_on("py-pytest@5.4:", when="@1.3:1")
        depends_on("py-pyyaml")
    # END DEPENDENCIES

