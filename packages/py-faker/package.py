# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFaker(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("9.8.2", sha256="876ba213aaddd661a539ada2158917c1be17064b72792ee788b81c13528865d0", url="https://pypi.org/packages/0a/ec/97397fbb5f17c9bb571bab49f939b973ef79729e929449630b0ca771396a/Faker-9.8.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-python-dateutil@2.4:", when="@0.7.3,0.7.6:")
        depends_on("py-text-unidecode@1.3:", when="@2.0.2:11")
    # END DEPENDENCIES

