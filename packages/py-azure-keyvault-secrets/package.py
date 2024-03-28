# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureKeyvaultSecrets(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("4.8.0", sha256="e5898c87cef95e54a8c4aa48cdbf4717ee30543a10b793c95bd57a476554a893", url="https://pypi.org/packages/a4/7e/4f3cd27b284e478b32835717aa19888405e42e72ffc9b774618c3a776fb1/azure_keyvault_secrets-4.8.0-py3-none-any.whl")
    version("4.8.0-beta2", sha256="7e3c9823ce72826363b13641171704554f270f7d38392a78def6b9e45e22eec4", url="https://pypi.org/packages/5b/fc/2eb2c7b92fd3da18afea12adc1abc1d0fbb4e3e7881035aa11ac9136c170/azure_keyvault_secrets-4.8.0b2-py3-none-any.whl")
    version("4.8.0-beta1", sha256="a4f896733e1168fa62b7706f914abc86934c60169800fb2f2e2a2f38a3d7865a", url="https://pypi.org/packages/aa/55/65835a5a3e182361fc51549bdfcfa964e9df94e5e198e1ab21cc7bd46b32/azure_keyvault_secrets-4.8.0b1-py3-none-any.whl")
    version("4.7.0", sha256="a16c7e6dfa9cba68892bb6fcb905bf2e2ec1f2a6dc05522b61df79621e050901", url="https://pypi.org/packages/d0/cf/92298854e657c29d31f9b028dec3ce9802467bff97c74d6c4145e9cfa96f/azure_keyvault_secrets-4.7.0-py3-none-any.whl")
    version("4.6.0", sha256="79369336c91b2dcadd2b53127cc2d2700421fcfd0d51e4131a6afec314eca90e", url="https://pypi.org/packages/62/21/475561b608aa0b8a253d667df1ae96c1a681f75f49042d1e0caf13f19cfa/azure_keyvault_secrets-4.6.0-py3-none-any.whl")
    version("4.5.1", sha256="6a1cbd6272c0fcd0f80f3aea59bbe982decb4bc92b8a7f991c94113fc94b4b79", url="https://pypi.org/packages/bd/05/4351e9db88b119c0f626d8dc5d99d9666f290d83f1e1f069cd8b7da3c123/azure_keyvault_secrets-4.5.1-py3-none-any.whl")
    version("4.4.0", sha256="7143c6e83398a7aba048e44413f7f26b6ce43505afb3e3c89ba62b25f06dd729", url="https://pypi.org/packages/66/37/10bcbf618f05b33f7cc2060f68f36f81947dc90851e48be97b6c8eea1099/azure_keyvault_secrets-4.4.0-py3-none-any.whl")
    version("4.3.0", sha256="fa4d780565520534939a4b1b4e87908f0c88b4423f6005c7a381ac01d6b32233", url="https://pypi.org/packages/34/35/8dde014664f144f2050d3072ced916b4ffcdd53748b0c7f08e1387e9403b/azure_keyvault_secrets-4.3.0-py2.py3-none-any.whl")
    version("4.2.0", sha256="08b8aa518590c394477514f4a0a5d9e557a00ff164de9f6f6e7b112f8d5e6aa1", url="https://pypi.org/packages/43/ae/4ad0c67e54f820d0ead249ce48e8cf498cfee42034dcd837d8f218ba9e76/azure_keyvault_secrets-4.2.0-py2.py3-none-any.whl")
    version("4.1.0", sha256="743a2eabb2bbb21d50b46fa6b321361b9b61121387ec35c0f3d953778793c179", url="https://pypi.org/packages/6e/66/dc763e4ad80ea059d2a3df55fab8fbfb9ce39f79c0fd38f9c469d05bdbea/azure_keyvault_secrets-4.1.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-common@1.1:", when="@:4.0,4.2.0:4.8.0-beta2")
        depends_on("py-azure-core@1.29.5:", when="@4.8.0:")
        depends_on("py-azure-core@1.24:", when="@4.7:4.8.0-beta2")
        depends_on("py-azure-core@1.20:", when="@4.4.0:4.6")
        depends_on("py-azure-core@1.7:", when="@4.2.0:4.4.0-beta1")
        depends_on("py-azure-core@1.2.1:", when="@4.0.1:4.2.0-beta1")
        depends_on("py-isodate@0.6.1:", when="@4.7:")
        depends_on("py-msrest@0.6.21:", when="@4.3:4.6")
        depends_on("py-msrest@0.6.0:", when="@4.0.1:4.2")
        depends_on("py-six@1.11:", when="@4.5:4.6")
        depends_on("py-typing-extensions@4.0.1:", when="@4.7:")
    # END DEPENDENCIES

