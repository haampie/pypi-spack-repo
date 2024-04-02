# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkMetrickit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="14cb02fd8fc338f6f15df5fd14c95419871b768cc8f5f71b1e0e99fde46b4712", url="https://pypi.org/packages/0a/b2/a5aa2544a35408094f17bcd471f0a72ac48d58d096fb974afc767e0e781a/pyobjc-framework-MetricKit-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

