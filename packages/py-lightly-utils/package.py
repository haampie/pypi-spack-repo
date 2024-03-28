# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLightlyUtils(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.0.2", sha256="57eaa99044bbdab428cc67cd336491096cd406c21b50f15ce51150c1a10843e9", url="https://pypi.org/packages/62/11/ff55b3f54440e604a589ae1fe6950bc1bf49b5aca1842bf4b3ab0b6f65cd/lightly_utils-0.0.2-py3-none-any.whl")
    version("0.0.1", sha256="7cdef62cd83cb45ae480fe2bd8769d57de72cdc3cbca6750725dbc283923951b", url="https://pypi.org/packages/17/a1/e36f214e3d22d8417b718f51cdc49853bd63a50584f13981926ef8c5a368/lightly_utils-0.0.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy")
        depends_on("py-pillow")
    # END DEPENDENCIES

