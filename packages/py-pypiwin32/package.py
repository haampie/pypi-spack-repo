# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPypiwin32(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("223", sha256="67adf399debc1d5d14dffc1ab5acacb800da569754fafdc576b2a039485aa775", url="https://pypi.org/packages/d0/1b/2f292bbd742e369a100c91faa0483172cd91a1a422a6692055ac920946c5/pypiwin32-223-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pywin32@223:", when="@223:")
    # END DEPENDENCIES

