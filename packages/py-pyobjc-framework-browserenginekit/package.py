##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkBrowserenginekit(PythonPackage):
    version("10.2", sha256="a47648e62d3482d39179ffe51543322817dd7a639cef9dcd555dfcc7d6a6497f", url="https://pypi.org/packages/bb/ff/a8c2f336ab96f4fb1f7685df468304ce62f91395a9fcc56e37c69f8eb5d2/pyobjc-framework-BrowserEngineKit-10.2.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:")
        depends_on("py-pyobjc-framework-coreaudio@10.2:")
        depends_on("py-pyobjc-framework-coremedia@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.2:")

