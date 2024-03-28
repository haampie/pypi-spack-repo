# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureCliCommandModulesNspkg(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.0.3", sha256="41b89d69c402bcbb7db8702733754dcfc52202f1c8c304ecc041c8fccbe90822", url="https://pypi.org/packages/42/51/436547f814054aa131640b6519647b2b0c9c179d1beaa533fa72221fcf0b/azure_cli_command_modules_nspkg-2.0.3-py3-none-any.whl")
    version("2.0.2", sha256="0698597ce4bf5d90e335415c271c8d025fe75dce1655c1934ac00bd16a661ca5", url="https://pypi.org/packages/e6/c9/cdeeeabc550848e2a07caa66cba28aa057d23b6feaa824ceafd32c3f2226/azure_cli_command_modules_nspkg-2.0.2-py2.py3-none-any.whl")
    version("2.0.1", sha256="3043b6cc934bec4a3d70510aa46bb4956988a8988a56a6a139ea9accb8c621ad", url="https://pypi.org/packages/21/bf/0a6c3a39bce63ed68a5612b46b0b228dea3177543729a38a9e2c3f674152/azure_cli_command_modules_nspkg-2.0.1-py2.py3-none-any.whl")
    version("2.0.0", sha256="353ccd1a335df5fe7e373ef3690c6976beaf14d67ccfab4137d61f80e595909c", url="https://pypi.org/packages/30/66/2e4bbd2f3d312e4ec600ed0c710a65ab0080d9193a2d2c116af59cc0f0f8/azure_cli_command_modules_nspkg-2.0.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-cli-nspkg@3:", when="@:2.0.0,2.0.2:")
    # END DEPENDENCIES

