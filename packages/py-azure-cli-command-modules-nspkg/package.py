# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureCliCommandModulesNspkg(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.0.3", sha256="41b89d69c402bcbb7db8702733754dcfc52202f1c8c304ecc041c8fccbe90822", url="https://pypi.org/packages/42/51/436547f814054aa131640b6519647b2b0c9c179d1beaa533fa72221fcf0b/azure_cli_command_modules_nspkg-2.0.3-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-cli-nspkg@3:", when="@:2.0.0,2.0.2:")
    # END DEPENDENCIES

