# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFlattenDict(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.4.2", sha256="7e245b20c4c718981212210eec4284a330c9f713e632e98765560e05421e48ad", url="https://pypi.org/packages/43/f5/ee39c6e92acc742c052f137b47c210cd0a1b72dcd3f98495528bb4d27761/flatten_dict-0.4.2-py2.py3-none-any.whl")
    version("0.4.1", sha256="59aac40e07bbf08647a023193f227d2794696a1701f96f342a4ecf220bdb7a4b", url="https://pypi.org/packages/81/f9/6eda8c26974276ed4c814077026b496455d91313752be1dfbd0179a651b8/flatten_dict-0.4.1-py2.py3-none-any.whl")
    version("0.4.0", sha256="dfc0413c243d42178c2bfb16156af837a8f47c04cc97533cffec668e9ca02c50", url="https://pypi.org/packages/ab/51/4e2cb420b4b544676d1806ff7c5a1121b793d6a1aec844d3ddc83f3f8069/flatten_dict-0.4.0-py2.py3-none-any.whl")
    version("0.3.0", sha256="96038f9a0a09dca205112ae890e1f2159cfdf2af173397b2aa93d1bb9d055890", url="https://pypi.org/packages/9f/30/02e342a45b85c17cdf8238c7e9b612998fc59c7314e13fcd00fbb806dafb/flatten_dict-0.3.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pathlib2@2.3:", when="@0.2:0.3")
        depends_on("py-six@1.12:", when="@0.2:")
    # END DEPENDENCIES

