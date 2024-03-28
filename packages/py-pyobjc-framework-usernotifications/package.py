# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkUsernotifications(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="3a1b7d77c95dff109f904451525752ece3c38f38cfa0825fd01735388c2b0264", url="https://pypi.org/packages/be/a5/9fc721a019096bf5caad76e0a288ed9b08d123166e04e5477154ec90930a/pyobjc-framework-UserNotifications-10.2.tar.gz")
    version("10.1", sha256="eca638b04b60d5d8f5efecafc1fd021a1b55d4a6d1ebd22e65771eddb3dd478f", url="https://pypi.org/packages/d0/39/7b98a78c7a373fe1cda0bb42bd6875ebe3c918845de1a5b84653df4d9a9b/pyobjc-framework-UserNotifications-10.1.tar.gz")
    version("10.0", sha256="d2646747d4ddbf9abb8e41937364ae074742449e2fd9d33b3138049ad686d555", url="https://pypi.org/packages/03/c4/3a0b6c374dfc7769b301c14dec06e8843947f743722fa9860053b5266200/pyobjc-framework-UserNotifications-10.0.tar.gz")
    version("9.2", sha256="496abf66e22c99c832fb6bb231e4c15f28ee0f6dc49e004b3e3983b3ade84340", url="https://pypi.org/packages/f7/fb/22924927c5e7d1496297d90f91811d1da425c31e8bcfac9f02444df0717a/pyobjc-framework-UserNotifications-9.2.tar.gz")
    version("9.1.1", sha256="409d390a2408fbec094b6f85605ad82a1579cec1732c1a8a3a93af98dc756a88", url="https://pypi.org/packages/4c/4e/eb073b72eb4aeff99ad310b1129cbca01b56718e46f76d7eaf1a8a452c56/pyobjc-framework-UserNotifications-9.1.1.tar.gz")
    version("9.1", sha256="c78832f3b9ada8cf23a91bc743a48d57b85e235903ef31afd6a63b1f8580fd0b", url="https://pypi.org/packages/41/f0/b39b626c628fb8512d98045a6ed02cd2e94fda180555d8e9cfbc3ee1b07b/pyobjc-framework-UserNotifications-9.1.tar.gz")
    version("9.1-beta1", sha256="4bf7bd74a482aa5cf05a9b4cbcd11559c9402c9e6fb131414848dd9a06faad0e", url="https://pypi.org/packages/e6/7a/da0df130ddebdbf241a4b7228e1daee71b8a8d4cc1d11f704f4050c3e5ce/pyobjc-framework-UserNotifications-9.1b1.tar.gz")
    version("9.0.1", sha256="38894aefa85bebb855559b16f798c2b8cf34cbcb7b292cd52fe143c64c6e411b", url="https://pypi.org/packages/bc/d1/2c23e989f985bba0763dd57eeab63abfb982d856be2a303011adccf59f33/pyobjc-framework-UserNotifications-9.0.1.tar.gz")
    version("9.0", sha256="8b51ee6b75456b4c9a767002c5482b3d034e4442e5b9ce079cf4bba5ac5883ee", url="https://pypi.org/packages/b7/3a/976a0cdf5437bb8952c58fb70c871e29f4f9c100abf1ec1f53eaa317a0ee/pyobjc-framework-UserNotifications-9.0.tar.gz")
    version("8.5.1", sha256="63af8bde4d3d57eb3b40fea2512f812487919d05dd30aabe3ca086e200d87bb3", url="https://pypi.org/packages/19/dd/c1051d4d2a154484aec111aa7b0baf53cacd451cb808d98e77ae3e2daa6c/pyobjc-framework-UserNotifications-8.5.1.tar.gz")
    version("8.5", sha256="718116e7a4fe590eedf2fd083c78c616e8d4f866c59e46c3ebc1de6a00ad0f88", url="https://pypi.org/packages/fb/62/5f2800caada0f6a898016a4afdf3b39e38e6107c9d70de2fcf4b15458f78/pyobjc-framework-UserNotifications-8.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
    # END DEPENDENCIES

