##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOptEinsum(PythonPackage):
    version("3.3.0", sha256="2455e59e3947d3c275477df7f5205b30635e266fe6dc300e3d9f9646bfcea147", url="https://pypi.org/packages/bc/19/404708a7e54ad2798907210462fd950c3442ea51acc8790f3da48d2bee8b/opt_einsum-3.3.0-py3-none-any.whl")
    version("3.2.1", sha256="96f819d46da2f937eaf326336a114aaeccbcbdb9de460d42e8b5f480a69adca7", url="https://pypi.org/packages/63/a5/e6c07b08b934831ccb8c98ee335e66b7761c5754ee3cabfe4c11d0b1af28/opt_einsum-3.2.1-py3-none-any.whl")
    version("3.2.0", sha256="f6fbfbb759e670305c5c9a4dc4432e30f65e06fede88293dacfe19915af73386", url="https://pypi.org/packages/b2/49/2233e63052d5686c72131b579837ddfb98ba9dd0b92bb91efcb441ada8ce/opt_einsum-3.2.0-py3-none-any.whl")
    version("3.1.0", sha256="edfada4b1d0b3b782ace8bc14e80618ff629abf53143e1e6bbf9bd00b11ece77", url="https://pypi.org/packages/b8/83/755bd5324777875e9dff19c2e59daec837d0378c09196634524a3d7269ac/opt_einsum-3.1.0.tar.gz")
    version("3.0.1", sha256="8aba07af4cf80e86ec57a0fcc0d36267a37e15a19fbdcf8734ed836e04defea9", url="https://pypi.org/packages/c0/1a/ab5683d8e450e380052d3a3e77bb2c9dffa878058f583587c3875041fb63/opt_einsum-3.0.1.tar.gz")
    version("2.3.2", sha256="d3d464b4da7ef09e444c30e4003a27def37f85ff10ff2671e5f7d7813adac35b", url="https://pypi.org/packages/f6/d6/44792ec668bcda7d91913c75237314e688f70415ab2acd7172c845f0b24f/opt_einsum-2.3.2.tar.gz")
    version("2.3.1", sha256="e24f369b2e8ad72a150c23c71bb0ddbdde2e03f487600a050c6cd323c84056d5", url="https://pypi.org/packages/70/de/3ba1fd12f861c1c4126720a9abd4b6d4d81282e2ee93ac1b1667cb83153f/opt_einsum-2.3.1.tar.gz")
    version("2.2.0", sha256="48d384956f408db32d17a6f3fd8a0261d1e17de71dd061e0300f6fc49b7ddc6d", url="https://pypi.org/packages/fa/b8/cc2d20fe4f3bcad9c1bb142fa7105229aa30585a095d6c7aa8f2f19a05b4/opt_einsum-2.2.0.tar.gz")
    version("2.1.3", sha256="fedbe085b2473f579116e4d10d109b29d7c0d1234215a2af7e03e147954c6f69", url="https://pypi.org/packages/84/f4/aed2ebbb710a3aa172cdf9dc849e8ce38e0df984c6e683fbbc1537942be7/opt_einsum-2.1.3.tar.gz")
    version("2.1.2", sha256="815fbb96d60edb10087c0bd80128d11116c374582ac489050cf31928195278d0", url="https://pypi.org/packages/36/24/97005b8d821e798ed68957b297595f161c22f2f31107703c0433e98195c5/opt_einsum-2.1.2.tar.gz")

    with default_args(type="run"):
        depends_on("py-numpy@1.7:", when="@2:2.0,3.2:")

