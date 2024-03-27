##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSensitivecontentanalysis(PythonPackage):
    version("10.2", sha256="3c875856837e217c9eba68e5c2b4f5b862dee1bb64513b463a7af8c3e67e5a50", url="https://pypi.org/packages/b9/5a/8786ea5a089a00820c423f4cfe9599fbef26b284b491c7bf344646e482ea/pyobjc_framework_SensitiveContentAnalysis-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="472c0fb0f1ad9c370cbc7cf636bb5888cbcf0ee8c9ecb9c5f6de25e2587771e5", url="https://pypi.org/packages/33/e7/1fbbd00034fb5d5872609442e063f39fbf54a2daf671f8b9c5117754e49c/pyobjc_framework_SensitiveContentAnalysis-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="99262f5d8a049973531a44113e9157874bba274ed8541b8b778878c664472042", url="https://pypi.org/packages/b5/11/43794b10d4a86a743309943ae6847d7caea6c3dd0f45de98d08fe065e9bd/pyobjc_framework_SensitiveContentAnalysis-10.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@:10.0")
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-quartz@10:", when="@:10.0")

