# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLhsmdu(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.1", sha256="863f85e215247181cfe36a002e13cbcce3484e56459c019ad31ad4c2a9d3443b", url="https://pypi.org/packages/a2/5c/c0f4e69093a4ebfc52c34cb1926dbe5f29181fcb934a624c4123d6ce1921/lhsmdu-1.1-py2.py3-none-any.whl")
    version("0.1", sha256="833818903027c655f04fd28b763891a1ef59c3120003fb51a3fdca909aa8fe4c", url="https://pypi.org/packages/7b/f0/e714a4dae734bcd7228a09d74fff7dc5857dc3311cd72a3e07b09c85d088/lhsmdu-0.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy")
        depends_on("py-scipy")
    # END DEPENDENCIES

