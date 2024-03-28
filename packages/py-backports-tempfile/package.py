# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBackportsTempfile(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0", sha256="05aa50940946f05759696156a8c39be118169a0e0f94a49d0bb106503891ff54", url="https://pypi.org/packages/b4/5c/077f910632476281428fe254807952eb47ca78e720d059a46178c541e669/backports.tempfile-1.0-py2.py3-none-any.whl")
    version("1.0-rc1", sha256="d346e3390c8fe145f5613d801b56eca8590961581e788880d541fef1ad624b52", url="https://pypi.org/packages/a0/85/45f6a8f2318025dad1ccce4bda15d7735c394f91be0afdf2514817e2054d/backports.tempfile-1.0rc1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

