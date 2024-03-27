##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyXmlplain(PythonPackage):
    version("1.6.0", sha256="a9ccfa8ab36e4df1b0580458312501b7ae7625bad3c4fcc1b8c124aad775d8e3", url="https://pypi.org/packages/2d/a7/56c2d1145b71b4dff6ffa63616760b21f5c25ac4e0d053be5e065c9a938d/xmlplain-1.6.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-ordereddict")
        depends_on("py-pyyaml")

