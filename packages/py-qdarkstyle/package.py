# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyQdarkstyle(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.2.3", sha256="ea980ee426d594909cf1058306832af71ff6cbad6f69237b036d1550635aefbc", url="https://pypi.org/packages/93/7d/c3c10498430dadcea4def5faddf71cd199e577d20a125e7ef1e9d7bdbbfa/QDarkStyle-3.2.3-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-qtpy@2:", when="@3.2:")
    # END DEPENDENCIES

