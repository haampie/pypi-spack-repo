# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyClickRepl(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.3.0", sha256="fb7e06deb8da8de86180a33a9da97ac316751c094c6899382da7feeeeb51b812", url="https://pypi.org/packages/52/40/9d857001228658f0d59e97ebd4c346fe73e138c6de1bce61dc568a57c7f8/click_repl-0.3.0-py3-none-any.whl")
    version("0.2.0", sha256="94b3fbbc9406a236f176e0506524b2937e4b23b6f4c0c0b2a0a83f8a64e9194b", url="https://pypi.org/packages/9b/33/15f401400cc0cf2470aa777d225e772f83a68541495e015d2fa5c77d33d0/click_repl-0.2.0-py3-none-any.whl")
    version("0.1.6", sha256="9c4c3d022789cae912aad8a3f5e1d7c2cdd016ee1225b5212ad3e8691563cda5", url="https://pypi.org/packages/6c/4e/577214ee76a5a36af485ae9ec01b4a47ee607b5d413b2063dafccf41f3ad/click_repl-0.1.6-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-click@7:", when="@0.3:")
        depends_on("py-prompt-toolkit@3.0.36:", when="@0.3:")
    # END DEPENDENCIES

