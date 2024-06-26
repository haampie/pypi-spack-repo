# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyIpyvuetify(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.9.0", sha256="a190f62a10e89e92a0e25641c84c739e31f66680858d987b8a180b24e2278dec", url="https://pypi.org/packages/d9/15/b3b6560dd4984660a75aff9cdf3e7d574b3b3fecb81fb6affa138d6c760b/ipyvuetify-1.9.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-ipyvue@1.7:1", when="@1.8.8:1")
    # END DEPENDENCIES

