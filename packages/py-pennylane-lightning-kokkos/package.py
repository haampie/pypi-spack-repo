# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPennylaneLightningKokkos(PythonPackage):
    # BEGIN VERSIONS
    version("0.32.0", sha256="4d527772d25c321af2a0c221bfbb18cc29d724a8f16c8611be54d3711981c7ad", url="https://pypi.org/packages/38/81/e93a2c37e7360737e91024c8611dd122f6ebbaccbe54e416946b275d3b25/PennyLane-Lightning-Kokkos-0.32.0.tar.gz")
    version("0.31.0", sha256="5846078bf1f31afb416456508e8a725e47d4508f574155ce329acd49216e37c6", url="https://pypi.org/packages/75/95/6c25960daad42f4614ab6ce5a7710ef62b4f2b0abd580c1fe97c0ba9a923/PennyLane-Lightning-Kokkos-0.31.0.tar.gz")
    version("0.30.0", sha256="2f995cfa21156e78b4efcfda45649d921a9864eb4942fae5ea3a845fe76f5b9c", url="https://pypi.org/packages/f0/4c/7ae0b66a3c18ffc647c5c9b3e347e649f64b5439b2b27cb9f4b8548c2a81/PennyLane-Lightning-Kokkos-0.30.0.tar.gz")
    version("0.29.1", sha256="96ba290809873856e28eb1939754cc20b6bce47fd30cee706217f1849955c044", url="https://pypi.org/packages/39/6c/326ef9cb4a4526c18d12697406c0871137e63900260b567cdbcea05ba9c8/PennyLane-Lightning-Kokkos-0.29.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("amdgpu_target", default=False, description="amdgpu_target")
    variant("build_type", default=False, description="build_type")
    variant("cpptests", default=False, description="cpptests")
    variant("cuda", default=False, description="cuda")
    variant("cuda_arch", default=False, description="cuda_arch")
    variant("generator", default=False, description="generator")
    variant("ipo", default=False, description="ipo")
    variant("native", default=False, description="native")
    variant("openmp", default=False, description="openmp")
    variant("openmptarget", default=False, description="openmptarget")
    variant("rocm", default=False, description="rocm")
    variant("sanitize", default=False, description="sanitize")
    variant("serial", default=False, description="serial")
    variant("sycl", default=False, description="sycl")
    variant("threads", default=False, description="threads")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

