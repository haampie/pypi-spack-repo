# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFenicsBasix(PythonPackage):
    # BEGIN VERSIONS
    version("0.7.0.post0", sha256="108fce5bd3858754dcf49c8ef071949456fe971bb99e66d5896a2eff0573954a", url="https://pypi.org/packages/6e/fb/5869a4fbcc318f08b06c08ee33085d2f68f7c10520141d43cd31bb7db93e/fenics_basix-0.7.0.post0.tar.gz")
    version("0.6.0", sha256="c933d6b5f903584959788a84a7f9bea3e8542743a13cb6e4e6466434fe0f6581", url="https://pypi.org/packages/67/d1/08bd442f122e1e535dc17e788a6ed4b875b320d91ac15287ab05f5bb2ac1/fenics-basix-0.6.0.tar.gz")
    version("0.5.0", sha256="5dace846ebb769e14e70fe42c8d1648ab108e9f9ca6e4bd8559e564f569e7433", url="https://pypi.org/packages/dc/1c/e84f268888ae85dd9f07f06bb1303c03d07dbd5b816795e6b80d3ed3012f/fenics-basix-0.5.0.tar.gz")
    version("0.4.2.post1", sha256="29e80d74a9896d962ebf67638e958aa63d47a3d4ee316e72f9b57e7b19cb4661", url="https://pypi.org/packages/7b/f6/153055b88120181a5d19ac11f660d8fa9ac283273cbe728434b7c574e4ec/fenics-basix-0.4.2.post1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@0.7:")
        depends_on("python@3.7:", when="@:0.6")
        depends_on("py-numpy@1.21.0:", when="@0.7:")
    # END DEPENDENCIES

