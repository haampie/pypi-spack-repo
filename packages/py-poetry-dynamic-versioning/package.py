# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPoetryDynamicVersioning(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.19.0", sha256="b59410538490aaeb35ae8672761a048d2cf58287b3ce261e50efef201813c1d6", url="https://pypi.org/packages/55/2b/939cc8ecb32bcaf262aad0eb69a57b77a90738e35856c44074a2d78375c6/poetry_dynamic_versioning-0.19.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-dunamai@1.12:", when="@0.16:0.19")
        depends_on("py-jinja2@2.11.1:", when="@0.13:")
        depends_on("py-tomlkit@0.4:", when="@0.2:0,1.0.0:")
    # END DEPENDENCIES

