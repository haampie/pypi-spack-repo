# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHepdataValidator(PythonPackage):
    # BEGIN VERSIONS
    version("0.3.5", sha256="0f5a97ef4f1a8e305b89c801a9ae294801c2f5f88a2f0c374218fe483f255ed7", url="https://pypi.org/packages/55/f6/4d870b584a1d624da6f9a3abe87f289af70890c9c48516ff6c4fd464bb24/hepdata_validator-0.3.5-py2.py3-none-any.whl")
    version("0.3.4", sha256="1698f85d829b611f5c5bf3b94aac097a7c9ee6a7ff9e60bd6787e9cfa58afe36", url="https://pypi.org/packages/65/b0/b147e3921de814c72c539f5962782f3d291d971216d80a35c70942a101f5/hepdata_validator-0.3.4-py2.py3-none-any.whl")
    version("0.3.3", sha256="50581e64199674117b4ba1eded5feb68755f5b412be30ac044f606ac207a6dd8", url="https://pypi.org/packages/b6/e8/0857e28b5b268f3b65aad0a4e3c986e2dbd7e48572eb24346f6893ec1610/hepdata_validator-0.3.3-py2.py3-none-any.whl")
    version("0.3.2", sha256="f0eb30ce3120029928a96d7b5239fd090d09ba76f67937aca57eb87c1a341ff1", url="https://pypi.org/packages/60/f2/ca6ceb76b11e600944c57835632e308efa5fc2515fe068c63aee609f498d/hepdata_validator-0.3.2-py2.py3-none-any.whl")
    version("0.3.1", sha256="27f57ff96fb6bd26430d9bcd591d9bca4ff4f4fd72f1783ec0410ff3e69d7dbe", url="https://pypi.org/packages/a6/b2/a431a229c55342d49e8a8040bd50e45cec9a962616bb7151fcf26471b15d/hepdata_validator-0.3.1-py2.py3-none-any.whl")
    version("0.3.0", sha256="355f001b2dd77c0cb0eab2aaad266d982901f7c516630d768f0f92f749b38c80", url="https://pypi.org/packages/75/a7/b6d791b596823a14061cdd29aeebb13c62e81ca83e5bd0961080662a69a8/hepdata_validator-0.3.0-py2.py3-none-any.whl")
    version("0.2.3", sha256="e7e39e92f68536d6749319eb3cec5aec34338237fc01e0fdbf92ea17f87113cf", url="https://pypi.org/packages/c0/8a/33c69f10e8def5dcfed3ed4e7f1a912cefba14a688241a1ed4a860fea274/hepdata_validator-0.2.3-py2.py3-none-any.whl")
    version("0.2.2", sha256="86faacb1e430c0a705c58e369ad0b64c3de22c3d855b08e82f6af93525eef438", url="https://pypi.org/packages/04/ca/5467930545d5e8d97db3833a979ba2af439bd667743eb5b3ed9aafbc714b/hepdata_validator-0.2.2-py2.py3-none-any.whl")
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

