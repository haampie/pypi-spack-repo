# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyEdflibPython(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0.8", sha256="0c4ac78a0ac7af00e1c0aec582223ff9e330544d5b758f0e06508ed5188dd9e4", url="https://pypi.org/packages/d9/74/3152076443abeee13bcc3c91585863d3a1491e337c983751d30e21b98aea/EDFlib_Python-1.0.8-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.17.0:")
    # END DEPENDENCIES

