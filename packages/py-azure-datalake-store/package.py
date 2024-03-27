##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureDatalakeStore(PythonPackage):
    version("0.0.53", sha256="a30c902a6e360aa47d7f69f086b426729784e71c536f330b691647a51dc42b2b", url="https://pypi.org/packages/88/2a/75f56b14f115189155cf12e46b366ad1fe3357af5a1a7c09f7446662d617/azure_datalake_store-0.0.53-py2.py3-none-any.whl")
    version("0.0.52", sha256="aaed72b9c856824aeab554f4dbe0ef2c6d0ff36700bdd8b93d8298793117c48e", url="https://pypi.org/packages/6d/8d/740066a475b4a98c752c47096501376c3cd385beb798bd2a2cb47f7d8b69/azure_datalake_store-0.0.52-py2.py3-none-any.whl")
    version("0.0.51", sha256="c8f4f8d4fe85f6c3bec9642e2c0762b8ad0edae25252ae3115de38b74ee540d2", url="https://pypi.org/packages/4d/4d/9a2c21ae74e4169ee45e13a3a74be68d3b7422aa4063fc65b730df16761c/azure_datalake_store-0.0.51-py2.py3-none-any.whl")
    version("0.0.50", sha256="8cca65c26df530fd3d012f90fb01401b384cf4982e23336ec760af712a719343", url="https://pypi.org/packages/b7/0b/911f64ed11bd4b8950c3573ebb2c14248df8b3e1efc2ccdfea6a16f00047/azure_datalake_store-0.0.50-py2.py3-none-any.whl")
    version("0.0.49", sha256="cdb6ad7d3a097e1b3945275f719a00c3497adcc982ad8af6c4b3e8244f6749ec", url="https://pypi.org/packages/c2/97/9cb8576593eef19f3d4c20f8ec7302ff2cc342b75ec6b454f5125bc18421/azure_datalake_store-0.0.49-py2.py3-none-any.whl")
    version("0.0.48", sha256="b35108939f9ac4b6bc568e9b735e3e38a5fdabe00065073b5e48659929d536d1", url="https://pypi.org/packages/27/9a/e7140775b3f8f011ef5d001c12a3519310094375671950105519e30bb12b/azure_datalake_store-0.0.48-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-adal@0.4.2:", when="@:0.0.1,0.0.10:0.0.12,0.0.14:0.0.52")
        depends_on("py-cffi", when="@:0.0.1,0.0.10:0.0.12,0.0.14:")
        depends_on("py-msal@1.16:", when="@0.0.53:")
        depends_on("py-requests@2.20:", when="@0.0.35:")

