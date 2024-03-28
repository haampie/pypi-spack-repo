# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPortpicker(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.5.2", sha256="01113f51c3cc63290a44dd7ae6e3eb9f8fe1b8a1f9d7988a897944230c39cd52", url="https://pypi.org/packages/53/47/085215ca086b0e456421158a912d573f162644d6ef7a96de60fbc6dc99b2/portpicker-1.5.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-psutil", when="@1.5:")
    # END DEPENDENCIES

