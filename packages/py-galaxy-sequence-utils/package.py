# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGalaxySequenceUtils(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.1.5", sha256="f46e9ccec9313b7f1d5566acec85ac9b2b940f2bed468576cc837d186d608bdc", url="https://pypi.org/packages/5d/bb/57457a4bf16c775f086269e77014b6ca6bb1295581c5fbfd8ee0638be475/galaxy_sequence_utils-1.1.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six")
    # END DEPENDENCIES

