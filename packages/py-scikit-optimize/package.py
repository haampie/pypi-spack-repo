# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyScikitOptimize(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.10.1", sha256="044fb125ede1275f7cae7c70327af7f0bd7ec3ed0243c7401b29a4b8f94cb385", url="https://pypi.org/packages/90/0e/15deb91b3db0003843e34e72fa865e1d92013781d986fdc65483c99a9f69/scikit_optimize-0.10.1-py2.py3-none-any.whl")
    version("0.10.0", sha256="3049d42b3990323450a1b5516936b1d8e8b6da753a808fdede307661eb71bc26", url="https://pypi.org/packages/62/43/ce85456e5152af5bfae809fb24b80f2bcd869f63f3dcf210c57341df733a/scikit_optimize-0.10.0-py2.py3-none-any.whl")
    version("0.9.0", sha256="5a439a18232381fad4bda78e914b616416720708e67f123498d14bd2842d861a", url="https://pypi.org/packages/55/f6/2d9efbd86126c40fe0f8a47611a9e2480b493b6f0ce9751bdf0240cfa091/scikit_optimize-0.9.0-py2.py3-none-any.whl")
    version("0.8.1", sha256="caf52bf67d005f97eb9855fa70f645d0510eea32c1ab1b171f1569ed2a6d532a", url="https://pypi.org/packages/8b/03/be33e89f55866065a02e515c5b319304a801a9f1027a9b311a9b1d1f8dc7/scikit_optimize-0.8.1-py2.py3-none-any.whl")
    version("0.8.0", sha256="66e096a7258ceecf321fc620a15127fe627d64f1b409a646a5caffba236d449e", url="https://pypi.org/packages/3e/53/bffa229d690b89705c336cdd8f4d33515ee7c4d2920de546d3efdaa0568e/scikit_optimize-0.8.0-py2.py3-none-any.whl")
    version("0.7.4", sha256="2ddcb5aa1f0c67396eee68d365de3d66928c40c609f4c12d079cc8151b9f5e76", url="https://pypi.org/packages/5c/87/310b52debfbc0cb79764e5770fa3f5c18f6f0754809ea9e2fc185e1b67d3/scikit_optimize-0.7.4-py2.py3-none-any.whl")
    version("0.7.3", sha256="ae0077b33f035628a6544960e85f59d1be3e4c4803a9388555141d7c4308c531", url="https://pypi.org/packages/aa/ea/6c9d15ba356e9c141a8042b971235c62b72bb2f360743d6b93d3b4d9413d/scikit_optimize-0.7.3-py2.py3-none-any.whl")
    version("0.7.2", sha256="773c03cb9437fd27b30e9541b4d495820f532a9c078f8525bf2ffd37d85717a7", url="https://pypi.org/packages/4f/cf/b4aee828215a882495f7696ac85f8c1ecc0275923a18fecbb109ceaca651/scikit_optimize-0.7.2-py2.py3-none-any.whl")
    version("0.7.1", sha256="7af3e31ff40e133a572498e5f7096fed5493e63c2973edf0cfde882d1e42ea3e", url="https://pypi.org/packages/cd/ff/4cd204e8ad092d7db2ddf383adc3747166117915a6a47df025c6b727a500/scikit_optimize-0.7.1-py2.py3-none-any.whl")
    version("0.7", sha256="8c5fd4959ad1b3ec58b64b50085e16e122fc35efcb6bf8a44047c89ac6149f62", url="https://pypi.org/packages/96/37/9c4cffe61a66982f5def376c12d802095d336e6d7451b9f5ad8a7db060b3/scikit_optimize-0.7-py2.py3-none-any.whl")
    version("0.5.2", sha256="a2304413f7b66b27dfaed64271c370e5e2c926fbc1cbecdb67fe47cd847f9d5c", url="https://pypi.org/packages/f4/44/60f82c97d1caa98752c7da2c1681cab5c7a390a0fdd3a55fac672b321cac/scikit_optimize-0.5.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("plots", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-joblib@0.11:", when="@0.7.3:")
        depends_on("py-joblib", when="@0.7-rc4:0.7.2")
        depends_on("py-matplotlib@2.0.0:", when="@0.7.3:+plots")
        depends_on("py-matplotlib", when="@0.5.2:0.7.2+plots")
        depends_on("py-matplotlib", when="@:0.5.1")
        depends_on("py-numpy@1.20.3:", when="@0.10-rc3:")
        depends_on("py-numpy@1.13.3:", when="@0.8.0:0.9")
        depends_on("py-numpy@1.11.0:", when="@0.7.3:0.7")
        depends_on("py-numpy", when="@:0.7.2")
        depends_on("py-packaging@21.3:", when="@0.10-rc3:")
        depends_on("py-pyaml@16:", when="@0.7.3:")
        depends_on("py-pyaml", when="@0.7-rc4:0.7.2")
        depends_on("py-scikit-learn@1.0:", when="@0.10-rc3:")
        depends_on("py-scikit-learn@0.20.0:", when="@0.8.0:0.9")
        depends_on("py-scikit-learn@0.19.1:", when="@0.5:0.8.dev")
        depends_on("py-scipy@1.1.0:", when="@0.10-rc3:")
        depends_on("py-scipy@0.19.1:", when="@0.8.0:0.9")
        depends_on("py-scipy@0.18.0:", when="@0.7.3:0.8.dev")
        depends_on("py-scipy@0.14:", when="@0.5:0.7.2")
    # END DEPENDENCIES

