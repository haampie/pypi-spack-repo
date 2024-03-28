# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkAdservices(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="b03fcd460b632fc1b3fd8275060255e518933d1d0da06d6eda9b128b4e2999ec", url="https://pypi.org/packages/ed/74/109e12c6ec935c883b9473e8ada60e49ac8b3591db303a570f8d9fdbc8b8/pyobjc_framework_AdServices-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="79ec6eb744635b72ffd0bdd5e55cb5ec57603633716861bbf40b236d8dba0dfd", url="https://pypi.org/packages/f5/3a/6314beea047c9a8f7dd4e1930e2725c0ffd1eba508f0dd2e0bfdeb1fdbc7/pyobjc_framework_AdServices-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="d3c9bb0c7da4c98879368ad22c6e558fff73c6d3d971ee5ac8bdd38f723f811b", url="https://pypi.org/packages/f1/83/980c266fbb872b72a359dfe8f3175e859f52d5bcb52d9257893a8cd8cef6/pyobjc_framework_AdServices-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="0b55fd918da4a5df2c878c59d9f0413cb94d6d0930c83de79bb9cc6d22149f8a", url="https://pypi.org/packages/5f/cb/3dd40a2d92647ec327cd1fcb0980734850cb161763a39c72713c8faccff7/pyobjc_framework_AdServices-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="9f60ea9150a8ca4e9511cd5c2786877b5e20f42d6418236341a4f5e8ca7dea8d", url="https://pypi.org/packages/13/ec/1e5070f804724e5e2e0a502108e58207fcef8bd7c8b3b3e53fe08dbd9e23/pyobjc_framework_AdServices-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="409e1f930c003a58000c2a6a16006908e55d48f0c61f50c5fb22e93ab6b5cd82", url="https://pypi.org/packages/7d/14/d64b299ba87246cd2e0387035b6c4e7afa7b3440f73711b98410bcd0afd8/pyobjc_framework_AdServices-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="a9e6265a26446ce897aecd97662659d8b861fe8fd808ad1dd4b808dff60b5a05", url="https://pypi.org/packages/99/ac/80c2a035e3560e7bbec2b151d3e876e655d519a8753ff35e9b9334c92f3a/pyobjc_framework_AdServices-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="29b4f26c066a2a4c7644d4d9990cd3595b036d9b1fa277029fc19680ae64c90a", url="https://pypi.org/packages/d9/4f/18b5b28daf0828b559c043612123e9cc049dde62aa6cd1d8c4827c950aa2/pyobjc_framework_AdServices-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="eb9dcf396af763f8755eb31970a13039ec72c29ae5872a1d427ac54cdff1c728", url="https://pypi.org/packages/69/20/1a9357eb51591bfea9af118127221f112bcf1063347487081a9a42344247/pyobjc_framework_AdServices-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="c0aa6123d4d2a9c8c427219024e291d299c9444d9fbf2ef82cf4f1b8efe076a9", url="https://pypi.org/packages/a4/4a/a200f8e3cfcca4b079f34bab96ee9364dee9f2c0af8013658a9a80e8204f/pyobjc_framework_AdServices-8.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-core@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-core@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-core@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-core@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-core@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-core@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-core@8.5:", when="@8.5:8.5.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-cocoa@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-cocoa@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-cocoa@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-cocoa@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-cocoa@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-cocoa@8.5:", when="@8.5:8.5.0")
    # END DEPENDENCIES

