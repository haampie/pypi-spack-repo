# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySnakemakeStoragePluginSftp(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.1.2", sha256="bc50da8349087bba5399e25a48e7b170cee6050cf7ffe461cea0fc8b14e0d433", url="https://pypi.org/packages/da/62/e2d71b388af5d75da5873b73c118106695c8de0d76a1ec6eb64a6f571753/snakemake_storage_plugin_sftp-0.1.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.11:3")
        depends_on("py-pysftp@0.2.9:")
        depends_on("py-snakemake-interface-common@1.14.3:")
        depends_on("py-snakemake-interface-storage-plugins@3:", when="@0.1.1:")
    # END DEPENDENCIES

