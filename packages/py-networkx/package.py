##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNetworkx(PythonPackage):
    version("3.2.1", sha256="f18c69adc97877c42332c170849c96cefa91881c99a7cb3e95b7c659ebdc1ec2", url="https://pypi.org/packages/d5/f0/8fbc882ca80cf077f1b246c0e3c3465f7f415439bdea6b899f6b19f61f70/networkx-3.2.1-py3-none-any.whl")
    version("3.2", sha256="8b25f564bd28f94ac821c58b04ae1a3109e73b001a7d476e4bb0d00d63706bf8", url="https://pypi.org/packages/f6/eb/5585c96636bbb2755865c31d83a19dd220ef88e716df4659dacb86e009cc/networkx-3.2-py3-none-any.whl")
    version("3.1", sha256="4f33f68cb2afcf86f28a45f43efc27a9386b535d567d2127f8f61d51dec58d36", url="https://pypi.org/packages/a8/05/9d4f9b78ead6b2661d6e8ea772e111fc4a9fbd866ad0c81906c11206b55e/networkx-3.1-py3-none-any.whl")
    version("3.0", sha256="58058d66b1818043527244fab9d41a51fcd7dcc271748015f3c181b8a90c8e2e", url="https://pypi.org/packages/11/eb/929b1a04b1778f4dd606c739c93c134306e4a31012e31e184c8308f3d985/networkx-3.0-py3-none-any.whl")
    version("2.8.8", sha256="e435dfa75b1d7195c7b8378c3859f0445cd88c6b0375c181ed66823a9ceb7524", url="https://pypi.org/packages/42/31/d2f89f1ae42718f8c8a9e440ebe38d7d5fe1e0d9eb9178ce779e365b3ab0/networkx-2.8.8-py3-none-any.whl")
    version("2.8.7", sha256="15cdf7f7c157637107ea690cabbc488018f8256fa28242aed0fb24c93c03a06d", url="https://pypi.org/packages/d0/00/1713dd6735d5a646cabdd99ff750e969795134d7d33f462ad71dfd07fa76/networkx-2.8.7-py3-none-any.whl")
    version("2.8.6", sha256="2a30822761f34d56b9a370d96a4bf4827a535f5591a4078a453425caeba0c5bb", url="https://pypi.org/packages/be/25/5b0fc262a2f2d7d11c22cb7785edf2befc756ae076b383034e79e255eb11/networkx-2.8.6-py3-none-any.whl")
    version("2.8.5", sha256="a762f4b385692d9c3a6f2912d058d76d29a827deaedf9e63ed14d397b8030687", url="https://pypi.org/packages/95/1b/14b5b17c52f7329b875e4ad2dcad23c808778b42ef6d250a7223d4dc378a/networkx-2.8.5-py3-none-any.whl")
    version("2.8.4", sha256="6933b9b3174a0bdf03c911bb4a1ee43a86ce3edeb813e37e1d4c553b3f4a2c4f", url="https://pypi.org/packages/34/71/1d6f7aaefa2fb38ea8c13dc47f3e2a32c4dc78f6229086ed90947fc49d3c/networkx-2.8.4-py3-none-any.whl")
    version("2.8.3", sha256="f151edac6f9b0cf11fecce93e236ac22b499bb9ff8d6f8393b9fef5ad09506cc", url="https://pypi.org/packages/4c/92/e2690ac6ecae3e5641fa49d49d93a7e3d4afc7e22574fa0514a2f513348e/networkx-2.8.3-py3-none-any.whl")
    version("2.7.1", sha256="011e85d277c89681e8fa661cf5ff0743443445049b0b68789ad55ef09340c6e0", url="https://pypi.org/packages/f6/34/4913f651b8e178dde5abcf8d62495e4dcd0757a9a6840f1b1f7a290afaea/networkx-2.7.1-py3-none-any.whl")
    version("2.6.3", sha256="80b6b89c77d1dfb64a4c7854981b60aeea6360ac02c6d4e4913319e0a313abef", url="https://pypi.org/packages/e9/93/aa6613aa70d6eb4868e667068b5a11feca9645498fd31b954b6c4bb82fa5/networkx-2.6.3-py3-none-any.whl")
    version("2.5.1", sha256="0635858ed7e989f4c574c2328380b452df892ae85084144c73d8cd819f0c4e06", url="https://pypi.org/packages/f3/b7/c7f488101c0bb5e4178f3cde416004280fd40262433496830de8a8c21613/networkx-2.5.1-py3-none-any.whl")
    version("2.5", sha256="8c5812e9f798d37c50570d15c4a69d5710a18d77bafc903ee9c5fba7454c616c", url="https://pypi.org/packages/9b/cd/dc52755d30ba41c60243235460961fc28022e5b6731f16c268667625baea/networkx-2.5-py3-none-any.whl")
    version("2.4", sha256="cdfbf698749a5014bf2ed9db4a07a5295df1d3a53bf80bf3cbd61edf9df05fa1", url="https://pypi.org/packages/41/8f/dd6a8e85946def36e4f2c69c84219af0fa5e832b018c970e92f2ad337e45/networkx-2.4-py3-none-any.whl")
    version("2.4-rc2", sha256="667e97c8ed026bddaa38b137f91fd6be72a5adb1bff0b649c2c8865097aebdfd", url="https://pypi.org/packages/ed/2b/22ffa2d177d8a324f65f1af41ceb2fc5d36649ccc150173345cced5617d6/networkx-2.4rc2-py3-none-any.whl")
    version("2.4-rc1", sha256="618995b7294db1bc3a3d5b85bdc9cc08e8367913df4cdcb066248cb833b747c0", url="https://pypi.org/packages/a8/1b/58909de8754d48181a0a17d738b59a775af47c74671793289353371520ff/networkx-2.4rc1.zip")
    version("2.3", sha256="8311ddef63cf5c5c5e7c1d0212dd141d9a1fe3f474915281b73597ed5f1d4e3d", url="https://pypi.org/packages/85/08/f20aef11d4c343b557e5de6b9548761811eb16e438cee3d32b1c66c8566b/networkx-2.3.zip")
    version("2.3-rc4", sha256="7ef8cafafb4db7147903923402d975b3c80f136a49602368e16676afbae60ad7", url="https://pypi.org/packages/43/72/edb64aaf87eb0dc10e5b0e712d0dc8a8714994d1aa54b509c2363943f09d/networkx-2.3rc4.zip")
    version("2.3-rc3", sha256="bb2b15283de865a0b1502beb54b010148238580e189bb7925be9561ebd824484", url="https://pypi.org/packages/42/6d/e9ca8e461a9137be5666620a88e1b41c3d735e16c62ad897e3b054998e31/networkx-2.3rc3.zip")
    version("2.2", sha256="45e56f7ab6fe81652fb4bc9f44faddb0e9025f469f602df14e3b2551c2ea5c8b", url="https://pypi.org/packages/f3/f4/7e20ef40b118478191cec0b58c3192f822cace858c19505c7670961b76b2/networkx-2.2.zip")
    version("2.2-rc1", sha256="74cf18c8e808e731a67bfce23cca678e7cd0ebb14495ac4f5421be02beb3ce77", url="https://pypi.org/packages/31/71/e9bf0d74e0488420e6a3eaea9d3c9741581cec6193d870f800a1d266b86f/networkx-2.2rc1.zip")
    version("2.1", sha256="64272ca418972b70a196cb15d9c85a5a6041f09a2f32e0d30c0255f25d458bb1", url="https://pypi.org/packages/11/42/f951cc6838a4dff6ce57211c4d7f8444809ccbe2134179950301e5c4c83c/networkx-2.1.zip")
    version("2.0", sha256="cd5ff8f75d92c79237f067e2f0876824645d37f017cfffa5b7c9678cae1454aa", url="https://pypi.org/packages/73/58/0add7d81cf64958f7a062aa287237364eb0a0959bf7a817f708d5c25d043/networkx-2.0.zip")
    version("1.11", sha256="1b229b54fe9ccb009cee4de02a88552191497a542a7d5d34adab216b9f15c1ff", url="https://pypi.org/packages/d3/2c/e473e54afc9fae58dfa97066ef6709a7e35a1dd1c28c5a3842989322be00/networkx-1.11-py2.py3-none-any.whl")
    version("1.10", sha256="1406d08a22eb52eaea22b47d3670fd6885442fcc5689b6b00db68a12f27d5b9a", url="https://pypi.org/packages/e6/e6/4b487d52f918102b46a00242b78e549ffe9c2a1621de5c69f9ea73afeac1/networkx-1.10.zip")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@3.2-rc0:")
        depends_on("py-decorator@4.3:4", when="@2.5.1:2.5")
        depends_on("py-decorator@4.3:", when="@2.4-rc2:2.5.0")
        depends_on("py-matplotlib@3.3.0:", when="@2.6-rc2:2.6.1")
        depends_on("py-matplotlib@3.3.0:", when="@2.6-rc1 ^python@:3.9")
        depends_on("py-numpy@1.19.0:", when="@2.6-rc2:2.6.1")
        depends_on("py-numpy@1.19.0:", when="@2.6-rc1 ^python@:3.9")
        depends_on("py-pandas@1.1.0:", when="@2.6-rc2:2.6.1")
        depends_on("py-pandas@1.1.0:", when="@2.6-rc1 ^python@:3.9")
        depends_on("py-scipy@1.5.0:1.6.0,1.6.2:", when="@2.6-rc2:2.6.1")
        depends_on("py-scipy@1.5.0:1.6.0,1.6.2:", when="@2.6-rc1 ^python@:3.9")

