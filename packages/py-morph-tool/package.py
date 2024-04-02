# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMorphTool(PythonPackage):
    # BEGIN VERSIONS
    version("2.9.1", sha256="305e9456c8047726588b23dfa070eb95ccbe5573e9fea3e0a83dc93eacdf61dc", url="https://pypi.org/packages/58/54/46395b70637868ca3a233abfcc517517b81bce814aed222e362c1ac93571/morph-tool-2.9.1.tar.gz")
    version("2.9.0", sha256="c60d4010e17ddcc3f53c864c374fffee05713c8f8fd2ba4eed7706041ce1fa47", url="https://pypi.org/packages/0b/5d/d0b3c6e3928a1ac9ea208c9273b56eab850c67ad65024ea4faf1be7abd5a/morph-tool-2.9.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("nrn", default=False, description="nrn")
    variant("parallel", default=False, description="parallel")
    variant("plot", default=False, description="plot")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@2.9.1:2.9")
    # END DEPENDENCIES

