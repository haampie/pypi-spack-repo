# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonKeystoneclient(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("4.2.0", sha256="5702f387e2a3f3645459a0850ef3e92bc8fc0eb36bd2f8ba1004a50dfed1e5f4", url="https://pypi.org/packages/26/71/a9ccf1faf72123909c87a06352366088a7f936ea04e5e4fe38e422dc2c1e/python_keystoneclient-4.2.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-debtcollector@1.2:")
        depends_on("py-keystoneauth1@3.4:")
        depends_on("py-oslo-config@5.2:")
        depends_on("py-oslo-i18n@3.15.3:")
        depends_on("py-oslo-serialization@2.18:2.19.0,2.20:")
        depends_on("py-oslo-utils@3.33:")
        depends_on("py-pbr@2:2.0,3:")
        depends_on("py-requests@2.14.2:")
        depends_on("py-six@1.10:", when="@:5.3")
        depends_on("py-stevedore@1.20:")
    # END DEPENDENCIES

