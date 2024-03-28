# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTzlocal(PythonPackage):
    # BEGIN VERSIONS
    version("2.1", sha256="e2cb6c6b5b604af38597403e9852872d7f534962ae2954c7f35efcb1ccacf4a4", url="https://pypi.org/packages/5d/94/d47b0fd5988e6b7059de05720a646a2930920fff247a826f61674d436ba4/tzlocal-2.1-py2.py3-none-any.whl")
    version("2.0.0", sha256="11c9f16e0a633b4b60e1eede97d8a46340d042e67b670b290ca526576e039048", url="https://pypi.org/packages/ef/99/53bd1ac9349262f59c1c421d8fcc2559ae8a5eeffed9202684756b648d33/tzlocal-2.0.0-py2.py3-none-any.whl")
    version("1.3", sha256="d160c2ce4f8b1831dabfe766bd844cf9012f766539cf84139c2faac5201882ce", url="https://pypi.org/packages/d3/64/e4b18738496213f82b88b31c431a0e4ece143801fb6771dddd1c2bf0101b/tzlocal-1.3.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pytz", when="@2")
    # END DEPENDENCIES

