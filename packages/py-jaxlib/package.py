##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJaxlib(PythonPackage):
    version("0.1.1", sha256="6053ab244648f4225bfa5cdabae620264c4e298dccafcace1258bf234219dcda", url="https://pypi.org/packages/d9/47/ccd003a3f4fbaffa94552aa2d1d3d3bbe5977a7372c6fd6ea2428a3b8dbe/jaxlib-0.1.1-py3-none-macosx_10_9_x86_64.whl")

    with default_args(type="run"):
        depends_on("py-absl-py")
        depends_on("py-numpy@1.12.0:")
        depends_on("py-protobuf@3.6:")
        depends_on("py-six")

