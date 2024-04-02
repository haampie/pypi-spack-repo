# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkAutomaticassessmentconfiguration(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="ead3f75200ad74dd013b4a6372054b84b2adeacdac656ca31e763e42fb76cf7b", url="https://pypi.org/packages/f2/f4/1690886940bd04ca5a2ca16a48f52494d13f522a90d17802d726172df26d/pyobjc-framework-AutomaticAssessmentConfiguration-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

