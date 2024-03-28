# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyClikit(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.6.2", sha256="71268e074e68082306e23d7369a7b99f824a0ef926e55ba2665e911f7208489e", url="https://pypi.org/packages/f2/3d/4394c710b9195b83382dc67bdd1040e5ebfc3fc8df90e20fe74341298c57/clikit-0.6.2-py2.py3-none-any.whl")
    version("0.6.1", sha256="b15a03a0d16cb1bf074b469c47b609dc28405d2541563e8723a3dd381243f93d", url="https://pypi.org/packages/3b/64/6b319c57fb31c1de9867cda04e9bef4fb6343766d8ca60b21a911462e9d4/clikit-0.6.1-py2.py3-none-any.whl")
    version("0.6.0", sha256="a666d0727b1ddbfdef9ed2bfbda00ad6f1dd1fa19255ff79b8ca05df77809b7b", url="https://pypi.org/packages/3f/96/813d44be4560f5bb22a786c953767d988b110c90d848b65e0e33dd8a6c11/clikit-0.6.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-crashtest@:0.3", when="@0.6:")
        depends_on("py-pastel@0.2:", when="@0.4.2:")
        depends_on("py-pylev@1.3:")
    # END DEPENDENCIES

