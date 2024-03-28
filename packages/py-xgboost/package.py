# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyXgboost(PythonPackage):
    # BEGIN VERSIONS
    version("1.6.2", sha256="e1f5c91ba88cf8edb409d7fd2ca150dcd80b6f2115587d87365f0c10b2d4f009", url="https://pypi.org/packages/25/e0/f00261d3357eafbe7c657de718abd3c0f6613633a38d05350f63ee099cde/xgboost-1.6.2.tar.gz")
    version("1.6.1", sha256="24072028656f3428e7b8aabf77340ece057f273e41f7f85d67ccaefb7454bb18", url="https://pypi.org/packages/0e/8c/19309bcaf9a88b0bab34b88935925153f3f3f646163acaae9aa148cf72bb/xgboost-1.6.1.tar.gz")
    version("1.5.2", sha256="404dc09dca887ef5a9bc0268f882c54b33bfc16ac365a859a11e7b24d49da387", url="https://pypi.org/packages/c4/04/32989ec64004dca894f1d3ea4c41b1397272857edf14c1a9d1492b692d2d/xgboost-1.5.2.tar.gz")
    version("1.3.3", sha256="397051647bb837915f3ff24afc7d49f7fca57630ffd00fb5ef66ae2a0881fb43", url="https://pypi.org/packages/f8/e0/d7c3e7c97d72e48425fda3d7eaa49db40e7122b6c8f7ab210b7167b3302b/xgboost-1.3.3.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("dask", default=False)
    variant("pandas", default=False)
    variant("plotting", default=False)
    variant("scikit-learn", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

