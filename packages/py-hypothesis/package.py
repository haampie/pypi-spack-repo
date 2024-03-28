# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHypothesis(PythonPackage):
    # BEGIN VERSIONS
    version("6.23.1", sha256="e1c5c4a7e1f9a1a1da03cf6a148703333c468fb036f3cd785da1210c23648a4f", url="https://pypi.org/packages/d2/46/dd7c1999679942dddf83cc8aa6d0769500c05c7d2cdd5f992900ad977d88/hypothesis-6.23.1-py3-none-any.whl")
    version("5.3.0", sha256="bfdac4e9ca4c6f9850be67699293dba3016f9c0521a73f5210f3d647888d6256", url="https://pypi.org/packages/a1/7e/75407f8633f20e4254effc8209b52b93197fa2ddf000e20fff8edccb0e1c/hypothesis-5.3.0-py3-none-any.whl")
    version("4.57.1", sha256="94f0910bc87e0ae8c098f4ada28dfdc381245e0c8079c674292b417dbde144b5", url="https://pypi.org/packages/f3/3b/16830a2b289079c5e8933344bde6326adf1fa4fbe4b4510083fab750eba9/hypothesis-4.57.1-py3-none-any.whl")
    version("4.41.2", sha256="acd47600deb55e9c2c98de6deef23384160ed0fdaafb6753146e556c077d3c78", url="https://pypi.org/packages/bc/af/392c2f90d69c6d3c5214a9c25fc7d336e1e600adf7ff80638139f12f7ae5/hypothesis-4.41.2-py3-none-any.whl")
    version("4.24.3", sha256="a2daa11895e1b93a0d11efd15bbc95b56309233a39e0ab6981df207199ed6a04", url="https://pypi.org/packages/ee/4b/717286b878b4f16a1bea68281612f82763a7472b3e1021f76e968872c7db/hypothesis-4.24.3-py3-none-any.whl")
    version("4.7.2", sha256="e3894dcda1f044c560882afe8485235c9e86736363a2c4658f7c13a5fc3f1aa8", url="https://pypi.org/packages/51/f3/d2522da59a8578ca58866bc873b92d5e7cc7a6a822af9947914613587762/hypothesis-4.7.2-py3-none-any.whl")
    version("3.7.0", sha256="0fea49d08f2d5884f014151a5af6fb48d862f6ad567ffc4a2e84abf2f186c423", url="https://pypi.org/packages/e1/cb/a444d3e96721240a86c7acc243b55355bf3b7161286e10184f57d30c51dc/hypothesis-3.7.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("django", default=False)
    variant("numpy", default=False)
    variant("pandas", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-attrs@19.2:", when="@4.38.2:6.91.0")
        depends_on("py-django@2.2:", when="@5.8.1:6.54.1+django")
        depends_on("py-django@1.11:", when="@4.24.6:5.8.0+django")
        depends_on("py-numpy@1.9:", when="@3.19,4.24.6:6.72,6.74:6.74.0+numpy")
        depends_on("py-pandas@0.25.0:", when="@5.41.3:6.52+pandas")
        depends_on("py-pandas@0.19.0:", when="@4.24.6:5.41.2+pandas")
        depends_on("py-pytz@2014:", when="@4.56.1:6.30+django")
        depends_on("py-pytz", when="@3.19,4.24.6:4.56.0+django")
        depends_on("py-sortedcontainers@2.1:", when="@4.55:")
    # END DEPENDENCIES

