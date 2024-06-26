# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFastdownload(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.0.5", sha256="bf5c48fd415e01484307dd619ff01fc0747f22b0ee01cafd1b2b3b98d34f31f4", url="https://pypi.org/packages/4a/7d/d352ae8f0aa2170f9e0ae4676148675a738cf9fd0c034bd024b82f7df8ed/fastdownload-0.0.5-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-fastcore@1.3.26:", when="@0.0.5:")
        depends_on("py-fastprogress")
    # END DEPENDENCIES

