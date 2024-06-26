# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPycm(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("4.0", sha256="7d198fb2422371d94d41b27316e4982bc887727a92a4b59471005772654d895a", url="https://pypi.org/packages/ba/a2/cde7186bb567df8e5244d9d885788fd2161bc6bbe0fa1b130eea56db1988/pycm-4.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-art@1.8:")
        depends_on("py-numpy@1.9:")
    # END DEPENDENCIES

