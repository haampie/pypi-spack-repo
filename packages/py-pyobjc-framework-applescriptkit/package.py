##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkApplescriptkit(PythonPackage):
    version("10.2", sha256="15af7d97f017563ff3771127a2b7c515496aa6083497415cbe8c27dd5811c50f", url="https://pypi.org/packages/86/24/8755153c7278aba29c434d0b3020b75a47dbb04fa27d3b0f3339bf7e62e5/pyobjc_framework_AppleScriptKit-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="b88bc8ae9e000d382c3e1d72b3c4f39499323fbe88cc84af259925448c187387", url="https://pypi.org/packages/38/96/e815ab0f0d52632e9128b48351809174aa1b7f75573caa8f70174162ca1b/pyobjc_framework_AppleScriptKit-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="567123701b86833118236f0177ce7979cd91be5c2d0fe26afb7b73499812f673", url="https://pypi.org/packages/e1/a4/0a9ffbdfa6bcb57956dbe917ea730a5bc42dbecf067d119ae8dd58d91901/pyobjc_framework_AppleScriptKit-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="e7be610629371efc96b2daf8b83fee814251ce0845d8cfd4cc458a69bd67e6fb", url="https://pypi.org/packages/c6/29/0152a476db6c9cd55b54b6c6f3e8b855fab4e698e8b8428b78757831fb7e/pyobjc_framework_AppleScriptKit-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="d83c2362edbc5be22a89fc465d698aa113a0f201d3d3c2cb7b63478cd1e7220b", url="https://pypi.org/packages/c9/25/02f021fa047518fccf0914e079c00130e31cb7991df599f6fb4cbc6181a8/pyobjc_framework_AppleScriptKit-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="a0130fc95f4897a6690da15830cb24f7c99dbc33baf66ecf9e5da823a764c9ff", url="https://pypi.org/packages/5e/41/8f3434d4c458aa99862381e271d4ee8ee55ecf00a9084c15c3acd11f108e/pyobjc_framework_AppleScriptKit-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="276ece60cae045351496295cf9f1491c80be76c92e25642eb99db828190b6ee6", url="https://pypi.org/packages/20/30/1d39a33cc7eea1946143408224c878433f7ce7795957d9fc0162821b452f/pyobjc_framework_AppleScriptKit-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="c3af04805370f8b51c0e8e4edee24a1b45fd56250712072deb99eb5447d4ba79", url="https://pypi.org/packages/c8/22/fbf2ae9f57d07037451a251922f33c1dad61cefcc774cc4e0e1b31ab93c0/pyobjc_framework_AppleScriptKit-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="13ce8f0c4f9fa45335c3b60494eb513b9fcf7271d89c02c58ecddd0e52a75a26", url="https://pypi.org/packages/e2/0a/ceb110579ecbf90f6994eddacf6b8b7637dca90aa79e1842556900090f51/pyobjc_framework_AppleScriptKit-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="1740850a3e970ec2a119658d4c00d1cd4c4f6aab16f4d0a08b093f78e2615a97", url="https://pypi.org/packages/0e/4a/8dedbb1b7e85812d5f3c47bef64eb0d5103dd78f652edec4a548b96404ea/pyobjc_framework_AppleScriptKit-8.5-py2.py3-none-any.whl")

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

