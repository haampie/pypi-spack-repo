# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtStorage(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("21.1.0", sha256="593f2544fc4f05750c4fe7ca4d83c32ea1e9d266e57899bbf79ce5940124e8cc", url="https://pypi.org/packages/58/31/4d37f8a85c37933961f8547f1df53018baef4e66d47f752ffd151f78af8a/azure_mgmt_storage-21.1.0-py3-none-any.whl")
    version("21.0.0", sha256="89d644c6192118b0b097deaa9c4925832d8f7ea4693d38d5fce3f0125b43a1c5", url="https://pypi.org/packages/6a/53/dd7f37c78faf77f15ec0acfea3094b317e7183014414ffe737c2e32e6fa7/azure_mgmt_storage-21.0.0-py3-none-any.whl")
    version("20.1.0", sha256="afdc830329c674d96a91c963fa03ac81a4e387dfbf9f5a4e823950dc1fe95659", url="https://pypi.org/packages/8c/24/33da34950a637df9bca4bac4b99be81e060613edf22a54589d17e2b7b51a/azure_mgmt_storage-20.1.0-py3-none-any.whl")
    version("20.0.0", sha256="bc7a79d16b2979a2d6e6adb0b90b323ddbd91457848095c89f73119df6c34565", url="https://pypi.org/packages/b5/76/da64c1971938f7d34f82bb4f88e6a792ac939ca6c04bb730552af1e23c59/azure_mgmt_storage-20.0.0-py3-none-any.whl")
    version("19.1.0", sha256="61c7a55395e7410a24bfc8def353429eb772a105dd8268dce91f5ee38e4fc04e", url="https://pypi.org/packages/52/7d/2e7224a1c33b7411a8fd2e68532b57d3763c40312aca2e56d06f4a28deb4/azure_mgmt_storage-19.1.0-py3-none-any.whl")
    version("19.0.0", sha256="d4960693a4e2aa046b510df13c2071df2eb3f99925384a127d843a3b969fc54b", url="https://pypi.org/packages/3e/c6/d49549f6530eb8d227c1c3fd80759d0049c9a032d00311d7df0a666e06a7/azure_mgmt_storage-19.0.0-py2.py3-none-any.whl")
    version("18.0.0", sha256="ec11d6aef47f8489559055e4c1a1891567828b9864f63ee8c7a81c9d911015b6", url="https://pypi.org/packages/b0/20/f996529e223c296a6da604a7cb042fd91a05c591b37fa2a1b5c1defbf47c/azure_mgmt_storage-18.0.0-py2.py3-none-any.whl")
    version("17.1.0", sha256="884ca5bdcb23fc7aaca45dfb1f256155a17d1f632a857c7c5b4396f7b672deee", url="https://pypi.org/packages/21/78/caf794ee639460e8c99f7bd65b090146e7f5a274776a59b895a96d7856a3/azure_mgmt_storage-17.1.0-py2.py3-none-any.whl")
    version("17.0.0", sha256="671a2c57bff42e32e18ea7891d2b81d6dcdbb454fe60dc7be7ab09b92c11fd01", url="https://pypi.org/packages/57/f4/c971322dd556b992b6a370b676d82f2c92d3a2f01841c484191c715afaef/azure_mgmt_storage-17.0.0-py2.py3-none-any.whl")
    version("16.0.0", sha256="a819e421d50c0b58416b551d3e9e9a9cf6029714cf977ffaaee86a37572e7113", url="https://pypi.org/packages/51/76/1cacd32812c88fc79435a90a64f37cbc92fb95516c91c0e856c2e88ac8f3/azure_mgmt_storage-16.0.0-py2.py3-none-any.whl")
    version("11.2.0", sha256="86a782cd1ca763f6680182a8b18e40a18814f84ff850be828a515fd221c26db7", url="https://pypi.org/packages/33/cc/8ace313fd151af6663b1e1778f216532eab0258133ef21498c0e2caefad6/azure_mgmt_storage-11.2.0-py2.py3-none-any.whl")
    version("11.1.0", sha256="62a6a8c1c359026ec560856da25221b66b6f1e0a84763a04e863c6e911bc1a5e", url="https://pypi.org/packages/60/6c/2f170614e3414e807c8f18a197237a0a54c3cebf770e4cb3b2ef31138f58/azure_mgmt_storage-11.1.0-py2.py3-none-any.whl")
    version("11.0.0", sha256="9148e4144919c55323555b787dd2dd9c473651039c5a2b49e95cb9461cdaf9c3", url="https://pypi.org/packages/08/64/04619c2c914aac4793ef0cf32e3aba7752ca2464e36c8f247829a0385ae5/azure_mgmt_storage-11.0.0-py2.py3-none-any.whl")
    version("10.0.0", sha256="1f9b2f3b4d633c522a7585cb8933300fdcc58226e90a99814dd1eaaec9680780", url="https://pypi.org/packages/44/09/8c521bd6004fb64e37ab8f467378dd6f47b2c10d17d48be9cd622e8d3e11/azure_mgmt_storage-10.0.0-py2.py3-none-any.whl")
    version("9.0.0", sha256="d340f01867c2986ba5a00c8d4b789e13c4c70c9d0bd1770bb50ecb4de56afbe8", url="https://pypi.org/packages/65/f0/8486761674c640c48219824b3ccd3cc571a792d1a0e90c8d25ed0e202d8d/azure_mgmt_storage-9.0.0-py2.py3-none-any.whl")
    version("8.0.0", sha256="bb00ea7c9b39dc5fd0a941a104b131f3bc74577f9c08cdbc22e3d41b06f3884d", url="https://pypi.org/packages/8a/d6/3e4e6b74fa810d94bbb69b52a35025d5ddfec7a573ac840b45f0439dca74/azure_mgmt_storage-8.0.0-py2.py3-none-any.whl")
    version("7.2.0", sha256="65bdf2d3bbf589d2856c39ff104bd9722faa4bddc55c6137e10a0a15dec758c4", url="https://pypi.org/packages/d4/14/ee62ad8023d6bebcde94f96acc2c7ae9e52969ef3b9464e5d6f20294400b/azure_mgmt_storage-7.2.0-py2.py3-none-any.whl")
    version("7.1.0", sha256="9926a4118e1c27af7bef54ec2d70a9ad26566015c11c63897f84ee657173e331", url="https://pypi.org/packages/ea/5a/a179c75e31a1bd8bc2f919638fe7b716062a6e59b39d0bb637e3d7051f6e/azure_mgmt_storage-7.1.0-py2.py3-none-any.whl")
    version("7.0.0", sha256="a74454fe0ed66081971a66a0a97b3db91968f3e68618e3a7220b1707fe5b4179", url="https://pypi.org/packages/5b/ee/1415439cbbbffce8c9cc9a55b4c0313a2f2a995f9655acfa5aa7344e6d8f/azure_mgmt_storage-7.0.0-py2.py3-none-any.whl")
    version("6.0.0", sha256="95220e51eca421707b704e59f023d7fe367382b1ec0dd5f7e279f8d221417a4d", url="https://pypi.org/packages/8a/d9/117216e5f671f6c3238c50cba583924252c5ee08091a7d10fa1d3113faa3/azure_mgmt_storage-6.0.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-common@1.1:", when="@1.2.1:2.0.0-rc2,3:")
        depends_on("py-azure-mgmt-core@1.3.2:", when="@21:")
        depends_on("py-azure-mgmt-core@1.3.1:", when="@20.1:20")
        depends_on("py-azure-mgmt-core@1.3.0:", when="@19.1:20.0")
        depends_on("py-azure-mgmt-core@1.2:", when="@16.0.0:19.0")
        depends_on("py-isodate@0.6.1:", when="@21.1.0:")
        depends_on("py-msrest@0.7.1:", when="@21:21.1.0-beta1")
        depends_on("py-msrest@0.6.21:", when="@17.1:20")
        depends_on("py-msrest@0.5:", when="@3:17.0")
        depends_on("py-msrestazure@0.4.32:", when="@2.0.0:11")
    # END DEPENDENCIES

