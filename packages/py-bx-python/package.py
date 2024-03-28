# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBxPython(PythonPackage):
    # BEGIN VERSIONS
    version("0.9.0", sha256="fe545c44d2ea74b239d41e9090618aaf6a859d1a1f64b4a21b133cb602dfdb49", url="https://pypi.org/packages/b1/79/6159768ef08fc5d037c184bc964d7a79984ac99d0c076b70251c89964550/bx-python-0.9.0.tar.gz")
    version("0.8.8", sha256="ad0808ab19c007e8beebadc31827e0d7560ac0e935f1100fb8cc93607400bb47", url="https://pypi.org/packages/5c/7f/03375de727d21c5aecd4ee210ce458a045203e723999f706325e06a81c4f/bx-python-0.8.8.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@0.8.3:0.8.9,0.11:")
        depends_on("py-six", when="@0.8.3:0.8.8")
    # END DEPENDENCIES

