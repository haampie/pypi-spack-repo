# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCallflow(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.1.2", sha256="1ee116c5c7282d89b1d168d079d3b77f15cf05762a3b7e8b102b895aed3bae82", url="https://pypi.org/packages/64/a9/e6dc4b21978427c2ed40ce8510af59921b0caced9e4791e196ef2a6621b4/CallFlow-1.1.2-py3-none-any.whl")
    version("1.1.1", sha256="ecc82351e9bb80d0c8285c78db57f257ac06d6ba7049297ade3156d24f37d8b8", url="https://pypi.org/packages/03/62/bd8263a18c108b986765d8fb30f0f77825a00eab088a23faca05da870708/CallFlow-1.1.1-py3-none-any.whl")
    version("1.1.0", sha256="d33320a2ec450520624c3357e2cabef35cded82ad76378f4a0a41d44b0608bf8", url="https://pypi.org/packages/57/67/39cf3f86ad8b6315af50fe30d2db9ffedc6663a0ded6ac60eadd94d262cf/CallFlow-1.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-colorlog", when="@1.1.1:1.1")
        depends_on("py-flask", when="@:1.1.0")
        depends_on("py-flask-socketio", when="@:1.1")
        depends_on("py-hatchet", when="@:1.1")
        depends_on("py-ipython", when="@1.1.1:1.1")
        depends_on("py-jsonschema", when="@1.1.1:1.1")
        depends_on("py-matplotlib", when="@1.1.1:1.1")
        depends_on("py-networkx", when="@:1.1")
        depends_on("py-numpy", when="@:1.1")
        depends_on("py-pandas", when="@:1.1")
        depends_on("py-scikit-learn", when="@1.1.1:1.1")
        depends_on("py-scipy", when="@1.1.1:1.1")
        depends_on("py-statsmodels", when="@:1.1")
        depends_on("py-tables", when="@:1.1.0")
    # END DEPENDENCIES

