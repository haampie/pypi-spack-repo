# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkLocalauthenticationembeddedui(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="eafbbc321082ff012cdb14e38abae7ced94c6d962cb64af43d6d515da976e175", url="https://pypi.org/packages/19/16/b0f47c5ee7e4fc102fcfc58679a2f156982682b431af5f8d22657c4f90ea/pyobjc_framework_LocalAuthenticationEmbeddedUI-10.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-localauthentication@10.2:", when="@10.2:")
    # END DEPENDENCIES

