##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPystache(PythonPackage):
    version("0.6.5", sha256="84546278219431f1a2ecc86a627cc1b0fe3c83b5612f8a7d9c81ea0119ac8f49", url="https://pypi.org/packages/e3/92/18f89156ffdb31115a29c98a3a1280aa248c5eec6fda5a6fb64168a6d069/pystache-0.6.5-py3-none-any.whl")
    version("0.6.4", sha256="ae510c1053ba573e46b7532cead8c90c9f1c6974c593bd0aa44f70ea64b23a94", url="https://pypi.org/packages/05/e6/190fb00dc30951a4843d1b88badb39ea709c8d34bc0e1bf0c68a56e110f1/pystache-0.6.4-py3-none-any.whl")
    version("0.6.2.dev28", sha256="86a78eddc2d8e31266c1ce8ae7dc9f2aec8e3ed9a043e8827163a12dd38052ca", url="https://pypi.org/packages/1a/b2/f725ae189e76ef0a64d0ce5b0e75c48a37adb26d7b6f05cfe977f744fcc0/pystache-0.6.2.dev28-py3-none-any.whl")
    version("0.6.0", sha256="93bf92b2149a4c4b58d12142e2c4c6dd5c08d89e4c95afccd4b6efe2ee1d470d", url="https://pypi.org/packages/3f/e7/8750ba6c6101d6aa5ceeb20c013adf2c6f3554a12c71d75654b468404bfa/pystache-0.6.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-importlib-metadata@4.6:", when="@:0.0,0.6.5: ^python@:3.9")

