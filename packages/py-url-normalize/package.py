# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyUrlNormalize(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.4.3", sha256="ec3c301f04e5bb676d333a7fa162fa977ad2ca04b7e652bfc9fac4e405728eed", url="https://pypi.org/packages/65/1c/6c6f408be78692fc850006a2b6dea37c2b8592892534e09996e401efc74b/url_normalize-1.4.3-py2.py3-none-any.whl")
    version("1.4.2", sha256="1bd7085349dcdf06e52194d0f75ff99fff2eeed0da85a50e4cc2346452c1b8bc", url="https://pypi.org/packages/6d/6f/ea35e59b39a007c3c242038490dd6ac21cb3570ccbf397a4396fe58bf2ad/url_normalize-1.4.2-py2.py3-none-any.whl")
    version("1.4.1", sha256="51e0f14050c79e732d175c33d12167f5e642cc23e0cb23275236af843faf884f", url="https://pypi.org/packages/e2/12/47dc7437c13ddc648b796deec34cca14841dc193131f7be215baea3e9b2f/url_normalize-1.4.1-py2.py3-none-any.whl")
    version("1.4.0", sha256="61a28f7aa7ed7825764c57b64d977eba04a9da7ec5e3564dea6671acd61e4ac3", url="https://pypi.org/packages/82/26/389f2d3424f52fb3e858235f7a35d8ebcc9ebefab449078f9ab4e996c795/url_normalize-1.4.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six", when="@1.4.3:")
        depends_on("py-six@1.11:", when="@1.4:1.4.2")
    # END DEPENDENCIES

