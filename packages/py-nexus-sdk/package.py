# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNexusSdk(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.3.2", sha256="5dd288515a3949035803511a195151c252243d3b097e1586d9efd28a227739e2", url="https://pypi.org/packages/1d/0c/354868778a580be31151dbb3ab6b309cc790523ba73021264dff1e789a72/nexus_sdk-0.3.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-puremagic", when="@0.3.1:")
        depends_on("py-requests", when="@:0.1,0.2.1:")
        depends_on("py-sseclient", when="@0.3:")
    # END DEPENDENCIES

