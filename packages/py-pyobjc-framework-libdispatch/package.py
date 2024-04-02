# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkLibdispatch(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="ae17602efbe628fa0432bcf436ee8137d2239a70669faefad420cd527e3ad567", url="https://pypi.org/packages/25/c5/731a26daec598dbcb4a281a85364e98ebd10c3d00ceb21b7fec0fd8c884e/pyobjc-framework-libdispatch-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

