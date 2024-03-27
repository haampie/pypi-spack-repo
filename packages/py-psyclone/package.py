##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPsyclone(PythonPackage):
    version("2.5.0", sha256="91d1743d9431f337e1c89c6bdfe74f4247a12b9af01bc78f5fe63706a59faec5", url="https://pypi.org/packages/ae/0c/9eeb55d9fe0cf54da09dfbe585d64c4d1e9960022a858ef8aaf82140c773/PSyclone-2.5.0-py3-none-any.whl")
    version("2.4.0", sha256="4bcb92168aac640acd16ab1508c78e990ff753eaabe5ce38b7c3b15575272b31", url="https://pypi.org/packages/7a/24/ebf8f67b8e683fd82528a2791ef1a1454781b822994f35fab2c0a1428fec/PSyclone-2.4.0-py3-none-any.whl")
    version("2.3.1", sha256="a7b844bbd629ae76cf30f36b7d9a477ae2e7937eab7aa464c8f2d6eaee1d6d02", url="https://pypi.org/packages/da/24/58eb4f53a6eb9d4f67306077cb21e34aafdbd408099e772be3a282b1a4b3/PSyclone-2.3.1-py3-none-any.whl")
    version("2.3.0", sha256="5ad8825fdaf12277d95fcf6b3a84afe603cba9e7d9cba84395c0651180359d42", url="https://pypi.org/packages/ca/14/39e74a3242e1012235ac8f9148b78686eb7e99ce50d6355e03217df0518a/PSyclone-2.3.0-py3-none-any.whl")
    version("2.2.0", sha256="e520f431bd8836a1ec17253fad54540690e6af84b7ac62329ff1fc257fdbe97e", url="https://pypi.org/packages/fe/ab/de724cb4e67a868e1ea8561bc3dbd098df14694144b24a771d4f3f82f4e3/PSyclone-2.2.0-py3-none-any.whl")
    version("2.1.0", sha256="860418e922dab9895adacd5883853fecdf01464f12233335ef7edf2c3aa9e623", url="https://pypi.org/packages/05/db/021ab7ab61c0de03eb4c655e3ad4761a69f8b10bb8edac24eb306494d99a/PSyclone-2.1.0-py3-none-any.whl")
    version("2.0.0", sha256="b78ba200e96585acba2b1d16dfd7ab00e9b8a9bf448bda21f416bb57dc33cf64", url="https://pypi.org/packages/e3/c5/3cf8d871c14433bfba4297f91d62661ef683c3ea0fb80f656d83f0f54ade/PSyclone-2.0.0-py3-none-any.whl")
    version("1.5.1", sha256="f053ad7316623b2a4002afc79607abda3b22306645e86f2312d9f3fe56d312dc", url="https://pypi.org/packages/d4/0f/3e0690a9522465bc13e2ec423a5dd7f1fb500ba9daa672b52b0488559c60/PSyclone-1.5.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-configparser", when="@1.9:")
        depends_on("py-fparser@0.1.4:", when="@2.5:")
        depends_on("py-fparser@0.1.3", when="@2.4")
        depends_on("py-fparser@0.0.16:0.0", when="@2.3.1:2.3")
        depends_on("py-fparser@0.0.15", when="@2.3:2.3.0")
        depends_on("py-fparser@0.0.14", when="@2.2")
        depends_on("py-fparser@0.0.13", when="@2.1")
        depends_on("py-fparser@0.0.12", when="@2:2.0")
        depends_on("py-jsonschema", when="@2.5:")
        depends_on("py-jsonschema@3.0.2:3.0", when="@2.1:2.4")
        depends_on("py-pyparsing", when="@1.9:")
        depends_on("py-six", when="@1.9:2.3")
        depends_on("py-sympy", when="@2.2:")

