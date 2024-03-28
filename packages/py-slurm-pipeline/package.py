# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySlurmPipeline(PythonPackage):
    # BEGIN VERSIONS
    version("4.0.4", sha256="5496e46edb890ef745231b4d05b8dfd194374b3fe2c6b33da43cda9685f145c8", url="https://pypi.org/packages/73/0a/01d5f542e6103301af697da1bab9f12b2be2f880cabe989c884a09a714f5/slurm-pipeline-4.0.4.tar.gz")
    version("3.0.2", sha256="28e07eb93e846b395a16e6778fd3fc8344a82d115a6a8420276ec68f67f7131c", url="https://pypi.org/packages/fe/d4/11a0af64de649477bdeccbb915539d556cc9d3d97ffe4610eed2ab5ee4ac/slurm-pipeline-3.0.2.tar.gz")
    version("2.0.9", sha256="2360e43965ecfa3701f287b7d597c99b4accd4dc8faf9d55cfdcc2228c4054cc", url="https://pypi.org/packages/37/0e/43eacfdce4474f3a169d08bd0ddd259217f61461eb88a62507b8d208e387/slurm-pipeline-2.0.9.tar.gz")
    version("1.1.13", sha256="6d6ca2e96a16780fd9520957166afd06272c57abd962e76bfe74c4d394b38da1", url="https://pypi.org/packages/f9/69/6d3b2d0999d3c8db422f75f95079d739948c9a2feb6411fcfccc93f51c36/slurm-pipeline-1.1.13.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

