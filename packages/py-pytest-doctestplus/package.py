##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestDoctestplus(PythonPackage):
    version("1.2.1", sha256="103705daee8d4468eb59d444c29b0d71eb85b8f6d582295c8bc3d68ee1d88911", url="https://pypi.org/packages/99/5f/2bbfe57a2b037bb415792c9719d8c56b02f09ea091154da771f2eed5300a/pytest_doctestplus-1.2.1-py3-none-any.whl")
    version("1.2.0", sha256="103d2e9db0afc78c5dca64baaec1e529ff666bb6cfd58482c563a4492afc6829", url="https://pypi.org/packages/f8/1f/89da5cd7255fe0fdb2179cda102021551e32e269a34915a71439adbd6c6a/pytest_doctestplus-1.2.0-py3-none-any.whl")
    version("1.1.0", sha256="b98d95b4956a03256c638f1f9f72200160e9885ab1cd40f35c4453bc1d2e32b2", url="https://pypi.org/packages/76/47/43c45ec70a1d7356eeed289e719f2ad29845c0310bcc8be463f537f839a5/pytest_doctestplus-1.1.0-py3-none-any.whl")
    version("1.0.0", sha256="dcba88e1e38bc4871c355e44b778ccfd49b25e33f6aa5393eed6b56440decb2a", url="https://pypi.org/packages/6e/54/f66c460a28892c44d948c6f3cbde9ca50474cb037eb96c2db88d70e7dd76/pytest_doctestplus-1.0.0-py3-none-any.whl")
    version("0.13.0", sha256="a2809d8b6faadc7f909013b52e1ad36ae6b5371a0393ee8d05bc5719868b3f7a", url="https://pypi.org/packages/d5/f1/95cbe47ec92b4945536f151789624dbaece4beed6b2c1feba4abf62d79e8/pytest_doctestplus-0.13.0-py3-none-any.whl")
    version("0.12.1", sha256="1046bac8dad27c3abcf370edf8f353b7f5d748d537296d481b0cad2cbb306052", url="https://pypi.org/packages/87/64/a1a4fd311b991e11dc919d4cc61a63939bf5f4893dbc6ee0a2c8b26a47c9/pytest_doctestplus-0.12.1-py3-none-any.whl")
    version("0.12.0", sha256="810c164e1ef43116e259cae793661f71728378ba15ce2edad77e4618496a49ae", url="https://pypi.org/packages/da/cd/8197ea85be562a3c11493a6111af0a4226392342e7f1fcd4dd44970f5735/pytest_doctestplus-0.12.0-py3-none-any.whl")
    version("0.11.2", sha256="d3ecfa8a301ccd6fae36f0108a6b789d587d656f0d1e3eb413170c6f5b81eb9f", url="https://pypi.org/packages/47/3b/a9dc1066874bd1379058fd5fd058c4c77225b4abd655b5db382397e2e39f/pytest_doctestplus-0.11.2-py3-none-any.whl")
    version("0.11.1", sha256="01fba5e1c646e38b053afb517e9b3e6af9a8d611d7909ec8a12189a2eb2b11ee", url="https://pypi.org/packages/ff/b8/5ae55621e0d10c31b41c7acfed97f1b1bc854366181c05f0e0bc7163601d/pytest_doctestplus-0.11.1-py3-none-any.whl")
    version("0.11.0", sha256="90e5aff08072aaea1221745482087b02d4851221a7342e539faa2370ed02b1bd", url="https://pypi.org/packages/3f/dd/33f085e73ed2529d7c518f824d9a55f38e8bca68169c21df8728359d83e7/pytest_doctestplus-0.11.0-py3-none-any.whl")
    version("0.9.0", sha256="66859d3c3d73793274803a91b4cb9912d1a7baf5c883e92859f2dfe11b35a631", url="https://pypi.org/packages/c3/a1/d25d7cd9eb48d78c54c24ded2d8338aead358e6e53a99f9324a31a4f9fa8/pytest_doctestplus-0.9.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-packaging@17:", when="@0.10:")
        depends_on("py-pytest@4.6:", when="@0.9:")
        depends_on("py-setuptools@30.3:", when="@0.9:")

