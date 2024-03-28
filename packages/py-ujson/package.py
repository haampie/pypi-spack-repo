# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyUjson(PythonPackage):
    # BEGIN VERSIONS
    version("5.7.0", sha256="e788e5d5dcae8f6118ac9b45d0b891a0d55f7ac480eddcb7f07263f2bcf37b23", url="https://pypi.org/packages/43/1a/b0a027144aa5c8f4ea654f4afdd634578b450807bb70b9f8bad00d6f6d3c/ujson-5.7.0.tar.gz")
    version("4.0.2", sha256="c615a9e9e378a7383b756b7e7a73c38b22aeb8967a8bfbffd4741f7ffd043c4d", url="https://pypi.org/packages/86/0a/80d87aa4ee79980bddabef13cb7d95de330f85355cf08dfdaf874889b02b/ujson-4.0.2.tar.gz")
    version("1.35", sha256="f66073e5506e91d204ab0c614a148d5aa938bdbf104751be66f8ad7a222f5f86", url="https://pypi.org/packages/16/c4/79f3409bc710559015464e5f49b9879430d8f87498ecdc335899732e5377/ujson-1.35.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

