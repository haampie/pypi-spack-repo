##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSoundanalysis(PythonPackage):
    version("10.2", sha256="a09b49acca76a3c161b937002e5d034cf32c33d033677a8143d446eb53ca941d", url="https://pypi.org/packages/ef/b6/56ce4f7d31a142f7c10fba19cec190d6be4c1e85bcff659f39f3bd4b967d/pyobjc_framework_SoundAnalysis-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="a33bc8a1ecee11387beb9db06aaf9c362f7dc171d60da913277ac482d67beabb", url="https://pypi.org/packages/46/10/e31c8a22c5a58a8186f011bb7cefed55fb55e4280f1226be4d68c86e40e0/pyobjc_framework_SoundAnalysis-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="b2de7dc4ee724fc7940a777ee50aa8b96b836aade84a408737bacf8818b9bde5", url="https://pypi.org/packages/c3/00/a7d6c8145ce6688efe412f34f1624f03d0bc12b0b2518b3a9f9aaecd8526/pyobjc_framework_SoundAnalysis-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="b15ef2f3eff025ca569543a5363e3c541de979fb234fbe4132fbe2b484cabf63", url="https://pypi.org/packages/c6/27/a22021c901e08e6be4836b5e14724fe5fa8f2fc421f59a88a42716258b7e/pyobjc_framework_SoundAnalysis-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="046bb27375bda0699ce897c6e62b5411989a9fc0949bf0914b8b4040b98c5221", url="https://pypi.org/packages/bf/b2/0ae132924e5066d4a2603780845c765b72226f373fbca52817f9f272dc4c/pyobjc_framework_SoundAnalysis-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="8896f52fc387188c56dcc3311eae5a256d1718b96e07282ca2784011862ed5c8", url="https://pypi.org/packages/1e/6f/278ed76d9680004739c54cdda39d1700d1b9508ae383ead3a0127d51c385/pyobjc_framework_SoundAnalysis-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="580135eedaf10b64721e4fc0120c1f8a1cbcb1398fff1656dabf573819a9a24c", url="https://pypi.org/packages/60/48/937441b4e81ea2e60d8049e454f0baf197a91ce6f1ced09bc8edc832ba03/pyobjc_framework_SoundAnalysis-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="7e2de66e74bb1207018a7d9bd8d8fd4deec4f3ee8f5ce056838ef5f0b2f47d2a", url="https://pypi.org/packages/dc/93/21282c2772785d861f74fc25d1c4da4d50ffb2d6c3ab6ad5f8236222c3b2/pyobjc_framework_SoundAnalysis-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="daf3ac5a11d3450ca1ced2b92866829399593298b3a0252aabaaed64ead63e4b", url="https://pypi.org/packages/a8/30/e2dc7c5659160959713756cec8241462309192edf7ee81b1583c615bc47c/pyobjc_framework_SoundAnalysis-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="edb1dc1f980578b633166599704f545218aea4ab4f4cf00252958cc1082de91d", url="https://pypi.org/packages/28/2d/0e39fb6b730963326e9ee33aad705c8dff4a4c5db5c2c8a1ba85fed960dc/pyobjc_framework_SoundAnalysis-8.5-py2.py3-none-any.whl")

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

