# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHist(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.6.1", sha256="bde4936ffbef70ced93aedd69eb921c0d851ad00a152e41bf6b93c396c8f7aff", url="https://pypi.org/packages/09/72/541e00346028efdd6274c15bcc8ccb4f9ec8e8e8461117ef9539a93014e0/hist-2.6.1-py3-none-any.whl")
    version("2.5.2", sha256="4d54c0b6afe62e6a1b4c8b7018b63085770b589aba4f887c02a1e49c3b4016d2", url="https://pypi.org/packages/77/90/091c1527c9fa3f6c653ba049fb7e0a197fc59b05bf84670c2c97252e199c/hist-2.5.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("plot", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-boost-histogram@1.3.1:1.3", when="@2.6:2.7.1")
        depends_on("py-boost-histogram@1.2", when="@2.5")
        depends_on("py-histoprint@2.2:", when="@2.5:")
        depends_on("py-iminuit@2:", when="@2.6.2:2.6+plot ^python@:3.10")
        depends_on("py-iminuit@2:", when="@2.3:2.6.1,2.7:2.7.0+plot")
        depends_on("py-matplotlib@3.0.0:", when="@2.0.0:+plot")
        depends_on("py-mplhep@0.2.16:", when="@2.1:+plot")
        depends_on("py-numpy@1.14.5:", when="@2.7.2: ^python@:3.11")
        depends_on("py-numpy@1.14.5:", when="@2.5:2.7.1")
        depends_on("py-scipy@1.4.0:", when="@2.6.2:2.6+plot ^python@:3.10")
        depends_on("py-scipy@1.4.0:", when="@2.0.0:2.6.1,2.7:2.7.0+plot")
        depends_on("py-scipy@1.4.0:", when="@2.0.0-alpha4:2.0.0-beta1")
        depends_on("py-uncertainties@3:", when="@2.0.0:2.2+plot")
        depends_on("py-uncertainties@3:", when="@2:2.0.0-beta1")
    # END DEPENDENCIES

