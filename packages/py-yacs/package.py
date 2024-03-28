# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyYacs(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.1.8", sha256="99f893e30497a4b66842821bac316386f7bd5c4f47ad35c9073ef089aa33af32", url="https://pypi.org/packages/38/4f/fe9a4d472aa867878ce3bb7efb16654c5d63672b86dc0e6e953a67018433/yacs-0.1.8-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyyaml", when="@0.1.2:")
    # END DEPENDENCIES

