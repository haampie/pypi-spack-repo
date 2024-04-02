# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkQuicklookthumbnailing(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="34349ff0b07b39ecfe5757eb80341a45f9d4426558b93946225f8b4fa2781c4c", url="https://pypi.org/packages/b2/e7/ccb104c6068b076113634d0ee16e68f14eb1131f42106bcd8fd19672797d/pyobjc_framework_QuickLookThumbnailing-10.2-py2.py3-none-any.whl")
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

