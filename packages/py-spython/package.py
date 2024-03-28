# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySpython(PythonPackage):
    # BEGIN VERSIONS
    version("0.3.1", sha256="6c0519abee020a27532890ecf2d9360e361af7aac8fb0b84b497ab595fc5ecf2", url="https://pypi.org/packages/2d/f8/61e554883703b48d1d2d4c8c31ca09f6eeb243b239a75d023c2872eef20a/spython-0.3.1-py3-none-any.whl")
    version("0.2.14", sha256="49e22fbbdebe456b27ca17d30061489db8e0f95e62be3623267a23b85e3ce0f0", url="https://pypi.org/packages/42/ad/0ed334e53b3f093817fe9973d08ceacc83854784e69547aeb1202ad8538a/spython-0.2.14.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("runtime", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

