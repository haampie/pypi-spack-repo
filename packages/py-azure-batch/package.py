# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureBatch(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("14.1.0", sha256="83a364ec644d5a6e89698b165035083fabe1269ae58f1fb6472ff2531ac12244", url="https://pypi.org/packages/dd/90/cf0533f89895b0040497f549213b0a3f5249a28bb6aac22bbc86fbed7a26/azure_batch-14.1.0-py3-none-any.whl")
    version("14.0.0", sha256="3dee0571c3b25e4d46a9f2c4ca910f1837d518bd64cd2fd7d867ea770e054574", url="https://pypi.org/packages/4c/2a/974380e5542fe967aed86b9275d7b1710782b670a2e4aaf21da0aa9c877d/azure_batch-14.0.0-py3-none-any.whl")
    version("13.0.0", sha256="6d2647f579c7de50a20fa8cd9121aca5ab9b102340dd9a900d212f1f377ef2d4", url="https://pypi.org/packages/35/21/0a986af818ea8b365d1328f46d6b86ad39f0515562a5225b3345e725f2dc/azure_batch-13.0.0-py3-none-any.whl")
    version("12.0.0", sha256="10470ab3aa43ec416569b68c1167fe7bea1ea53b54c7fea8842c51ec8a68fd76", url="https://pypi.org/packages/0a/91/a2c0d597176015993a5b889e4897c014cbff6a598691ed9b7a89249a8229/azure_batch-12.0.0-py2.py3-none-any.whl")
    version("11.0.0", sha256="7059a82d1f7e466896d2f24fd4fa040a3717a7c3dc110e21c9fc2e754fc3ac72", url="https://pypi.org/packages/d0/fc/1b63a150b575fd5ed0120fa6e5f8035810d0a596ea4e95bb4d2aedc074d2/azure_batch-11.0.0-py2.py3-none-any.whl")
    version("10.0.0", sha256="706adae8301ee49f2e694584d45296d824e6216057d9b625c11c4b4f5c29b657", url="https://pypi.org/packages/c9/a9/b8d3136a5690ab38b9104fea2c5cc150785c942f8615183d89caab48b388/azure_batch-10.0.0-py2.py3-none-any.whl")
    version("9.0.0", sha256="787871825864fbae3b065d90f1dbb31cc44c5c7ce636a61d9b0950157d7f2216", url="https://pypi.org/packages/3c/86/1168fd710abd7e91606ebf2c46834f3ec6e4c0f2344003cf932768566ef0/azure_batch-9.0.0-py2.py3-none-any.whl")
    version("8.0.0", sha256="393a33c91e0a124b61ab436c25caebf400386b58ae088df2380221f56a6de5df", url="https://pypi.org/packages/e6/81/1787b8d36f3b90ef6c06fd47f27aaff248279e4c03856fba9c83b87c1ef7/azure_batch-8.0.0-py2.py3-none-any.whl")
    version("7.0.0", sha256="82e20992cfa824ab09f66615edc89641a1c6aa334ba32c2dd8d05fee0e479f23", url="https://pypi.org/packages/a5/19/cfdcdbcf08b0be9decb259c64ec8c1d15baf1a5de863ca300c4d3e9de068/azure_batch-7.0.0-py2.py3-none-any.whl")
    version("6.0.1", sha256="26ea1add581b7ca4d34d4226e1e36c456f9fc35cb0d15192958fffafeb76fec0", url="https://pypi.org/packages/20/0d/bfac3be449a6f2b07b3865699f87b8b50c8b81305ce04bd33ba0b1a8ffae/azure_batch-6.0.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-common@1.1:", when="@3.1:")
        depends_on("py-msrest@0.6.21:", when="@11:12")
        depends_on("py-msrest@0.5:", when="@5.1.1:10")
        depends_on("py-msrestazure@0.4.32:", when="@5.1.1:")
    # END DEPENDENCIES

