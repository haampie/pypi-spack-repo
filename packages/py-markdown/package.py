##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMarkdown(PythonPackage):
    version("3.6", sha256="48f276f4d8cfb8ce6527c8f79e2ee29708508bf4d40aa410fbc3b4ee832c850f", url="https://pypi.org/packages/fc/b3/0c0c994fe49cd661084f8d5dc06562af53818cc0abefaca35bdc894577c3/Markdown-3.6-py3-none-any.whl")
    version("3.5.2", sha256="d43323865d89fc0cb9b20c75fc8ad313af307cc087e84b657d9eec768eddeadd", url="https://pypi.org/packages/42/f4/f0031854de10a0bc7821ef9fca0b92ca0d7aa6fbfbf504c5473ba825e49c/Markdown-3.5.2-py3-none-any.whl")
    version("3.5.1", sha256="5874b47d4ee3f0b14d764324d2c94c03ea66bee56f2d929da9f2508d65e722dc", url="https://pypi.org/packages/70/58/2c5a654173937d9f540a4971c569b44dcd55e5424a484d954cdaeebcf79c/Markdown-3.5.1-py3-none-any.whl")
    version("3.5", sha256="4afb124395ce5fc34e6d9886dab977fd9ae987fc6e85689f08278cf0c69d4bf3", url="https://pypi.org/packages/bb/c1/50caaec6cadc1c6adc8fe351e03bd646d6e4dd17f55fca0f4c8d7ea8d3e9/Markdown-3.5-py3-none-any.whl")
    version("3.4.4", sha256="a4c1b65c0957b4bd9e7d86ddc7b3c9868fb9670660f6f99f6d1bca8954d5a941", url="https://pypi.org/packages/1a/b5/228c1cdcfe138f1a8e01ab1b54284c8b83735476cb22b6ba251656ed13ad/Markdown-3.4.4-py3-none-any.whl")
    version("3.4.3", sha256="065fd4df22da73a625f14890dd77eb8040edcbd68794bcd35943be14490608b2", url="https://pypi.org/packages/9a/a1/1352b0e5a3c71a79fa9265726e2217f69df9fd4de0bcb5725cc61f62a5df/Markdown-3.4.3-py3-none-any.whl")
    version("3.4.2", sha256="590e8c8139ce62a1121b4b07fd471eced441378f19f3265540de0791851977e5", url="https://pypi.org/packages/e3/f3/cdefcc25d25b3c8726c8a1966d6d5261bde662a20be9a217a415dc25ccb6/Markdown-3.4.2-py3-none-any.whl")
    version("3.4.1", sha256="08fb8465cffd03d10b9dd34a5c3fea908e20391a2a90b88d66362cb05beed186", url="https://pypi.org/packages/86/be/ad281f7a3686b38dd8a307fa33210cdf2130404dfef668a37a4166d737ca/Markdown-3.4.1-py3-none-any.whl")
    version("3.4", sha256="e90f851d4b0f788ee2e9c352205d8a592fd0c713ca6b934f87b81bc14d24dab7", url="https://pypi.org/packages/fb/55/e4b2e4709b66b2e623cba7fda352e9d1166935d27e53d0e716728ccac51b/Markdown-3.4-py3-none-any.whl")
    version("3.3.7", sha256="f5da449a6e1c989a4cea2631aa8ee67caa5a2ef855d551c88f9e309f4634c621", url="https://pypi.org/packages/f3/df/ca72f352e15b6f8ce32b74af029f1189abffb906f7c137501ffe69c98a65/Markdown-3.3.7-py3-none-any.whl")
    version("3.3.6", sha256="9923332318f843411e9932237530df53162e29dc7a4e2b91e35764583c46c9a3", url="https://pypi.org/packages/9f/d4/2c7f83915d437736996b2674300c6c4b578a6f897f34e40f5c04db146719/Markdown-3.3.6-py3-none-any.whl")
    version("3.3.4", sha256="96c3ba1261de2f7547b46a00ea8463832c921d3f9d6aba3f255a6f71386db20c", url="https://pypi.org/packages/6e/33/1ae0f71395e618d6140fbbc9587cc3156591f748226075e0f7d6f9176522/Markdown-3.3.4-py3-none-any.whl")
    version("3.3.3", sha256="c109c15b7dc20a9ac454c9e6025927d44460b85bd039da028d85e2b6d0bcc328", url="https://pypi.org/packages/ac/ef/24a91ca96efa0d7802dffb83ccc7a3c677027bea19ec3c9ee80be740408e/Markdown-3.3.3-py3-none-any.whl")
    version("3.3.2", sha256="77b7bff443b1f97b4814fa438c181fd5882e31edb01b422856b3feca91475f3e", url="https://pypi.org/packages/a0/34/4d6b7e3044044e89eaa25ed5395656cc351163c625fda0656d2729de399f/Markdown-3.3.2-py3-none-any.whl")
    version("3.3.1", sha256="10db1204a6c4aff7c7cf3cf25cc02761703baea54b6fb5e2b9ce2c186d81116f", url="https://pypi.org/packages/7a/2e/d769892bfb09144ad79ef525de0cb1765382e012cdd31aa117bef2ca7f66/Markdown-3.3.1-py3-none-any.whl")
    version("3.3", sha256="fbb1ba54ca41e8991dc5a561d9c6f752f5e4546f8750e56413ea50f2385761d3", url="https://pypi.org/packages/0e/ee/173f66a1954046debff7f4199cc826fc29d9e8521e1ae7a1c9d2bf858ea1/Markdown-3.3-py3-none-any.whl")
    version("3.2.2", sha256="c467cd6233885534bf0fe96e62e3cf46cfc1605112356c4f9981512b8174de59", url="https://pypi.org/packages/a4/63/eaec2bd025ab48c754b55e8819af0f6a69e2b1e187611dd40cbbe101ee7f/Markdown-3.2.2-py3-none-any.whl")
    version("3.2.1", sha256="e4795399163109457d4c5af2183fbe6b60326c17cfdf25ce6e7474c6624f725d", url="https://pypi.org/packages/ab/c4/ba46d44855e6eb1770a12edace5a165a0c6de13349f592b9036257f3c3d3/Markdown-3.2.1-py2.py3-none-any.whl")
    version("3.1.1", sha256="56a46ac655704b91e5b7e6326ce43d5ef72411376588afa1dd90e881b83c7e8c", url="https://pypi.org/packages/c0/4e/fd492e91abdc2d2fcb70ef453064d980688762079397f779758e055f6575/Markdown-3.1.1-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-importlib-metadata@4.4:", when="@3.3.6: ^python@:3.9")
        depends_on("py-setuptools@36:", when="@3.1:3.2.1")

