# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCmyt(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.1.2", sha256="2846241500e50639e1e271d7f05b1e1684d0db266b5a135d360a26e69ac0715d", url="https://pypi.org/packages/41/03/c64f1562bb12a5340fe170229355b74e3d78530dddd74091d4c1ccc73bca/cmyt-1.1.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.4:")
        depends_on("py-colorspacious@1.1.2:", when="@0.2:1.2")
        depends_on("py-matplotlib@3.2.0:", when="@1.1:1.2")
        depends_on("py-more-itertools@8.4:", when="@:1.2")
        depends_on("py-numpy@1.17.4:", when="@1.1:1.3")
    # END DEPENDENCIES

