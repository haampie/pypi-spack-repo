# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTypeshedClient(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.5.1", sha256="8cc254766b38f949effd3c9d4e0934d706d787127d7aedcabc648e4f094f7292", url="https://pypi.org/packages/45/66/a8eb53dc5f071e66cfc43c980c565f93085cc421f2f3aa921418de692705/typeshed_client-2.5.1-py3-none-any.whl")
    version("2.5.0", sha256="dd2aecca6d359e29881940dbdf994ae080560b75609a91dcc94462a9294761a4", url="https://pypi.org/packages/f0/27/b2af46f29d89f5ff94c95616a668ca839130abb75c5cc8be26402bf07b95/typeshed_client-2.5.0-py3-none-any.whl")
    version("2.4.0", sha256="5358cab27cf2d7b1cd1e77dd92a3ac3cd9cd31df9eb2e958bd280a38160a3219", url="https://pypi.org/packages/3b/ab/bdb75d8769bb63cadae3429ab5bcb0b9e6d9e17234c8e7d7fed246ad0b0e/typeshed_client-2.4.0-py3-none-any.whl")
    version("2.3.0", sha256="27976287e0682be3005233f08f6f3cedf0c496413bcb213378f46e08798988c4", url="https://pypi.org/packages/2f/e4/14dc927c45361de492b310f9edc5d4e6022d501f2fbb20edc5800d759369/typeshed_client-2.3.0-py3-none-any.whl")
    version("2.2.0", sha256="6f5a5841a0cf664ac66ea05f1ed3372a191d307b146f8b9aaa09719d1156626e", url="https://pypi.org/packages/e4/78/a4b88147bb721ed237e7fa736f84a494c0b97703f48fa16c5c9b4f3a9e92/typeshed_client-2.2.0-py3-none-any.whl")
    version("2.1.0", sha256="95aabf54a80ee19b56ac349ca3fb9bdd4cf03e10ee46778ec2ba05e737290ff5", url="https://pypi.org/packages/0f/41/800089b9b6ff9222b2477e59905296baef77464b206cb69f17656a5d9478/typeshed_client-2.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-importlib-resources@1.4:", when="@1:")
        depends_on("py-typing-extensions@4.5:", when="@2.5:")
    # END DEPENDENCIES

