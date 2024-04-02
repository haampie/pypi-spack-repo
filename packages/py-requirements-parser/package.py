# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRequirementsParser(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.5.0", sha256="e7fcdcd04f2049e73a9fb150d8a0f9d51ce4108f5f7cbeac74c484e17b12bcd9", url="https://pypi.org/packages/f8/89/612e3b326d87780dc1daf39af7696634f969838213cddae4f553f75d04ae/requirements_parser-0.5.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@:3", when="@0.3:")
        depends_on("py-types-setuptools", when="@0.4:")
    # END DEPENDENCIES

