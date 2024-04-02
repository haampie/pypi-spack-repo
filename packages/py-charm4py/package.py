# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCharm4py(PythonPackage):
    # BEGIN VERSIONS
    version("1.0", sha256="8ddb9f021b7379fde94b28c31f4ab6a60ced2c2a207a2d75ce57cb91b6be92bc", url="https://pypi.org/packages/b4/a8/3287448c7061fbf5a37493eab1b4838cbc5f5ceb86750ce56fa7caf6b3e5/charm4py-1.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("mpi", default=False, description="mpi")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-greenlet", when="@1:")
        depends_on("py-numpy@1.10:", when="@0.12:")
    # END DEPENDENCIES

