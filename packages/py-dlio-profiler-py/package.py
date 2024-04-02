# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDlioProfilerPy(PythonPackage):
    # BEGIN VERSIONS
    version("0.0.2", sha256="386e201245c71489af590db2685f6eb16b3ec6cce958d95c36a868d454f97435", url="https://pypi.org/packages/ac/b0/6ed842fd785ce692268b92461e6348b39fe9dca5d9ebea725d7d54edfa3b/dlio_profiler_py-0.0.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:")
        depends_on("py-pybind11", when="@:0.0.2")
    # END DEPENDENCIES

