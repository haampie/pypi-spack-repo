##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGmxapi(PythonPackage):
    version("0.4.2", sha256="c746c6498c73a75913d7fcb01c13cc001d4bcb82999e9bf91d63578565ed1a1f", url="https://pypi.org/packages/11/49/9d7e072de7918c28d02dd39c2ab83d0c3cd1176acd0bf8d2f9d18c4fa0aa/gmxapi-0.4.2.tar.gz")
    version("0.4.1", sha256="cc7a2e509ab8a59c187d388dcfd21ea78b785c3b355149b1818085f34dbda62a", url="https://pypi.org/packages/96/d2/fecfa126eca62f87bc100834ca7fe856ead4b5e50553c27be6ee9395c550/gmxapi-0.4.1.tar.gz")
    version("0.4.0", sha256="7fd58e6a4b1391043379e8ba55555ebeba255c5b394f5df9d676e6a5571d7eba", url="https://pypi.org/packages/4d/f9/12d6e204f1d7fa466dd6093ea3c575f34d527605ec369795f261d02827e0/gmxapi-0.4.0.tar.gz")

    with default_args(type="run"):
        depends_on("python@:3.8", when="@0.1.0-beta2:0.2.0-alpha1")

