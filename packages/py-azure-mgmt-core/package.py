# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtCore(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.4.0", sha256="81071675f186a585555ef01816f2774d49c1c9024cb76e5720c3c0f6b337bb7d", url="https://pypi.org/packages/b1/5a/3a31578b840600dffb75f3ffb383cc4c5e8ea0d06a1085f86b17e18c3193/azure_mgmt_core-1.4.0-py3-none-any.whl")
    version("1.3.2", sha256="fd829f67086e5cf6f7eb016c9e80bb0fb293cbbbd4d8738dc90af9aa1055fb7b", url="https://pypi.org/packages/29/99/d06021eb45ff660cd4cf1bf16a60645a8256672edf46ff1976a709a50918/azure_mgmt_core-1.3.2-py3-none-any.whl")
    version("1.3.1", sha256="9667b9d65f2b41fed854e9d3a56f293739d327bf0d4e16252d9e785a6f4fe581", url="https://pypi.org/packages/5a/e9/7e3b17b65360d796a5890bb4af432fe16d2852fdf532d339bca6e4fabf4c/azure_mgmt_core-1.3.1-py3-none-any.whl")
    version("1.3.0", sha256="7b7fa952aeb9d3eaa13eff905880f3d3b62200f7be7a8ba5a50c8b2e7295322a", url="https://pypi.org/packages/0f/10/622b03f37b5377c1db8dcd679a28cfdb464963109c9c8879fa052d287a54/azure_mgmt_core-1.3.0-py2.py3-none-any.whl")
    version("1.3.0-beta3", sha256="f70e065be929088f662de71fb3187a477ea5f47793111383825e62f5a76a8d5c", url="https://pypi.org/packages/1d/16/e745a57872a4cfdff8b82e044023e0ae6065996d33793db85c5634a73dd9/azure_mgmt_core-1.3.0b3-py2.py3-none-any.whl")
    version("1.3.0-beta2", sha256="72825893ab60ce65b08b53c52f78c8613d359ca636c832d2378fffd9d02a6968", url="https://pypi.org/packages/0e/8f/28d55fa89af456086698a12903531aa5e113ca4430f88296b166e5a4c45a/azure_mgmt_core-1.3.0b2-py2.py3-none-any.whl")
    version("1.3.0-beta1", sha256="493fb8d8d132e5f64f9b9c9715b9a283d929bbdd1818166ee033ce9f0c476558", url="https://pypi.org/packages/bd/a5/e2df449cc14013adf8b7cbf79c11c870d75a5985a8472e3043d7c8b4ae93/azure_mgmt_core-1.3.0b1-py2.py3-none-any.whl")
    version("1.2.2", sha256="d36bd595dff6a1509ed52a89ee8dd88b83200320a6afa60fb4186afcb8978ce5", url="https://pypi.org/packages/63/a0/2074af80e53b9d50ce9ac3d358778d3eca4508823afec83ea76ba989234b/azure_mgmt_core-1.2.2-py2.py3-none-any.whl")
    version("1.2.1", sha256="bd4503a2d81b86780f15936af2e4244c1345062f4c2422f0b377b56cb80d7796", url="https://pypi.org/packages/59/03/6cd17cf14999a7c87106835d2c51f87e84ade36178fe1eab94837ea5d712/azure_mgmt_core-1.2.1-py2.py3-none-any.whl")
    version("1.2.0", sha256="6966226111e92dff26d984aa1c76f227ce0e8b2069c45c72cfb67f160c452444", url="https://pypi.org/packages/4f/da/545b3d2496ac08fb4b4c2d784c8d92cb9bfc843801a53dc870bfafe81f0d/azure_mgmt_core-1.2.0-py2.py3-none-any.whl")
    version("1.0.0", sha256="b481a7d4239b11476a2f54e947ccb8c8fdf26dd35f72e13b904e9f1208a0bad6", url="https://pypi.org/packages/62/4e/e8b0fbfe9595eb971a6a4438d280b8c67a403421db32e8d1d40215688cf4/azure_mgmt_core-1.0.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-core@1.26.2:", when="@1.4:")
        depends_on("py-azure-core@1.24:", when="@1.3.2:1.3")
        depends_on("py-azure-core@1.23:", when="@1.3.1")
        depends_on("py-azure-core@1.15.0:", when="@1.3.0-beta3:1.3.0")
        depends_on("py-azure-core@1.15:1.15.0-beta1", when="@1.3.0-beta2")
        depends_on("py-azure-core@1.13:", when="@1.3:1.3.0-beta1")
        depends_on("py-azure-core@1.9:", when="@1.2.2:1.2")
        depends_on("py-azure-core@1.8.2:", when="@1.2.1")
        depends_on("py-azure-core@1.7:", when="@1.2:1.2.0")
        depends_on("py-azure-core@1.4:", when="@1.0.0:1.1")
    # END DEPENDENCIES

