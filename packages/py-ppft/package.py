##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPpft(PythonPackage):
    version("1.7.6.8", sha256="de2dd4b1b080923dd9627fbdea52649fd741c752fce4f3cf37e26f785df23d9b", url="https://pypi.org/packages/ff/fa/5160c7d2fb1d4f2b83cba7a40f0eb4b015b78f6973b7ab6b2e73c233cfdc/ppft-1.7.6.8-py3-none-any.whl")
    version("1.7.6.7", sha256="fedb1b1253729d62483f2e1f36547fd50a5fc873ffbf9b78b48cfdc727d4180c", url="https://pypi.org/packages/f0/f8/0a493dfdf73edbfe58cae1323aec72d0152f463c7a351bd285e9d500985c/ppft-1.7.6.7-py3-none-any.whl")
    version("1.7.6.6", sha256="f355d2caeed8bd7c9e4a860c471f31f7e66d1ada2791ab5458ea7dca15a51e41", url="https://pypi.org/packages/0f/c1/dd740386023b1472d2635db9d8f7107024d9931cc8c01b37b48a85eb3811/ppft-1.7.6.6-py3-none-any.whl")
    version("1.7.6.5", sha256="07166097d7dd45af7b98859654390d579d11dadf20780f6baca4bded3f55a580", url="https://pypi.org/packages/dc/e9/5060afcfad6e19f4725d59e64398e31ec9439863244b401cb3437becbbff/ppft-1.7.6.5-py2.py3-none-any.whl")
    version("1.6.6.4", sha256="473442cc6731856990bd25bd6b454bb98720007de4523a73c560bdd0060463d2", url="https://pypi.org/packages/6b/89/871fdf9f6b295559099de627d56e8a5d052d2654c80e249a71b10037f232/ppft-1.6.6.4.zip")
    version("1.6.6.3", sha256="1beab076fb9452fd729a9f1183e990d016fcd8ee67252f6897f3785d5b807a22", url="https://pypi.org/packages/95/a9/f6fcdbba44a8366f9da431a67af04f92ba150a88d7b7ef62bfd10a77fdac/ppft-1.6.6.3.zip")
    version("1.6.4.9", sha256="5537b00afb7b247da0f59cc57ee5680178be61c8b2e21b5a0672b70a3d247791", url="https://pypi.org/packages/a5/6c/16bdc13a8defc8ccab8b5c1a3dfb1331343b313f52984be0f4d6521eb92c/ppft-1.6.4.9.tar.gz")
    version("1.6.4.7.1", sha256="f94b26491b4a36adc975fc51dba7568089a24756007a3a4ef3414a98d7337651", url="https://pypi.org/packages/af/5c/1caaa791e4bd77a977692250b0fe5c14fc816576485c88e8ccf328f03fc9/ppft-1.6.4.7.1.zip")
    version("1.6.4.6", sha256="92d09061f5425634c43dbf99c5558f2cf2a2e1e351929f8da7e85f4649c11095", url="https://pypi.org/packages/d6/6b/dcd9898e6fa21cf708ce95b45eaa7ac867453ae104ec510c22d1365e8943/ppft-1.6.4.6.zip")
    version("1.6.4.5", sha256="800f4fbb797305a7f1074db22fe90618181ffe0a0c8212fe518bbaed831e78b6", url="https://pypi.org/packages/65/ec/0fd42f9c7496c5a4c4d244d49acc976ccb3ae276c314c0e525c1bcbe416d/ppft-1.6.4.5.tgz")

    with default_args(type="run"):
        depends_on("py-six@1.7.3:", when="@1.7:1.7.6.5")
