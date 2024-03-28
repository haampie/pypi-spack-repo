# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPureSasl(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.6.2", sha256="edb33b1a46eb3c602c0166de0442c0fb41f5ac2bfccbde4775183b105ad89ab2", url="https://pypi.org/packages/37/b2/ef1124540ee2c0b417be8d0f74667957e6aa084a3f26621aa67e2e77f3fb/pure_sasl-0.6.2-py2-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("gssapi", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

