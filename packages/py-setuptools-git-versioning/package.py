# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySetuptoolsGitVersioning(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.13.3", sha256="0ae47836c30563c30f06d2e1e97fab4455a6b770f7a0496793239eccf4a6dd9f", url="https://pypi.org/packages/b7/3b/99abd999c3e88cd91097498d5455d9013fc7ae647e28b458cb45ccf0836b/setuptools_git_versioning-1.13.3-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:")
        depends_on("py-packaging")
        depends_on("py-setuptools")
        depends_on("py-toml@0.10.2:", when="@1.13: ^python@:3.10")
    # END DEPENDENCIES

