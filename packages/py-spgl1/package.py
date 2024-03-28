# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySpgl1(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.0.2", sha256="16ddc94a46a574855c605af13f0702b6bc5ccae1208c0685a83226324467226d", url="https://pypi.org/packages/17/8e/143c7c424c8c9e8e1ce5f080430b8ec875143dcb00ec9d6edfc1e03efb1c/spgl1-0.0.2-py3-none-any.whl")
    version("0.0.1", sha256="5b848cd7ab744a50f367587cf001aa50ce3ea255406cb0f85ad6cd570160ed06", url="https://pypi.org/packages/31/be/cd07d566e2e4ea4634c78e40aed9e69ae3fbf2010df6ba0d59307174db9c/spgl1-0.0.1-py3-none-any.whl")
    version("0.0.0", sha256="89422f8d1a012713606f2035cae9a2138d6c0ffb23a70e8efd89c85c702790d2", url="https://pypi.org/packages/a0/1e/7c665ceb688fe87a5b37aa9f987c40a7cf1e1a2b605b7f4ee2a4195e02be/spgl1-0.0.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.15.0:")
        depends_on("py-scipy")
    # END DEPENDENCIES

