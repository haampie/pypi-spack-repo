##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPhotutils(PythonPackage):
    version("1.5.0", sha256="014f7aa5a571401094d5cf9ffb57803b48869233feb80476ce377ecb91113689", url="https://pypi.org/packages/27/c3/1b1338862d28722f621d6a1c9851f93ca2de1d4337107b7bab06ec4189de/photutils-1.5.0.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.9:")

