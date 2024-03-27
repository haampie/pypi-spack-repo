##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkVideosubscriberaccount(PythonPackage):
    version("10.2", sha256="300c9f419821aab400ab9798bed9fc659984f19eb8577934e6faae0428b89096", url="https://pypi.org/packages/13/81/9b32994d20adbb9f3ce8ce5764bbcb4f9bc5d872e2d44ba7aac5c74f2ad3/pyobjc_framework_VideoSubscriberAccount-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="f32716070f849989e3ff052effb54f951b89a538208651426848d9d924ac1625", url="https://pypi.org/packages/f1/73/a595029be9e5b3dd79d2433cd276cf4651f3e9e4e8b73a52fb91f83e2354/pyobjc_framework_VideoSubscriberAccount-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="d7616cc2302372211a415e5afb83f3b52b9582b2f1381ba83b0cf955180ca2ba", url="https://pypi.org/packages/7b/1a/ee6e6ea9a41f3fd6014f44078bdb8c83857b5558e68098b999fb5b1415fe/pyobjc_framework_VideoSubscriberAccount-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="28bae8cb13dea6289e62e185b7526f4505e10f3cea56c21cd4861aa6bfa0bcbe", url="https://pypi.org/packages/17/bb/40875a825d291abf6a718ea8c8c6dd28a4a9155d82ab217d19faaf69305f/pyobjc_framework_VideoSubscriberAccount-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="a317d4d8fbec32fd0644c1e3f20a94359150880950ccce35799e8ecb02f018a7", url="https://pypi.org/packages/f3/a6/137cb9ddd5cc9ffdc25fd53df48504a4ad4a81fdc3ed55e800d1432886e7/pyobjc_framework_VideoSubscriberAccount-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="319d3cb2969efb13cf469ace1394acd5089461421cca9f126b9705eada194b3f", url="https://pypi.org/packages/5b/03/96b34dd756bbc474d1b8b59422dd85fbc217ea3d23773801a41b8ef1e926/pyobjc_framework_VideoSubscriberAccount-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="4a40c908d8590a75bf71006df7429c3cbe8f4a3ccbbab8e56b6d09ad92ac1b9e", url="https://pypi.org/packages/6a/46/834c831d5e76caddaa9fc18d94610ab67e9b30d93aba6a31dc9e79fca268/pyobjc_framework_VideoSubscriberAccount-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="7cc1f988169e3fe3abcbdfe936d30f3454f680b47f6fee1271443740f0c3a30c", url="https://pypi.org/packages/99/fd/f4f82bd862dff73750e5f239470063ea95f621b02e7317039cbf9bcae2de/pyobjc_framework_VideoSubscriberAccount-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="d46a3fefdcc204faa41ab96a7c7778426594c8d02a2b32b2a7bf41aafb423c75", url="https://pypi.org/packages/bb/0c/9446080c42dedf104cc7286a04138abb2c9157da6cb52be75f2399ad9e70/pyobjc_framework_VideoSubscriberAccount-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="08b355939a2d595a0864cccc2693933159b3956deef3e1e24d3c55413ca297b9", url="https://pypi.org/packages/2f/fc/c62a7a490ffaade30aca092ab55629740bcb3aca0599a11eedd7ca5cdc19/pyobjc_framework_VideoSubscriberAccount-8.5-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-core@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-core@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-core@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-core@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-core@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-core@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-core@8.5:", when="@8.5:8.5.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-cocoa@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-cocoa@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-cocoa@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-cocoa@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-cocoa@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-cocoa@8.5:", when="@8.5:8.5.0")

