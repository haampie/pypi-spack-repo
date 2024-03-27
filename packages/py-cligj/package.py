##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCligj(PythonPackage):
    version("0.7.2", sha256="c1ca117dbce1fe20a5809dc96f01e1c2840f6dcc939b3ddbb1111bf330ba82df", url="https://pypi.org/packages/73/86/43fa9f15c5b9fb6e82620428827cd3c284aa933431405d1bcf5231ae3d3e/cligj-0.7.2-py3-none-any.whl")
    version("0.7.1", sha256="07171c1e287f45511f97df4ea071abc5d19924153413d5683a8e4866369bc676", url="https://pypi.org/packages/42/1e/947eadf10d6804bf276eb8a038bd5307996dceaaa41cfd21b7a15ec62f5d/cligj-0.7.1-py3-none-any.whl")
    version("0.7.0", sha256="2bf2042a81be581d707f726aef5efbbd935a62af85d5521305026dabeb798f5d", url="https://pypi.org/packages/e2/40/54e99109411c4d9e6bea449238babe9d83b6ffb3477888929379f371f704/cligj-0.7.0.tar.gz")
    version("0.6.0", sha256="a5f080858fd584d73fcc2b75f80ed05054130944e2283019d1828a6deb9e4110", url="https://pypi.org/packages/a1/48/7f32ccb3f14d3ae8d92ad491aa6794fee5eb2a5ef87af699861d74b11cb2/cligj-0.6.0.tar.gz")
    version("0.6-beta1", sha256="f44937f11519da45af14146975e1adaad73caf669dab6f9489ce9d3bcde510b4", url="https://pypi.org/packages/ca/82/6f1296349fd23c037c5c2c57d5de6458902f92453e1ac3e3fa7c84b01b5c/cligj-0.6b1.tar.gz")
    version("0.5.0", sha256="6c7d52d529a78712491974f975c33473f430c0f7beb18c0d7a402a743dcb460a", url="https://pypi.org/packages/7a/75/20752146e9c73e74a286f66d4ee84ed102b4855c04d9bb8892b52a1f166c/cligj-0.5.0.tar.gz")
    version("0.4.0", sha256="12ad07994f5c1173b06087ffbaacec52f9ebe4687926e5aacfc22b6b0c8b3f54", url="https://pypi.org/packages/fc/53/b89c392f33aa48b3063ad49e4dab70e424659d1fc4103b28b183f477f476/cligj-0.4.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-click@4:7", when="@0.5,0.7.1")
        depends_on("py-click@4:", when="@0.3:0.4,0.7.2:")

