# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCligj(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.7.2", sha256="c1ca117dbce1fe20a5809dc96f01e1c2840f6dcc939b3ddbb1111bf330ba82df", url="https://pypi.org/packages/73/86/43fa9f15c5b9fb6e82620428827cd3c284aa933431405d1bcf5231ae3d3e/cligj-0.7.2-py3-none-any.whl")
    version("0.7.1", sha256="07171c1e287f45511f97df4ea071abc5d19924153413d5683a8e4866369bc676", url="https://pypi.org/packages/42/1e/947eadf10d6804bf276eb8a038bd5307996dceaaa41cfd21b7a15ec62f5d/cligj-0.7.1-py3-none-any.whl")
    version("0.7.0", sha256="394a0905fe6f36821b82f086bf8cc12fef20d99d0a3c26a8a92a9207a18b70c6", url="https://pypi.org/packages/ba/06/e3440b1f2dc802d35f329f299ba96153e9fcbfdef75e17f4b61f79430c6a/cligj-0.7.0-py3-none-any.whl")
    version("0.6.0", sha256="639242b1df173fdaef11c6214b2bc7404c7c6909730a1cfa1e69b5255acf2d60", url="https://pypi.org/packages/2d/0a/004ba68cd29bde809847c5f7e5990699d7a1ff3fe71a5703adc60b464e5f/cligj-0.6.0-py3-none-any.whl")
    version("0.6-beta1", sha256="d380773acc6db25a5097da26e9886ced5b8271ebe7cf796b4ad0fd891220389a", url="https://pypi.org/packages/65/bf/e282082672480a1d33843952b7acf9ae18fa8d152d6f70068b270e8765d9/cligj-0.6b1-py3-none-any.whl")
    version("0.5.0", sha256="20f24ce9abfde3f758aec3399e6811b936b6772f360846c662c19bf5537b4f14", url="https://pypi.org/packages/e4/be/30a58b4b0733850280d01f8bd132591b4668ed5c7046761098d665ac2174/cligj-0.5.0-py3-none-any.whl")
    version("0.4.0", sha256="7588487f1afcefbe65ae477cdbd4fca1828a3000fc3332e165dacb1dcb005f8a", url="https://pypi.org/packages/e8/c1/d2a5a83f1bf59b820b5ffb0c63fc31d13279d7b985f260c1f8c5ca1693d0/cligj-0.4.0-py2-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-click@4:7", when="@0.5:0.7.1")
        depends_on("py-click@4:", when="@0.3:0.4,0.7.2:")
    # END DEPENDENCIES

