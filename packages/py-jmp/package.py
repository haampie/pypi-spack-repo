# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJmp(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.0.4", sha256="6aa7adbddf2bd574b28c7faf6e81a735eb11f53386447896909c6968dc36807d", url="https://pypi.org/packages/27/e5/cce82de2831e5aff9332d8d624bb57188f1b2af6ccf6979caf898a8a4348/jmp-0.0.4-py3-none-any.whl")
    version("0.0.3", sha256="1934bd2de39f6d9dd90ba9fdbd3cbfc596028b03357b29ec030106f6e86927b3", url="https://pypi.org/packages/50/d1/ce0b1388199af93c0b15844b87c56aa9e43cec9591f731bf37c7aac94071/jmp-0.0.3-py3-none-any.whl")
    version("0.0.2", sha256="48f94b2ba0c9db759851a23cce2fbfa622e954c3c811651bc11b196246f02527", url="https://pypi.org/packages/ff/5c/1482f4a4a502e080af2ca54d7f80a60b5d4735f464c151666d583b78c226/jmp-0.0.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.19.5:", when="@0.0.2:")
    # END DEPENDENCIES

