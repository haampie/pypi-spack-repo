# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDomToml(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.6.1", sha256="ebdd69c571268dfa5a56b5085b5311583d8a8d2dc1811349e796160c9f36d501", url="https://pypi.org/packages/d2/9d/1c36fc21dd9c1cfa21d74ca090074adfa1e2e778f79aa3d203bacdabbb35/dom_toml-0.6.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-domdf-python-tools@2.8:", when="@0.5.1:")
        depends_on("py-toml@0.10.2:")
    # END DEPENDENCIES

