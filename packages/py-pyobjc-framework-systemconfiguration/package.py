##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSystemconfiguration(PythonPackage):
    version("10.2", sha256="e9ec946ca56514a68e28040c55c79ba105c9a70b56698635767250e629c37e49", url="https://pypi.org/packages/12/4a/409177e9530ba9334c2014c5e7ef7a016950da88a12c9ccd5d36fc65b4d6/pyobjc-framework-SystemConfiguration-10.2.tar.gz")
    version("10.1", sha256="7e125872d4b54c8d04f15d83e7f7f706c18bd87960b3873c797e6a71b95030b0", url="https://pypi.org/packages/ac/48/8c7feb30342715b6b707cb643a84648b7555f33e4ba3845f6aae0ce55147/pyobjc-framework-SystemConfiguration-10.1.tar.gz")
    version("10.0", sha256="f9ab1759933c77688615810f8278519158273a658f11fc3d75a1a2446fd0f774", url="https://pypi.org/packages/97/19/a932bcc059c5c33c74f56e7b62d460eec2515bd0124e37dfe223d150b137/pyobjc-framework-SystemConfiguration-10.0.tar.gz")
    version("9.2", sha256="0473a97d66ff0937df8f8d2c7109edc6ca8797d711d727823b296f0cff9878fb", url="https://pypi.org/packages/a1/49/d59fb1cb18bcb901de39faee2244eaedc33162be06bccf5baf5d2945d487/pyobjc-framework-SystemConfiguration-9.2.tar.gz")
    version("9.1.1", sha256="69a4b29cdb9fb925fa847a13359f19e8ab3b3417e8768c56373d23f74cb45a44", url="https://pypi.org/packages/3a/fd/0ce897d80144cc0075a0073df8807e372af2febffbf010b5f7de13ebc615/pyobjc-framework-SystemConfiguration-9.1.1.tar.gz")
    version("9.1", sha256="a37c5df1efd81e9d59dcbefe58fcbbbb536da78e6cf4d61a7fb4590ea586c991", url="https://pypi.org/packages/f6/b9/42806c2775c24dec025314277dedc338cbe45c8ca5cf98bf83a052652b83/pyobjc-framework-SystemConfiguration-9.1.tar.gz")
    version("9.0.1", sha256="0d328f3908b272d987aeaf56913dd4acf35bdb85a0a783cd3907c60e39b75bf3", url="https://pypi.org/packages/eb/e3/057c5de466858b68e752116cee36c83e3c46a59543b4da9baa6c536cdce5/pyobjc-framework-SystemConfiguration-9.0.1.tar.gz")
    version("9.0", sha256="5cd79dc8bb11922c125cfd1e2c514e35d588f187cf86a73ee50dccbabd77ea29", url="https://pypi.org/packages/3d/b8/19f707ee23e8be2c29220ff9899e8f969ad475010efa91e88211f8db5f35/pyobjc-framework-SystemConfiguration-9.0.tar.gz")
    version("8.5.1", sha256="f0c75fda3498d296e10a673700032ae0562e4c24b1f41c6290751edb939f84b5", url="https://pypi.org/packages/2a/05/357dc095f678bb60e9d602e89bb1e0d7c913f3020a7749742899830b070b/pyobjc-framework-SystemConfiguration-8.5.1.tar.gz")
    version("8.5", sha256="fb34bb38a9ae1597c4365b15ed8ffdd9243a20661b5619f7667691270206a1f4", url="https://pypi.org/packages/23/d0/bc4dbba0e3f258995e5fd201c2e86aa58fef29d608bb60e57769555c11d0/pyobjc-framework-SystemConfiguration-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")

