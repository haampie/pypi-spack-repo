##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureKeyvaultCertificates(PythonPackage):
    version("4.8.0", sha256="6466b8ce33b628d7336e5f4fba3e18fb9a42f1342f19a7e4029f69b1b2fa1198", url="https://pypi.org/packages/20/f0/e5404eb87d20a6937a6672b070f820b5b6e81050723eea8494b04e3699df/azure_keyvault_certificates-4.8.0-py3-none-any.whl")
    version("4.8.0-beta3", sha256="8c0c3ad364a7b42061a8049e983a4a0b6051aed7bf1de49281d46193a5e99e09", url="https://pypi.org/packages/a6/a3/62d9ee5308665b37ce619c4bd84fd2cf49f5d0ce09ac52edc6ac708a3065/azure_keyvault_certificates-4.8.0b3-py3-none-any.whl")
    version("4.7.0", sha256="4ddf29529309da9587d9afdf8be3c018a3455ed27bffae9428acb1802789a3d6", url="https://pypi.org/packages/a4/14/fbdca7fba9ae90f550a64f4f1c96dc294b09116a17d1ad73c72977da29d4/azure_keyvault_certificates-4.7.0-py3-none-any.whl")
    version("4.6.0", sha256="e64e55444d30375c7efcd80078e49fada8ae5125657a7d31d73ddd32eb7b69ca", url="https://pypi.org/packages/21/09/b23afd6b20b28dd60c6fca543498d49b43cbc3f7af190a47d7c5090901d8/azure_keyvault_certificates-4.6.0-py3-none-any.whl")
    version("4.5.1", sha256="0ebd1a150d99884a7fa915e03cdcc936089d1b86cdf0f81f8d88feade9a101a2", url="https://pypi.org/packages/39/01/5a85f727894642cb28bed48711d09eea20da08429df01c0db745af1920de/azure_keyvault_certificates-4.5.1-py3-none-any.whl")
    version("4.4.0", sha256="ef122c36cdc3e0d4612dc5c5b1beebb7a09144a71d5c9597b0ea677f62afde1a", url="https://pypi.org/packages/e6/9f/249b689c1fc9a135a47395b1249f3a178c6bb507860aed92aec11a5dbb4f/azure_keyvault_certificates-4.4.0-py3-none-any.whl")
    version("4.3.0", sha256="c332e2d35d25d52e8f8601c0a213a693b2bd664e1429e952c4da6e40e30bbe6f", url="https://pypi.org/packages/03/e5/7b2609ba13210072ce555395f07cd1c8259ff295501241b5274ce28bc58f/azure_keyvault_certificates-4.3.0-py2.py3-none-any.whl")
    version("4.2.1", sha256="9959a1e49cac4dfaa8e7e36c86fe7d7c4159a3b76a29788d042d41ec41200a8b", url="https://pypi.org/packages/23/2b/e3219ae48391263b4657817b61eb5104ac1190d360e288e4546a18e61ca5/azure_keyvault_certificates-4.2.1-py2.py3-none-any.whl")
    version("4.2.0", sha256="1954404eed6806e7f00cabd15e20d4816e0893468f8972c518f08f111df2540d", url="https://pypi.org/packages/69/24/6ef689b2c6433de7a047fbeb967aa685f0f182c9ddf7bd92c5cb76563606/azure_keyvault_certificates-4.2.0-py2.py3-none-any.whl")
    version("4.1.0", sha256="763f4db3cfa4e1ae86d05812276fa50c6d67269eb77926b8367c09c669f5df79", url="https://pypi.org/packages/4c/98/d557642c6a2f610475edae7a772eeffcfb4bf02f690994e2fba502176fab/azure_keyvault_certificates-4.1.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-azure-common@1.1:", when="@:4.0,4.2.0:4.8.0-beta3")
        depends_on("py-azure-core@1.29.5:", when="@4.8.0:")
        depends_on("py-azure-core@1.24:", when="@4.7:4.8.0-beta3")
        depends_on("py-azure-core@1.20:", when="@4.4.0:4.6")
        depends_on("py-azure-core@1.7:", when="@4.2.0:4.4.0-beta1")
        depends_on("py-azure-core@1.2.1:", when="@4.0.1:4.2.0-beta1")
        depends_on("py-isodate@0.6.1:", when="@4.7:")
        depends_on("py-msrest@0.6.21:", when="@4.3:4.6")
        depends_on("py-msrest@0.6.0:", when="@4.0.0-beta6:4.2")
        depends_on("py-six@1.11:", when="@4.5:4.6")
        depends_on("py-typing-extensions@4.0.1:", when="@4.7:")

