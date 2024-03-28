# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJupyterServerTerminals(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.5.3", sha256="41ee0d7dc0ebf2809c668e0fc726dfaf258fcd3e769568996ca731b6194ae9aa", url="https://pypi.org/packages/07/2d/2b32cdbe8d2a602f697a649798554e4f072115438e92249624e532e8aca6/jupyter_server_terminals-0.5.3-py3-none-any.whl")
    version("0.5.2", sha256="1b80c12765da979513c42c90215481bbc39bd8ae7c0350b4f85bc3eb58d0fa80", url="https://pypi.org/packages/7c/ec/ebb52454525e1d346bfa2ea91b3dcda3b92687bb73b2c25a6d621d9eeaf1/jupyter_server_terminals-0.5.2-py3-none-any.whl")
    version("0.5.1", sha256="5e63e947ddd97bb2832db5ef837a258d9ccd4192cd608c1270850ad947ae5dd7", url="https://pypi.org/packages/13/50/9e4688558eb1a20d16e99171af9026be27d31a8b212c241595241736811a/jupyter_server_terminals-0.5.1-py3-none-any.whl")
    version("0.5.0", sha256="2fc0692c883bfd891f4fba0c4b4a684a37234b0ba472f2e97ed0a3888f46e1e4", url="https://pypi.org/packages/63/9a/98d252b7977ac3aa0aa4152b87b356e2048d4b193f38840c0e00dd85fadc/jupyter_server_terminals-0.5.0-py3-none-any.whl")
    version("0.4.4", sha256="75779164661cec02a8758a5311e18bb8eb70c4e86c6b699403100f1585a12a36", url="https://pypi.org/packages/ea/7f/36db12bdb90f5237766dcbf59892198daab7260acbcf03fc75e2a2a82672/jupyter_server_terminals-0.4.4-py3-none-any.whl")
    version("0.4.3", sha256="ec67d3f1895d25cfb586a87a50b8eee13b709898a4afd721058e551e0a0f480d", url="https://pypi.org/packages/c3/5e/c8433b8c9b9f5638c1f4f11d75cddb7e5819f3742d7f7a4bfff8aee664d3/jupyter_server_terminals-0.4.3-py3-none-any.whl")
    version("0.4.2", sha256="c0eaacee6cac21b597c23c38dd523dc4e9b947f97af5101e0396c08f28db3e37", url="https://pypi.org/packages/5e/85/279bb5a32f7f49a6c68964a19871b3ac27a03ac47783879a860ca4d26598/jupyter_server_terminals-0.4.2-py3-none-any.whl")
    version("0.4.1", sha256="7dec54557b1de2bfa5c72ea79475a0b10da2224639916ff3df43ba7e100a535c", url="https://pypi.org/packages/b1/3c/0651895fae267acac20852774c8fe9c0a33df619d44a7587d519ab2407b6/jupyter_server_terminals-0.4.1-py3-none-any.whl")
    version("0.4.0", sha256="325508eab9cb2f5ed12f50ac5f3b6bfae484756ad10ff1ef5b946c60ba4a3835", url="https://pypi.org/packages/38/8c/b07e602a33389ed99f707f7d428b2b2502500666cd448bf2e328f8521a4d/jupyter_server_terminals-0.4.0-py3-none-any.whl")
    version("0.3.2", sha256="5e677bc52e225ab49e168306d7d3fb9a32df5810477c245fa6bb4dc7f2df92cc", url="https://pypi.org/packages/22/10/667f326c78a7842958bda2b2eb7fb47839b15215ffbe89ab5dc8858bb1b2/jupyter_server_terminals-0.3.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-terminado@0.8.3:", when="@:0.1,0.3:")

        # marker: os_name == "nt"
        # depends_on("py-pywinpty@2.0.3:", when="@:0.1,0.3:")
    # END DEPENDENCIES

