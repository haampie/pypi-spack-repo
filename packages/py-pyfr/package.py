# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyfr(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.15.0", sha256="bc308528639c336d7d1b2860b571e333d0536abb38f7b6b51b92b2b448230ab8", url="https://pypi.org/packages/f9/0d/90a54962442625e4037efb3838a1785c06cfc456f40148817b5055498235/pyfr-1.15.0-py3-none-any.whl")
    version("1.14.0", sha256="bdcd5fc32fb79361abd9cf1eaf58f07bfc4c7e2d10415a7846fc7504a404bf91", url="https://pypi.org/packages/99/15/59bada54f04b67da8c31cba79b0170e466cddaee0d58fef5a2dfec165329/pyfr-1.14.0-py3-none-any.whl")
    version("1.13.0", sha256="6303f3e4471c359b4a44162d23c6ec9ca00903bbfb5447854cc5b942b37cb9a3", url="https://pypi.org/packages/0b/80/1e1a2184d07de56066ab88cfbe7f7d7a5d1124248ad54c263ed06ffcabec/pyfr-1.13.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("amdgpu_target", default=False)
    variant("cuda", default=False)
    variant("cuda_arch", default=False)
    variant("hip", default=False)
    variant("libxsmm", default=False)
    variant("metis", default=False)
    variant("rocm", default=False)
    variant("scipy", default=False)
    variant("scotch", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.10:", when="@2:")
        depends_on("python@3.9:", when="@1.14:1")
        depends_on("py-gimmik@3:", when="@1.15:1")
        depends_on("py-gimmik@2.3:2", when="@1.14")
        depends_on("py-gimmik@2.2:2", when="@1.13")
        depends_on("py-h5py@2.10:", when="@1.12.3:")
        depends_on("py-mako@1:", when="@1.8.5:")
        depends_on("py-mpi4py@3.1:", when="@1.13:")
        depends_on("py-numpy@1.20.0:", when="@1.12.1:1")
        depends_on("py-platformdirs@2.2:", when="@1.13:")
        depends_on("py-pytools@2016.2.1:", when="@1.8.5:")
    # END DEPENDENCIES

