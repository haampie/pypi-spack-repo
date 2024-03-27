##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureLoganalytics(PythonPackage):
    version("0.1.1", sha256="7975a8d91b1fdc7e69af2ef911f9cb04e3d40e00b03b02bcde514ee97c45f3c8", url="https://pypi.org/packages/6f/76/c4b3f49a75c7d30ff63e3e4104007ee3a7a5ec036c1516e45a0370facadd/azure_loganalytics-0.1.1-py2.py3-none-any.whl")
    version("0.1.0", sha256="5a1bdb33e1fd3dfb275d9eec45ed8e1126eda51e9072ccf08a19922ee5e0ad98", url="https://pypi.org/packages/54/e2/1d30270441a50efce1d52eb426710fc98269eb8bdac44ee966bbd07846da/azure_loganalytics-0.1.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-azure-common@1.1:")
        depends_on("py-azure-nspkg@2:", when="@:0.1.0")
        depends_on("py-msrest@0.5:", when="@0.1.1:")
        depends_on("py-msrest@0.4.29:", when="@:0.1.0")

