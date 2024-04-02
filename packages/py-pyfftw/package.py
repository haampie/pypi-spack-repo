# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyfftw(PythonPackage):
    # BEGIN VERSIONS
    version("0.13.1", sha256="09155e90a0c6d0c1f2d1f3668180a7de95fb9f83fef5137a112fb05978e87320", url="https://pypi.org/packages/9f/bc/7376df0393e816b60bdc627fc8f653706f4caa95bcf79d07302a672f893e/pyFFTW-0.13.1.tar.gz")
    version("0.13.0", sha256="da85102405c0bd95d57eb19e99b01a0729d8406cb204c3900894b873784253da", url="https://pypi.org/packages/18/a1/5eb99c183af0a49bf632fed3260a6cad3f7978bb19fd661a573d3728a986/pyFFTW-0.13.0.tar.gz")
    version("0.12.0", sha256="60988e823ca75808a26fd79d88dbae1de3699e72a293f812aa4534f8a0a58cb0", url="https://pypi.org/packages/4b/38/6f9539d274d02fbc3262e2f9a0c9dbac9b53393b3ed935612993f8df54bf/pyFFTW-0.12.0.tar.gz")
    version("0.11.1", sha256="05ea28dede4c3aaaf5c66f56eb0f71849d0d50f5bc0f53ca0ffa69534af14926", url="https://pypi.org/packages/fa/7f/e65fe8b9f1b66aab22c8d76c2f03180714a558fcef4a723263fa8f3754f8/pyFFTW-0.11.1.tar.gz")
    version("0.10.4", sha256="739b436b7c0aeddf99a48749380260364d2dc027cf1d5f63dafb5f50068ede1a", url="https://pypi.org/packages/c2/2e/b25edc6960fc837e915eb1b38e5f0e3013e32e90aff14a1d0f4556b3d145/pyFFTW-0.10.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@0.13.1:")
        depends_on("python@3.7:", when="@0.13:0.13.0")
        depends_on("py-numpy@1.10:1", when="@0.12")
    # END DEPENDENCIES

