##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtNspkg(PythonPackage):
    version("3.0.2", sha256="8b2287f671529505b296005e6de9150b074344c2c7d1c805b3f053d081d58c52", url="https://pypi.org/packages/c4/d4/a9a140ee15abd8b0a542c0d31b7212acf173582c10323b09380c79a1178b/azure-mgmt-nspkg-3.0.2.zip")
    version("3.0.1", sha256="ab70466469de573eafe13e511aa342ac7f0d798777836313dd46d0801b68bbb5", url="https://pypi.org/packages/45/2d/1cd3391bf8a46402aac5d68590782a9993eb507ece0716ef8afb30a3f4df/azure-mgmt-nspkg-3.0.1.zip")
    version("2.0.0", sha256="0bd439a8e9529387246c3e335920d6474fb67e12f963e4a40bec54933b347220", url="https://pypi.org/packages/c9/e3/48b98f929290b0cd0aaa4707ecabb8aaeb267e8ef628af907f1d1c506ec7/azure_mgmt_nspkg-2.0.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-azure-nspkg@3:", when="@3:")
        depends_on("py-azure-nspkg@2:", when="@2")

