# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkDictionaryservices(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="39b577b35c52a033cbac030df1fdcd16fb109144e8c59cb2044a13fcd803ab49", url="https://pypi.org/packages/b7/41/d6a796ce075c36770d80cd89c8820fb37f6b84efa214b394a9ad5006c81c/pyobjc_framework_DictionaryServices-10.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coreservices@10.2:", when="@10.2:")
    # END DEPENDENCIES

