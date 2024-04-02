# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTimemory(PythonPackage):
    # BEGIN VERSIONS
    version("3.2.3", sha256="2335961755a304bfc33a8d2427161c13f9592f87ae7a7ae8c901ca41c0127504", url="https://pypi.org/packages/0c/5f/f95868de08d4928a22ac702b29d6e5fcc45a36287d03250c406558812132/timemory-3.2.3.tar.gz")
    version("3.2.2", sha256="b7425357d3c028aaf1f15622f8c29a897add0d332210f4c5dbc834b4e412f8cb", url="https://pypi.org/packages/4a/ba/77e66c27c53df66a8304432d52f7009736b52e545c7eb600baa315db345f/timemory-3.2.2.tar.gz")
    version("3.2.1", sha256="2b3f2b1f675d9e5ca56e17ab945c16bf2a44582205d0a3e0731be732fb5a8477", url="https://pypi.org/packages/13/ea/ada6073456c25cc8e3e9ecabc8ee0a6b56386b2ede5080bc6a55737ac153/timemory-3.2.1.tar.gz")
    version("3.2.0", sha256="57607b098850716f8205dda4bab503a3f16a2050c8deff78e5aca292cdd7b4e6", url="https://pypi.org/packages/ef/fd/61a179c2fcfa4019d2b7caf4093864a2795cc1d6b6fed9e7768affb04de0/timemory-3.2.0.tar.gz")
    version("3.1.0", sha256="51f85868d442db7c979f9852a94faf33c2af9063af8ac7e7303aedbb00e78ef9", url="https://pypi.org/packages/1b/27/6bedba0164d4a708279939bd336ec1b937a04ddff914064240f9166da8d1/timemory-3.1.0.tar.gz")
    version("3.0.1", sha256="a4ee67e20fb8536d2c08d643514229a34fe4e748029dc54cf916a3eca5c09417", url="https://pypi.org/packages/93/81/f998caa046fb5125d0125a053e3343f20befef9a5642e1eb35a2a09236a5/timemory-3.0.1.tar.gz")
    version("3.0.0", sha256="6bb9a4726a39a7714e3d7cc70b0e379a1b2f110f68b9676e8933e895eeca939e", url="https://pypi.org/packages/49/fa/91d772becf0c8b6521bf322cd1a6413b30bd2505010c9d27c0dde5ea86cf/timemory-3.0.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("allinea_map", default=False, description="allinea_map")
    variant("build_type", default=False, description="build_type")
    variant("caliper", default=False, description="caliper")
    variant("compiler", default=False, description="compiler")
    variant("cpu_target", default=False, description="cpu_target")
    variant("cuda", default=False, description="cuda")
    variant("cuda_arch", default=False, description="cuda_arch")
    variant("cudastd", default=False, description="cudastd")
    variant("cupti", default=False, description="cupti")
    variant("cxxstd", default=False, description="cxxstd")
    variant("dyninst", default=False, description="dyninst")
    variant("ert", default=False, description="ert")
    variant("examples", default=False, description="examples")
    variant("extra_optimizations", default=False, description="extra_optimizations")
    variant("generator", default=False, description="generator")
    variant("gotcha", default=False, description="gotcha")
    variant("gperftools", default=False, description="gperftools")
    variant("install_config", default=False, description="install_config")
    variant("install_headers", default=False, description="install_headers")
    variant("ipo", default=False, description="ipo")
    variant("kokkos_build_config", default=False, description="kokkos_build_config")
    variant("kokkos_tools", default=False, description="kokkos_tools")
    variant("likwid", default=False, description="likwid")
    variant("likwid_nvmon", default=False, description="likwid_nvmon")
    variant("lto", default=False, description="lto")
    variant("mpi", default=False, description="mpi")
    variant("mpip_library", default=False, description="mpip_library")
    variant("nccl", default=False, description="nccl")
    variant("ompt", default=False, description="ompt")
    variant("ompt_library", default=False, description="ompt_library")
    variant("papi", default=False, description="papi")
    variant("pic", default=False, description="pic")
    variant("python", default=False, description="python")
    variant("python_deps", default=False, description="python_deps")
    variant("python_hatchet", default=False, description="python_hatchet")
    variant("python_line_profiler", default=False, description="python_line_profiler")
    variant("require_packages", default=False, description="require_packages")
    variant("shared", default=False, description="shared")
    variant("static", default=False, description="static")
    variant("statistics", default=False, description="statistics")
    variant("tau", default=False, description="tau")
    variant("tls_model", default=False, description="tls_model")
    variant("tools", default=False, description="tools")
    variant("unity_build", default=False, description="unity_build")
    variant("upcxx", default=False, description="upcxx")
    variant("use_arch", default=False, description="use_arch")
    variant("vtune", default=False, description="vtune")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

