##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureKeyvaultKeys(PythonPackage):
    version("4.9.0", sha256="05eff85600f2f288a38e5c818ff77c5121840d327e66188cfa7ad333defb545b", url="https://pypi.org/packages/ad/ce/2414b3cdc9cd2a2f09fb048eb2d5b7677dfce8ef89c0eb7efaec78f079fe/azure_keyvault_keys-4.9.0-py3-none-any.whl")
    version("4.8.0", sha256="d1080fa1ffcb3bc16fc3a6b7acce63c8f0e81ad0b498673b2871b162396674f0", url="https://pypi.org/packages/57/6e/8622fe03dc6c8d76faddd052cb67f8d2de7117d21ab0e2d40c1e121eabdd/azure_keyvault_keys-4.8.0-py3-none-any.whl")
    version("4.7.0", sha256="cab6d1efc19381c6d9b1a1c8e38c3673af5b2f5a98314c85cd3b725aff346e06", url="https://pypi.org/packages/00/fc/0dd62814c52558475371e3a7675e6048189802e2d0e082bbd271b23ad9c1/azure_keyvault_keys-4.7.0-py3-none-any.whl")
    version("4.6.1", sha256="ac3acb8ced51f29cb48c73f71a718ca77726d6670f4927feca17ca5047c47915", url="https://pypi.org/packages/f8/8f/ec53dab1f9c04f44b7d85e378324c41033dda76cde9c98d252472c012239/azure_keyvault_keys-4.6.1-py3-none-any.whl")
    version("4.5.1", sha256="337010172984ce969e3e448599a99eb5b2eecc7746534dd29345d28dd7c71d95", url="https://pypi.org/packages/45/dd/16bc8cfa717b0e069d4d85bbf02647c509fbeb52d368b4e96cb26b851a16/azure_keyvault_keys-4.5.1-py3-none-any.whl")
    version("4.5.0", sha256="0687aa41e6268a529f0ae56d6cfc5cc5562c54fbb7001d2554b54ceaa5506016", url="https://pypi.org/packages/70/b6/bba4789b66c4d19e3d12769f0605c56f6f60a082b49a52866627778c6d4f/azure_keyvault_keys-4.5.0-py3-none-any.whl")
    version("4.4.0", sha256="e12c5554f7f0d5547e52cc2e725e94825fb40db1dbde7c39ec8a7f1fd150c46d", url="https://pypi.org/packages/04/cc/65bf29b27d44c75c1e5b4d40530d56af4a2d1c8ee77b1b41b4f62d3a91cd/azure_keyvault_keys-4.4.0-py2.py3-none-any.whl")
    version("4.3.1", sha256="25cf889bbcafd8dee0e068fd48d84e24e11143bf85e35c68d997a222e4a0f7fb", url="https://pypi.org/packages/a5/7f/a626704af6f0fb36bdc16397b49ab313a7e7a801ded5b43c6a74391f536a/azure_keyvault_keys-4.3.1-py2.py3-none-any.whl")
    version("4.3.0", sha256="a50e6f663378f3603a66d80c7c01e9544ae7e9cfdf4d3a3ae92f5df9fb9f64da", url="https://pypi.org/packages/6d/3b/1dfc8170e2546424a21b89d459581ca2d9c40674025963bbcfff20c8f5f4/azure_keyvault_keys-4.3.0-py2.py3-none-any.whl")
    version("4.2.0", sha256="1f81de153d37a64bde43d2038371780159c71419d66671f8ee54079066584aa3", url="https://pypi.org/packages/52/d5/a7f1a6963efb2d24af77f250d9bcc63a56bbd9a494d4a345e84014c4f11a/azure_keyvault_keys-4.2.0-py2.py3-none-any.whl")
    version("4.1.0", sha256="baf18c6a4b1724a783531ae222a83a5c4600d7fbb581e4d694f3ee759ef18579", url="https://pypi.org/packages/bd/11/2b9f1b1dd59337f844b9f857e1bcd1db87af28f84716b6e44fbd48cffea6/azure_keyvault_keys-4.1.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-azure-common@1.1:", when="@:4.0,4.2.0:4.9.0-beta3")
        depends_on("py-azure-core@1.29.5:", when="@4.9.0:")
        depends_on("py-azure-core@1.24:", when="@4.7:4.7.0-beta1,4.8:4.9.0-beta3")
        depends_on("py-azure-core@1.20:", when="@4.5.0-beta6:4.6,4.7.0:4.7")
        depends_on("py-azure-core@1.7:", when="@4.2.0:4.5.0-beta4")
        depends_on("py-azure-core@1.2.1:", when="@4.0.1:4.2.0-beta1")
        depends_on("py-cryptography@2.1.4:", when="@4.0.0-beta3:")
        depends_on("py-isodate@0.6.1:", when="@4.8.0-beta2:")
        depends_on("py-msrest@0.6.21:", when="@4.4:4.7")
        depends_on("py-msrest@0.6.0:", when="@4.0.1:4.3")
        depends_on("py-six@1.12:", when="@4.4.0-beta3:4.8.0-beta1")
        depends_on("py-typing-extensions@4.0.1:", when="@4.8.0-beta2:")

