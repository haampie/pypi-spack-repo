# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureStorageCommon(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.1.0", sha256="b01a491a18839b9d05a4fe3421458a0ddb5ab9443c14e487f40d16f9a1dc2fbe", url="https://pypi.org/packages/6b/a0/6794b318ce0118d1a4053bdf0149a60807407db9b710354f2b203c2f5975/azure_storage_common-2.1.0-py2.py3-none-any.whl")
    version("1.4.2", sha256="de4817cce35a23d1c89563edc38b481ebd8da4655bdf32d26fa2b06095179e4a", url="https://pypi.org/packages/05/6c/b2285bf3687768dbf61b6bc085b0c1be2893b6e2757a9d023263764177f3/azure_storage_common-1.4.2-py2.py3-none-any.whl")
    version("1.4.1", sha256="51262eeaa7d24ae11e6bcd4b76368248c617584d76c414048ef68c241a235b04", url="https://pypi.org/packages/fa/d9/eeaa581ed43f9314ec30fb1bceb81403956b462a66fb7bd7c6ce909e6281/azure_storage_common-1.4.1-py2.py3-none-any.whl")
    version("1.4.0", sha256="69bba6aad1e8a717eeee0f95c2feeeed72ef802001e66d6d15bf8446c4f53e6a", url="https://pypi.org/packages/73/84/025ac436a6a1d5516d1a67887d7122b3b2ea04ba6b2d2c46fe949accb62b/azure_storage_common-1.4.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-common@1.1.5:", when="@0.37.1:1.1,1.3,1.4.2:1,2.1:")
        depends_on("py-cryptography", when="@0.37.1:1.1,1.3,1.4.2:1,2.1:")
        depends_on("py-python-dateutil", when="@0.37.1:1.1,1.3,1.4.2:1,2.1:")
        depends_on("py-requests", when="@0.37.1:1.1,1.3,1.4.2:1,2.1:")
    # END DEPENDENCIES

