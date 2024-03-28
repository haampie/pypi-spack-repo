# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDnspython(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.2.1", sha256="a851e51367fb93e9e1361732c1d60dab63eff98712e503ea7d92e6eccb109b4f", url="https://pypi.org/packages/9b/ed/28fb14146c7033ba0e89decd92a4fa16b0b69b84471e2deab3cc4337cc35/dnspython-2.2.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-sniffio@1.1:", when="@2.4:2.4.0")
    # END DEPENDENCIES

