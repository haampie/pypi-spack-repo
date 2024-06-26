# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJupyterServerTerminals(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.4.4", sha256="75779164661cec02a8758a5311e18bb8eb70c4e86c6b699403100f1585a12a36", url="https://pypi.org/packages/ea/7f/36db12bdb90f5237766dcbf59892198daab7260acbcf03fc75e2a2a82672/jupyter_server_terminals-0.4.4-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@0.4.1:")
        depends_on("py-terminado@0.8.3:", when="@:0.1,0.3:")
    # END DEPENDENCIES


        # marker: os_name == "nt"
        # depends_on("py-pywinpty@2.0.3:", when="@:0.1,0.3:")
