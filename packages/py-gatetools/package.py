# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGatetools(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.12.1", sha256="b967f673fd9b20c08046774d4c9736865087d9b0c3345bad28e93a2bb960e763", url="https://pypi.org/packages/71/3f/0c2321fefbacca73c428b9a6087266ae6167f21b97c6dd4612e7a231b4d6/gatetools-0.12.1-py3-none-any.whl")
    version("0.11.2", sha256="c9e0e50b33d4732874055d2589b4a27b845c2478ff1d137be0fdb906418e0f8d", url="https://pypi.org/packages/40/84/abeb9a0aea0b9ccd95fd0bb38e3f7aea7c05cba4a3ec782401a15f9bb011/gatetools-0.11.2-py3-none-any.whl")
    version("0.9.14", sha256="55bfaa0bdc009f92d155928af920a6aaf51f1e064c93f19877def287023b2e2b", url="https://pypi.org/packages/00/b9/b180af0627cf2a6ce1a955c7f6dd28c0c91f59afe1ca7fbdca5ecc798082/gatetools-0.9.14-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-click", when="@:0.9.3,0.9.5:")
        depends_on("py-colorama", when="@0.11:")
        depends_on("py-colored", when="@:0.9.3,0.9.5:")
        depends_on("py-itk@5.2.0:", when="@0.12:")
        depends_on("py-itk@5.1.0:", when="@0.9.5:0.11")
        depends_on("py-lz4", when="@0.11:")
        depends_on("py-matplotlib", when="@:0.9.3,0.9.5:")
        depends_on("py-numpy", when="@:0.9.3,0.9.5:")
        depends_on("py-pydicom", when="@:0.9.3,0.9.5:")
        depends_on("py-python-box", when="@0.10:")
        depends_on("py-scipy", when="@0.9.13:")
        depends_on("py-tqdm", when="@:0.9.3,0.9.5:")
        depends_on("py-uproot", when="@:0.9.3,0.9.5:0.9.9,0.9.14:")
        depends_on("py-wget", when="@:0.9.3,0.9.5:")
        depends_on("py-xxhash", when="@0.11:")
    # END DEPENDENCIES

