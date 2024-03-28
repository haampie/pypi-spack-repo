# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkThreadnetwork(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="f7ad31b4a67f9ed00097a21c7bbd48ffa4ce2c22174a52ac508beedf7cb2aa9e", url="https://pypi.org/packages/e2/6a/650232363d6563c5e4b287da34ba8ff3122ee56e9b861b3c1a16645ad697/pyobjc_framework_ThreadNetwork-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="720d4a14619598431a22be2a720bf877f996d65cee430b96c5d7ec833b676b68", url="https://pypi.org/packages/0d/bf/24a5dbc3ee6c48098fa4792ccc12c5afe87a5b1fd67dd702bfa1665d4d50/pyobjc_framework_ThreadNetwork-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="f4f24ad1457e2a89c80f3aa5133e8015e67cbd0e2654d8f08abe0f4690eb7cb3", url="https://pypi.org/packages/17/69/eab5013cd199e908d5814a2c0f5a5fd33ed6898fb9b85c655d8135009ecf/pyobjc_framework_ThreadNetwork-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="24db5b1ec9fd4ffd7198c6ec0ca7ab8d19333b6af746096be2a08c49dac07db3", url="https://pypi.org/packages/07/eb/c237863e96ab065f2525e1c46ffe136dd03c90f0ca890b3f2a5c71ea3b12/pyobjc_framework_ThreadNetwork-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="667c767f0c491c06aa7bfebd78fdc38f22602bb951c8ac58ffc14a09f98ad9f3", url="https://pypi.org/packages/4b/a6/a24e92d62c4644e2e991734c92f0c9f1c6dea432ba3c449c10c092f46656/pyobjc_framework_ThreadNetwork-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="f0b840693380c7b4316538948eeaeca200d6e3def3228cc5ceceff943c34b6ae", url="https://pypi.org/packages/ef/19/3e5867336724818dcd8eba5e4d9f3ac48b74ebb0cb5bbbe7300113d4e91b/pyobjc_framework_ThreadNetwork-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="791fcb393d0ba4c42dd0225b852b07f84ab52faff938370cdc63892ebd871512", url="https://pypi.org/packages/a1/71/bd0fffb939219d215b9d682e95ae0b90fe641992932f4c35ab55a169f40b/pyobjc_framework_ThreadNetwork-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="41dc1a5b2d8fa452618481c5487f5e0d027e6467019fd1112757cc9d2ba0ec9c", url="https://pypi.org/packages/75/6a/2f7216b95833d95d0234d7b13f933da983639734b6804ccafbfecd0fbccc/pyobjc_framework_ThreadNetwork-9.0-py2.py3-none-any.whl")
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
        depends_on("py-pyobjc-core@9:", when="@:9.0.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-cocoa@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-cocoa@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-cocoa@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-cocoa@9:", when="@:9.0.0")
    # END DEPENDENCIES

