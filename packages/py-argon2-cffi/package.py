# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyArgon2Cffi(PythonPackage):
    # BEGIN VERSIONS
    version("21.3.0", sha256="8c976986f2c5c0e5000919e6de187906cfd81fb1c72bf9d88c01177e77da7f80", url="https://pypi.org/packages/a8/07/946d5a9431bae05a776a59746ec385fbb79b526738d25e4202d3e0bbf7f4/argon2_cffi-21.3.0-py3-none-any.whl")
    version("21.1.0", sha256="f710b61103d1a1f692ca3ecbd1373e28aa5e545ac625ba067ff2feca1b2bb870", url="https://pypi.org/packages/7b/39/a26aaef5c3f0c6cfd67c80599b5b40a794fdab46f4ee3be925d71e2f9596/argon2-cffi-21.1.0.tar.gz")
    version("20.1.0", sha256="d8029b2d3e4b4cea770e9e5a0104dd8fa185c1724a0f01528ae4826a6d25f97d", url="https://pypi.org/packages/74/fd/d78e003a79c453e8454197092fce9d1c6099445b7e7da0b04eb4fe1dbab7/argon2-cffi-20.1.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-argon2-cffi-bindings", when="@21.2:")
    # END DEPENDENCIES

