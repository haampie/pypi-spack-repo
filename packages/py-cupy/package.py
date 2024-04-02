# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCupy(PythonPackage):
    # BEGIN VERSIONS
    version("12.1.0", sha256="f6d31989cdb2d96581da12822e28b102f29e254427195c2017eac327869b7320", url="https://pypi.org/packages/e1/e0/fdc8115aea34e990a74471b126f04dbd79b8b035a28a7118d4eb7cf81c8a/cupy-12.1.0.tar.gz")
    version("12.0.0", sha256="61ddbbef73d50d606bd5087570645f3c91ec9176c2566784c1d486d6a3404545", url="https://pypi.org/packages/7d/9a/5c9e4947efc4c7e20287b40ec69456e1ed719f08657f88467401bb61abd7/cupy-12.0.0.tar.gz")
    version("11.6.0", sha256="53dbb840072bb32d4bfbaa6bfa072365a30c98b1fcd1f43e48969071ad98f1a7", url="https://pypi.org/packages/e3/62/c808623b8000185efebd8b4542efdf76cc93d20dfd3f0a3eaeb5e5697430/cupy-11.6.0.tar.gz")
    version("11.5.0", sha256="4bc8565bded22cc89b210fd9fb48a5d5316f30701e12bb23852a60314e1f9f6e", url="https://pypi.org/packages/2b/7d/6f7ba8894524f96f9b6749411d25ab7f9da7c0d365f046b48019ab216cbb/cupy-11.5.0.tar.gz")
    version("11.4.0", sha256="03d52b2626e02a3a2b46d714c1cd03e702c8fe33915fcca6ed8de5c539964f49", url="https://pypi.org/packages/41/29/c7ead5a0e05692fee23bf9238faa4c7cf4ffb9c6f49935b76755fdf676d6/cupy-11.4.0.tar.gz")
    version("11.3.0", sha256="d057cc2f73ecca06fae8b9c270d9e14116203abfd211a704810cc50a453b4c9e", url="https://pypi.org/packages/c1/a7/e8470d74c066a91ba6a5d2ee9c69cc5717b9d10409eef4f8b2225ce03092/cupy-11.3.0.tar.gz")
    version("11.2.0", sha256="c33361f117a347a63f6996ea97446d17f1c038f1a1f533e502464235076923e2", url="https://pypi.org/packages/92/3c/f72d7a85c770ddded45ade707a756f596df1097809480bba2a46996fe278/cupy-11.2.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("all", default=False, description="all")
    variant("amdgpu_target", default=False, description="amdgpu_target")
    variant("cuda", default=False, description="cuda")
    variant("cuda_arch", default=False, description="cuda_arch")
    variant("rocm", default=False, description="rocm")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@12.0.0-rc1:13.0.0-alpha1")
        depends_on("python@3.7:", when="@:12.0.0-beta3")
    # END DEPENDENCIES

