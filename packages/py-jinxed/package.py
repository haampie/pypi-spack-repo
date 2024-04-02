# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJinxed(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.2.1", sha256="37422659c4925969c66148c5e64979f553386a4226b9484d910d3094ced37d30", url="https://pypi.org/packages/d8/96/f79f67f5f3c2d24bb8183a1d5bbf0ef4f39e343d49a46203e4d7a51ee849/jinxed-1.2.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-ansicon", when="@0.5.6: platform=windows")
    # END DEPENDENCIES

