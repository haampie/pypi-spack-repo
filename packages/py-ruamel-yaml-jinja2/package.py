# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRuamelYamlJinja2(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2.7", sha256="eb36abd4d308794e9a497e48f98cbd2b921d2cd2946bbc9f1bea42c9b142a241", url="https://pypi.org/packages/d0/ef/6281be4ef86a6a0e6f06004c2e4526de3d880f4eaf4210a07a269ad330b3/ruamel.yaml.jinja2-0.2.7-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-ruamel-yaml@0.16.1:", when="@0.2.5:")
    # END DEPENDENCIES

