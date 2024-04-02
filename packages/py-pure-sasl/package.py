# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPureSasl(PythonPackage):
    # BEGIN VERSIONS
    version("0.6.2", sha256="53c1355f5da95e2b85b2cc9a6af435518edc20c81193faa0eea65fdc835138f4", url="https://pypi.org/packages/83/b7/a0d688f86c869073cc28c0640899394a1cf68a6d87ee78a09565e9037da6/pure-sasl-0.6.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("gssapi", default=False, description="gssapi")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

