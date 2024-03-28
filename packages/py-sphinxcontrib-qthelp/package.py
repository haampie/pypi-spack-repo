# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySphinxcontribQthelp(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0.3", sha256="bd9fc24bcb748a8d51fd4ecaade681350aa63009a347a8c14e637895444dfab6", url="https://pypi.org/packages/2b/14/05f9206cf4e9cfca1afb5fd224c7cd434dcc3a433d6d9e4e0264d29c6cdb/sphinxcontrib_qthelp-1.0.3-py2.py3-none-any.whl")
    version("1.0.2", sha256="513049b93031beb1f57d4daea74068a4feb77aa5630f856fcff2e50de14e9a20", url="https://pypi.org/packages/ce/5b/4747c3ba98b3a3e21a66faa183d8f79b9ded70e74212a7988d236a6eb78a/sphinxcontrib_qthelp-1.0.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.0.4:")
    # END DEPENDENCIES

