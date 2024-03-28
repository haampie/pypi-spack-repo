# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureCliNspkg(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.0.4", sha256="34ff69dfed9180aa945bca2c0b7e5603d84e92b28c531efe4beae51a7230791d", url="https://pypi.org/packages/fe/1f/babf85745bc6b1ab770e38a330edd651dde61dd662174adb562d4452d9be/azure_cli_nspkg-3.0.4-py3-none-any.whl")
    version("3.0.3", sha256="34095c34a04a31868356115f7a2a5eba5e93afb28a35713a713f2ea587b72d2c", url="https://pypi.org/packages/a7/85/601ef6484bf7a722daa76a4383c4ccfd4980b74ed6c2895392f53ed210d5/azure_cli_nspkg-3.0.3-py2.py3-none-any.whl")
    version("3.0.2", sha256="983f9502fa8e0548264b627d2f206c222fa8317b4647a6cdf75927fa28f2847f", url="https://pypi.org/packages/7c/94/cf884b92a870422f02c3f1f86573d04d5cc1abdc2ac51b8419c7ee2e2a00/azure_cli_nspkg-3.0.2-py2.py3-none-any.whl")
    version("3.0.1", sha256="199948b8de83d469ad28cea789ada89df23d131872576444b85514427e0bc50d", url="https://pypi.org/packages/ed/dc/47204daed774040dfb57bc758ace4c7cb85a2c6d71e80e4d787c76151a86/azure_cli_nspkg-3.0.1-py2.py3-none-any.whl")
    version("3.0.0", sha256="83734064086dab02983670996eb779433ac65ce8d3b7efd73ccd03570f5f43ae", url="https://pypi.org/packages/9d/72/224f496cc4b07826dfac4242e9ccc8d3eacc890a661afae4f0cc31b038d3/azure_cli_nspkg-3.0.0-py2.py3-none-any.whl")
    version("2.0.0", sha256="fd2c943e89f186ccb8e27601a93d6a184a096ad4981aafc8a347f27dfa2c6dfb", url="https://pypi.org/packages/79/10/d13677c955f05fd6e37d17a67fc473b83dc345060001984a9ddd55a7fe55/azure_cli_nspkg-2.0.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-nspkg@2:", when="@3:3.0.0,3.0.2:")
    # END DEPENDENCIES

