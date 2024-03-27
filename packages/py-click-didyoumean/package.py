##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyClickDidyoumean(PythonPackage):
    version("0.3.1", sha256="5c4bb6007cfea5f2fd6583a2fb6701a22a41eb98957e63d0fac41c10e7c3117c", url="https://pypi.org/packages/1b/5b/974430b5ffdb7a4f1941d13d83c64a0395114503cc357c6b9ae4ce5047ed/click_didyoumean-0.3.1-py3-none-any.whl")
    version("0.3.0", sha256="a0713dc7a1de3f06bc0df5a9567ad19ead2d3d5689b434768a6145bff77c0667", url="https://pypi.org/packages/ad/36/4599267417fc78b587b1588e0647a468c60b36c02bb723d450d050738fa8/click_didyoumean-0.3.0-py3-none-any.whl")
    version("0.2.0", sha256="4a49fefdddaed47fe316d259e8255a2d0e9e1189aa6dde9f13ec524163860a30", url="https://pypi.org/packages/b5/79/c8fee1e4675ce2228aef2914206447a7aaae99027ceeb078df634b606336/click_didyoumean-0.2.0-py3-none-any.whl")
    version("0.1.0", sha256="f343bfc710caacc2312061b3deffcfca5da2d9df0ef409925d2c3fdbb01863df", url="https://pypi.org/packages/c3/6e/4d5de0180182f4380fadac5df6ae109c82fef703d6087ee01674534d5e55/click_didyoumean-0.1.0-py3-none-any.whl")
    version("0.0.3", sha256="112229485c9704ff51362fe34b2d4f0b12fc71cc20f6d2b3afabed4b8bfa6aeb", url="https://pypi.org/packages/9f/79/d265d783dd022541b744d002745d9e55d84c04a41930e35d8795934f6526/click-didyoumean-0.0.3.tar.gz")

    with default_args(type="run"):
        depends_on("py-click@7:", when="@0.3:")
        depends_on("py-click@8.0.1:", when="@0.1:0.2")

