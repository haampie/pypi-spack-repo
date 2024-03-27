##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGrequests(PythonPackage):
    version("0.4.0", sha256="eb574b08f69b48c54e1029415f5f3316899ee006daa5624bbc5320648cdfdd52", url="https://pypi.org/packages/4b/b1/c728222e53380685642bab115240e7bf134837c288fe89cce3b3bb591a5d/grequests-0.4.0-py3-none-any.whl")
    version("0.3.0", sha256="0f41c4eee83bab39f5543af49665c08681637a0562a5704a3f7b2e4a996531c9", url="https://pypi.org/packages/25/9f/dff6f21676ca5d3e806e60cf0a49c52eb8f8c859310d28b1e740bc49b93e/grequests-0.3.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-gevent", when="@0.4:")
        depends_on("py-requests", when="@0.4:")

