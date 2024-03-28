# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPromptToolkit(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.0.38", sha256="45ea77a2f7c60418850331366c81cf6b5b9cf4c7fd34616f733c5427e6abbb1f", url="https://pypi.org/packages/87/3f/1f5a0ff475ae6481f4b0d45d4d911824d3218b94ee2a97a8cb84e5569836/prompt_toolkit-3.0.38-py3-none-any.whl")
    version("3.0.31", sha256="9696f386133df0fc8ca5af4895afe5d78f5fcfe5258111c2a79a1c3e41ffa96d", url="https://pypi.org/packages/26/ec/2ebddd1f0584fec4a6d4b5dc57627254070c3db310f00981bc5de03dd5ab/prompt_toolkit-3.0.31-py3-none-any.whl")
    version("3.0.29", sha256="62291dad495e665fca0bda814e342c69952086afb0f4094d0893d357e5c78752", url="https://pypi.org/packages/3f/2d/dcb44d69f388ca2ee1a4a4d3c204ab66b36975c0d5166781eaeeff76b882/prompt_toolkit-3.0.29-py3-none-any.whl")
    version("3.0.24", sha256="e56f2ff799bacecd3e88165b1e2f5ebf9bcd59e80e06d395fa0cc4b8bd7bb506", url="https://pypi.org/packages/fb/37/4f9ae5a6cd0ebdfc1fbafcfd03e812df1ed92a92bf0bee09441c52164f58/prompt_toolkit-3.0.24-py3-none-any.whl")
    version("3.0.17", sha256="4cea7d09e46723885cb8bc54678175453e5071e9449821dce6f017b1d1fbfc1a", url="https://pypi.org/packages/ce/ee/08ceeb759c570bf96b4c636582ebf18c14c3c844a601b2e77b17f462aa6b/prompt_toolkit-3.0.17-py3-none-any.whl")
    version("3.0.16", sha256="62c811e46bd09130fb11ab759012a4ae385ce4fb2073442d1898867a824183bd", url="https://pypi.org/packages/a6/0b/c6de29441b29f8b54d5bbe29a8b223de6e400714ff50e85541bd4c783421/prompt_toolkit-3.0.16-py3-none-any.whl")
    version("3.0.7", sha256="83074ee28ad4ba6af190593d4d4c607ff525272a504eb159199b6dd9f950c950", url="https://pypi.org/packages/2b/c1/53ac685833200eb77ef485c2220dac5bfc255418e660790a9eb5cf3abf25/prompt_toolkit-3.0.7-py3-none-any.whl")
    version("2.0.10", sha256="e7f8af9e3d70f514373bf41aa51bc33af12a6db3f71461ea47fea985defb2c31", url="https://pypi.org/packages/66/6a/2c0693ec21528c10dfea279662788b28b2a01cce961160791084d975521a/prompt_toolkit-2.0.10-py2-none-any.whl")
    version("2.0.9", sha256="977c6583ae813a37dc1c2e1b715892461fcbdaa57f6fc62f33a528c4886c8f55", url="https://pypi.org/packages/c8/ab/10d2c114828bd20ca0d757acee37ab5a7bae588139739b24d6cd3f45f8de/prompt_toolkit-2.0.9-py2-none-any.whl")
    version("1.0.16", sha256="1e71341526efa4b11bb44d323e687a5d9cef204aabe2907e3f0dc1534cda0ecc", url="https://pypi.org/packages/57/a8/a151b6c61718eabe6b4672b6aa760b734989316d62ec1ba4996765e602d4/prompt_toolkit-1.0.16-py3-none-any.whl")
    version("1.0.9", sha256="b7bbbc221159be8daab91269d48575f6c740000c03d537fc076ee176476c8b4c", url="https://pypi.org/packages/fc/80/6a3cb891118635fd79be261c1f5a5d1fe479f15841526808c5aaa246f1ef/prompt_toolkit-1.0.9-py2-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-wcwidth", when="@3:")
    # END DEPENDENCIES

