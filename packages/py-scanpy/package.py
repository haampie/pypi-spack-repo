# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyScanpy(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.10.0", sha256="8cd83448837b808ebf4005fcb78a89fc3b7c4d5a97580b6a4254e394ab062911", url="https://pypi.org/packages/e4/78/1ae66df53e8dfe2d83a186719bc0585caa55bbbad916d353513ce1ea8385/scanpy-1.10.0-py3-none-any.whl")
    version("1.9.8", sha256="abcca12dfe6975146277b6a76841e2328e07c6a9f518d234ba6a889b26b456dc", url="https://pypi.org/packages/3b/72/436046ca332b933ca7d09cd45b86154232203e068e8307a102d5349e9444/scanpy-1.9.8-py3-none-any.whl")
    version("1.9.7", sha256="046af177640f5d00a240f47a384cb7e769f1707a9af4871d9437d230e3cfc028", url="https://pypi.org/packages/15/c9/c278b9d9eb6cb0270821e4f94be35e93b441f2eb1040fea3b5c412aa5135/scanpy-1.9.7-py3-none-any.whl")
    version("1.9.6", sha256="30a96bfa2a56fefc810fc6407d7488c56b4c40fd1d14090a4d572e1fabf89bef", url="https://pypi.org/packages/39/d5/992cb22882523b873b981c1bdebbf28baffeb7ac931cd5d60cb53f2d8a24/scanpy-1.9.6-py3-none-any.whl")
    version("1.9.5", sha256="0795625d5aaf4b2e88b5328cf8cbefe2f5ebc26d45de44acf49ad9763382a301", url="https://pypi.org/packages/be/c7/414c92e855ac07f6cd3c04e289688c8e2cc420d0fb60446c4af5386aa9c1/scanpy-1.9.5-py3-none-any.whl")
    version("1.9.4", sha256="0ed1916c8eddcbe947361323088c54b07883be630e0e711f1f2863ecba26820a", url="https://pypi.org/packages/df/96/a01cdfe76376eb4937fdcb7ca3c9ee78374081cc5bbf7a7b00a79e547a5c/scanpy-1.9.4-py3-none-any.whl")
    version("1.9.3", sha256="e1d9b44067de401bca89ef1932e00bc73019f4d67d3907361044618f53bc3767", url="https://pypi.org/packages/8e/7b/a5bf0891a36069db8c0dbc3e5ffe35447b4b54f3f3de12af3202cedb00fa/scanpy-1.9.3-py3-none-any.whl")
    version("1.9.2", sha256="cdf4e3f86a64f12f1e1d0b98d69bc41a8e04e09e15479489d2f0a0af7ac572a7", url="https://pypi.org/packages/f4/a9/cfd581f27f0b1dac4bbbaccad78a2d0ef497011790f9ad3018648db44136/scanpy-1.9.2-py3-none-any.whl")
    version("1.9.1", sha256="9fca3597aef176034ebc3438be3bf859db5c47441e36481d7f9272bd4cd51d2a", url="https://pypi.org/packages/51/87/a55c7992cba9b189de70eae37e9f1e2abe6fdaf3f087d30356f28698948e/scanpy-1.9.1-py3-none-any.whl")
    version("1.9.0", sha256="d454b150e77a39f69f3f5f390288060f83fd1b87f1af1b57bf02c4a0640284f6", url="https://pypi.org/packages/a4/0f/5667b6d6a60cb8ab11a7bfc80d82f0eefc7b2023ccacd2d2459752029539/scanpy-1.9.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.10:")
        depends_on("py-anndata@0.8.0:", when="@1.10:")
        depends_on("py-anndata@0.7.4:", when="@1.7:1.9")
        depends_on("py-get-annotations", when="@1.9.6: ^python@:3.9")
        depends_on("py-h5py@3.1:", when="@1.10:")
        depends_on("py-h5py@3.0.0:", when="@1.9")
        depends_on("py-igraph", when="@:0.2.4")
        depends_on("py-joblib", when="@:0.2.4,0.2.9:0.2.9.0,0.4:0.4.0,0.4.2:0,1.1-alpha1,1.3.8:1.4.0,1.4.4,1.4.5.post2:1.4.5,1.5:")
        depends_on("py-legacy-api-wrap@1.4:", when="@1.10:")
        depends_on("py-matplotlib@3.6.0:", when="@1.9.7:")
        depends_on("py-matplotlib@3.4.0:", when="@1.9.1:1.9.6")
        depends_on("py-matplotlib@3.1.2:", when="@1.5:1.9.0")
        depends_on("py-natsort", when="@:0.2.4,0.2.9:0.2.9.0,0.4:0.4.0,0.4.2:0,1.1-alpha1,1.3.8:1.4.0,1.4.4,1.4.5.post2:1.4.5,1.5:")
        depends_on("py-networkx@2.7:", when="@1.10:")
        depends_on("py-networkx@2.3:", when="@1.6:1.9")
        depends_on("py-numba@0.56.0:", when="@1.10:")
        depends_on("py-numba@0.41:", when="@1.4.4,1.4.5.post2:1.4.5,1.5:1.9")
        depends_on("py-numpy@1.23.0:", when="@1.10:")
        depends_on("py-numpy@1.17.0:", when="@1.6:1.9")
        depends_on("py-packaging@21.3:", when="@1.10:")
        depends_on("py-packaging", when="@1.4.5.post2:1.4.5,1.5:1.9")
        depends_on("py-pandas@1.5.0:", when="@1.10:")
        depends_on("py-pandas@1.1.1:2.1.1,2.1.3:", when="@1.9.6:1.9")
        depends_on("py-pandas@1.0.0:", when="@1.9.1:1.9.5")
        depends_on("py-pandas@0.21.0:", when="@0.4.3:0,1.1-alpha1,1.3.8:1.4.0,1.4.4,1.4.5.post2:1.4.5,1.5:1.9.0")
        depends_on("py-patsy", when="@1.3.8:1.4.0,1.4.4,1.4.5.post2:1.4.5,1.5:")
        depends_on("py-pynndescent@0.5.0:", when="@1.10:")
        depends_on("py-python-igraph", when="@0.2.9:0.2.9.0")
        depends_on("py-scikit-learn@0.24.0:", when="@1.9.4:")
        depends_on("py-scikit-learn@0.22:", when="@1.8:1.9.3")
        depends_on("py-scipy@1.8.0:", when="@1.10:")
        depends_on("py-scipy@1.4.0:", when="@1.6:1.9")
        depends_on("py-seaborn@0.13.0:", when="@1.9.7:")
        depends_on("py-seaborn@:0.13.0-rc0,0.13.1:", when="@1.9.6")
        depends_on("py-seaborn", when="@:0.2.4,0.2.9:0.2.9.0,0.4:0.4.0,0.4.2:0,1.1-alpha1,1.3.8:1.4.0,1.4.4,1.4.5.post2:1.4.5,1.5:1.9.5")
        depends_on("py-session-info", when="@1.9:")
        depends_on("py-setuptools-scm", when="@1.4.5.post2:1.4.5,1.5:1.6")
        depends_on("py-statsmodels@0.13.0:", when="@1.10:")
        depends_on("py-statsmodels@0.10:", when="@1.4.4,1.4.5.post2:1.4.5,1.5:1.9")
        depends_on("py-tqdm", when="@:0.2.4,0.2.9:0.2.9.0,0.4:0.4.0,0.4.2,1.4.4,1.4.5.post2:1.4.5,1.5:")
        depends_on("py-umap-learn@0.5.1:", when="@1.10:")
        depends_on("py-umap-learn@0.3.10:", when="@1.4.5.post2:1.4.5,1.5:1.6.0,1.7.0:1.9")
    # END DEPENDENCIES

