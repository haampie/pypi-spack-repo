# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHepdataValidator(PythonPackage):
    # BEGIN VERSIONS
    version("0.3.3", sha256="50581e64199674117b4ba1eded5feb68755f5b412be30ac044f606ac207a6dd8", url="https://pypi.org/packages/b6/e8/0857e28b5b268f3b65aad0a4e3c986e2dbd7e48572eb24346f6893ec1610/hepdata_validator-0.3.3-py2.py3-none-any.whl")
    version("0.3.0", sha256="355f001b2dd77c0cb0eab2aaad266d982901f7c516630d768f0f92f749b38c80", url="https://pypi.org/packages/75/a7/b6d791b596823a14061cdd29aeebb13c62e81ca83e5bd0961080662a69a8/hepdata_validator-0.3.0-py2.py3-none-any.whl")
    version("0.2.3", sha256="e7e39e92f68536d6749319eb3cec5aec34338237fc01e0fdbf92ea17f87113cf", url="https://pypi.org/packages/c0/8a/33c69f10e8def5dcfed3ed4e7f1a912cefba14a688241a1ed4a860fea274/hepdata_validator-0.2.3-py2.py3-none-any.whl")
    version("0.1.16", sha256="3d7f725328ecdbb66826bff2e48a40a1d9234249859c8092ca0e92be7fb78111", url="https://pypi.org/packages/51/7a/8bfb559edd3f03bf65bf5522b20fa9360b7057b649c511b1be150f9c5b17/hepdata_validator-0.1.16.tar.gz")
    version("0.1.15", sha256="1030654b1a1cfc387c2759f8613f033da467c8182dc027e181227aeb52854bb2", url="https://pypi.org/packages/4b/6d/aaa8a0ef686d64f501bae84d640179ffc5cfb42e48f4e782ded0a733d97e/hepdata_validator-0.1.15.tar.gz")
    version("0.1.14", sha256="d1596741fb26be234c2adb6972306908f09b049dc670d8312cf2636f1a615a52", url="https://pypi.org/packages/66/d0/61f2dbc68ff048dae74e2203d85045cce13beedf3a8513e3fd7088f5cc4c/hepdata_validator-0.1.14.tar.gz")
    version("0.1.8", sha256="08686563e0130c5dd6d9fb8d5c7bf5a2617a637b105a42f7106b96a31eaffa61", url="https://pypi.org/packages/12/04/dda896ee4d0b845d9555c570f297b60ecdf79876f6eaa27d821b3b10c48c/hepdata_validator-0.1.8.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-click", when="@0.3:")
        depends_on("py-jsonschema", when="@0.2:")
        depends_on("py-packaging", when="@0.3:")
        depends_on("py-pyyaml@5.4.1:", when="@0.3:")
        depends_on("py-pyyaml", when="@0.2")
        depends_on("py-requests", when="@0.2.2:")
    # END DEPENDENCIES

