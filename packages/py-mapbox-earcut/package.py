# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMapboxEarcut(PythonPackage):
    # BEGIN VERSIONS
    version("1.0.1", sha256="9f155e429a22e27387cfd7a6372c3a3865aafa609ad725e2c4465257f154a438", url="https://pypi.org/packages/97/f9/38f72877be0a5bf35c04a75c8ceb261589f2807eeaffaa22055079f53839/mapbox_earcut-1.0.1.tar.gz")
    version("1.0.0", sha256="997ab14b9afbc14b1aede880b8f57efc7f28d6811a08db0adf1804b63bab0d9b", url="https://pypi.org/packages/35/35/9e643fb6aab46b71857603024a8cfdfc7c122c7ee3e281df851e0554efd2/mapbox_earcut-1.0.0.tar.gz")
    version("0.12.11", sha256="2808757f8a95eb816d3ce225528c9cb15355afe175f3bcb6837eb7700972e0b9", url="https://pypi.org/packages/01/5c/35d5bc8fb1f6844e832466f3b56bce19a646493ccb7df66bec484bbc84b5/mapbox_earcut-0.12.11.tar.gz")
    version("0.12.10", sha256="50d995673ac9ce8cb9abb7ab64b709d611c1d27557907e00b631b5272345c453", url="https://pypi.org/packages/9f/2a/9f10ef5bf10829a101e2a385bc6109dfc67bb2401b651a680bf96205a69b/mapbox_earcut-0.12.10.tar.gz")
    version("0.12.7", sha256="dbddc079b9ba9b458bb5d2ad0bfe0364ae2803b1d9520411e0cf0ee32d5993c8", url="https://pypi.org/packages/4a/aa/b516bb6976183ca31f59d1163ce95b8d08a5e46e19d161cc840a08a6dfa7/mapbox_earcut-0.12.7.tar.gz")
    version("0.12.6", sha256="f18438c5f20b8c128c054754d9e9a985af8acb55e1b497b12b4505eb5bc93876", url="https://pypi.org/packages/86/20/26e084cad2839bb0890be283bf157a15eb0cd3707a82f3a89bc4a2a2cb0a/mapbox_earcut-0.12.6.tar.gz")
    version("0.12.5.1", sha256="70454498a2076ae247426502c4d0e8adc12acbc3fc0e02bcc294827cbfe48774", url="https://pypi.org/packages/86/8a/5cf15018be1a5211aeebee91280250b358de8f260acd26c9a679c02d1b5a/mapbox_earcut-0.12.5.1.tar.gz")
    version("0.12.5", sha256="c5b71559aafb074df11afd1fc4df843b3e2d1e2108c6be256f305b57d8c4f2ae", url="https://pypi.org/packages/3a/b0/cc2feae85b5a5c09fddc10ec6bdc0574866521244e73bba759b8fa513562/mapbox_earcut-0.12.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@:0.12.5,0.12.7:0.12.10")
    # END DEPENDENCIES

