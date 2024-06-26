# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDbf(PythonPackage):
    # BEGIN VERSIONS
    version("0.99.3", sha256="2bb941aca650cfa1cd26cab5667e573a895ba92d942eff3114813fa6f41bd866", url="https://pypi.org/packages/5b/8f/02615e518585713a25c9f7b9cf3c9ed027b651425ff0058dd4cb17b2b98e/dbf-0.99.3-py3-none-any.whl")
    version("0.97.11", sha256="93cccbcfd08322415c06f326fac44429749ee93ef1406826d7178547f8382cb8", url="https://pypi.org/packages/e4/c5/102b00f539915c55208ce232b4c29d5fb9dddc95dd78e534f0df69d5069e/dbf-0.97.11-py3-none-any.whl")
    version("0.96.5", sha256="5a4b54157bcd40cd9149155c21b71073570f4bb83ad495f3a88b23c463bd4f98", url="https://pypi.org/packages/22/fd/2819d7907074f097098be527471e03144520fcef968939e0c1e7a33ec2b4/dbf-0.96.005.zip")
    version("0.94.3", sha256="c95b688d2f28944004368799cc6e2999d78af930a69bb2643ae098c721294444", url="https://pypi.org/packages/7c/ef/79873517838910e8f1bd5610ab3de380a3886675103072727266eec91bbc/dbf-0.94.003.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-aenum", when="@0.96.8:0.97.2,0.97.4:0.97.5,0.97.8:")
    # END DEPENDENCIES

