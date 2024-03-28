# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDuecredit(PythonPackage):
    # BEGIN VERSIONS
    version("0.9.3", sha256="5ec1df6f2cfabd2255181b70ab0766cd96b540f9770fd63fd98132303f5da16d", url="https://pypi.org/packages/1b/e9/1177c7fcc7a6bc60efb397686a8cf4d5a8b5a9c0f867988976ef9532e078/duecredit-0.9.3-py3-none-any.whl")
    version("0.9.2", sha256="fb64bdbadfbbc598b0acc5066154a5c46e2772f975738365573c1746ffcaf31b", url="https://pypi.org/packages/14/89/3143635ce114edf19f03a1e16f3c71a76f5a43402257b43a36a9ce155638/duecredit-0.9.2-py3-none-any.whl")
    version("0.9.1", sha256="202944e97f195503d964f838a4f7994c8d9efbdbb71027f0e3ed5fc42e83e6da", url="https://pypi.org/packages/37/8a/9c69652395715d88ea72a4f9733e687f17d5f7937b7b0745d02e792e9b5a/duecredit-0.9.1-py3-none-any.whl")
    version("0.9.0", sha256="417d0f0116d240654d2239fd2f97b6128ee58b34d93c772f6dc15e7dbca84a59", url="https://pypi.org/packages/f0/2b/b3612ad95fed1a33b9c75b4c8ebe93515e787c0aaeec1741051e0f1e7148/duecredit-0.9.0.tar.gz")
    version("0.8.1", sha256="43b3f01ab5fb2bf2ecc27d3fcf92b873c6b288f44becef3e2e87c96cb89d7b01", url="https://pypi.org/packages/72/c5/cdf5b50c96fefbdb78317a39d5d59a7bcd936fb9e8605ff67f9101f62aa5/duecredit-0.8.1.tar.gz")
    version("0.8.0", sha256="a0c773f38af623f08010ca8ee151d594767b868f405308307479aa9b4e41adfb", url="https://pypi.org/packages/56/07/de31665385ded5d7e234deb7226d15b6134e49a7da2c57086fb1cf363dfa/duecredit-0.8.0.tar.gz")
    version("0.7.0", sha256="8a13be317afcf56bdccba6a5d3d82c2f4e3509ffa1aff47d61c1a91e6d454010", url="https://pypi.org/packages/22/d1/7366b7b41a62ece9fe5fded08a7989b6ae5cd7d50292b5c730013f971c6d/duecredit-0.7.0.tar.gz")
    version("0.6.5", sha256="da3746c24f048e1b2e9bd15c001f0f453a29780ebb9d26367f478a63d15dee9b", url="https://pypi.org/packages/a6/6c/cf8dcf6522f342c624ecd39f86dc1358041863028e8b9bbab7e194e033f2/duecredit-0.6.5.tar.gz")
    version("0.6.4", sha256="f0168f4dd6649d9faa145e1b9e95d9da5f499a55c4f906eb6bb7e7e5213bdbea", url="https://pypi.org/packages/91/78/b00fa5ed4477cd010ccd895f678b1fd1087f6b0c85fdb8374ecf471999e3/duecredit-0.6.4.tar.gz")
    version("0.6.3", sha256="93b84a0333b9f6985f025f5f7daa049e0d4081ebde54905ef4d97a5f36b4df17", url="https://pypi.org/packages/99/ff/edfa328d391bb6b04ee26debc808f029d6721afe70afc60193b45f86d787/duecredit-0.6.3.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-citeproc-py@0.4:", when="@0.9.1:")
        depends_on("py-requests", when="@0.9.1:")
        depends_on("py-six", when="@0.9.1:0.9.2")
    # END DEPENDENCIES

