# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySphinxcontribHtmlhelp(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.0.1", sha256="c38cb46dccf316c79de6e5515e1770414b797162b23cd3d06e67020e1d2a6903", url="https://pypi.org/packages/6e/ee/a1f5e39046cbb5f8bc8fba87d1ddf1c6643fbc9194e58d26e606de4b9074/sphinxcontrib_htmlhelp-2.0.1-py3-none-any.whl")
    version("2.0.0", sha256="d412243dfb797ae3ec2b59eca0e52dac12e75a241bf0e4eb861e450d06c6ed07", url="https://pypi.org/packages/63/40/c854ef09500e25f6432dcbad0f37df87fd7046d376272292d8654cc71c95/sphinxcontrib_htmlhelp-2.0.0-py2.py3-none-any.whl")
    version("1.0.2", sha256="d4fd39a65a625c9df86d7fa8a2d9f3cd8299a3a4b15db63b50aac9e161d8eff7", url="https://pypi.org/packages/e4/35/80a67cc493f4a8a9634ab203a77aaa1b84d79ccb1c02eca72cb084d2c7f7/sphinxcontrib_htmlhelp-1.0.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@2.0.1")
    # END DEPENDENCIES

