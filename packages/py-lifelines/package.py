# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLifelines(PythonPackage):
    # BEGIN VERSIONS
    version("0.25.5", sha256="ac2e4c12a6c350e77bc30e9e2e5625314c41c1dce4d07a0a6381b7ef8f8b8890", url="https://pypi.org/packages/39/8b/239479f5c4317fe92ccc9e8690b60fa6d4613125eae2c03062356b4c32dd/lifelines-0.25.5-py3-none-any.whl")
    version("0.9.4", sha256="0f19a8b18ace80c231de60487b2b1a3de3eb418445c6a6d0d72c1110d860f676", url="https://pypi.org/packages/b2/8f/dbc3a1f7636cb8ea5dc2ad2c287ce95ac16e492da503d143dab1f9948f80/lifelines-0.9.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.28:")
        depends_on("python@:3.10,3.12:", when="@0.27.3")
        depends_on("py-autograd@1.3:", when="@0.22.3:0.27.3")
        depends_on("py-autograd-gamma@0.3:", when="@0.22.1:")
        depends_on("py-matplotlib@3.0.0:", when="@0.20:")
        depends_on("py-numpy@1.14.0:", when="@0.22.2:0.25.9,0.25.11:0.27.7")
        depends_on("py-pandas@0.23.0:", when="@0.20.4:0.26")
        depends_on("py-patsy@0.5:", when="@0.25.1:0.25.7")
        depends_on("py-scipy@1.2.0:", when="@0.24:")
    # END DEPENDENCIES

