##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGpaw(PythonPackage):
    version("21.1.0", sha256="96843b68e04bd1c12606036c9f99b0ddfa5e6ee08ce46835e6bb347a6bd560a3", url="https://pypi.org/packages/39/6a/fdbcd3843f5daf2e8a351c37eec4a9137cedf881b2d2bf7a42f1c38f4e0d/gpaw-21.1.0.tar.gz")
    version("20.10.0", sha256="77c3d3918f5cc118e448f8063af4807d163b31d502067f5cbe31fc756eb3971d", url="https://pypi.org/packages/16/62/cf268b7ea00581bf2f735f6abed89ab13f4effc73e17763dc1edd92fd465/gpaw-20.10.0.tar.gz")
    version("20.1.0", sha256="c84307eb9943852d78d966c0c8856fcefdefa68621139906909908fb641b8421", url="https://pypi.org/packages/3d/c1/d93c45a291fdb8a329430068453afc6324e31ac8ac910979dda8f2f5bee4/gpaw-20.1.0.tar.gz")
    version("19.8.1", sha256="79dee367d695d68409c4d69edcbad5c8679137d6715da403f6c2500cb2178c2a", url="https://pypi.org/packages/97/15/93a211c8e612b6a185806794688a2b701c44b2bfd77dc35a46003a334332/gpaw-19.8.1.tar.gz")
    version("1.3.0", sha256="cf601c69ac496421e36111682bcc1d23da2dba2aabc96be51accf73dea30655c", url="https://pypi.org/packages/11/59/bfb6102911f9c0c35bfd0c1f3f51e0f4c31523b9f700674d18e4f60d7081/gpaw-1.3.0.tar.gz")


