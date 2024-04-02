# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkGamecenter(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="43341b428cad2e50710cb974728924280e520e04ae9f750bc7beda5006457ae3", url="https://pypi.org/packages/a3/13/a371d6aec4aa3da321f38554d7b994f83c0e61388d2c268cba5788f22730/pyobjc-framework-GameCenter-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

