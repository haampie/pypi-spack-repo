# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDateparser(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.7.2", sha256="983d84b5e3861cb0aa240cad07f12899bb10b62328aae188b9007e04ce37d665", url="https://pypi.org/packages/82/9d/51126ac615bbc4418478d725a5fa1a0f112059f6f111e4b48cfbe17ef9d0/dateparser-0.7.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("calendars", default=False, description="calendars")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-python-dateutil", when="@0.3.5:")
        depends_on("py-pytz")
        depends_on("py-regex", when="@0.3.3:0.7.2")
        depends_on("py-tzlocal", when="@0.5:")
    # END DEPENDENCIES

