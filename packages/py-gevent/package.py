# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGevent(PythonPackage):
    # BEGIN VERSIONS
    version("23.7.0", sha256="d0d3630674c1b344b256a298ab1ff43220f840b12af768131b5d74e485924237", url="https://pypi.org/packages/8a/fb/d16e63f0dfce72f49edaa0b22f69218d196601c0c3366e5094ea90a6bbca/gevent-23.7.0.tar.gz")
    version("21.12.0", sha256="f48b64578c367b91fa793bf8eaaaf4995cb93c8bc45860e473bf868070ad094e", url="https://pypi.org/packages/c8/18/631398e45c109987f2d8e57f3adda161cc5ff2bd8738ca830c3a2dd41a85/gevent-21.12.0.tar.gz")
    version("21.8.0", sha256="43e93e1a4738c922a2416baf33f0afb0a20b22d3dba886720bc037cd02a98575", url="https://pypi.org/packages/33/2e/49317db0bbd846720ce15fd43641b17a208e6466c582ecbe845e35092ea2/gevent-21.8.0.tar.gz")
    version("1.5.0", sha256="b2814258e3b3fb32786bb73af271ad31f51e1ac01f33b37426b66cb8491b4c29", url="https://pypi.org/packages/5a/79/2c63d385d017b5dd7d70983a463dfd25befae70c824fedb857df6e72eff2/gevent-1.5.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cffi@1.12.2:", when="@1.5-alpha1:1.5-alpha3,1.5.0:1,23.9.1: platform=windows")
        depends_on("py-greenlet@0.4.14:", when="@1.3.7:1.5-alpha3,1.5.0:1")
        depends_on("py-zope-event", when="@23.9.1:")
        depends_on("py-zope-interface", when="@23.9.1:")
    # END DEPENDENCIES

