##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMemoryProfiler(PythonPackage):
    version("0.61.0", sha256="400348e61031e3942ad4d4109d18753b2fb08c2f6fb8290671c5513a34182d84", url="https://pypi.org/packages/49/26/aaca612a0634ceede20682e692a6c55e35a94c21ba36b807cc40fe910ae1/memory_profiler-0.61.0-py3-none-any.whl")
    version("0.60.0", sha256="6a12869511d6cebcb29b71ba26985675a58e16e06b3c523b49f67c5497a33d1c", url="https://pypi.org/packages/06/dd/7308a8ef1902db9d81c5bc226befe346a87ed8787caff00b8d91ed9f3b86/memory_profiler-0.60.0.tar.gz")
    version("0.57.0", sha256="23b196f91ea9ac9996e30bfab1e82fecc30a4a1d24870e81d1e81625f786a2c3", url="https://pypi.org/packages/f4/03/175d380294b2333b9b79c2f2aa235eb90ee95e3ddef644497a9455404312/memory_profiler-0.57.0.tar.gz")
    version("0.47", sha256="e992f2a341a5332dad1ad4a008eeac7cfe78c7ea4abdf7535a3e7e79093328cb", url="https://pypi.org/packages/bf/f0/15dc10cac0d8c56782e51d94855955664aa4f420eaa6291314bc3a0a52a3/memory_profiler-0.47.tar.gz")

    with default_args(type="run"):
        depends_on("py-psutil", when="@0.61:")

