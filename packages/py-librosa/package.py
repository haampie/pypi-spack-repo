##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLibrosa(PythonPackage):
    version("0.9.1", sha256="c2bb61a8008367cca89a3f1dad352d8e55fe5ca5f7414fb5d5258eb52765db33", url="https://pypi.org/packages/5b/da/bd63187b2ca1b97c04c270df90c934a97cbe512c8238ab65c89c1b043ae2/librosa-0.9.1-py3-none-any.whl")
    version("0.7.2", sha256="656bbda80e98e6330db1ead79cd084b13a762284834d7603fcf7cf7c0dc65f3c", url="https://pypi.org/packages/77/b5/1817862d64a7c231afd15419d8418ae1f000742cac275e85c74b219cbccb/librosa-0.7.2.tar.gz")

    with default_args(type="run"):
        depends_on("py-audioread@2.1.5:", when="@0.9:0.9.1")
        depends_on("py-decorator@4.0.10:", when="@0.9")
        depends_on("py-joblib@0.14:", when="@0.9:")
        depends_on("py-numba@0.45.1:", when="@0.9")
        depends_on("py-numpy@1.17.0:", when="@0.9")
        depends_on("py-packaging@20:", when="@0.9")
        depends_on("py-pooch@1:", when="@0.9:0.10.0.post1,0.10.1:")
        depends_on("py-resampy@0.2.2:", when="@0.9")
        depends_on("py-scikit-learn@0.19.1:", when="@0.9")
        depends_on("py-scipy@1.2.0:", when="@0.9:")
        depends_on("py-soundfile@0.10.2:", when="@0.9")

