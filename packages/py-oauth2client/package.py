# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOauth2client(PythonPackage):
    # BEGIN VERSIONS
    version("4.1.3", sha256="b8a81cc5d60e2d364f0b1b98f958dbd472887acaf1a5b05e21c28c31a2d6d3ac", url="https://pypi.org/packages/95/a9/4f25a14d23f0786b64875b91784607c2277eff25d48f915e39ff0cff505a/oauth2client-4.1.3-py2.py3-none-any.whl")
    version("3.0.0", sha256="5b5b056ec6f2304e7920b632885bd157fa71d1a7f3ddd00a43b1541a8d1a2460", url="https://pypi.org/packages/c0/7b/bc893e35d6ca46a72faa4b9eaac25c687ce60e1fbe978993fe2de1b0ff0d/oauth2client-3.0.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-httplib2@0.9.1:", when="@4:")
        depends_on("py-pyasn1@0.1.7:", when="@4:")
        depends_on("py-pyasn1-modules@0.0.5:", when="@4:")
        depends_on("py-rsa@3.1.4:", when="@4:")
        depends_on("py-six@1.6.1:", when="@4:")
    # END DEPENDENCIES

