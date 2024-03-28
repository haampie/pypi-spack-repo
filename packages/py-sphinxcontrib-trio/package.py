# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySphinxcontribTrio(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.1.2", sha256="1b849be08a147ef4113e35c191a51c5792613a9a54697b497cd91656d906a232", url="https://pypi.org/packages/a7/4d/6e1598531046c272730501337d5303ce3958387a4fde1da8875580f5c41b/sphinxcontrib_trio-1.1.2-py3-none-any.whl")
    version("1.1.0", sha256="39196d15b8c9a9947be2e593518f404bc0da6020ae69007b9f8ce49b4ba3d49b", url="https://pypi.org/packages/57/39/e00e5c1fc21e10dcfd103e2b0de6ce9f2901aab28eaef8075fbf4946ad20/sphinxcontrib_trio-1.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-sphinx@1.7.0:", when="@1.1:")
    # END DEPENDENCIES

