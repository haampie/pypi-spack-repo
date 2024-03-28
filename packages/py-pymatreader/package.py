# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPymatreader(PythonPackage):
    # BEGIN VERSIONS
    version("0.0.32", sha256="30fbe85ef919bcd7707fa9b7dfaf90f2d26d59ff1de84ab425a1a0a7e85a6f8a", url="https://pypi.org/packages/aa/d5/8e74f943efba658bc34702ff8032287a62a0a07f213b523347a2a597fa26/pymatreader-0.0.32-py3-none-any.whl")
    version("0.0.31", sha256="632003d32b3e46cacfca9aa0952d8a843edfd9770d266cdc5b018c16ac46d55f", url="https://pypi.org/packages/8e/8f/6120fcb9cd4970da52f2ecd2789a4c6169db20cdd2a5d20c0e23b16eb215/pymatreader-0.0.31-py3-none-any.whl")
    version("0.0.30", sha256="d5719dd9b4d018c7ec59c69ed1320d15eb5957eb071e8d01d9b4f6468779cc25", url="https://pypi.org/packages/11/b1/9d2db885e5bfbd6b552090f4d0fb80d05f9c555f9b6f4e37135d164304a7/pymatreader-0.0.30-py3-none-any.whl")
    version("0.0.29", sha256="653f1a10a8290e9328d8cd90c42e62378a02a7ad814af32346a29fda1b70ffe6", url="https://pypi.org/packages/33/b3/7d8127bd01bffb115e56390628896b38430b3e8bbae63700c3797ed5d600/pymatreader-0.0.29-py3-none-any.whl")
    version("0.0.27", sha256="eb290128f1d686960690dafd8555a2550df22e69a0e59a6e91b711fedc02559a", url="https://pypi.org/packages/fe/87/7451521d7015d9aee22157c2bd7834596e4b4e2d968dd8b3466329b8de60/pymatreader-0.0.27-py3-none-any.whl")
    version("0.0.26", sha256="93aa09a5265fe430e43f6b085f9bd9131384c441c6600d2f9a60ce994cfee392", url="https://pypi.org/packages/7d/d1/65ae037bdbb62dbd0a368944307f8595f201486756cef813b189dd2b3b16/pymatreader-0.0.26.tar.gz")
    version("0.0.25", sha256="5095ea56017cb4a8a122eb41dcbe451f34ded026ba6fa23cc328abb808b60674", url="https://pypi.org/packages/72/e2/896fef48187a0f2b49ce6a0f6333b1e3f065416d3153eba100088f3f5afc/pymatreader-0.0.25.tar.gz")
    version("0.0.24", sha256="e0d8b3e18c46057930b5ebb93591ebdc4c399486d020c20432a0296c1062538c", url="https://pypi.org/packages/2f/aa/62a7a27b66be1e7ca0621a5bb71edd3410f3fb1b58bcbe5c92d9caa9279c/pymatreader-0.0.24.tar.gz")
    version("0.0.23", sha256="dff4fa7bcb204d3efd066d64da123daad6ffa7a8fe23918722f4a050a2516e64", url="https://pypi.org/packages/de/2a/01990e62c70b02e512dbb4fb4c4b078b9db60162d9c51f4c6d9775398683/pymatreader-0.0.23.tar.gz")
    version("0.0.22", sha256="068e73425ead5a12eb3046ae4376cd99da017c41c189bd44be0b46e691c699a1", url="https://pypi.org/packages/b9/17/7469cc22621a19d1940fd0e096cdace35574f9aa0969b190ab1efc009798/pymatreader-0.0.22.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-future", when="@0.0.27:0.0.30")
        depends_on("py-h5py", when="@0.0.27:")
        depends_on("py-numpy", when="@0.0.27:")
        depends_on("py-scipy@:1.7.0-rc2,1.7.1:", when="@0.0.27:")
        depends_on("py-xmltodict", when="@0.0.27:")
    # END DEPENDENCIES

