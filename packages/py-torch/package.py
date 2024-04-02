# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTorch(PythonPackage):
    # BEGIN VERSIONS
    version("0.1.2.post2", sha256="a43e37f8f927c5b18f80cd163daaf6a1920edafcab5102e02e3e14bb97d9c874", url="https://pypi.org/packages/f8/02/880b468bd382dc79896eaecbeb8ce95e9c4b99a24902874a2cef0b562cea/torch-0.1.2.post2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("amdgpu_target", default=False, description="amdgpu_target")
    variant("breakpad", default=False, description="breakpad")
    variant("caffe2", default=False, description="caffe2")
    variant("cuda", default=False, description="cuda")
    variant("cuda_arch", default=False, description="cuda_arch")
    variant("cudnn", default=False, description="cudnn")
    variant("debug", default=False, description="debug")
    variant("distributed", default=False, description="distributed")
    variant("fbgemm", default=False, description="fbgemm")
    variant("gloo", default=False, description="gloo")
    variant("kineto", default=False, description="kineto")
    variant("magma", default=False, description="magma")
    variant("metal", default=False, description="metal")
    variant("mkldnn", default=False, description="mkldnn")
    variant("mpi", default=False, description="mpi")
    variant("mps", default=False, description="mps")
    variant("nccl", default=False, description="nccl")
    variant("nnpack", default=False, description="nnpack")
    variant("numa", default=False, description="numa")
    variant("numpy", default=False, description="numpy")
    variant("onnx_ml", default=False, description="onnx_ml")
    variant("openmp", default=False, description="openmp")
    variant("qnnpack", default=False, description="qnnpack")
    variant("rocm", default=False, description="rocm")
    variant("tensorpipe", default=False, description="tensorpipe")
    variant("test", default=False, description="test")
    variant("valgrind", default=False, description="valgrind")
    variant("xnnpack", default=False, description="xnnpack")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

