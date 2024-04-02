# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkIntents(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="ec27d5d19212fcec180ff04e2bc617fee0a018e2eaf29b2590c5512da167aa6a", url="https://pypi.org/packages/bf/26/f36e7e0f0078b5b2667e76afb7f9df36778a3db80252c0c4440be309d374/pyobjc-framework-Intents-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

