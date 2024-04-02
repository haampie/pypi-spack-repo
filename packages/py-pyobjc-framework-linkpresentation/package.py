# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkLinkpresentation(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="1cada96d3eb03e51e1bbb7e7c10b9c08c80fd098132541b4e992234fe43cfa37", url="https://pypi.org/packages/a3/8c/bb2eee65472555c821297871c36100296964e80ca3db5eda8740e5b80dbf/pyobjc_framework_LinkPresentation-10.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
    # END DEPENDENCIES

