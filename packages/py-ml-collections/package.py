# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMlCollections(PythonPackage):
    # BEGIN VERSIONS
    version("0.1.1", sha256="3fefcc72ec433aa1e5d32307a3e474bbb67f405be814ea52a2166bfc9dbe68cc", url="https://pypi.org/packages/aa/ea/853aa32dfa1006d3eb43384712f35b8f2d6f0a757b8c779d40c29e3e8515/ml_collections-0.1.1.tar.gz")
    version("0.1.0", sha256="0f30752d52fae1c09c10a406fc5d405716da2b60fa5f13dd15498615cb44d3c9", url="https://pypi.org/packages/03/d4/9ab1a8c2aebf78c348404c464733974dc4e7088174d6272ed09c2fa5a8fa/ml_collections-0.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-absl-py", when="@:0.1.0")
        depends_on("py-contextlib2", when="@:0.1.0")
        depends_on("py-pyyaml", when="@:0.1.0")
        depends_on("py-six", when="@:0.1.0")
    # END DEPENDENCIES

