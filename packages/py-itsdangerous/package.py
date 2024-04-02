# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyItsdangerous(PythonPackage):
    # BEGIN VERSIONS
    version("2.1.2", sha256="2c2349112351b88699d8d4b6b075022c0808887cb7ad10069318a8b0bc88db44", url="https://pypi.org/packages/68/5f/447e04e828f47465eeab35b5d408b7ebaaaee207f48b7136c5a7267a30ae/itsdangerous-2.1.2-py3-none-any.whl")
    version("2.0.1", sha256="5174094b9637652bdb841a3029700391451bd092ba3db90600dea710ba28e97c", url="https://pypi.org/packages/9c/96/26f935afba9cd6140216da5add223a0c465b99d0f112b68a4ca426441019/itsdangerous-2.0.1-py3-none-any.whl")
    version("1.1.0", sha256="b12271b2047cb23eeb98c8b5622e2e5c5e9abd9784a153e9d8ef9cb4dd09d749", url="https://pypi.org/packages/76/ae/44b03b253d6fade317f32c24d100b3b35c2239807046a4c953c7b89fa49e/itsdangerous-1.1.0-py2.py3-none-any.whl")
    version("0.24", sha256="cbb3fcf8d3e33df861709ecaf89d9e6629cff0a217bc2848f1b41cd30d360519", url="https://pypi.org/packages/dc/b4/a60bcdba945c00f6d608d8975131ab3f25b22f2bcfe1dab221165194b2d4/itsdangerous-0.24.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@2.1:")
    # END DEPENDENCIES

