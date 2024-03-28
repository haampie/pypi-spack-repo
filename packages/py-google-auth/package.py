# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGoogleAuth(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.28.2", sha256="9fd67bbcd40f16d9d42f950228e9cf02a2ded4ae49198b27432d0cded5a74c38", url="https://pypi.org/packages/92/94/35ba55b5011185ea1c995938e7851b25e6092f15658afa9263cd65a67dd4/google_auth-2.28.2-py2.py3-none-any.whl")
    version("2.28.1", sha256="25141e2d7a14bfcba945f5e9827f98092716e99482562f15306e5b026e21aa72", url="https://pypi.org/packages/b7/1d/f152a5f6d243b6acbb2a710ed19aa47154d678359bed995abdd9daf0cff0/google_auth-2.28.1-py2.py3-none-any.whl")
    version("2.28.0", sha256="7634d29dcd1e101f5226a23cbc4a0c6cda6394253bf80e281d9c5c6797869c53", url="https://pypi.org/packages/ff/ce/1b4dc8b5ecdc9a99202b093729192b69301c33064d0e312fb8d9e384dbe0/google_auth-2.28.0-py2.py3-none-any.whl")
    version("2.27.0", sha256="8e4bad367015430ff253fe49d500fdc3396c1a434db5740828c728e45bcce245", url="https://pypi.org/packages/82/41/7fb855444cead5b2213e053447ce3a0b7bf2c3529c443e0cf75b2f13b405/google_auth-2.27.0-py2.py3-none-any.whl")
    version("2.26.2", sha256="3f445c8ce9b61ed6459aad86d8ccdba4a9afed841b2d1451a11ef4db08957424", url="https://pypi.org/packages/aa/42/c3873f5a4369d28eb0006bfc80837f28b18bd4e04526f55cc9c8eac7a803/google_auth-2.26.2-py2.py3-none-any.whl")
    version("2.26.1", sha256="2c8b55e3e564f298122a02ab7b97458ccfcc5617840beb5d0ac757ada92c9780", url="https://pypi.org/packages/93/54/180b2447607fb63c10ba4bed48044b71d112ca83496f96141b65eb278e37/google_auth-2.26.1-py2.py3-none-any.whl")
    version("2.26.0", sha256="11f56129d30902cc9f4b93ed0c84ef7323f7328e6520eab1716740f3171afe35", url="https://pypi.org/packages/53/ce/1b43eb86c8487ff775189ac4e6f07073cab7014e4f7741a978d93ad4b7f2/google_auth-2.26.0-py2.py3-none-any.whl")
    version("2.25.2", sha256="473a8dfd0135f75bb79d878436e568f2695dce456764bf3a02b6f8c540b1d256", url="https://pypi.org/packages/f4/d2/9f6f3b9c0fd486617816cff42e856afea079d0bad99f0e60dc186c76b881/google_auth-2.25.2-py2.py3-none-any.whl")
    version("2.25.1", sha256="dfd7b44935d498e106c08883b2dac0ad36d8aa10402a6412e9a1c9d74b4773f1", url="https://pypi.org/packages/1f/eb/29123fbd92e4cb25d24713ab5d26ea74e02ce04290edc7c35356441de4f2/google_auth-2.25.1-py2.py3-none-any.whl")
    version("2.25.0", sha256="2e7d37702e617ea9f4ac2568625a9fc2cdea910dcdca90e378db09ac94ee9ab3", url="https://pypi.org/packages/15/f8/18c45d61d84769c02141e723a2ccfabfdb42d14768d42363fd23abf9b4b9/google_auth-2.25.0-py2.py3-none-any.whl")
    version("2.23.4", sha256="d4bbc92fe4b8bfd2f3e8d88e5ba7085935da208ee38a134fc280e7ce682a05f2", url="https://pypi.org/packages/86/a7/75911c13a242735d5aeaca6a272da380335ff4ba5f26d6b2ae20ff682d13/google_auth-2.23.4-py2.py3-none-any.whl")
    version("2.20.0", sha256="23b7b0950fcda519bfb6692bf0d5289d2ea49fc143717cc7188458ec620e63fa", url="https://pypi.org/packages/9a/1a/5866a7c6e16abc1df395e6d2b9808984d0905c747d75f5e20f1a052421d1/google_auth-2.20.0-py2.py3-none-any.whl")
    version("2.16.2", sha256="2fef3cf94876d1a0e204afece58bb4d83fb57228aaa366c64045039fda6770a2", url="https://pypi.org/packages/93/c4/16f8ad44ed7544244a9883f35cc99dc96378652a0ec7cc39028b1c697a1e/google_auth-2.16.2-py2.py3-none-any.whl")
    version("2.11.0", sha256="be62acaae38d0049c21ca90f27a23847245c9f161ff54ede13af2cb6afecbac9", url="https://pypi.org/packages/bb/6c/9b2dab3aff0dd9f685386598434dd8a0f205096b0a68d2c5e0c11be6f4b6/google_auth-2.11.0-py2.py3-none-any.whl")
    version("2.3.2", sha256="6e99f4b3b099feb50de20302f2f8987c1c36e80a3f856ce852675bdf7a0935d3", url="https://pypi.org/packages/89/a9/2264dce8fd1e4d55c73044d01c5a35565d179cd885174ad4fcdf0fa6ee36/google_auth-2.3.2-py2.py3-none-any.whl")
    version("1.35.0", sha256="997516b42ecb5b63e8d80f5632c1a61dddf41d2a4c2748057837e06e00014258", url="https://pypi.org/packages/fb/7a/1b3eb54caee1b8c73c2c3645f78a382eca4805a301a30c64a078e736e446/google_auth-1.35.0-py2.py3-none-any.whl")
    version("1.34.0", sha256="bd6aa5916970a823e76ffb3d5c3ad3f0bedafca0a7fa53bc15149ab21cb71e05", url="https://pypi.org/packages/35/bb/694d851e2c0776a422d43d579b82b7cc065da248d557f37595563824b1c9/google_auth-1.34.0-py2.py3-none-any.whl")
    version("1.33.1", sha256="036dd68c1e8baa422b6b61619b8e02793da2e20f55e69514612de6c080468755", url="https://pypi.org/packages/d7/13/35b1e0a63e160ecad04985e60339382e48e6020d22f8328a2ab47226c910/google_auth-1.33.1-py2.py3-none-any.whl")
    version("1.33.0", sha256="a756a33978fac611e4f00b69715b80e35467c30cc6262132d29d33a0e398ac55", url="https://pypi.org/packages/17/89/a11e6820a9fb7a2bb275a125bd01535776a801aa8964413bb3538e7c6f86/google_auth-1.33.0-py2.py3-none-any.whl")
    version("1.32.1", sha256="9266252e11393943410354cf14a77bcca24dd2ccd9c4e1aef23034fe0fbae630", url="https://pypi.org/packages/6e/1d/e4718af587967b8fb6ac7e0e257809934005a3f8fde8f31a304c7e682874/google_auth-1.32.1-py2.py3-none-any.whl")
    version("1.32.0", sha256="b3a67fa9ba5b768861dacf374c2135eb09fa14a0e40c851c3b8ea7abe6fc8fef", url="https://pypi.org/packages/c7/ef/6594c495bd51e2a9601a3d57d4a796f29bda8be42627613c7976ae587f97/google_auth-1.32.0-py2.py3-none-any.whl")
    version("1.31.0", sha256="6d47c79b5d09fbc7e8355fd9594cc4cf65fdde5d401c63951eaac4baa1ba2ae1", url="https://pypi.org/packages/50/ac/12df156754ee13ea4d57c77de8c4298e8fd00b0e580fecd8c7395374a7d8/google_auth-1.31.0-py2.py3-none-any.whl")
    version("1.30.2", sha256="eb017521276a75492282c6ca4b718f26de112ed3bcbeaeeb02c1b82de425f909", url="https://pypi.org/packages/96/21/bfde897baf6f0df050205a23bbfd9dcbedcac522b22eb9382d29e39fdd15/google_auth-1.30.2-py2.py3-none-any.whl")
    version("1.30.1", sha256="b3ca7a8ff9ab3bdefee3ad5aefb11fc6485423767eee016f5942d8e606ca23fb", url="https://pypi.org/packages/35/d2/0a79bc7e201c1b38ce46d607eb9398dc362dff1b054c7bba8e4e195c2ed7/google_auth-1.30.1-py2.py3-none-any.whl")
    version("1.30.0", sha256="588bdb03a41ecb4978472b847881e5518b5d9ec6153d3d679aa127a55e13b39f", url="https://pypi.org/packages/d2/c1/44179a1cfc5c3b5832a5f9c925161612471ec5f346bcd186235651d74f35/google_auth-1.30.0-py2.py3-none-any.whl")
    version("1.6.3", sha256="20705f6803fd2c4d1cc2dcb0df09d4dfcb9a7d51fd59e94a3a28231fd93119ed", url="https://pypi.org/packages/c5/9b/ed0516cc1f7609fb0217e3057ff4f0f9f3e3ce79a369c6af4a6c5ca25664/google_auth-1.6.3-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("aiohttp", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-aiohttp@3.6.2:3", when="@1.22.1:+aiohttp")
        depends_on("py-aiohttp@3.6.2:3", when="@1.22:1.22.0")
        depends_on("py-cachetools@2:4", when="@1.10:2.3")
        depends_on("py-cachetools@2:", when="@0.10:1.6,2.4:")
        depends_on("py-pyasn1-modules@0.2:", when="@1.3:")
        depends_on("py-requests@2.20:", when="@1.30.2:2.0.0.0,2.0.1:+aiohttp")
        depends_on("py-rsa@3.1.4:", when="@0.1:0.6,0.9:1.6,1.17:")
        depends_on("py-setuptools@40.3:", when="@1.7:2.3")
        depends_on("py-six@1.9:", when="@0.1:0.6,0.9:1,2.0.0.dev:2.0.0,2.3.1:2.22")
        depends_on("py-urllib3@:1", when="@2.18:2.23.0")
    # END DEPENDENCIES

