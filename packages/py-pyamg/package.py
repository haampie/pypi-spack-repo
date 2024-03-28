# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyamg(PythonPackage):
    # BEGIN VERSIONS
    version("5.0.0", sha256="eab967228f614342ce23c7b4d6bbca25ad8b927a45cb7626d1ef17c9f062a02e", url="https://pypi.org/packages/dd/22/e8c569797fc2ffb6c5115237eeb60f48201d63792d8a829b0f997839cafa/pyamg-5.0.0.tar.gz")
    version("4.2.3", sha256="37ad3c1dcaff2435c2ab7c8ec36942af0726c563d35059bcd18eb07473f7182e", url="https://pypi.org/packages/6d/1a/c6602b4e25093563c9f7a9b79fd462b2db9076043471588c96e307255fc2/pyamg-4.2.3.tar.gz")
    version("4.1.0", sha256="b4cacfcfd13379762a4551ac059a2e52a093b476ca1ad44b9202e736490a8863", url="https://pypi.org/packages/28/a5/cffa0f1ca92f0b145f0989212a559ba616911354bf9551070954d7c83166/pyamg-4.1.0.tar.gz")
    version("4.0.0", sha256="3ceb38ffd86e29774e759486f2961599c8ed847459c68727493cadeaf115a38a", url="https://pypi.org/packages/10/02/a1a320517c930fac45e48fe061d2a3365d3290c73751241f7550c44bd69d/pyamg-4.0.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.7:", when="@3.2.1:4.0")
        depends_on("py-pybind11@2.2:", when="@4:4.0")
        depends_on("py-pytest", when="@3.2.1:4.0")
        depends_on("py-scipy@0.12:", when="@3.2.1:4.0")
    # END DEPENDENCIES

