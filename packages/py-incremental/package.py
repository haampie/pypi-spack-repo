##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyIncremental(PythonPackage):
    version("22.10.0", sha256="b864a1f30885ee72c5ac2835a761b8fe8aa9c28b9395cacf27286602688d3e51", url="https://pypi.org/packages/77/51/8073577012492fcd15628e811db585f447c500fa407e944ab3a18ec55fb7/incremental-22.10.0-py2.py3-none-any.whl")
    version("22.10.0-rc1", sha256="0c2628cc71b81fd011a8e7385e5bf44d64eebe6a1940af0cc99bcc8ed8221c9e", url="https://pypi.org/packages/57/45/adb9659cd3e47d55dad9bf2be35ff19d6eb55463bd2e4bcb0136f8abecf2/incremental-22.10.0rc1-py2.py3-none-any.whl")
    version("21.3.0", sha256="92014aebc6a20b78a8084cdd5645eeaa7f74b8933f70fa3ada2cfbd1e3b54321", url="https://pypi.org/packages/99/3b/4f80dd10cb716f3a9e22ae88f026d25c47cc3fdf82c2747f3d59c98e4ff1/incremental-21.3.0-py2.py3-none-any.whl")


