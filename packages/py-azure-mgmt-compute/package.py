# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtCompute(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("13.1.1", sha256="9b41c8c5a35750f1bf5c4e87bb3d82f13223371ec732ef474ffcd4c4e61f9c91", url="https://pypi.org/packages/01/11/b8db8afbfcc0681ec3bb02c3ddea8f889c9de94dfac5825b328b9b4b760e/azure_mgmt_compute-13.1.1-py2.py3-none-any.whl")
    version("13.1.0", sha256="9469b104634228233a7274e36e76ac4f900378441131fa07fef12212484afbc6", url="https://pypi.org/packages/fb/79/f70c4cb715d63b69b58014b6ea7c9d7861a18f9750e9a2cae7f2afc63e16/azure_mgmt_compute-13.1.0-py2.py3-none-any.whl")
    version("13.0.0", sha256="0848fe37b4b6e49bed07d3969789072da7c259e8a8d21458251c3912f695e7c2", url="https://pypi.org/packages/f3/5d/e42ae8d9f9ee8ba36a800a8eaf16cd14a0ea6cb79d8cccfb203c505cc802/azure_mgmt_compute-13.0.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-common@1.1:", when="@3:4.0.0-rc2,4.1:30.5")
        depends_on("py-msrest@0.5:", when="@4.0.0:19")
        depends_on("py-msrestazure@0.4.32:", when="@4.1:14")
    # END DEPENDENCIES

