# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTriangle(PythonPackage):
    # BEGIN VERSIONS
    version("20200424", sha256="fc207641f8f39986f7d2bee1b91688a588cd235d2e67777422f94e61fece27e9", url="https://pypi.org/packages/cc/30/eb72adcd01a8ab9766a2d5418624e978522708de38e375129dadbcbffd86/triangle-20200424.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@20200424:")
    # END DEPENDENCIES

