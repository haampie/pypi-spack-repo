##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSymbols(PythonPackage):
    version("10.2", sha256="3b5fa1e162acb04eab092e0e1dbe686e2fb61cf648850953e15314edb56fb05f", url="https://pypi.org/packages/f6/6a/214e0e0148892384dcab861884ba2b3081cd2e69ad2d3b4b1fb2ed6c5aac/pyobjc_framework_Symbols-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="88b48102ba33ac3d8bc5c047cc892ab21e8e102c3b25b4186b77c5d1f5c1bc40", url="https://pypi.org/packages/af/d9/a9cb45ebc811172a597238c545ec2b13d8c78e45565271491fee413e126e/pyobjc_framework_Symbols-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="fd1bfc2958d860aef26b15994714abcbb6b3340eda2c67df31c12df0740a661f", url="https://pypi.org/packages/41/c4/cd1be96ae9b6a212a446fc678fbd495840343a46077fdb514a20cee6d13c/pyobjc_framework_Symbols-10.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@:10.0")

