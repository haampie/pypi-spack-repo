# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkDiscrecordingui(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="e0423c548851cd9eb4ad7e9e085da4db2cde2420e1f3e05d46e649498edf97d8", url="https://pypi.org/packages/1c/1c/b316298dd8e426af04bca9dffb4760a753d0abe3b6206534cbfd971e0a53/pyobjc_framework_DiscRecordingUI-10.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-discrecording@10.2:", when="@10.2:")
    # END DEPENDENCIES

