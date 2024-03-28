# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPystacClient(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.5.1", sha256="f181c5d078e3c0b0769d492c79b213afb673666c6d0dc89c5f194dde0a8bcbb4", url="https://pypi.org/packages/df/c6/9ffa4d823a628a1addc1718cb0bd37352c17c6365637a62c7bcf46d741f2/pystac_client-0.5.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pystac@1.4:", when="@0.3.3:0.6.0")
        depends_on("py-python-dateutil@2.7:", when="@:0.3.0,0.3.4:0.6")
        depends_on("py-requests@2.27.1:", when="@0.5:0.6")
    # END DEPENDENCIES

