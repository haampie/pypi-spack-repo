# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySnakemakeExecutorPluginSlurmJobstep(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.1.11", sha256="2e9ff8059d0535d51310249d6026933731c01ee4be3081008bf85d37ea667a9b", url="https://pypi.org/packages/8c/bc/06dfa4e26c3782962f07ade44bc4d8ac74e176f989f92c614a3b61de2f2e/snakemake_executor_plugin_slurm_jobstep-0.1.11-py3-none-any.whl")
    version("0.1.10", sha256="ba4a7eea38b409b8e50f357385dca7830d9e4a20494649d6b6257cd5d91b6809", url="https://pypi.org/packages/98/79/0156409cbcc1523f0600c7c463c26d5a592f02d86bcab7e953465e65f455/snakemake_executor_plugin_slurm_jobstep-0.1.10-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.11:", when="@0.1.5:")
        depends_on("python@3.9:", when="@:0.1.3")
        depends_on("py-snakemake-interface-common@1.13:", when="@0.1.5:")
        depends_on("py-snakemake-interface-executor-plugins@9:", when="@0.1.11:")
        depends_on("py-snakemake-interface-executor-plugins@8.2:8", when="@0.1.10")
    # END DEPENDENCIES

