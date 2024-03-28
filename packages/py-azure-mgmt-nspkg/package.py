# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtNspkg(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.0.2", sha256="1c6f5134de78c8907e8b73a8ceaaf1f336a24193a543039994fe002bb5f7f39f", url="https://pypi.org/packages/a1/6e/464d039ec6184234b188d6a9d199e658cce86b38afe4db0e8edd1629f3f6/azure_mgmt_nspkg-3.0.2-py2-none-any.whl")
    version("3.0.1", sha256="5d774a838e9807e09ff9d0551ba90043697b64de5b82f4d904f14295f9cacbfb", url="https://pypi.org/packages/5f/5b/d7744ec797bf5c8b0598af799f403b222d319fe0c2462554595d1930a73b/azure_mgmt_nspkg-3.0.1-py2-none-any.whl")
    version("2.0.0", sha256="0bd439a8e9529387246c3e335920d6474fb67e12f963e4a40bec54933b347220", url="https://pypi.org/packages/c9/e3/48b98f929290b0cd0aaa4707ecabb8aaeb267e8ef628af907f1d1c506ec7/azure_mgmt_nspkg-2.0.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-nspkg@3:", when="@3:")
        depends_on("py-azure-nspkg@2:", when="@2")
    # END DEPENDENCIES

