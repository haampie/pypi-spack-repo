##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNvidiaDaliCuda110(PythonPackage):
    version("1.36.0", sha256="1373e2dfed77e3bd423afb3b3abd2ca42ed2ef6650addb44abf24a5b0cfe7a26", url="https://pypi.org/packages/f0/72/9b9cf635e77f52b4016ec705e7b73aaee1fffdc4700bb973d06614ae9a77/nvidia_dali_cuda110-1.36.0.tar.gz")
    version("1.35.0", sha256="b2f8475289efaa6c01967555dbb16c6a249cb5f44444b8fa10e7edc88f961311", url="https://pypi.org/packages/6f/18/c7571514ec9203f26a4ec3302b1c733c8e0fcaeac764e235e8026a42dfa4/nvidia_dali_cuda110-1.35.0-12768316-py3-none-manylinux2014_aarch64.whl")
    version("1.34.0", sha256="9e12ce02e60b3c21ef1d665ab4d9d3ecebb60ba73b72a84df974e1f4a74d1c26", url="https://pypi.org/packages/eb/2e/7f655eba68a489f80c3286fb5c70a373fc2d6add4bf28722cdae9491a97d/nvidia_dali_cuda110-1.34.0-12152783-py3-none-manylinux2014_x86_64.whl")
    version("1.33.0", sha256="aba70abf096e7242c09a10aaa84b5c2b46019000e12e92bdb30db67d6e4eeb5e", url="https://pypi.org/packages/d5/7a/32cf3da8e7c48e81ac905d3c7f87b50eb673eeac89b7ced9967067f63ea6/nvidia_dali_cuda110-1.33.0-11414177-py3-none-manylinux2014_x86_64.whl")
    version("1.32.0", sha256="07df8947737250a34037aaae1bff1d47d8fe84d694a70997d7143488a2bf5c28", url="https://pypi.org/packages/55/db/c7d40e8114d05139a6946f8c4a52b5bab9220cc94c3305b2c883eb5488bc/nvidia_dali_cuda110-1.32.0-10610165-py3-none-manylinux2014_aarch64.whl")
    version("1.31.0", sha256="65a3c9e6375967d0f3ece9c2e4eb1621d6b45167f76dacfa40c1c7efe70f7c31", url="https://pypi.org/packages/51/22/51c80903bd13756a3b2965ab30b52cc16566583d24ff9212831e94095df7/nvidia_dali_cuda110-1.31.0-10168358-py3-none-manylinux2014_aarch64.whl")
    version("1.30.0", sha256="d149a924e032c45fbff295f5cded3548988e2e6c126ef46a2702d10f841419be", url="https://pypi.org/packages/21/da/e53ec8eea5199e8dc3390d328ea024bfab533485d77573cdd984793c8891/nvidia_dali_cuda110-1.30.0-9783405-py3-none-manylinux2014_aarch64.whl")
    version("1.29.0", sha256="a51f167e7712e3dcbbf9d7b03d48efedb5ab3681f4269c677880f624b0cae53a", url="https://pypi.org/packages/08/98/1c325fa3bf2f00964657724a53484d41fc1849f32908237fabd0a70b863e/nvidia_dali_cuda110-1.29.0-9289311-py3-none-manylinux2014_x86_64.whl")
    version("1.28.0", sha256="cfdb3aaf603103b57b004f3f2c8a5636bbc400fc807bb312cea49d22fd8cc391", url="https://pypi.org/packages/8e/16/e876deafa261bb69bfc79fc766d98a76511324e453349998303beec93e3f/nvidia_dali_cuda110-1.28.0-8915299-py3-none-manylinux2014_aarch64.whl")
    version("1.27.0", sha256="8c28429f979c3fcb45f40f08efdae4b6ed3f4743634d41722a6c94d18c4cd995", url="https://pypi.org/packages/7b/6a/019e6ad19c8d1051712d64515b75d7f7119625afd6204c779d7803e36a6f/nvidia_dali_cuda110-1.27.0-8625303-py3-none-manylinux2014_aarch64.whl")

    with default_args(type="run"):
        depends_on("python@:3.12", when="@1.34:")
        depends_on("python@:3.11", when="@1.23:1.33")
        depends_on("python@:3.10", when="@1:1.22")
        depends_on("py-astunparse@1.6:", when="@1.22:")
        depends_on("py-dm-tree", when="@1.27:")
        depends_on("py-gast@0.3.3:", when="@1.27:")
        depends_on("py-nvidia-nvimgcodec-cu11", when="@1.36:")

