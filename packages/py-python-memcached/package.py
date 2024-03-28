# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonMemcached(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.59", sha256="4dac64916871bd3550263323fc2ce18e1e439080a2d5670c594cf3118d99b594", url="https://pypi.org/packages/f5/90/19d3908048f70c120ec66a39e61b92c253e834e6e895cd104ce5e46cbe53/python_memcached-1.59-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six@1.4:", when="@1.59")
    # END DEPENDENCIES

