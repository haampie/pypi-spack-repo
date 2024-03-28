# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGcsfs(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2024.2.0", sha256="20bf70cc81d580474dd299d55e1ffcf8b3e81721aeb562e148ca0a3c900d0421", url="https://pypi.org/packages/5b/18/f40a808abb7ce9aaf8a2143b699dd0b246e61ea590ce55810ceae45610ed/gcsfs-2024.2.0-py2.py3-none-any.whl")
    version("2023.1.0", sha256="62c491b9e2a8e9e58b8a899eec2ce111f827718a65539019ff3cadf447e48f41", url="https://pypi.org/packages/d7/6b/f5e347eda42ecfbe0a1d87f35a4d65c9a94bc90563f8df27735b4191ba3c/gcsfs-2023.1.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-aiohttp@:3", when="@2022.8:")
        depends_on("py-decorator@4.2:", when="@2021.10:")
        depends_on("py-fsspec@2024:2024.2", when="@2024:2024.2")
        depends_on("py-fsspec@2023:2023.1", when="@2023:2023.1")
        depends_on("py-google-auth@1.2:", when="@0.0.4,0.3:0.3.0,0.4:")
        depends_on("py-google-auth-oauthlib", when="@0.0.4,0.3:0.3.0,0.4:")
        depends_on("py-google-cloud-storage", when="@2021.10.1:")
        depends_on("py-requests", when="@0.0.3:0.0.4,0.3:0.3.0,0.4:")
    # END DEPENDENCIES

