##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyVistir(PythonPackage):
    version("0.8.0", sha256="7b8d2301c860707a7a7f02c457eef685b9711470a6df157b692baf529606622f", url="https://pypi.org/packages/3d/9c/2efda79e5086d25befc7618b61c8bfa52230bff532572d24202af98d8adc/vistir-0.8.0-py2.py3-none-any.whl")
    version("0.7.5", sha256="116bf6e9b6a3cf72100565ee303483abd821b7f67bba25d57df01a0f49e46bec", url="https://pypi.org/packages/70/98/400bb033da0fa667f5f396cb73200aa827d1c4ef9eb3d272e270325c0c1a/vistir-0.7.5-py2.py3-none-any.whl")
    version("0.7.4", sha256="bd469cbfd078298019997de464c728f422d01820d0e3374e8fdfd99277d6fbe6", url="https://pypi.org/packages/0b/cd/f5d01e227709b9f8b39948b2e4dee3a3c58e01622a0bc9f0abf4227fb648/vistir-0.7.4-py2.py3-none-any.whl")
    version("0.6.1", sha256="1a89a612fb667c26ed6b4ed415b01e0261e13200a350c43d1990ace0ef44d35b", url="https://pypi.org/packages/63/4f/26201aada1255209517b405f399aa9e5c46e7a9011b5504a69eb44803b66/vistir-0.6.1-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-colorama@0.3.4:0.4.1,0.4.3:", when="@0.5:")
        depends_on("py-requests", when="@:0.4")
        depends_on("py-yaspin", when="@0.1.5")

