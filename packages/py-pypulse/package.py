##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPypulse(PythonPackage):
    version("0.1.1", sha256="df72d572772f5d31828238f762871172b8888516c4a15c0a56b54a647484db96", url="https://pypi.org/packages/d1/75/2d2450cd511f8ec2bb3a7f2c753f472f7dbde4d587d9bbba7000dbf3191c/PyPulse-0.1.1-py3-none-any.whl")
    version("0.0.1", sha256="239823737644bdf1e09e23e81b3fc439db096aa589581d9fa2b5717f1572e75b", url="https://pypi.org/packages/df/cd/599f92848d4f01e22b479127b07bccc5324304c153dac3e6af5e75be0b36/PyPulse-0.0.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-astropy", when="@0.1:")
        depends_on("py-matplotlib", when="@0.1:")
        depends_on("py-numpy", when="@0.1:")
        depends_on("py-scipy", when="@0.1:")

