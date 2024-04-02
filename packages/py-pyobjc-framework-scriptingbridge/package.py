# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkScriptingbridge(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="c02d88b4a4d48d54ce2260f5c7e1757e74cd91281352cdd32492a4c7ee4b0e7c", url="https://pypi.org/packages/7a/b5/12685787d801a53cdd535ef71487b0b0bd9dca937a6a106f0e8a3a908b66/pyobjc-framework-ScriptingBridge-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

