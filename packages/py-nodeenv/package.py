# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNodeenv(PythonPackage):
    # BEGIN VERSIONS
    version("1.8.0", sha256="df865724bb3c3adc86b3876fa209771517b0cfe596beff01a92700e0e8be4cec", url="https://pypi.org/packages/1a/e6/6d2ead760a9ddb35e65740fd5a57e46aadd7b0c49861ab24f94812797a1c/nodeenv-1.8.0-py2.py3-none-any.whl")
    version("1.7.0", sha256="27083a7b96a25f2f5e1d8cb4b6317ee8aeda3bdd121394e5ac54e498028a042e", url="https://pypi.org/packages/96/a8/d3b5baead78adadacb99e7281b3e842126da825cf53df61688cfc8b8ff91/nodeenv-1.7.0-py2.py3-none-any.whl")
    version("1.3.3", sha256="ad8259494cf1c9034539f6cced78a1da4840a4b157e23640bc4a0c0546b0cb7a", url="https://pypi.org/packages/00/6e/ed417bd1ed417ab3feada52d0c89ab0ed87d150f91590badf84273e047c9/nodeenv-1.3.3.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@1.7:")
        depends_on("py-setuptools", when="@1.7:")
    # END DEPENDENCIES

