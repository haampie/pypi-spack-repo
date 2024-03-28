# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySip(PythonPackage):
    # BEGIN VERSIONS
    version("6.7.9", sha256="35d51fc10f599d3696abb50f29d068ad04763df7b77808c76b74597660f99b17", url="https://pypi.org/packages/48/75/98987181e897ef378d6c239ee733328a7264a41f2d8263e61d7b7c4c0909/sip-6.7.9.tar.gz")
    version("6.6.2", sha256="0e3efac1c5dfd8e525ae57140927df26993e13f58b89d1577c314f4105bfd90d", url="https://pypi.org/packages/5b/cb/c27c925ae07bd03a2597fa1db17bfc2a4ac57da61aeb90f8ec98ffbb975b/sip-6.6.2.tar.gz")
    version("6.4.0", sha256="42ec368520b8da4a0987218510b1b520b4981e4405086c1be384733affc2bcb0", url="https://pypi.org/packages/c4/de/76c2927ea8f74dc4909c9affeba4c0191c43a4aefbe2118cc69b2cbd8461/sip-6.4.0.tar.gz")
    version("5.5.0", sha256="5d024c419b30fea8a6de8c71a560c7ab0bc3c221fbfb14d55a5b865bd58eaac5", url="https://pypi.org/packages/33/e9/27730ac17713c0a80d81d8f3bb56213f1549d96f9dc183fd16a7eec6287c/sip-5.5.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("module", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

