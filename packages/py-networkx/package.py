# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNetworkx(PythonPackage):
    # BEGIN VERSIONS
    version("3.1", sha256="4f33f68cb2afcf86f28a45f43efc27a9386b535d567d2127f8f61d51dec58d36", url="https://pypi.org/packages/a8/05/9d4f9b78ead6b2661d6e8ea772e111fc4a9fbd866ad0c81906c11206b55e/networkx-3.1-py3-none-any.whl")
    version("3.0", sha256="58058d66b1818043527244fab9d41a51fcd7dcc271748015f3c181b8a90c8e2e", url="https://pypi.org/packages/11/eb/929b1a04b1778f4dd606c739c93c134306e4a31012e31e184c8308f3d985/networkx-3.0-py3-none-any.whl")
    version("2.8.6", sha256="2a30822761f34d56b9a370d96a4bf4827a535f5591a4078a453425caeba0c5bb", url="https://pypi.org/packages/be/25/5b0fc262a2f2d7d11c22cb7785edf2befc756ae076b383034e79e255eb11/networkx-2.8.6-py3-none-any.whl")
    version("2.7.1", sha256="011e85d277c89681e8fa661cf5ff0743443445049b0b68789ad55ef09340c6e0", url="https://pypi.org/packages/f6/34/4913f651b8e178dde5abcf8d62495e4dcd0757a9a6840f1b1f7a290afaea/networkx-2.7.1-py3-none-any.whl")
    version("2.6.3", sha256="80b6b89c77d1dfb64a4c7854981b60aeea6360ac02c6d4e4913319e0a313abef", url="https://pypi.org/packages/e9/93/aa6613aa70d6eb4868e667068b5a11feca9645498fd31b954b6c4bb82fa5/networkx-2.6.3-py3-none-any.whl")
    version("2.5.1", sha256="0635858ed7e989f4c574c2328380b452df892ae85084144c73d8cd819f0c4e06", url="https://pypi.org/packages/f3/b7/c7f488101c0bb5e4178f3cde416004280fd40262433496830de8a8c21613/networkx-2.5.1-py3-none-any.whl")
    version("2.5", sha256="8c5812e9f798d37c50570d15c4a69d5710a18d77bafc903ee9c5fba7454c616c", url="https://pypi.org/packages/9b/cd/dc52755d30ba41c60243235460961fc28022e5b6731f16c268667625baea/networkx-2.5-py3-none-any.whl")
    version("2.4", sha256="cdfbf698749a5014bf2ed9db4a07a5295df1d3a53bf80bf3cbd61edf9df05fa1", url="https://pypi.org/packages/41/8f/dd6a8e85946def36e4f2c69c84219af0fa5e832b018c970e92f2ad337e45/networkx-2.4-py3-none-any.whl")
    version("2.3", sha256="8311ddef63cf5c5c5e7c1d0212dd141d9a1fe3f474915281b73597ed5f1d4e3d", url="https://pypi.org/packages/85/08/f20aef11d4c343b557e5de6b9548761811eb16e438cee3d32b1c66c8566b/networkx-2.3.zip")
    version("2.2", sha256="45e56f7ab6fe81652fb4bc9f44faddb0e9025f469f602df14e3b2551c2ea5c8b", url="https://pypi.org/packages/f3/f4/7e20ef40b118478191cec0b58c3192f822cace858c19505c7670961b76b2/networkx-2.2.zip")
    version("2.1", sha256="64272ca418972b70a196cb15d9c85a5a6041f09a2f32e0d30c0255f25d458bb1", url="https://pypi.org/packages/11/42/f951cc6838a4dff6ce57211c4d7f8444809ccbe2134179950301e5c4c83c/networkx-2.1.zip")
    version("2.0", sha256="cd5ff8f75d92c79237f067e2f0876824645d37f017cfffa5b7c9678cae1454aa", url="https://pypi.org/packages/73/58/0add7d81cf64958f7a062aa287237364eb0a0959bf7a817f708d5c25d043/networkx-2.0.zip")
    version("1.11", sha256="1b229b54fe9ccb009cee4de02a88552191497a542a7d5d34adab216b9f15c1ff", url="https://pypi.org/packages/d3/2c/e473e54afc9fae58dfa97066ef6709a7e35a1dd1c28c5a3842989322be00/networkx-1.11-py2.py3-none-any.whl")
    version("1.10", sha256="1406d08a22eb52eaea22b47d3670fd6885442fcc5689b6b00db68a12f27d5b9a", url="https://pypi.org/packages/e6/e6/4b487d52f918102b46a00242b78e549ffe9c2a1621de5c69f9ea73afeac1/networkx-1.10.zip")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("default", default=False, description="default")
    variant("extra", default=False, description="extra")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@2.7-rc1:3.1")
        depends_on("python@3.7:", when="@2.6-rc1:2.6")
        depends_on("py-decorator@4.3:4", when="@2.5.1:2.5")
        depends_on("py-decorator@4.3:", when="@2.4-rc2:2.5.0")
        depends_on("py-lxml@4.6:", when="@2.7-rc1:+extra")
        depends_on("py-lxml@4.5:", when="@2.6-rc1:2.6+extra")
        depends_on("py-matplotlib@3.4.0:", when="@2.7-rc1:3.1+default")
        depends_on("py-matplotlib@3.3.0:", when="@2.6.2:2.6+default")
        depends_on("py-numpy@1.20.0:", when="@3:3.1+default")
        depends_on("py-numpy@1.19.0:", when="@2.6.2:2+default")
        depends_on("py-pandas@1.3.0:", when="@2.7-rc1:3.1+default")
        depends_on("py-pandas@1.1.0:", when="@2.6.2:2.6+default")
        depends_on("py-pydot@1.4.2:", when="@2.7-rc1:+extra")
        depends_on("py-pydot@1.4.1:", when="@2.6-rc1:2.6+extra")
        depends_on("py-pygraphviz@1.10:", when="@3:3.1+extra")
        depends_on("py-pygraphviz@1.9:", when="@2.7-rc1:2+extra")
        depends_on("py-pygraphviz@1.7:", when="@2.6-rc1:2.6+extra")
        depends_on("py-scipy@1.8.0:", when="@2.7-rc1:3.1+default")
        depends_on("py-scipy@1.5.0:1.6.0,1.6.2:", when="@2.6.2:2.6+default")
        depends_on("py-sympy@1.10:", when="@2.8-rc1:+extra")
    # END DEPENDENCIES

