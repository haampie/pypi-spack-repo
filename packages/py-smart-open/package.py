# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySmartOpen(PythonPackage):
    # BEGIN VERSIONS
    version("5.2.1", sha256="71d14489da58b60ce12fc3ecb823facc59a8b23cd1b58edb97175640350d3a62", url="https://pypi.org/packages/cd/11/05f68ea934c24ade38e95ac30a38407767787c4e3db1776eae4886ad8c95/smart_open-5.2.1-py3-none-any.whl")
    version("1.10.0", sha256="bea5624c0c2e49987c227bdf3596573157eccd96fd1d53198856c8d53948fa2c", url="https://pypi.org/packages/6e/14/47cf88d290e4681be35f3b6e8889ba26ed809a0ba14336dc8ae46ffcfda8/smart_open-1.10.0.tar.gz")
    version("1.8.4", sha256="788e07f035defcbb62e3c1e313329a70b0976f4f65406ee767db73ad5d2d04f9", url="https://pypi.org/packages/37/c0/25d19badc495428dec6a4bf7782de617ee0246a9211af75b302a2681dea7/smart_open-1.8.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("azure", default=False, description="azure")
    variant("gcs", default=False, description="gcs")
    variant("http", default=False, description="http")
    variant("s3", default=False, description="s3")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@:3", when="@5:")
        depends_on("py-azure-common", when="@5:+azure")
        depends_on("py-azure-core", when="@5:+azure")
        depends_on("py-azure-storage-blob", when="@5:+azure")
        depends_on("py-boto3", when="@5:+s3")
        depends_on("py-google-cloud-storage", when="@5+gcs")
        depends_on("py-requests", when="@5:+http")
    # END DEPENDENCIES

