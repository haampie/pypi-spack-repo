# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyZict(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.0.0", sha256="5796e36bd0e0cc8cf0fbc1ace6a68912611c1dbd74750a3f3026b9b9d6a327ae", url="https://pypi.org/packages/80/ab/11a76c1e2126084fde2639514f24e6111b789b0bfa4fc6264a8975c7e1f1/zict-3.0.0-py2.py3-none-any.whl")
    version("2.2.0", sha256="dabcc8c8b6833aa3b6602daad50f03da068322c1a90999ff78aed9eecc8fa92c", url="https://pypi.org/packages/a2/9d/e6b14a2627ead7692fcccbed526de1c88d026fd9e6332ddbd67b6a976401/zict-2.2.0-py2.py3-none-any.whl")
    version("2.1.0", sha256="3b7cf8ba91fb81fbe525e5aeb37e71cded215c99e44335eec86fea2e3c43ef41", url="https://pypi.org/packages/59/70/d184759f9d67182b048201a4b90bdce5ad44b373613ffbce169135f5d1d5/zict-2.1.0-py3-none-any.whl")
    version("2.0.0", sha256="26aa1adda8250a78dfc6a78d200bfb2ea43a34752cf58980bca75dde0ba0c6e9", url="https://pypi.org/packages/5a/65/0f743c740c30cace984ef8ff96fd1e991083fa884900a8aad3efff3252b9/zict-2.0.0-py3-none-any.whl")
    version("1.0.0", sha256="be8c7a24e3e78f871b72bfff16245105d1f0448606b1decdae054a14bfdf5996", url="https://pypi.org/packages/64/b4/a904be4184814adb9dfc2e679c4e611392080a32726a657a34cab93b38c2/zict-1.0.0-py2.py3-none-any.whl")
    version("0.1.4", sha256="d57434102b247719aeda1f543cb55d0ae7ab44f1e1a1f286e299164d1d40da58", url="https://pypi.org/packages/bd/45/a2e6f95a850cd407d785f2f8624b02e72baf6ab910aea4bdcac7e18b4871/zict-0.1.4-py2.py3-none-any.whl")
    version("0.1.3", sha256="c7fbbd9d93f9bb8f2dd85c680fa74abcb7d399d20a1640c2382a567eb5dc15e5", url="https://pypi.org/packages/5d/c9/eddd6c9a7ebd65fc799f9b87e56b45599a4e35d66e3da2722d7fc2a89f1f/zict-0.1.3-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-heapdict", when="@0.0.3:2")
    # END DEPENDENCIES

