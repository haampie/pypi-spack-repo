# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNumpyStl(PythonPackage):
    # BEGIN VERSIONS
    version("3.0.0", sha256="44d56dec3b409b73f7126089ece859d0213d302e39c2375496e64f6dc574347c", url="https://pypi.org/packages/02/ee/72e3df8eeedfb9cebc4c5c9038b3922084d0eaef1cc2b5ee81e555ee0451/numpy_stl-3.0.0-py3-none-any.whl")
    version("2.10.1", sha256="f6b529b8a8112dfe456d4f7697c7aee0aca62be5a873879306afe4b26fca963c", url="https://pypi.org/packages/a2/08/19caa3c20fd9a486a0a603e329b22578aca7e6f184f0575fcd0980ba3ac5/numpy-stl-2.10.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@2.17:")
        depends_on("py-python-utils@3.4.5:", when="@3:")
    # END DEPENDENCIES

