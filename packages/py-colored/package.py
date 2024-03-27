##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyColored(PythonPackage):
    version("2.2.4", sha256="a7069673bd90a35f46cb748d012c17284a0668d2f1c06bc7a51822a2d5ad2112", url="https://pypi.org/packages/75/d1/548f697f88872321525e294f8863efbdd1c313964b7f94e49ab0dc4f2895/colored-2.2.4-py3-none-any.whl")
    version("2.2.3", sha256="1318b2fb8e0313d39724b8ab0707af79d1e2c0e60710b608a00e70fe0f84ff5d", url="https://pypi.org/packages/6f/0d/a10351ef1a98e0b03d66887ec2d87c261f9a0fbff8f2bdb75614cc0a2850/colored-2.2.3-py3-none-any.whl")
    version("2.2.2", sha256="c7790b4557c8911ac877fff211a3ebe8b8655d4f0281dbbe1930d33ff23f96ed", url="https://pypi.org/packages/3d/03/15850bec2dcbccaa9c1d9779acd26e3c020b6c3528b086a3c5ecfaec956c/colored-2.2.2-py3-none-any.whl")
    version("2.2.1", sha256="0a0a18d07d9215a39125d0ef17128608601be9adb97a9ea548d6bfdfef81c154", url="https://pypi.org/packages/a5/0b/204ac450f4d728ad7b8ea9ad9f0cbe1097625b225464ecca7f09cc92d763/colored-2.2.1-py3-none-any.whl")
    version("2.2.0", sha256="1394ade3ecbbbaa66c8e4e17b22e927e3fa969316bcc99874a8339108ee57913", url="https://pypi.org/packages/63/bb/d42b490a3ecbd7652b8f868fd2498f6bc53787e51f77ea711c9df00b7384/colored-2.2.0-py3-none-any.whl")
    version("2.1.1", sha256="64a2eb8443def36dd376df3fce5be1d00a3d06f96997de158039075c5e02f069", url="https://pypi.org/packages/5c/1e/c2173cb2f3d228cd45574be4462371b16620256d808d05be116031b91299/colored-2.1.1-py3-none-any.whl")
    version("2.1.0", sha256="cd9d65a26d6a2df26b53c63fd670faf8fe460b1e13db6283acff5bc15dfc2cee", url="https://pypi.org/packages/ba/78/2161695f090e5b515382cb9e5848c8849e111faf31fdd435e1f7f043ef75/colored-2.1.0-py3-none-any.whl")
    version("2.0.0", sha256="eb6f17d722d6e9d75908702855475302bda942f75bcbe3693e7021f123c233b7", url="https://pypi.org/packages/c2/ae/4fa55b276f7f28df5f9181c69c522838615dc22e0d15096c27ac971e0bd8/colored-2.0.0-py3-none-any.whl")
    version("1.5.0", sha256="dcc1f29223b8e2e8fbace0570a4ebf888b3321373fa14db45fecd3fe0261e679", url="https://pypi.org/packages/31/5e/75b2e14e2177655d3572df324e851efd035294ae67044f4934d68a67d5b2/colored-1.5.0-py3-none-any.whl")
    version("1.4.4", sha256="04ff4d4dd514274fe3b99a21bb52fb96f2688c01e93fba7bef37221e7cb56ce0", url="https://pypi.org/packages/f3/d6/00203998f27ab30b2417998006ad0608f236740bb129494dd7c5621861e1/colored-1.4.4.tar.gz")
    version("1.4.2", sha256="056fac09d9e39b34296e7618897ed1b8c274f98423770c2980d829fd670955ed", url="https://pypi.org/packages/b2/16/04827e24c14266d9161bd86bad50069fea453fa006c3d2b31da39251184a/colored-1.4.2.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.5:")

