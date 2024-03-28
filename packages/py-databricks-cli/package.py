# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDatabricksCli(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.18.0", sha256="1176a5f42d3e8af4abfc915446fb23abc44513e325c436725f5898cbb9e3384b", url="https://pypi.org/packages/ae/a3/d56f8382c40899301f327d1c881278b09c9b8bc301c2c111633a0346d06e/databricks_cli-0.18.0-py2.py3-none-any.whl")
    version("0.17.8", sha256="dfb7d3aeec17489b6051789bf7321694d875ea487be8652f8f58fabceead7d9e", url="https://pypi.org/packages/af/d0/d14ec29bef1b012e3585704e1c1396b15fdf6d86b65090177d8f4598a24f/databricks_cli-0.17.8-py2-none-any.whl")
    version("0.17.7", sha256="5b025943c70bbd374415264d38bfaddfb34ce070fadb083d851aec311e0f8901", url="https://pypi.org/packages/57/c3/9380e05c7297daae4d587b694771522256164a29ecc8554b07bc583a1eee/databricks_cli-0.17.7-py2-none-any.whl")
    version("0.17.6", sha256="99c8fef80ef3215a36c09f594e7788e59bf9990792b4697d8daece754abe1660", url="https://pypi.org/packages/92/a8/a12ff8f4975ff40502db9153bbd3d341a54c636817026e23c51625d2726d/databricks_cli-0.17.6-py2-none-any.whl")
    version("0.17.5", sha256="70e0dec96c05046a28dbff70c44e85ab17cbf639393a490b3b189fd9a83eda14", url="https://pypi.org/packages/a1/fa/3344e47d45dfbc82c3a055cd02e5424a03286f446afe7ca255a44bed80df/databricks_cli-0.17.5-py2-none-any.whl")
    version("0.17.4", sha256="bbd57bc21c88ac6d1f8f0b250db986e500490c4d3cb69664229384632eaeed81", url="https://pypi.org/packages/58/7d/4bd6e5dc4420fb5dbb5ae895c1d9934fc0c9e77d9c5dc010725195f093a7/databricks_cli-0.17.4-py2-none-any.whl")
    version("0.17.3", sha256="f090c2e4f99c39d69a7f7228e6c7df8cb1cebd5fddad6292e0625daf29d4be01", url="https://pypi.org/packages/9b/c7/1855de624b57f468e7272e091677765b4526b35e5d99e94a0c2d28b76d30/databricks_cli-0.17.3-py2-none-any.whl")
    version("0.17.2", sha256="cdcc073df0c79efc12f3220f8b76d3247aed88624338eb531c381123601bf36d", url="https://pypi.org/packages/cf/6a/06aa58144b6f1c19a4e411f9b931e7cc697c9aa41b5e9cf6cd5463a1a70a/databricks_cli-0.17.2-py2-none-any.whl")
    version("0.17.1", sha256="4efab931aff1a4d021a3fae3580c34b84a4d2a7f2aa9b933e310c2456bf25e0a", url="https://pypi.org/packages/62/11/db4b3fded3ee49f034ef794186b2386bc50fb8fe3c576cf010e0d8425049/databricks_cli-0.17.1-py2-none-any.whl")
    version("0.17.0", sha256="66c0ecb315041c28ba4ab3576c6c367b6933dc7c3b7d3130c4b8dc1f4f9140a1", url="https://pypi.org/packages/a2/86/61b2175aadb6b413b5c113262056a5bbe07c9cd1843ab6dde87d4d4be34f/databricks_cli-0.17.0-py2-none-any.whl")
    version("0.14.3", sha256="2c628fd9963f30e51646fceab16d64310e4d1f149028117de077259ee383e3ea", url="https://pypi.org/packages/a9/44/fc98bde2037fbd1880731a88e2b15f4c8a6d91f88b55ea9c50bf76de8e12/databricks_cli-0.14.3-py2-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-click@7:", when="@0.18:")
        depends_on("py-oauthlib@3.1:", when="@0.18:")
        depends_on("py-pyjwt@1.7:", when="@0.18:")
        depends_on("py-requests@2.17.3:", when="@0.18:")
        depends_on("py-six@1.10:", when="@0.18:")
        depends_on("py-tabulate@0.7.7:", when="@0.18:")
        depends_on("py-urllib3@1.26.7:", when="@0.18:")
    # END DEPENDENCIES

