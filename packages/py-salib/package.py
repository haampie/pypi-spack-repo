# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySalib(PythonPackage):
    # BEGIN VERSIONS
    version("1.4.4", sha256="8179bc98f2fdaf4b5bad39a3d6680ee86fd68bde37dcedc8d6e49403c384800a", url="https://pypi.org/packages/50/88/5a002f70bbd70db57313ca63bcd99f699a435b08efd74e43e7989cf8b7a5/SALib-1.4.4-py2.py3-none-any.whl")
    version("1.4.0.1", sha256="dbf6e865af9f3be82a79cf64889ed66d6d3b6803f0c22a242a112876789d49e7", url="https://pypi.org/packages/ea/97/35ff17688b065dce5220af6c6f7bbff6ef07843169b4e706dd6d107fa9c9/SALib-1.4.0.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-matplotlib", when="@:0.0,1.4.1:1.4.6-beta1")
        depends_on("py-numpy", when="@:0.0,1.4.1:1.4.6-beta1")
        depends_on("py-pandas", when="@:0.0,1.4.1:1.4.6-beta1")
        depends_on("py-pathos", when="@:0.0,1.4.1:1.4.6-beta1")
        depends_on("py-scipy", when="@:0.0,1.4.1:1.4.6-beta1")
        depends_on("py-setuptools", when="@:0.0,1.4.1:1.4.6-beta1")
        depends_on("py-wheel", when="@:0.0,1.4.1:1.4.6-beta1")
    # END DEPENDENCIES

