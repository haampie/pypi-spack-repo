# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyvistaqt(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.11.0", sha256="21f88d7e6fb6cf11767807bf13684975759e61d642582a16ff5fcf8e12aa6a60", url="https://pypi.org/packages/ac/92/043070db56638897574ad7cdf3de08dce2170e0a1779c26b25c0de4ca5f6/pyvistaqt-0.11.0-py3-none-any.whl")
    version("0.10.0", sha256="91bf9f52f703e88a112d3237ace3818978559c5ac8f5dd60f292e34ecb25cad0", url="https://pypi.org/packages/74/f9/45fea0c8b59b78d68dae431aca467e680ab5156d9d49aa3d4f226690f048/pyvistaqt-0.10.0-py3-none-any.whl")
    version("0.9.1", sha256="5f1867b8df646f701f7303fa48d0db458e9451d9560bd8a58e264c83bc98e465", url="https://pypi.org/packages/3d/e4/9443e0f72403b291cf509a8e55cd8fc30e8b7651aa21dd1c33b33947d176/pyvistaqt-0.9.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-importlib-resources@5.10.2:", when="@0.10 ^python@:3.8")
        depends_on("py-pyvista@0.32.0:")
        depends_on("py-qtpy@1.9:")
    # END DEPENDENCIES

