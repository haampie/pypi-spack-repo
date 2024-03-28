# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOptEinsum(PythonPackage):
    # BEGIN VERSIONS
    version("3.3.0", sha256="2455e59e3947d3c275477df7f5205b30635e266fe6dc300e3d9f9646bfcea147", url="https://pypi.org/packages/bc/19/404708a7e54ad2798907210462fd950c3442ea51acc8790f3da48d2bee8b/opt_einsum-3.3.0-py3-none-any.whl")
    version("3.2.1", sha256="96f819d46da2f937eaf326336a114aaeccbcbdb9de460d42e8b5f480a69adca7", url="https://pypi.org/packages/63/a5/e6c07b08b934831ccb8c98ee335e66b7761c5754ee3cabfe4c11d0b1af28/opt_einsum-3.2.1-py3-none-any.whl")
    version("3.2.0", sha256="f6fbfbb759e670305c5c9a4dc4432e30f65e06fede88293dacfe19915af73386", url="https://pypi.org/packages/b2/49/2233e63052d5686c72131b579837ddfb98ba9dd0b92bb91efcb441ada8ce/opt_einsum-3.2.0-py3-none-any.whl")
    version("3.1.0", sha256="edfada4b1d0b3b782ace8bc14e80618ff629abf53143e1e6bbf9bd00b11ece77", url="https://pypi.org/packages/b8/83/755bd5324777875e9dff19c2e59daec837d0378c09196634524a3d7269ac/opt_einsum-3.1.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.7:", when="@2:2.0,3.2:")
    # END DEPENDENCIES

