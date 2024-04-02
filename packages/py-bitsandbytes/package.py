# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBitsandbytes(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.42.0", sha256="63798680912cc63bb77b535a2d0860af024e290a52e157f777ad2a52e2585967", url="https://pypi.org/packages/9b/63/489ef9cd7a33c1f08f1b2be51d1b511883c5e34591aaa9873b30021cd679/bitsandbytes-0.42.0-py3-none-any.whl")
    version("0.41.0", sha256="dfaebbdcf48bff6628ca04880877a10b4da61e4fff62cdd3433764b1571ab3d1", url="https://pypi.org/packages/b9/33/1cea2d1c909dd3e2b595f7b73c4417f3786c385a4b269a5c40c7699bb14b/bitsandbytes-0.41.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-scipy", when="@0.42:")
    # END DEPENDENCIES

