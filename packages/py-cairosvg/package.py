# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCairosvg(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.7.1", sha256="8a5222d4e6c3f86f1f7046b63246877a63b49923a1cd202184c3a634ef546b3b", url="https://pypi.org/packages/01/a5/1866b42151f50453f1a0d28fc4c39f5be5f412a2e914f33449c42daafdf1/CairoSVG-2.7.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cairocffi", when="@2.3:")
        depends_on("py-cssselect2", when="@2.3:")
        depends_on("py-defusedxml", when="@2.3:")
        depends_on("py-pillow", when="@2.3:")
        depends_on("py-tinycss2", when="@2.3:")
    # END DEPENDENCIES

