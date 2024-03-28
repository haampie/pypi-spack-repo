# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDataladNeuroimaging(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.3.5", sha256="dc6a5341d3c2a75ff70ed39649aa1034b413913e536e4b6a83ca2204ef637e80", url="https://pypi.org/packages/7b/4b/85a5b0927d278a4533398541aef7d42a2d2b91d2803fca706f2d5e43a7ad/datalad_neuroimaging-0.3.5-py3-none-any.whl")
    version("0.3.4", sha256="e5e06905f97edcf9c2b1124f7b135f7ad2bf53d8134b35b69a99f7cfcc8f8809", url="https://pypi.org/packages/4e/19/92669f28839112d6a2635849a62f5c9d4e7da56cf6dc9b5c0a0e74540b9f/datalad_neuroimaging-0.3.4-py3-none-any.whl")
    version("0.3.3", sha256="484b6ed3911129fcb9d692af6acbd29de6c3010848eb4dc4b2de7fed9bb0d501", url="https://pypi.org/packages/07/c4/4d6591e0b72dbd744ebe76c743ead79a500637a6d0778c199624951489c5/datalad_neuroimaging-0.3.3-py3-none-any.whl")
    version("0.3.2", sha256="b49c170b5cdd71fcca78e1abc37383644ccf1cc6ba0deee56227b2d19c9d68f3", url="https://pypi.org/packages/b5/2d/dca4c606bff0023b84071eedac30dc1d56790dd4f5eb7ff9b78fa4458550/datalad_neuroimaging-0.3.2-py3-none-any.whl")
    version("0.3.1", sha256="7d33f7e9c0d6450bbf7a9fc0521ca036ba1801970e48efff088d1096c6a9cc02", url="https://pypi.org/packages/bb/9d/b50c4972202c9386da65467e71b7152668447fe19db7acaa80ec959b0a5a/datalad_neuroimaging-0.3.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-datalad@0.16.7:", when="@0.3.2:")
        depends_on("py-datalad@0.12.0:", when="@0.3.1")
        depends_on("py-datalad-deprecated@0.2.7:", when="@0.3.3:")
        depends_on("py-datalad-deprecated@0.2.5:", when="@0.3.2")
        depends_on("py-datalad-metalad@0.4.5:", when="@0.3.2:")
        depends_on("py-nibabel", when="@:0.1.3,0.1.5:0.1,0.2.1,0.3.1:")
        depends_on("py-pandas", when="@:0.1.3,0.1.5:0.1,0.2.1,0.3.1:")
        depends_on("py-pybids@0.15.1:", when="@0.3.2:")
        depends_on("py-pybids@0.9.2:", when="@0.3.1")
        depends_on("py-pydicom", when="@:0.1.3,0.1.5:0.1,0.2.1,0.3.1:")
    # END DEPENDENCIES

