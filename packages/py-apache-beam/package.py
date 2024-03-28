# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyApacheBeam(PythonPackage):
    # BEGIN VERSIONS
    version("2.54.0", sha256="4a8675de29afef7e128349b031ebcfee2e08d39c205bdb1855051ef122a11803", url="https://pypi.org/packages/5b/d6/3f2c9be542cb8f5cdbb2a1fd7ab9f00b62414742b9d48334aa09c5d3251e/apache-beam-2.54.0.tar.gz")
    version("2.53.0", sha256="06b41f182f8a15cd248930fbc517a2f1f87daef2fd2006f1b5f74abf81010405", url="https://pypi.org/packages/6f/aa/d883d7e6c80ee098c504319a9fdb53ff4989aab593a3944b3dbaa29361b2/apache-beam-2.53.0.tar.gz")
    version("2.52.0", sha256="605ca0c80ea34d5af43eb7c6f8697b8fff7f799f271f286fb861aadc32d7148c", url="https://pypi.org/packages/d6/ef/8cebb992981c1b95ae0f2ba437148eba8538181032264cb722aadab1f2d6/apache-beam-2.52.0.tar.gz")
    version("2.51.0", sha256="2303bc6030072b033a567abb8c20de1d00faa86a69e2b168a952c3b692af97a2", url="https://pypi.org/packages/89/d5/48ca435cac3d73a422bcb1f51ffdeebbcee6b89107ebc5b0c3cc2f35857a/apache-beam-2.51.0.zip")
    version("2.50.0", sha256="dcce384078c6ad7667da3bf11b19a82fcd54d1bb53e07f81ec5ca818047ad710", url="https://pypi.org/packages/5b/20/3c5f65d335652e7ee68e37f752f70f6c926a23e99d81ae46c3697638062a/apache-beam-2.50.0.zip")
    version("2.49.0", sha256="b4a72ef7f73bc254cf377d2363847cabbb4795e23db7a14a235e435a90e2cfac", url="https://pypi.org/packages/51/f8/919302054c4b0bebeddbeb5b3f53b5da3aa1decba4346dd7280112431102/apache-beam-2.49.0.zip")
    version("2.48.0", sha256="611b9e0015e9d1d2ca34b91453117ee5b54ca7446de505b95b2c5a5c4d9f4b1e", url="https://pypi.org/packages/78/bb/e3dac120444c9ac73b653bd6d396f746f0cc5a4c86afa9dcccdb71872b84/apache-beam-2.48.0.zip")
    version("2.47.0", sha256="31b235be2e6eee3f05ec9bae5731810289bab7771b56a333732964ade4b63d7e", url="https://pypi.org/packages/d1/2d/cd86f6428882df21725b9c75682f518457dd5cb54e2d2a7bfd8744c13358/apache-beam-2.47.0.zip")
    version("2.46.0", sha256="871e88fb137341f0f3d647ba36938b792db135cb08cfb0664c5124b81437c712", url="https://pypi.org/packages/28/6c/512a45761b06bb42a1a8dfa39b12e77ef3e399639ab3ce21da07ccff80eb/apache-beam-2.46.0.zip")
    version("2.45.0", sha256="7fed999def2e4e3bb9a062045249ee02eec97caf8293a9ecbe73e1812fa241d2", url="https://pypi.org/packages/09/07/a8cef9d9193a65f7d7a35d72b46c97cc3684eea7b7728a89f5accbb5f297/apache-beam-2.45.0.zip")
    version("2.24.0", sha256="55c50b1a964bacc840a5e4cc3b4a42c4ef09d12192d215ba3cad65d4d22e09dd", url="https://pypi.org/packages/ea/e1/c186bdbd462c6984da2a99d6a742c6f7f3e31f02fd4fbbad23a949bb47b2/apache-beam-2.24.0.zip")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cloudpickle@2.2.1:2", when="@2.52:")
        depends_on("py-crcmod@1.7:", when="@2.11,2.14:2.22,2.52:")
        depends_on("py-dill@0.3.1.1:0.3.1", when="@2.18:2.22,2.52:")
        depends_on("py-fastavro@0.23.6:", when="@2.52:")
        depends_on("py-fasteners", when="@2.52:")
        depends_on("py-grpcio@1.33.1:1.48.0-rc1,1.48.1:", when="@2.52:")
        depends_on("py-hdfs@2.1:", when="@2.11,2.14:2.22,2.52:")
        depends_on("py-httplib2@0.8:", when="@2.52:")
        depends_on("py-js2py@0.74:", when="@2.52:")
        depends_on("py-jsonpickle@3:", when="@2.53:")
        depends_on("py-jsonschema@4.0.0:", when="@2.52:")
        depends_on("py-numpy@1.14.3:1.24", when="@2.52:2.54")
        depends_on("py-objsize@0.6.1:", when="@2.54:")
        depends_on("py-objsize@0.6.1:0.6", when="@2.52:2.53")
        depends_on("py-orjson@3.9.7:", when="@2.52:")
        depends_on("py-packaging@22:", when="@2.52:")
        depends_on("py-proto-plus@1.7.1:", when="@2.52:")
        depends_on("py-protobuf@3.20.3:3,4.22:4.22.0-rc3,4.22.1:4.22,4.25:4", when="@2.52:")
        depends_on("py-pyarrow@3:14", when="@2.53:")
        depends_on("py-pyarrow@3:11", when="@2.52")
        depends_on("py-pyarrow-hotfix", when="@2.52.0-rc4:")
        depends_on("py-pydot@1.2:1", when="@2.14:2.22,2.52:")
        depends_on("py-pymongo@3.8:", when="@2.52:")
        depends_on("py-python-dateutil@2.8:", when="@2.16:2.22,2.52:")
        depends_on("py-pytz@2018:", when="@2.11,2.14:2.22,2.52:")
        depends_on("py-regex@2020.6.8:", when="@2.52:")
        depends_on("py-requests@2.24:", when="@2.52:")
        depends_on("py-typing-extensions@3.7:", when="@2.52:")
        depends_on("py-zstandard@0.18:", when="@2.52:")
    # END DEPENDENCIES

