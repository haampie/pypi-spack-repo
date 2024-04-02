# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyIsal(PythonPackage):
    # BEGIN VERSIONS
    version("1.1.0", sha256="1364f4e3255a57d51c01422ab3ae785a43c076d516ebf49f6a25adecf8232105", url="https://pypi.org/packages/72/21/885d092e829e454700eb8acd1b086acb35d9c2756882afc0d22f4cec2ae5/isal-1.1.0.tar.gz")
    version("1.0.0", sha256="a30369de6852109eef8ca1bdd46d7e4b5c4517846a25acfc707cbb19db66ac80", url="https://pypi.org/packages/4f/0a/e500ff6f277d93649bf8d24d9043b0b9c080fe26c50bae7dcd39ba1ba7e1/isal-1.0.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@1:1.3")
    # END DEPENDENCIES

