# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCftime(PythonPackage):
    # BEGIN VERSIONS
    version("1.6.3", sha256="d0a6b29f72a13f08e008b9becff247cc75c84acb213332ede18879c5b6aa4dfd", url="https://pypi.org/packages/ee/cb/2dcae27c58d3dc773848d273eb4036513eca06ae92733dc2ba4b7a59878f/cftime-1.6.3.tar.gz")
    version("1.6.2", sha256="8614c00fb8a5046de304fdd86dbd224f99408185d7b245ac6628d0276596e6d2", url="https://pypi.org/packages/cd/db/c528f26ee2dbac1dc348189386c2df745770bb22c02542e281d60212cb13/cftime-1.6.2.tar.gz")
    version("1.6.1", sha256="511215f45ed7cc79ead84020e88e1fc476b8aba71b47d2fcdef8e65242406927", url="https://pypi.org/packages/5b/31/9536027132f9fe8d01ab6b4a7ff6a42136f3a26208825231f5785e6a50d6/cftime-1.6.1.tar.gz")
    version("1.6.0", sha256="13103e6650beea6552316bd5825d6aa3b7e98f5b8115026df4826798dff9f741", url="https://pypi.org/packages/20/3f/607a69f1253e5c8835400641da91a6b54cc49e3e9f6ac5848a745638f9ea/cftime-1.6.0.tar.gz")
    version("1.5.2", sha256="375d37d9ab8bf501c048e44efce2276296e3d67bb276e891e0e93b0a8bbb988a", url="https://pypi.org/packages/6e/66/7efbe3afbab26c2e774628e00587e9f0da5f6c0832deea93f98f4c4b6384/cftime-1.5.2.tar.gz")
    version("1.5.1.1", sha256="6dc4d76ec7fe5a2d3c00dbe6604c757f1319613b75ef157554ef3648bf102a50", url="https://pypi.org/packages/c4/1f/a91a359605b4e67b57cc7170370ba24e86d800e8bd8260669165c8d7acce/cftime-1.5.1.1.tar.gz")
    version("1.5.1", sha256="8a398caed78389b366f1037ca62939ff01af2f1789c77bce05eb903f19ffd840", url="https://pypi.org/packages/8e/0a/89df2ae91ec6f95f5295f826058eb6a5108cf6e968bdcf61d821d6ad764b/cftime-1.5.1.tar.gz")
    version("1.5.0", sha256="b644bcb53346b6f4fe2fcc9f3b574740a2097637492dcca29632c817e0604f29", url="https://pypi.org/packages/a1/f1/cbded664cf2b68224ff1915e6fdc722dcd3c86143d72c31036a519653d6d/cftime-1.5.0.tar.gz")
    version("1.4.1", sha256="7c55540bc164746c3c4f86a07c9c7b9ed4dfb0b0d988348ec63cec065c58766d", url="https://pypi.org/packages/9d/c3/80dd52e4cadb4ae60ea957fa5aa3f45b6678294d96d66f7759f745573f8e/cftime-1.4.1.tar.gz")
    version("1.4.0", sha256="2c6fe0279b1913ea7c67fbe020a736d5740cd21e4f81a10f91260267681795d7", url="https://pypi.org/packages/b5/23/74ae9be7d1b985b0f0783a0c105a70a9f53622cabb532b45e3842c381fda/cftime-1.4.0.tar.gz")
    version("1.0.3.4", sha256="dd74d0d470baf1c50e31335215793a5e78436903e34b4f151fa9ccbf3a6cc20c", url="https://pypi.org/packages/7a/83/a61141ec141ceb0617468e04cc163dbdb9007b958191043618d1dc950b8f/cftime-1.0.3.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@:1.0.1,1.0.3.3:1.2")
    # END DEPENDENCIES

