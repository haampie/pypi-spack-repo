# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyqtgraph(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.13.4", sha256="1dc9a786aa43cd787114366058dc3b4b8cb96a0e318f334720c7e6cc6c285940", url="https://pypi.org/packages/ae/2d/28d5d4efd20a69f6a3cb450a171e8562b379a14483c365c082e00b24d267/pyqtgraph-0.13.4-py3-none-any.whl")
    version("0.13.3", sha256="fdcc04ac4b32a7bedf1bf3cf74cbb93ab3ba5687791712bbfa8d0712377d2f2b", url="https://pypi.org/packages/61/57/0a096b8949d0ee5ca32de180f19240ddd5a81015a27c6f2e7342b9044d45/pyqtgraph-0.13.3-py3-none-any.whl")
    version("0.13.2", sha256="078afbd9528164f3dd524f68cbf56618055b851384cfacc675ac189d919544a8", url="https://pypi.org/packages/42/52/63d6f7be8f57fe0bff1204611b60edf881295a13c360bcb9be3f325b5597/pyqtgraph-0.13.2-py3-none-any.whl")
    version("0.13.1", sha256="906b2784c213890bf2a1df43e3675eff1921ee894ab9673468747fb993ea2d6c", url="https://pypi.org/packages/a2/88/8f2e85c0e171b7b08357f61551614ff39c4cab644a242bc80907e2275e47/pyqtgraph-0.13.1-py3-none-any.whl")
    version("0.13.0", sha256="fcc83d5f8e2a665f2edfa29c85e658c0cc54bde0e4e21a20d9429350c374109c", url="https://pypi.org/packages/5f/3c/962ec71d0d42fefd9c907d528a54afe4d696f3b0ca16f3e1872ba018cd60/pyqtgraph-0.13.0-py3-none-any.whl")
    version("0.12.4", sha256="d98c6e26e9eda6d1d1bba92d6df381ef77fca18b701f9e136759ce31a17c6217", url="https://pypi.org/packages/83/44/d84034102ff3888ca33a7e7840b0a2831fbf5b9075918e5a88be1c733397/pyqtgraph-0.12.4-py3-none-any.whl")
    version("0.12.3", sha256="06997eaae40bfa2b870647f98384a63b12f75118303b674337a080f8eb9a0030", url="https://pypi.org/packages/bd/d6/162374003f3906a10e7427b17981b219822621d4b9e106d0f5030e3f02da/pyqtgraph-0.12.3-py3-none-any.whl")
    version("0.12.2", sha256="151f2616c75353fdfffa9915ad37b9391af86e5d42ec1e99cb1d1b3062e6353e", url="https://pypi.org/packages/a4/4c/f869feb87608b9425a3645efff80c27ace605ec67d57d92c1838c957f7c9/pyqtgraph-0.12.2-py3-none-any.whl")
    version("0.12.1", sha256="174a57300751bc41148a654d735218f3d6c76590b3107c9a43b9514294045b80", url="https://pypi.org/packages/6d/7a/6d07b9ea6ca1876fd7de15ebc34be407255f0d28bcd007b0cab816ede8e3/pyqtgraph-0.12.1-py3-none-any.whl")
    version("0.12.0", sha256="3d155b037a25aa6701c880d2f36e1101a95d0ceecce82897806d7e52d0ffd9f3", url="https://pypi.org/packages/f5/2f/60e8749bf264ecc5cdedec7b9230c165c54fb42601bbd9eca955127d1d12/pyqtgraph-0.12.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.13.4:")
        depends_on("py-numpy@1.22.0:", when="@0.13.4:")
        depends_on("py-numpy@1.20.0:", when="@0.13:0.13.3")
        depends_on("py-numpy@1.17.0:", when="@0.12")
    # END DEPENDENCIES

