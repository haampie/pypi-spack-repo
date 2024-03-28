# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyKneaddata(PythonPackage):
    # BEGIN VERSIONS
    version("0.12.0", sha256="b211bf973ea50cc89dd5935761ca3b101d422cfb62b215aae08f5ed92a624a58", url="https://pypi.org/packages/63/b8/5d380501db6bc6b35ec6aace96fbbf57e653e4ef0a74c3821665a96f7a63/kneaddata-0.12.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("bam", default=False)
    variant("fastqc", default=False)
    variant("trf", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

