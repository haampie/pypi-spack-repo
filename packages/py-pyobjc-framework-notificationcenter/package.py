# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkNotificationcenter(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="3771c7a8b8e839d07c7cb51eef2e83666254bdd88bd873b0ba7e385245cda684", url="https://pypi.org/packages/23/76/4e24d50cab85ea0736b09b3ec5d52d206168121658febbb337f2ac2bbd99/pyobjc-framework-NotificationCenter-10.2.tar.gz")
    version("10.1", sha256="697e29da4fdd5899e5db5bda7bdb5afc97f4a6e4d959caf2316aef3b300c5575", url="https://pypi.org/packages/1b/62/3b32b0a4b5c39568054f3fa902554113deb30c4308ff679c8fb13e6a96fb/pyobjc-framework-NotificationCenter-10.1.tar.gz")
    version("10.0", sha256="64f85eaea8e8811afbfa265e56d3d07ab8b0e57a4a7b5b33a9f72a50a3ede83b", url="https://pypi.org/packages/e5/9a/0414428049e20eab078ea69576ba6fd76fdec4e6930e8103b230ad1ab31c/pyobjc-framework-NotificationCenter-10.0.tar.gz")
    version("9.2", sha256="ee70375c42dede539aee9a5694aa3f38dfde6e848cf60b366ab5100e9bd76e00", url="https://pypi.org/packages/1f/42/11b98338738861ec35102fdd02a34cb075e13293d3dc2738700db47322b2/pyobjc-framework-NotificationCenter-9.2.tar.gz")
    version("9.1.1", sha256="4dd1ca5bda1e938496f7a053b78ebaa0c358fc54f647fdc644f323728f5dfd5c", url="https://pypi.org/packages/a4/fa/86a7ebb36eba8b13941d03d2167f67f0e67765ed89ff1a9d08edec1750b3/pyobjc-framework-NotificationCenter-9.1.1.tar.gz")
    version("9.1", sha256="f131031db961675bd6cfa8c0e35b32dd3d3de25930f1f0bc6a2ebdab80320953", url="https://pypi.org/packages/d0/53/61d760bb8c9bfec29c174f77d0f4229ace50dc05345291af2806591687f4/pyobjc-framework-NotificationCenter-9.1.tar.gz")
    version("9.0.1", sha256="24331121e8dd0d7f18ce04a2d696922fe87494426a7903955b413572a6b2096b", url="https://pypi.org/packages/30/d6/e85930273fad8e96362744a807c440218bb0ae6fb583defa423bd67fee32/pyobjc-framework-NotificationCenter-9.0.1.tar.gz")
    version("9.0", sha256="317dae872ba62abf1e483854542da912e3e2f0e287e5fe2d0d41037a5fb8a30c", url="https://pypi.org/packages/cf/3f/589bbaef9022b066a1cf6034c1045d1ff0a9adf7f2ab648a6e29f7fd1170/pyobjc-framework-NotificationCenter-9.0.tar.gz")
    version("8.5.1", sha256="ea173b38a74a004fe0df6729b076314600cbfa3d4b7683a862db6e56c26e4663", url="https://pypi.org/packages/a1/e2/15aec289b4c65e3766bed117f52c829748212cb3a212fe0f0a7791a2a081/pyobjc-framework-NotificationCenter-8.5.1.tar.gz")
    version("8.5", sha256="23fce23e4f8eab0849f2db9870a05433c1de0ef538664faf444cf8013c707cb3", url="https://pypi.org/packages/79/3d/5c0591758ddac199a0cab3b66d446a6cf5177a235bb840f920b8c951eb82/pyobjc-framework-NotificationCenter-8.5.tar.gz")
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

