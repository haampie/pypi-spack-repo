# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyspnego(PythonPackage):
    # BEGIN VERSIONS
    version("0.10.2", sha256="3d5c5c28dbd0cd6a679acf45219630254db3c0e5ad4a16de521caa0585b088c0", url="https://pypi.org/packages/cc/fd/06a7618de50ad13b7e85115bd1e42c1625e3365313a4c971898386781f89/pyspnego-0.10.2-py3-none-any.whl")
    version("0.10.1", sha256="06c22e8e3aa57196f97205569c03152fc4c19246547be38120fd34e5e8e04cb8", url="https://pypi.org/packages/72/79/64f27a0e74d2a4e99f1d23756caac5f99afe85905a12931105f13453d521/pyspnego-0.10.1-py3-none-any.whl")
    version("0.10.0", sha256="68f9e44fe6a6f8a1c0decbfc7f5b9346990b58aa97a60e023174ec17161dd8ff", url="https://pypi.org/packages/2c/68/1fa0bf80cfd8af66e513fd197598249d882bceae761b9616c56f678adf3a/pyspnego-0.10.0-py3-none-any.whl")
    version("0.9.2", sha256="0e16cb331f1bd9c85f9b80e2be04bb5da2ecaff678cc0342f68b45e4667d7966", url="https://pypi.org/packages/5d/48/6e1d700165da513d76c3115779d207d79cb2d7a5a0a54112f791e2c8665c/pyspnego-0.9.2.tar.gz")
    version("0.9.1", sha256="6eea64f511bdfa192c2f80593ddf124258b0ea560327468953d18420e0ab3597", url="https://pypi.org/packages/fb/38/46174701e2a2de8b72e79c980324b034203edafff3c543a4134b2c1ae9af/pyspnego-0.9.1.tar.gz")
    version("0.9.0", sha256="3f10ca7a2f0d5170c2032bb5d55183384208314032aa44c1684d6920d50e97de", url="https://pypi.org/packages/ee/08/6cd62d64ce42a2eaf433eb41a837d3da2b49ce1cb796a0265cc02652f839/pyspnego-0.9.0.tar.gz")
    version("0.8.0", sha256="e0499cc066c56762f8a315bb053243d34240cb85e384afc6b87b4fa0142543df", url="https://pypi.org/packages/97/b7/2ca5b546fc91d6c41e1796e49d0615fe7dfb4845d088da8a938934b3d63c/pyspnego-0.8.0.tar.gz")
    version("0.7.0", sha256="da78096fd7c9f40e716f6fbe3e30d913103d75fd676f839f98fc3a6fee92fbe3", url="https://pypi.org/packages/97/f3/bdf3cd5f4c5a1bf9e1d4bb771c133850ee08241c18cafd90a6d872937a9f/pyspnego-0.7.0.tar.gz")
    version("0.6.3", sha256="6060a0e683171090adcf92c9d319ddd334f15117fa199a703d8c9bd094d9f6c0", url="https://pypi.org/packages/ba/13/7b4e7dcff1eb24a13e0a631a4b49eab361678e4490d691c03253ae736da4/pyspnego-0.6.3.tar.gz")
    version("0.6.2", sha256="e0ceeb2a1202b646b1586aa9e1cc528e03325644745c37ff836cb5d7774e008f", url="https://pypi.org/packages/f0/6b/823c4363e2c24d8b57c3ab24680b62186f567fc40ec007723f6793257459/pyspnego-0.6.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cryptography", when="@:0.1.0-rc3,0.10:")
        depends_on("py-sspi@0.1:", when="@0.10:0.10.0 platform=windows")
        depends_on("py-sspic", when="@0.10.1 platform=windows")
        depends_on("py-sspilib", when="@0.10.2: platform=windows")
    # END DEPENDENCIES

