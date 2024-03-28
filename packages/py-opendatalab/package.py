# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOpendatalab(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.0.9", sha256="4129a2e70820754538e24132e5b37acefa0abffda6ff687c75f42479e17d6e6f", url="https://pypi.org/packages/13/6e/5725353a3eb77c65b7400fc163f02e8b689d5f0c7e0504c55b1b1d33091f/opendatalab-0.0.9-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-click@7:", when="@0.0.1-beta54:")
        depends_on("py-colorama", when="@0.0.1-beta71:")
        depends_on("py-pycryptodome", when="@0.0.6:")
        depends_on("py-pywin32", when="@0.0.1-beta92: platform=windows")
        depends_on("py-requests@2.4.2:", when="@0.0.1-beta54:")
        depends_on("py-rich", when="@0.0.1-beta75:")
        depends_on("py-tqdm", when="@:0.0.1-beta53,0.0.6:")
    # END DEPENDENCIES

