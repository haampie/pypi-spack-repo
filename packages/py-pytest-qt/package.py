# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestQt(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.3.0", sha256="5f8928288f50489d83f5d38caf2d7d9fcd6e7cf769947902caa4661dc7c851e3", url="https://pypi.org/packages/38/b4/c1e8d65fac47eb48c265b7ab926cf5c439e5517fbdfc892dcf5e8aa303a5/pytest_qt-3.3.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pytest@3:", when="@3.3:4.3")
    # END DEPENDENCIES

