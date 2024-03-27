##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySetuptoolsGitVersioning(PythonPackage):
    version("1.13.3", sha256="0ae47836c30563c30f06d2e1e97fab4455a6b770f7a0496793239eccf4a6dd9f", url="https://pypi.org/packages/b7/3b/99abd999c3e88cd91097498d5455d9013fc7ae647e28b458cb45ccf0836b/setuptools_git_versioning-1.13.3-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-packaging", when="@1.9:")
        depends_on("py-setuptools", when="@:1.1.1,1.9:")
        depends_on("py-toml@0.10.2:", when="@1.13: ^python@:3.10")
        depends_on("py-toml@0.10.2:", when="@1.9:1.12")

