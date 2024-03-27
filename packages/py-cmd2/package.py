##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCmd2(PythonPackage):
    version("2.4.3", sha256="f1988ff2fff0ed812a2d25218a081b0fa0108d45b48ba2a9272bb98091b654e6", url="https://pypi.org/packages/f3/9a/495a0577cbae4a11dc0b2a2174688f0bab83d1b81245a105f1613a365828/cmd2-2.4.3-py3-none-any.whl")
    version("2.4.2", sha256="a77e3056751393270b4125c990cf527db132f15951a20a3a5dd2df4290aadf20", url="https://pypi.org/packages/5c/21/80227985a8f4b66b5cb90cda0384841b475f507667e0e204f481a59f3038/cmd2-2.4.2-py3-none-any.whl")
    version("2.4.1", sha256="e6f49b0854b6aec2f20073bae99f1deede16c24b36fde682045d73c80c4cfb51", url="https://pypi.org/packages/5e/5a/a7f61b3fd99f07e95cb7a76357079aac5ace3c09c819164ecef7206c8c29/cmd2-2.4.1-py3-none-any.whl")
    version("2.4.0", sha256="6fe6d46099edaf4a99163c191aeb4babfd7e4dfbac6009f423ecc8370895b58f", url="https://pypi.org/packages/e5/66/df700c6d87abd0edf12468642b1a344b69e2e3fd92bc6025309c04b21778/cmd2-2.4.0-py3-none-any.whl")
    version("2.3.3", sha256="871713244c1f31defa3250149ba3ed071130be33bc755f39b84ae7ef6f721951", url="https://pypi.org/packages/8c/0b/3d6c9940c81b55750cda9aa941599161e62678bd6baaea9863b5c75ad42b/cmd2-2.3.3-py3-none-any.whl")
    version("2.3.2", sha256="6bd0d181b7a4b01ad82bc542b000d384a69b224ee695748a30e78d1d52070aca", url="https://pypi.org/packages/00/07/6c5c0ce0647b0054b7ec459036497565f66b55ff5809934792917e161a3c/cmd2-2.3.2-py3-none-any.whl")
    version("2.3.1", sha256="9df7400aadb3f8f65d12665eb8c9dc86b03a08d93599c7f7cb0b71f945759afc", url="https://pypi.org/packages/9d/21/44af97ab1ffa56279a74a428ea5b7141ef85fb3c6775851e5116e3d4505b/cmd2-2.3.1-py3-none-any.whl")
    version("2.3.0", sha256="97a7dffbb2c4a9e94b7ded51322878ae824896abacabd408644e986cd1966709", url="https://pypi.org/packages/a9/29/98644975387d34d50980694173552f15f18f967e3959a487e46c737c0473/cmd2-2.3.0-py3-none-any.whl")
    version("2.2.0", sha256="d2f75a0f8712541d6a31e46fe5d5a33cff719bd676c4b5ef2201e1c9dc4ccfac", url="https://pypi.org/packages/99/84/14429a401f70d8b722116a4dfdd9e0be65353e6fb19b39c044d18ad259a6/cmd2-2.2.0-py3-none-any.whl")
    version("2.1.2", sha256="d967708a62d1166c3a7f55c630e74d4680bed425f68a13d07ce2a1b45a38da1c", url="https://pypi.org/packages/44/ca/d407811641ec1d8bd8a38ee3165d73aa44776d7700436bd4d4a6606f2736/cmd2-2.1.2-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-attrs@16.3:", when="@0.9.5:")
        depends_on("py-colorama@0.3.7:", when="@0.9.15:2.2")
        depends_on("py-pyperclip@1.6:", when="@0.9.15:")
        depends_on("py-pyreadline3", when="@1.5: platform=windows")
        depends_on("py-wcwidth@0.1.7:", when="@0.9.6:")

