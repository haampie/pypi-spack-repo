# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDeeptools(PythonPackage):
    # BEGIN VERSIONS
    version("3.5.3", sha256="3cd6193a9f8018a1b637df0c5ed36e904208d08fd06060f1d63040c188f375b6", url="https://pypi.org/packages/40/97/5fd3bbdffd30c649ac6a837817c9e61470e65ee460a21190c49dfbbe2b00/deepTools-3.5.3-py3-none-any.whl")
    version("3.5.2", sha256="9367f9037b1822b7d69d5abaf47ca25bf0e5dc4cb8be85bd55b6f63c90781941", url="https://pypi.org/packages/25/65/1e5834ca0c71fa3b79e0f96df87795112a27e1ef80acbf49bc7fa5031083/deepTools-3.5.2.tar.gz")
    version("3.3.0", sha256="a9a6d2aff919f45e869acfb477e977db627da84f8136e4b4af0a5100057e6bc3", url="https://pypi.org/packages/3d/16/3e1757b61db790c86d1d9cf189a80946785ee69a60648647e1a44bfe504f/deepTools-3.3.0.tar.gz")
    version("3.2.1", sha256="ccbabb46d6c17c927e96fadc43d8d4770efeaf40b9bcba3b94915a211007378e", url="https://pypi.org/packages/cb/31/bfd1dd80e048075269d083230a635d1285ad2229cf22af14fb104e764cce/deepTools-3.2.1.tar.gz")
    version("2.5.2", sha256="305d0b85d75bd8af19dbe8947bb76c399fd5aaebd02f441455f4ba9e6c66ad9b", url="https://pypi.org/packages/0f/b5/2da5b555da6eb5d30e893bee6a0786d45c873034ffae6296c1319df01d50/deepTools-2.5.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-deeptoolsintervals@0.1.8:", when="@3.5.1,3.5.3:")
        depends_on("py-importlib-metadata", when="@3.5.3:3.5.4")
        depends_on("py-matplotlib@3.3.0:", when="@3.5.1,3.5.3")
        depends_on("py-numpy@1.9:", when="@3.5.1,3.5.3:")
        depends_on("py-numpydoc@0.5:", when="@3.5.1,3.5.3:")
        depends_on("py-plotly@4.9.0:", when="@3.5.1,3.5.3:")
        depends_on("py-py2bit@0.2:", when="@3.5.1,3.5.3:")
        depends_on("py-pybigwig@0.2.1:", when="@3.5.1,3.5.3:")
        depends_on("py-pysam@0.14:", when="@3.5.1,3.5.3:")
        depends_on("py-scipy@0.17:", when="@3.5.1,3.5.3:")
    # END DEPENDENCIES

