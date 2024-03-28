# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySip(PythonPackage):
    # BEGIN VERSIONS
    version("6.8.3", sha256="11c332566de0d752df92906101260e81401bf574417a6bc31fb99364ae6b652d", url="https://pypi.org/packages/22/cb/3763a07a046884cdc14668758895cc6a8cd1b8d06281d5b6914b0e6948bc/sip-6.8.3-py3-none-any.whl")
    version("6.8.2", sha256="dabd8a065564b63f1314698811fcffac4dec8da51539a5b584b0f472b591895c", url="https://pypi.org/packages/5e/20/a5f88409f0152d707e72809eac9b5a58fc5c7e989145fcfe051ba087ade8/sip-6.8.2-py3-none-any.whl")
    version("6.8.1", sha256="ce489991d249777321bc48e42aff7f107b3333d217b8b5ebb858179a7d4116a7", url="https://pypi.org/packages/e9/5a/157a032999c8b69132182c73193801e429cf973b6e5ee71fee7998bdc140/sip-6.8.1-py3-none-any.whl")
    version("6.8.0", sha256="5da5638ed88ee95cb800c5a1bb3f2217f8ca21d93750e10aa171f2d0280ac0e2", url="https://pypi.org/packages/22/dd/55a69862572792e7725c11210ac42557e4f2898f101ed14dfbe6ce7872fd/sip-6.8.0-py3-none-any.whl")
    version("6.7.12", sha256="08e66f742592eb818ac8fda4173e2ed64c9f2d40b70bee11db1c499127d98450", url="https://pypi.org/packages/a6/4e/c34eee70109e9a8110672f074fc18b5022bf4b9b4c92641245c73ae0b21a/sip-6.7.12.tar.gz")
    version("6.7.11", sha256="f0dc3287a0b172e5664931c87847750d47e4fdcda4fe362b514af8edd655b469", url="https://pypi.org/packages/ce/8c/f66d1c45946e73a46f258b9628fe974ba8cc46c41b4750a59be192981695/sip-6.7.11.tar.gz")
    version("6.7.10", sha256="398aeb84ee03f3a953947cac70e60d3b02dceba3c4f4dd46c5383e9dbe3936bb", url="https://pypi.org/packages/50/3a/ae9b9e36c7f1db92675b25f722ff7a8c3f6efd50817d5c946a7637dacd88/sip-6.7.10.tar.gz")
    version("6.7.9", sha256="35d51fc10f599d3696abb50f29d068ad04763df7b77808c76b74597660f99b17", url="https://pypi.org/packages/48/75/98987181e897ef378d6c239ee733328a7264a41f2d8263e61d7b7c4c0909/sip-6.7.9.tar.gz")
    version("6.7.8", sha256="7e7186a36818c9d325c82e59ac5b049d9022c2d5783942c38d49497ac8a94c8f", url="https://pypi.org/packages/c7/09/68bfefcdc48875e66aabafc946620483d0cd93aba52dde37d2059e5bf927/sip-6.7.8.tar.gz")
    version("6.7.7", sha256="dee9c06fa8ae6d441a401f922867fc6196edda274eebd9fbfec54f0769c2a9e2", url="https://pypi.org/packages/f1/ba/19f9cb16416a3c98bd5969b1bd9bf3c92dd278788d8d949ed66b8e0edf0d/sip-6.7.7.tar.gz")
    version("6.6.2", sha256="0e3efac1c5dfd8e525ae57140927df26993e13f58b89d1577c314f4105bfd90d", url="https://pypi.org/packages/5b/cb/c27c925ae07bd03a2597fa1db17bfc2a4ac57da61aeb90f8ec98ffbb975b/sip-6.6.2.tar.gz")
    version("6.4.0", sha256="42ec368520b8da4a0987218510b1b520b4981e4405086c1be384733affc2bcb0", url="https://pypi.org/packages/c4/de/76c2927ea8f74dc4909c9affeba4c0191c43a4aefbe2118cc69b2cbd8461/sip-6.4.0.tar.gz")
    version("5.5.0", sha256="5d024c419b30fea8a6de8c71a560c7ab0bc3c221fbfb14d55a5b865bd58eaac5", url="https://pypi.org/packages/33/e9/27730ac17713c0a80d81d8f3bb56213f1549d96f9dc183fd16a7eec6287c/sip-5.5.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("module", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-packaging", when="@5.0.1:5.3,6.8:")
        depends_on("py-setuptools", when="@6.8:")
        depends_on("py-tomli", when="@6.8: ^python@:3.10")
    # END DEPENDENCIES

