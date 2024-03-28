# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAccelerate(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.28.0", sha256="8ae25f8a8dc4cf12283842c469113836300545fb0dfa46fef331fb0a2ac8b421", url="https://pypi.org/packages/a0/11/9bfcf765e71a2c84bbf715719ba520aeacb2ad84113f14803ff1947ddf69/accelerate-0.28.0-py3-none-any.whl")
    version("0.27.2", sha256="a818dd27b9ba24e9eb5030d1b285cf4cdd1b41bbfa675fb4eb2477ddfc097074", url="https://pypi.org/packages/1b/da/24a54b9205fce3bdbaad521c35944d0b0a2d292ac5ae921e484b76312b43/accelerate-0.27.2-py3-none-any.whl")
    version("0.27.1", sha256="7d138f6c00ead40c3a8de88f44d467b1f658ef687aac83cbeb475b39d1804300", url="https://pypi.org/packages/e0/e5/20373eaee15adeb12872bc03355636c283cf3092fd7eb290bb974174b14e/accelerate-0.27.1-py3-none-any.whl")
    version("0.27.0", sha256="87eb754a1600a63d6fdbf8683603800388544456bfbdaaf622b89458005937de", url="https://pypi.org/packages/c8/14/73c3d62e709c2ace755c826997b12f883f3cb6b138dec63ac1e2a68cd910/accelerate-0.27.0-py3-none-any.whl")
    version("0.26.1", sha256="04df826b84ac7bad8a0a8ab90e6aeacdecb1ea5a2d744d7e94f6735c29183227", url="https://pypi.org/packages/a6/b9/44623bdb05595481107153182e7f4b9f2ef9d3b674938ad13842054dcbd8/accelerate-0.26.1-py3-none-any.whl")
    version("0.26.0", sha256="fec56ee3f934fb441a75486e43d50ca2639d94f752baaa92799f1ff494c3dd1b", url="https://pypi.org/packages/63/9c/c10fc10df1d4968406b3f3cffe5a7d9988a8583e3423fc4156d6c91ab62d/accelerate-0.26.0-py3-none-any.whl")
    version("0.25.0", sha256="c7bb817eb974bba0ff3ea1ba0f24d55afb86d50e3d4fe98d6922dc69cf2ccff1", url="https://pypi.org/packages/f7/fc/c55e5a2da345c9a24aa2e1e0f60eb2ca290b6a41be82da03a6d4baec4f99/accelerate-0.25.0-py3-none-any.whl")
    version("0.24.1", sha256="866dec394da60e8da964be212379d8cf6cc0d0e5e28a7c0d7e09507715d21c61", url="https://pypi.org/packages/13/9e/ee987874058f2d93006961f6ff49e0bcb60ab9c26709ebe06bfa8707a4d8/accelerate-0.24.1-py3-none-any.whl")
    version("0.24.0", sha256="04bb1483c90eacb3beb2687cb54950d8caf9a0b93432f6b2d42efebbb6c0491e", url="https://pypi.org/packages/d0/cf/364d550af711b5abe5129ac676896b223ba5a082d97fe400527a59c0c1f8/accelerate-0.24.0-py3-none-any.whl")
    version("0.23.0", sha256="fba5065ff4e7c8f0a39df50785023703cd9bf8388073aa13c6457920f3bc5225", url="https://pypi.org/packages/d9/92/2d3aecf9f4a192968035880be3e2fc8b48d541c7128f7c936f430d6f96da/accelerate-0.23.0-py3-none-any.whl")
    version("0.21.0", sha256="e2609d37f2c6a56e36a0612feae6ff6d9daac9759f4899432b86b1dc97024ebb", url="https://pypi.org/packages/70/f9/c381bcdd0c3829d723aa14eec8e75c6c377b4ca61ec68b8093d9f35fc7a7/accelerate-0.21.0-py3-none-any.whl")
    version("0.16.0", sha256="27aa39b2076560b3ee674b9650c237c58520b3fd7907e5da1f922cf6868c1576", url="https://pypi.org/packages/dc/0c/f95215bc5f65e0a5fb97d4febce7c18420002a4c3ea5182294dc576f17fb/accelerate-0.16.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-huggingface-hub", when="@0.23:")
        depends_on("py-numpy@1.17.0:", when="@0.5:")
        depends_on("py-packaging@20:", when="@0.10:")
        depends_on("py-psutil", when="@0.10:")
        depends_on("py-pyyaml", when="@0.4:")
        depends_on("py-safetensors@0.3.1:", when="@0.25:")
        depends_on("py-torch@1.10:", when="@0.21:")
        depends_on("py-torch@1.4:", when="@0.1:0.18")
    # END DEPENDENCIES

