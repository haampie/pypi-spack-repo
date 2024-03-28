# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPreshed(PythonPackage):
    # BEGIN VERSIONS
    version("3.0.8", sha256="6c74c70078809bfddda17be96483c41d06d717934b07cab7921011d81758b357", url="https://pypi.org/packages/f1/78/c28a568317088b9cef21f8516bed2f41210492ae569c5842ad80251631a0/preshed-3.0.8.tar.gz")
    version("3.0.2", sha256="61d73468c97c1d6d5a048de0b01d5a6fd052123358aca4823cdb277e436436cb", url="https://pypi.org/packages/5f/14/de231123ddbe0bf12bd9b1993122d67f22859643bee4dad3b6ce91986336/preshed-3.0.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cymem@2:", when="@3.0.1:3.0.2,3.0.9:3")
        depends_on("py-murmurhash@0.28:1.0", when="@3.0.1:3.0.2,3.0.9:3")
    # END DEPENDENCIES

