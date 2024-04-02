# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkFsevents(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="3a75f38bb1d5d2cf6a0d3e92801b3510f32e96cf6443d81b9dd92a84d72eff0a", url="https://pypi.org/packages/6e/5b/42b1dcca24ebf2eebc29846a7779a9f7edc4104b6a2161a62532a7054023/pyobjc-framework-FSEvents-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

