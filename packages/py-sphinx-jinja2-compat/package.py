# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySphinxJinja2Compat(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2.0.post1", sha256="f9d329174bdde8db19dc12c62528367196eb2f6b46c91754eca604acd0c0f6ad", url="https://pypi.org/packages/5f/94/e11d74a25c9888fade340197211226d6300b0323d1da27c63e14110cbd8a/sphinx_jinja2_compat-0.2.0.post1-py3-none-any.whl")
    version("0.2.0", sha256="a5f3112d6873991c2cf28e37287163a0485d9c0812863b8aa4df7182722501fb", url="https://pypi.org/packages/75/c7/18ffe4d7cb65ea20094645d640ff18ac4cd6a64b1f26b71f8308d26c9d32/sphinx_jinja2_compat-0.2.0-py3-none-any.whl")
    version("0.2.0-beta1", sha256="2f6bcaec4cded0a8fba890f495dd2ac8aeceef113458d564ad1dd1b425cfdf30", url="https://pypi.org/packages/c4/79/6c38f38103b8acd20e0153bf9f9f7275726b5e2e9fcea8ec6f56d051c44d/sphinx_jinja2_compat-0.2.0b1-py3-none-any.whl")
    version("0.1.2", sha256="6fd822875a3b6850657423ecd496ed578c124e078169442f2c6d0908124dbd38", url="https://pypi.org/packages/b0/9e/5b8a56ecfec2b992f86b3774d0e9def37f7873e811e7191467441442f7f2/sphinx_jinja2_compat-0.1.2-py3-none-any.whl")
    version("0.1.1", sha256="90c26f01cb0b9fdf6609680ccb81dfc0e2e2588e10772b2fe296df767cbace35", url="https://pypi.org/packages/b5/3c/b2d69c935466807b043e304ee953acfdcb03c6b11a1f63b8f96a32b4ed5c/sphinx_jinja2_compat-0.1.1-py3-none-any.whl")
    version("0.1.0", sha256="14043263edeffd9d7499e9ce45307507db44cfbed9e05d0f8f1b95bb36a49c4b", url="https://pypi.org/packages/2b/d6/e30ed0b5e8b1e979b51b276a3fa94a62ffb54f682ae9df8476780422965c/sphinx_jinja2_compat-0.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-jinja2@2.10:")
        depends_on("py-markupsafe@1:")
    # END DEPENDENCIES

