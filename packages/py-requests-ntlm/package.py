# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRequestsNtlm(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.2.0", sha256="b7781090c647308a88b55fb530c7b3705cef45349e70a83b8d6731e7889272a6", url="https://pypi.org/packages/b6/0b/84787a85a4aee9860a510747e9a0cffd08ebfa32d9c728b0db6306883ad1/requests_ntlm-1.2.0-py3-none-any.whl")
    version("1.1.0", sha256="1eb43d1026b64d431a8e0f1e8a8c8119ac698e72e9b95102018214411a8463ea", url="https://pypi.org/packages/03/4b/8b9a1afde8072c4d5710d9fa91433d504325821b038e00237dc8d6d833dc/requests_ntlm-1.1.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cryptography@1.3:", when="@1.1:")
        depends_on("py-ntlm-auth@1.0.2:", when="@1:1.1")
        depends_on("py-pyspnego@0.1.6:", when="@1.2:")
        depends_on("py-requests@2:", when="@0.3:")
    # END DEPENDENCIES

