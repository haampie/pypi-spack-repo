# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPdoc3(PythonPackage):
    # BEGIN VERSIONS
    version("0.10.0", sha256="ba45d1ada1bd987427d2bf5cdec30b2631a3ff5fb01f6d0e77648a572ce6028b", url="https://pypi.org/packages/67/36/add16f4705689ed1f31aba24c973d035fc953c6fe54af9143837cc3b1315/pdoc3-0.10.0-py3-none-any.whl")
    version("0.9.2", sha256="9df5d931f25f353c69c46819a3bd03ef96dd286f2a70bb1b93a23a781f91faa1", url="https://pypi.org/packages/48/05/6c987ce02df70ae11849a64c3ec2b32de68531d6b227e7dccdae7eb43fdb/pdoc3-0.9.2.tar.gz")
    version("0.9.1", sha256="e1848d5485b8dd4662272f83bb5f7df4a68e0a5d76c87be30327977777168894", url="https://pypi.org/packages/67/68/ce1035e720f1c5b80372164c389907d26cb488d600b42d136c75f587a427/pdoc3-0.9.1.tar.gz")
    version("0.9.0", sha256="3d04d5d84e88e3b7e0953c501552a77c85de996221415fd3ed354967c08c1ba3", url="https://pypi.org/packages/0d/b5/021c2247f65483ab181c66a9503a240a5ec2718afd79d2a3876c9789daea/pdoc3-0.9.0.tar.gz")
    version("0.8.5", sha256="63e59a7f723869e06d854c73215831dc04098f7038d9da3a1715be698e0d9551", url="https://pypi.org/packages/3b/5a/aea73303ed039c3f6122a4dcdb4356f9a0a40ca0def3887e45008300132e/pdoc3-0.8.5.tar.gz")
    version("0.8.4", sha256="9b2ec2279b004372810ab6b7465489ccf402428625dfecf3bd3f13b45aa5a3ea", url="https://pypi.org/packages/d9/79/dd3b035c0e3cdfdb972524138b9b6e623dcebbaf787e4e4af7d022b7c09d/pdoc3-0.8.4.tar.gz")
    version("0.8.3", sha256="19bd1a72e1c82875a6927b244aca826dedb635ea2a7a36ac62cbe063a8ddc30d", url="https://pypi.org/packages/1b/ae/0bf8314a56ba26fa701f89b50542e0306a2097fe08aed5eb6098fe79925a/pdoc3-0.8.3.tar.gz")
    version("0.8.2", sha256="fa8b851e0bdef77c37115e54ec55d6aed862d8bd4e865fd0f72ed058113c2e93", url="https://pypi.org/packages/05/ea/6b53f6708f93bc9d9ff2005fb66608799403927d4d840738049ed9d7aba7/pdoc3-0.8.2.tar.gz")
    version("0.8.1", sha256="d7b56e67b5e049d53dcde94245a28040b640b2e06c344fc58ab2bdf2d91dc00f", url="https://pypi.org/packages/11/1c/ce4459d7aab0890b6059a8c5cc3494c92d3a1cfe1938e2ae49555b3bf31a/pdoc3-0.8.1.tar.gz")
    version("0.8.0", sha256="793e7a83db96fc7a992bc593265a0963d0bdf7d66a1dd5d443a6c6ea885b73be", url="https://pypi.org/packages/56/49/0f8577808aa4e784650cff028519b4a5cff27feb3e227e50d2a3e9c474ac/pdoc3-0.8.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-mako", when="@0.10:")
        depends_on("py-markdown@3:", when="@0.10:")
    # END DEPENDENCIES

