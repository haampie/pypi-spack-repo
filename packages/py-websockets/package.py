# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyWebsockets(PythonPackage):
    # BEGIN VERSIONS
    version("10.4", sha256="eef610b23933c54d5d921c92578ae5f89813438fded840c2e9809d378dc765d3", url="https://pypi.org/packages/85/dc/549a807a53c13fd4a8dac286f117a7a71260defea9ec0c05d6027f2ae273/websockets-10.4.tar.gz")
    version("10.3", sha256="fc06cc8073c8e87072138ba1e431300e2d408f054b27047d047b549455066ff4", url="https://pypi.org/packages/f8/a3/622d9acbfb9a71144b5d7609906bc648c62e3ca5fdbb1c8cca222949d82c/websockets-10.3.tar.gz")
    version("10.1", sha256="181d2b25de5a437b36aefedaf006ecb6fa3aa1328ec0236cdde15f32f9d3ff6d", url="https://pypi.org/packages/69/77/591bbc51a5ed6a906a7813e60a9627f988f9546513fcf9d250eb31ec8689/websockets-10.1.tar.gz")
    version("8.1", sha256="5c65d2da8c6bce0fca2528f69f44b2f977e06954c8512a952222cea50dad430f", url="https://pypi.org/packages/e9/2b/cf738670bb96eb25cb2caf5294e38a9dc3891a6bcd8e3a51770dbc517c65/websockets-8.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

