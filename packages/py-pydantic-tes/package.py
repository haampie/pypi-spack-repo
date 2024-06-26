# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPydanticTes(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.1.5", sha256="7acf9b206ed3351a15731937976957d560194858ff2f316ea6039e1cb694663a", url="https://pypi.org/packages/e9/d0/cfd25f895c611dc07c2d17926edfedbed65938a04fd32b013a101fe9b8b1/pydantic_tes-0.1.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pydantic")
        depends_on("py-requests")
        depends_on("py-typing-extensions")
    # END DEPENDENCIES

