##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGoogleCloudAppengineLogging(PythonPackage):
    version("1.4.3", sha256="8e30af51d853f219caf29e8b8b342b9ce8214b29f334dafae38d39aaaff7d372", url="https://pypi.org/packages/98/05/5a85665473aacae44094cdd0ee986b1893a5430172eb3980797cc5339d38/google_cloud_appengine_logging-1.4.3-py2.py3-none-any.whl")
    version("1.4.2", sha256="08d46bacf7e6bb4cb963dc5c0ab6995f2cd3fec69c7a2862405e98dce0c194bc", url="https://pypi.org/packages/ea/ce/f1378e69b78ac7738ee7e5a704a855a0924378f07d2c9cdca0fb91f00a3a/google_cloud_appengine_logging-1.4.2-py2.py3-none-any.whl")
    version("1.4.1", sha256="851dad2c4dd85dcf5b9e32879acda998a250e82c4d4f2bd5ef67b904840c7b17", url="https://pypi.org/packages/ea/4c/cc55e3ebaeca3cbb87441cd296051d5aafce3c9f5ff8b7f5b69549fc66a5/google_cloud_appengine_logging-1.4.1-py2.py3-none-any.whl")
    version("1.4.0", sha256="226721903a2d50b6e51c43e59edb548c0bb08cc5f70e1a5f289d3edf2f09a8c9", url="https://pypi.org/packages/f3/83/4a3b64bff9c57beebd405e894228702bd2f06ba093d812a1925c8455fb73/google_cloud_appengine_logging-1.4.0-py2.py3-none-any.whl")
    version("1.3.2", sha256="6ac6261567b56611f6891fa650f76db8a48d528762e5c2a09230b41d82ee2be0", url="https://pypi.org/packages/31/2c/5ca1eccbc69dbf62f2b4d5a002bb45dd9e76237862edde157ee1cdc9c9d7/google_cloud_appengine_logging-1.3.2-py2.py3-none-any.whl")
    version("1.3.1", sha256="8b1ec202de1ad4dbe5e40076af0324e179695b8dc4735c7dcedf6297786e761f", url="https://pypi.org/packages/1e/4c/aa3a0b051023f2e6cbe9a634a127b08a13e4c7d58609d707ce19b0c4bf69/google_cloud_appengine_logging-1.3.1-py2.py3-none-any.whl")
    version("1.3.0", sha256="97272ed554c9077d666e045b6686b46cb67e9b072aab76726c5404d6098b52d2", url="https://pypi.org/packages/07/04/4678121f095f4141ff2dd7450a5186d13b014c5262bf718d1db159ad41b0/google_cloud_appengine_logging-1.3.0-py2.py3-none-any.whl")
    version("1.2.0", sha256="8257fe68d0c2f4eb1085fde875e2929196e4ded9cb522c3faaddf14307e8e588", url="https://pypi.org/packages/82/07/eeba8e8b156e329e60869c7acff967194e18b845d30efc498212179c1b94/google_cloud_appengine_logging-1.2.0-py2.py3-none-any.whl")
    version("1.1.6", sha256="75091dc527c2ff3459f5327d6e699069f12d68ee8732c08dcdba894aa1f0faec", url="https://pypi.org/packages/7e/db/17ced89c1977e3ba51c9feb6433b89442beb60b9f4c14c963e2bdb72ef3c/google_cloud_appengine_logging-1.1.6-py2.py3-none-any.whl")
    version("1.1.5", sha256="1a06dc41997c7daacadd83497b26208d49c30625103e790c4ce6dafa8ea5501c", url="https://pypi.org/packages/d8/ff/0e8ea6e2a904e0167cbb10cd7a6ba2ab7055ce56161e42d69eb17cd132ad/google_cloud_appengine_logging-1.1.5-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-google-api-core@1.34.1:1,2.11:+grpc", when="@1.4.2:")
        depends_on("py-google-api-core@1.34:1,2.11:+grpc", when="@1.2:1.4.1")
        depends_on("py-google-api-core@1.31.5:1,2.3.1:+grpc", when="@1.1.1:1.1")
        depends_on("py-google-auth@2.14.1:2.23,2.25.1:", when="@1.4.3:")
        depends_on("py-google-auth@2.14.1:", when="@1.4.1:1.4.2")
        depends_on("py-proto-plus@1.22.3:", when="@1.4:")
        depends_on("py-proto-plus@1.22.2:", when="@1.3 ^python@3.11:")
        depends_on("py-proto-plus@1.22:", when="@1.1.4:1.3")
        depends_on("py-protobuf@3.19.5:3.20.0-rc2,3.20.1-rc1,3.20.2:4.21.0-rc2,4.21.6:4", when="@1.1.6:")
        depends_on("py-protobuf@3.20.2:4", when="@1.1.5")

