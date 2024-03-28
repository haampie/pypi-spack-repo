# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJsonschemaSpecifications(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2023.12.1", sha256="87e4fdf3a94858b8a2ba2778d9ba57d8a9cafca7c7489c46ba0d30a8bc6a9c3c", url="https://pypi.org/packages/ee/07/44bd408781594c4d0a027666ef27fab1e441b109dc3b76b4f836f8fd04fe/jsonschema_specifications-2023.12.1-py3-none-any.whl")
    version("2023.11.2", sha256="e74ba7c0a65e8cb49dc26837d6cfe576557084a8b423ed16a420984228104f93", url="https://pypi.org/packages/d7/48/b62ccba8f4ac91817d6a11b340e63806175dafb10234a8cf7140bd389da5/jsonschema_specifications-2023.11.2-py3-none-any.whl")
    version("2023.11.1", sha256="f596778ab612b3fd29f72ea0d990393d0540a5aab18bf0407a46632eab540779", url="https://pypi.org/packages/20/a9/384ec45013ab883d7c2bf120f2988682986fdead973decf0bae28a4523e7/jsonschema_specifications-2023.11.1-py3-none-any.whl")
    version("2023.7.1", sha256="05adf340b659828a004220a9613be00fa3f223f2b82002e273dee62fd50524b1", url="https://pypi.org/packages/1c/24/83349ac2189cc2435e84da3f69ba3c97314d3c0622628e55171c6798ed80/jsonschema_specifications-2023.7.1-py3-none-any.whl")
    version("2023.6.1", sha256="3d2b82663aff01815f744bb5c7887e2121a63399b49b104a3c96145474d091d7", url="https://pypi.org/packages/a9/e9/856737e6b58e5be1778e73f7bcfe655041cfd2b16ff3c51fde76d8c6b69a/jsonschema_specifications-2023.6.1-py3-none-any.whl")
    version("2023.5.2", sha256="51d2972bf690cfe21970f722f878580d863f7c127d200fce671c5dae10b88f5f", url="https://pypi.org/packages/79/45/1f9d75340d8b151903cf50828fc54a0862343dc93bcc7ca0377f62755896/jsonschema_specifications-2023.5.2-py3-none-any.whl")
    version("2023.5.1", sha256="2914352153a22053662886c096a4d905a41e771f28baa52c86d135b359dc64ed", url="https://pypi.org/packages/18/d4/b0c10e87dd0b33cf3acafb9a389819954e716f5c7136116c4b3d6ae6e39a/jsonschema_specifications-2023.5.1-py3-none-any.whl")
    version("2023.3.6", sha256="a743d6acd3d6ce0aa4d691b001be145eb8d0075d5beb3ce77c4e17cb13ebf158", url="https://pypi.org/packages/de/5b/e74d5dcee46c38689c93038b0569881f57221a0847be54430d8deb7eb834/jsonschema_specifications-2023.3.6-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-importlib-resources@1.4:", when="@2022: ^python@:3.8")
        depends_on("py-referencing@0.31:", when="@2023.11:")
        depends_on("py-referencing@0.28:", when="@2023.5:2023.7")
        depends_on("py-referencing@0.25:", when="@2023.3.5:2023.3")
    # END DEPENDENCIES

