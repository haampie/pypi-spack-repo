# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCroniter(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.3.8", sha256="d6ed8386d5f4bbb29419dc1b65c4909c04a2322bd15ec0dc5b2877bfa1b75c7a", url="https://pypi.org/packages/0f/4d/0cc5a7f4bdcefecebdf8a95c8372606c13d3355e8536d9cd3e7070e94269/croniter-1.3.8-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-python-dateutil")
    # END DEPENDENCIES

