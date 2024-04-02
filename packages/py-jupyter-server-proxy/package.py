# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJupyterServerProxy(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.2.2", sha256="9420814a2f0ef629bd343b4f4e971d6a5ebceb56eabefd6ba03f590fe698cb82", url="https://pypi.org/packages/53/e6/35f9cf3fea354aa2befae9f34534e3312f0d719361585a5ada3ced3f73f8/jupyter_server_proxy-3.2.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-aiohttp")
        depends_on("py-jupyter-server@1.0.0:", when="@3.0.0:")
        depends_on("py-simpervisor@0.4:", when="@1.5.3:4.0")
    # END DEPENDENCIES

