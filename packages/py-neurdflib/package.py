# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNeurdflib(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("5.0.1", sha256="b542bf337d3ffea111e8fe35ceb35c85172949e42c0597acc12820f7f27344d8", url="https://pypi.org/packages/41/66/304a1ad40fecee3504a315d831afcaebe156a62ff1628311bac3cb8d55c8/neurdflib-5.0.1-py3-none-any.whl")
    version("5.0.1.dev0", sha256="dd70b55418a2680b6d1e9ff1a924ddfe30807d1938351f2cd14d39ec0094b83e", url="https://pypi.org/packages/b4/33/fb9e010fe66cc2a28e48709e8a5370d483578069414754e05289de5c54e1/neurdflib-5.0.1.dev0-py3-none-any.whl")
    version("5.0.0.post1", sha256="b67fabecf09d2d650a2ae7d661b0451b7dd87f48471f85fde9cc974bceb6f3e7", url="https://pypi.org/packages/b9/47/f3acc236fcc523c7938dbd031cac45929b829ca6c4e5b9dc1acc858406d6/neurdflib-5.0.0.post1-py2.py3-none-any.whl")
    version("5.0.0", sha256="5a88153fc2dc45a8a8097674d940a7ac54b8fb1f4630c280d22dafbbecd11585", url="https://pypi.org/packages/cf/2d/1e00d710b88ed2f7e08c96c3f57a28e82b15f0b17c9fd4a05adf71c08e5f/neurdflib-5.0.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-isodate")
        depends_on("py-pyparsing")
        depends_on("py-six")
    # END DEPENDENCIES

