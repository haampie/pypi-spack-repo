##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytzDeprecationShim(PythonPackage):
    version("0.1.0.post0", sha256="8314c9692a636c8eb3bda879b9f119e350e93223ae83e70e80c31675a0fdc1a6", url="https://pypi.org/packages/eb/73/3eaab547ca809754e67e06871cff0fc962bafd4b604e15f31896a0f94431/pytz_deprecation_shim-0.1.0.post0-py2.py3-none-any.whl")
    version("0.1.0", sha256="4b4adc9952240b638de66a0a4d040050fcb8b48112619e38bbd58ead83de5506", url="https://pypi.org/packages/d3/99/8e6c2e788d301eba74fb911f2531f03e8064f9dbcd149ebb53ddef81fd4a/pytz_deprecation_shim-0.1.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-backports-zoneinfo", when="^python@:3.8")
        depends_on("py-tzdata")

