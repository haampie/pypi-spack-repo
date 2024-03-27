##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkItuneslibrary(PythonPackage):
    version("10.2", sha256="4e6cf6073a902f77e0b0c33d2d52e3ab3f0c869cb339b7685b5e7f079df8ef4e", url="https://pypi.org/packages/d0/69/58e9d5ebe7fae6d90941b7ab1530fd9a936b37f1b5483f432d3bd334a86d/pyobjc_framework_iTunesLibrary-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="043a2ede182f41a3ca70be50bf95f18641e2945f0077797ff2bb42a3e1984e37", url="https://pypi.org/packages/67/fd/8af71c9f0f5c04797044df3e6a6e8816bf63a27283b69f29d577e9bb4bbb/pyobjc_framework_iTunesLibrary-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="2d3d8457f9ba6bf415535263dee6973e468f140b04b3cf436481551a25c8f07f", url="https://pypi.org/packages/d5/0f/5bb949f372122f5a76017dfea96f3e4aa3c96a65c7b552770af18d1b8a95/pyobjc_framework_iTunesLibrary-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="1403c9c42eb4795590070e9128c6df91cee6e1dc82ac847787d32468edc69b23", url="https://pypi.org/packages/74/20/cb3b4319f8ea65716c7b0ca64480b04dbe675077b026ee0fe4bd4d8465f2/pyobjc_framework_iTunesLibrary-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="be6ba8719826490be261c472730df22995114bdc23b3d2fcc4427e6abdda7546", url="https://pypi.org/packages/c3/ca/19c8cef34bb365731b370eebf959ecd7649713baa31ae274ff8a0b5a5667/pyobjc_framework_iTunesLibrary-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="0343025b5f561a00f42ed01fbc2cb8df3009cb225e347966e3923fe2832d6f01", url="https://pypi.org/packages/ea/ac/7c543d8ee39a5b6f24b086dcb898150a986a6ee90540c1759fc6958ba41b/pyobjc_framework_iTunesLibrary-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="f6400c9fc73308d00a171397875562f1b2cb1d6d999790fc5213f341083df8b9", url="https://pypi.org/packages/7c/3b/f6baf9f0e6ed9f2f33222511cda3893f2220aa4ba182880d778b98600166/pyobjc_framework_iTunesLibrary-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="c51af741bd1231493f8a318bbdf29aece34a4261462d55ce47d53de947eb0605", url="https://pypi.org/packages/1f/e5/0a5b81d3dd5700319825ec52ec4733cb40c699c5b306e7ec3db59865886e/pyobjc_framework_iTunesLibrary-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="f697815661ec04e5a5a06d61561e16c16a61bc9f2feda39de051ee826e8f6feb", url="https://pypi.org/packages/96/0d/66b3553419b33381eabcdf4ec3c401ff5a3c050845bf111afee5ad698e7c/pyobjc_framework_iTunesLibrary-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="972d814cca7821c5b00008065e3184fee92bf75a22115b4929d0af152012d20a", url="https://pypi.org/packages/cf/63/13a9d40e6bb5e3cca5e77aca78ba4b85430c3d61d5e162a36c9cc00c5ed6/pyobjc_framework_iTunesLibrary-8.5-py2.py3-none-any.whl")

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

