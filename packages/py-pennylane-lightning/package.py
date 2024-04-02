# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPennylaneLightning(PythonPackage):
    # BEGIN VERSIONS
    version("0.32.0", sha256="fc7e2e3432cf45ff739d8b0651263975c45a25ef78118d5fe1d5cd64155bc279", url="https://pypi.org/packages/99/a1/cda69a7bfad3733ed043e5378c1c7aaf2a5aa565151fe77f2f42255d1232/PennyLane_Lightning-0.32.0.tar.gz")
    version("0.31.0", sha256="8c8772a6a516ddeedf0b29b58a492f29b3aaf176fb9f89b678e001fe825898af", url="https://pypi.org/packages/12/98/fbcc98af988c4fdc2d4b01fe383f846caaebb309404c66f1c8f24a12b001/PennyLane-Lightning-0.31.0.tar.gz")
    version("0.30.0", sha256="e02615b8d89d970a5b4669faaf7ab29bdd58ed181b6f518fb325b27144f31e0c", url="https://pypi.org/packages/60/37/5f96dfc2d9cf01255aad9ece197b74f06064f2d1f0c10a6b47cf23d2af43/PennyLane-Lightning-0.30.0.tar.gz")
    version("0.29.0", sha256="d9cb0886f78c71923b6be2e0001ed368763af565f82e8fa529e3fe80425344cb", url="https://pypi.org/packages/ad/4b/4ba11d66fa3ac57655d6fd7b6cd0c0d9cab6ae9e077f0da62af11162ad49/PennyLane-Lightning-0.29.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("blas", default=False, description="blas")
    variant("build_type", default=False, description="build_type")
    variant("cppbenchmarks", default=False, description="cppbenchmarks")
    variant("cpptests", default=False, description="cpptests")
    variant("dispatcher", default=False, description="dispatcher")
    variant("generator", default=False, description="generator")
    variant("ipo", default=False, description="ipo")
    variant("kokkos", default=False, description="kokkos")
    variant("native", default=False, description="native")
    variant("openmp", default=False, description="openmp")
    variant("verbose", default=False, description="verbose")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

