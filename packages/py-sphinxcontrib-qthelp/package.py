# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySphinxcontribQthelp(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0.7", sha256="e2ae3b5c492d58fcbd73281fbd27e34b8393ec34a073c792642cd8e529288182", url="https://pypi.org/packages/80/b3/1beac14a88654d2e5120d0143b49be5ad450b86eb1963523d8dbdcc51eb2/sphinxcontrib_qthelp-1.0.7-py3-none-any.whl")
    version("1.0.6", sha256="bf76886ee7470b934e363da7a954ea2825650013d367728588732c7350f49ea4", url="https://pypi.org/packages/1f/e5/1850f3f118e95581c1e30b57028ac979badee1eb29e70ee72b0241f5a185/sphinxcontrib_qthelp-1.0.6-py3-none-any.whl")
    version("1.0.5", sha256="962730a6ad15d21fd6760b14c9e95c00a097413595aa6ee871dd9dfa4b002a16", url="https://pypi.org/packages/c1/54/d3f8d78634c43be776bbec969cce56cf6a6ba49fc950774179b6cc20176b/sphinxcontrib_qthelp-1.0.5-py3-none-any.whl")
    version("1.0.4", sha256="82f0871fb042efa309ee8c7929d228ed5c4be478d9914492b4bad5bfa469c160", url="https://pypi.org/packages/8d/57/6edeb937dbc2858d980242ffc5913303c19774048b68654e5bee9556e146/sphinxcontrib_qthelp-1.0.4-py3-none-any.whl")
    version("1.0.3", sha256="bd9fc24bcb748a8d51fd4ecaade681350aa63009a347a8c14e637895444dfab6", url="https://pypi.org/packages/2b/14/05f9206cf4e9cfca1afb5fd224c7cd434dcc3a433d6d9e4e0264d29c6cdb/sphinxcontrib_qthelp-1.0.3-py2.py3-none-any.whl")
    version("1.0.2", sha256="513049b93031beb1f57d4daea74068a4feb77aa5630f856fcff2e50de14e9a20", url="https://pypi.org/packages/ce/5b/4747c3ba98b3a3e21a66faa183d8f79b9ded70e74212a7988d236a6eb78a/sphinxcontrib_qthelp-1.0.2-py2.py3-none-any.whl")
    version("1.0.1", sha256="18ec9f74ea2c92fd512d5f3b532d6ab4ac2be76b12cc2490f7729842ba2a60c9", url="https://pypi.org/packages/cd/02/3e28f003cacee424f7fd1eb76927c093edad4f12080b5b3ba7e210f947a3/sphinxcontrib_qthelp-1.0.1-py2.py3-none-any.whl")
    version("1.0.0", sha256="ec18eb340f712b5e93e7fe0c673956f373a45831661c5418b7edf1c42e60f56b", url="https://pypi.org/packages/07/c0/8d1fd8e042398821fddc960658a157de79ac3596682da2653b9b47950a10/sphinxcontrib_qthelp-1.0.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.0.4:")
        depends_on("py-sphinx@5.0.0:", when="@1.0.4:1.0.6")
    # END DEPENDENCIES

