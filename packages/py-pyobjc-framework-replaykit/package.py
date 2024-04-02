# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkReplaykit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="12544028e59ef25ea5c96ebd451cee70d1833d6b5991d3a1b324c6d81ecfb49e", url="https://pypi.org/packages/69/0e/b618ccb5ffb028ea72d3fd0374d52c24cbbd1540d1a02ffdf8b4272890ed/pyobjc-framework-ReplayKit-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

