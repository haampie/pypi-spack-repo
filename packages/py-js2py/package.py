# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJs2py(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.74", sha256="40a508a79e2f8d624e3f2e604f90a1e6f46ac75b416d7f4745939ff4a2e95e09", url="https://pypi.org/packages/88/58/2feb430d47c9f18f331494b429697342722b51f28dad8ad92a511c0f6fc8/Js2Py-0.74-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyjsparser@2.5.1:", when="@0.51:")
        depends_on("py-six@1.10:", when="@0.51:")
        depends_on("py-tzlocal@1.2:", when="@0.51:")
    # END DEPENDENCIES

