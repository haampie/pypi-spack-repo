##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtContainerinstance(PythonPackage):
    version("2.0.0", sha256="1d08587c30d870e2f7961e865dab01db3160f8a8ad53a525d94b0ce7115d39e7", url="https://pypi.org/packages/47/89/20bf1f4bb8d54f7f6fb96f0743c3b35871a7fac7dd5273c84c7201ff12c4/azure_mgmt_containerinstance-2.0.0-py2.py3-none-any.whl")
    version("1.5.0", sha256="0e55fb1dddcc01a9d58a99095e5cca50252bb6c42150b225e552560fe29fd8a5", url="https://pypi.org/packages/fd/d1/d770050f20ad81b80f7eb41f89e1a5d841cf74bf41c7e1ff137c46f28a1e/azure_mgmt_containerinstance-1.5.0-py2.py3-none-any.whl")
    version("1.4.1", sha256="9b0a1e8eaaed636f75f31cab3c06558daf037e3ce0a93d41d1aa4b780773264a", url="https://pypi.org/packages/db/b6/83c0e03246706119a364798a410567e998128061acb574f51cf33dedf845/azure_mgmt_containerinstance-1.4.1-py2.py3-none-any.whl")
    version("1.4.0", sha256="f1ea7d150447f0d8d670b7db13bd2f47320385526021053445d15c427cba6713", url="https://pypi.org/packages/77/50/f7f419e0ac788d41d080d5f25daf988b993063aab3bfd90def54e93e72d7/azure_mgmt_containerinstance-1.4.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-azure-common@1.1:")
        depends_on("py-msrest@0.5:", when="@1.1:7")
        depends_on("py-msrestazure@0.4.32:", when="@1.1:3")

