# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPubchempy(PythonPackage):
    # BEGIN VERSIONS
    version("1.0.4", sha256="24e9dc2fc90ab153b2764bf805e510b1410700884faf0510a9e7cf0d61d8ed0e", url="https://pypi.org/packages/aa/fb/8de3aa9804b614dbc8dc5c16ed061d819cc360e0ddecda3dcd01c1552339/PubChemPy-1.0.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("pandas", default=False, description="pandas")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

