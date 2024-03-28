# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTorch(PythonPackage):
    # BEGIN VERSIONS
    version("0.1.2.post2", sha256="a43e37f8f927c5b18f80cd163daaf6a1920edafcab5102e02e3e14bb97d9c874", url="https://pypi.org/packages/f8/02/880b468bd382dc79896eaecbeb8ce95e9c4b99a24902874a2cef0b562cea/torch-0.1.2.post2.tar.gz")
    version("0.1.2.post1", sha256="4e9560ce89042e0bc40cda5b1f3ed7e0a2339d76356435a302e88a115c1e0c71", url="https://pypi.org/packages/5f/e9/bac4204fe9cb1a002ec6140b47f51affda1655379fe302a1caef421f9846/torch-0.1.2.post1.tar.gz")
    version("0.1.2", sha256="93e87a9573db7f40a12818661ea436d5bb7c79a541f66063e5f1c3bc44877b5e", url="https://pypi.org/packages/c0/66/2a0696bdac7ed0a99b65f6d8a5da7bc2583835ea04cac058bcd982cbb9ef/torch-0.1.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("amdgpu_target", default=False)
    variant("breakpad", default=False)
    variant("caffe2", default=False)
    variant("cuda", default=False)
    variant("cuda_arch", default=False)
    variant("cudnn", default=False)
    variant("debug", default=False)
    variant("distributed", default=False)
    variant("fbgemm", default=False)
    variant("gloo", default=False)
    variant("kineto", default=False)
    variant("magma", default=False)
    variant("metal", default=False)
    variant("mkldnn", default=False)
    variant("mpi", default=False)
    variant("mps", default=False)
    variant("nccl", default=False)
    variant("nnpack", default=False)
    variant("numa", default=False)
    variant("numpy", default=False)
    variant("onnx_ml", default=False)
    variant("openmp", default=False)
    variant("qnnpack", default=False)
    variant("rocm", default=False)
    variant("tensorpipe", default=False)
    variant("test", default=False)
    variant("valgrind", default=False)
    variant("xnnpack", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

