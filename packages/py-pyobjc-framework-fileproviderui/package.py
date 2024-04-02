# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkFileproviderui(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="5fac2067c09a23a436708e05d71faf65d64f4c36b45ad254617720b1a682aad6", url="https://pypi.org/packages/b3/a4/be98b494eab0288487110cf1be54b379d883b834926e7fd44bf57d6e4027/pyobjc_framework_FileProviderUI-10.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-fileprovider@10.2:", when="@10.2:")
    # END DEPENDENCIES

