##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySubmitit(PythonPackage):
    version("1.4.5", sha256="148022ea179bfebcd85df7fcf741c41c3d803eb2e67c1470f22e8b075c13dca6", url="https://pypi.org/packages/a0/4d/d5ab8bb1be0c2b066e9ca65ee74b124e791d491534d397da5bfe7a9a60f7/submitit-1.4.5-py3-none-any.whl")
    version("1.3.3", sha256="efaa77b2df9ea9ee02545478cbfc377853ddf8016bff59df6988bebcf51ffa7e", url="https://pypi.org/packages/bf/e9/c206d0199a71656ea2ceba9a96cf436a1c9581ecf171dfaf1cc54ec42d3a/submitit-1.3.3.tar.gz")

    with default_args(type="run"):
        depends_on("py-cloudpickle@1.2.1:", when="@1:1.1.0,1.4:")
        depends_on("py-typing-extensions@3.7.4.2:", when="@1:1.1.0,1.4:")

