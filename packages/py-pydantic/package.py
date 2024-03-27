##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPydantic(PythonPackage):
    version("2.6.4", sha256="cc46fce86607580867bdc3361ad462bab9c222ef042d3da86f2fb333e1d916c5", url="https://pypi.org/packages/e5/f3/8296f550276194a58c5500d55b19a27ae0a5a3a51ffef66710c58544b32d/pydantic-2.6.4-py3-none-any.whl")
    version("2.6.3", sha256="72c6034df47f46ccdf81869fddb81aade68056003900a8724a4f160700016a2a", url="https://pypi.org/packages/ac/86/c98520827f58c8753783be4bf2286b4f73a18ac71c93ab597ae1aeb26fc8/pydantic-2.6.3-py3-none-any.whl")
    version("2.6.2", sha256="37a5432e54b12fecaa1049c5195f3d860a10e01bdfd24f1840ef14bd0d3aeab3", url="https://pypi.org/packages/42/28/f19be8d493c59a8ddf32c15d69765c6423ad712da1c6255b418df2fc1443/pydantic-2.6.2-py3-none-any.whl")
    version("2.6.1", sha256="0b6a909df3192245cb736509a92ff69e4fef76116feffec68e93a567347bae6f", url="https://pypi.org/packages/db/dc/afecbd9650f486889181c6d1a0d675b580c06253ea7e304588e4c7485bdb/pydantic-2.6.1-py3-none-any.whl")
    version("2.6.0", sha256="1440966574e1b5b99cf75a13bec7b20e3512e8a61b894ae252f56275e2c465ae", url="https://pypi.org/packages/e4/37/3ffe6e7daa1ea1b4bf5228807a92ccbae538cf57c0c50b93564c310c11a8/pydantic-2.6.0-py3-none-any.whl")
    version("2.6.0-beta1", sha256="a9560d042a8113eec5acd0474067f4edf493e7b9bb03d8f83e342dfb4b0dcf84", url="https://pypi.org/packages/6c/55/9f51ea8a4fe6cacc0d516f39757e420204ecdf2594032b2337176edba527/pydantic-2.6.0b1-py3-none-any.whl")
    version("2.5.3", sha256="d0caf5954bee831b6bfe7e338c32b9e30c85dfe080c843680783ac2b631673b4", url="https://pypi.org/packages/dd/b7/9aea7ee6c01fe3f3c03b8ca3c7797c866df5fecece9d6cb27caa138db2e2/pydantic-2.5.3-py3-none-any.whl")
    version("2.5.2", sha256="80c50fb8e3dcecfddae1adbcc00ec5822918490c99ab31f6cf6140ca1c1429f0", url="https://pypi.org/packages/0a/2b/64066de1c4cf3d4ed623beeb3bbf3f8d0cc26661f1e7d180ec5eb66b75a5/pydantic-2.5.2-py3-none-any.whl")
    version("2.5.1", sha256="dc5244a8939e0d9a68f1f1b5f550b2e1c879912033b1becbedb315accc75441b", url="https://pypi.org/packages/e2/2c/9906b7abc337b0250a5634de5396e2f3cb1b837af0616424c2225a65aa80/pydantic-2.5.1-py3-none-any.whl")
    version("2.1.1", sha256="43bdbf359d6304c57afda15c2b95797295b702948082d4c23851ce752f21da70", url="https://pypi.org/packages/87/80/52770e747e4bee5012e60b2684db36c8fdf010f8dadb4ded0efec808b07d/pydantic-2.1.1-py3-none-any.whl")
    version("2.1.0", sha256="868e036da92a263da265e34f2d1ff5ad1c24d23c93e7a1e7da50cb96fa8b05e8", url="https://pypi.org/packages/5a/25/55002e826c764e85bcd0910f21e0de2ebb8796a0cc27b350ca6d2bc41b07/pydantic-2.1.0-py3-none-any.whl")
    version("2.0.3", sha256="614eb3321eb600c81899a88fa9858b008e3c79e0d4f1b49ab1f516b4b0c27cfb", url="https://pypi.org/packages/1f/1a/71b404f9acb44402f5b581ade106e9219d6d83824d50943e630fc0ca12e5/pydantic-2.0.3-py3-none-any.whl")
    version("2.0.2", sha256="f5581e0c79b2ec2fa25a9d30d766629811cdda022107fa73d022ab5578873ae3", url="https://pypi.org/packages/79/bf/ce11dc07156bdbf12009c560ba5fdb308522f77e7484b64f4aff682d93cf/pydantic-2.0.2-py3-none-any.whl")
    version("2.0.1", sha256="7a3e3b1d0384eaa313f0810cffa475d6849794a9ae5768989518114771cb9241", url="https://pypi.org/packages/d9/fd/618a146a5958aa356ecf4c39e6f7669e3b21ce230de1f567f6908775696c/pydantic-2.0.1-py3-none-any.whl")
    version("2.0", sha256="8bf7355be5e1207c756dfbc8046236dadd4ce04101fb482e6c8834a06d9aa04f", url="https://pypi.org/packages/10/e8/c7a1f0dd3d921bccb1d2239b84c894f677eba3950936e9d4c74803ba5bdb/pydantic-2.0-py3-none-any.whl")
    version("2.0-alpha3", sha256="4bbd961e806eeeb5c9489c7352fb2cfcd0c58f80e0702065b251ce309fc8f6ec", url="https://pypi.org/packages/8c/90/497f95d8c3c5441fe62541b363f1d459402f385196fd8ac17546562b2286/pydantic-2.0a3-py3-none-any.whl")
    version("1.10.5", sha256="9e337ac83686645a46db0e825acceea8e02fca4062483f40e9ae178e8bd1103a", url="https://pypi.org/packages/28/59/5d2fc3499d9ce8ce48ee7e00f043d5cc429a9198bd96c3512809428ade15/pydantic-1.10.5.tar.gz")
    version("1.10.4", sha256="b9a3859f24eb4e097502a3be1fb4b2abb79b6103dd9e2e0edb70613a4459a648", url="https://pypi.org/packages/53/17/34e54e352f6a3d304044e52d5ddd5cd621a62ec8fb7af08cc73af65dd3e1/pydantic-1.10.4.tar.gz")
    version("1.10.3", sha256="01d450f1b6a642c98f58630e807f7554df0a8ce669ffaff087ce9e1fd4ff7ec8", url="https://pypi.org/packages/f1/c1/cac2a3a28a1d9adffa633dfb7b1ab90e7e6e432d26af4f587a7f7c297db2/pydantic-1.10.3.tar.gz")
    version("1.10.2", sha256="91b8e218852ef6007c2b98cd861601c6a09f1aa32bbbb74fab5b1c33d4a1e410", url="https://pypi.org/packages/7d/7d/58dd62f792b002fa28cce4e83cb90f4359809e6d12db86eedf26a752895c/pydantic-1.10.2.tar.gz")
    version("1.10.1", sha256="d41bb80347a8a2d51fbd6f1748b42aca14541315878447ba159617544712f770", url="https://pypi.org/packages/d5/eb/d5ee9e58b2a4608c320fc72e5d471ba0cd949e8ef6f2689d30d1bd782d9f/pydantic-1.10.1.tar.gz")
    version("1.10.0", sha256="e13788fcad1baf5eb3236856b2a9a74f7dac6b3ea7ca1f60a4ad8bad4239cf4c", url="https://pypi.org/packages/86/83/0fed6af08fec0f29e7b02ead602393b0cac8dfb99cfc4b0816784ab28e2e/pydantic-1.10.0.tar.gz")
    version("1.10.0-beta1", sha256="841e955fd241ef676d454098f174eb7b6fcdd50187b66a452a6d2e05a5ecf71c", url="https://pypi.org/packages/32/03/3a73b898fa30d124d7ccf3258714367dc5d8de15aa1d91efb8f6ea1e0abc/pydantic-1.10.0b1.tar.gz")
    version("1.10.0-alpha2", sha256="22390eea9d277e562b1fe935d9c5e61e5f723c4fe4da27eab3f3184327f162ef", url="https://pypi.org/packages/5b/78/ad5dc7de0ce6c0a6c526c17ec4260a30e89a6af8a2ddaff545e5ba67893b/pydantic-1.10.0a2.tar.gz")
    version("1.10.0-alpha1", sha256="6c533e575b392b78bea53bd904bfbd206965c2b07c122eda46719dd5f8200099", url="https://pypi.org/packages/90/c7/9d7a06cb74df1b9da482236a3780788b2b9d5f898a4b3914201fbb4b72df/pydantic-1.10.0a1.tar.gz")
    version("1.9.2", sha256="8cb0bc509bfb71305d7a59d00163d5f9fc4530f0881ea32c74ff4f74c85f3d3d", url="https://pypi.org/packages/fd/8f/3f7e88b507dbdfec8f1f914294aa8831edffb03d668799c65b4b46331c8a/pydantic-1.9.2.tar.gz")
    version("1.9.1", sha256="1ed987c3ff29fff7fd8c3ea3a3ea877ad310aae2ef9889a119e22d3f2db0691a", url="https://pypi.org/packages/d0/a5/e4a25a0becf35530a3d90459a88855743e942f2e502da49ca5b10aa78568/pydantic-1.9.1.tar.gz")
    version("1.9.0", sha256="742645059757a56ecd886faf4ed2441b9c0cd406079c2b4bee51bcc3fbcd510a", url="https://pypi.org/packages/60/a3/23a8a9378ff06853bda6527a39fe317b088d760adf41cf70fc0f6110e485/pydantic-1.9.0.tar.gz")
    version("1.9.0-alpha2", sha256="2f159193e14fb61a0642e481f539fad6d88c9b063b01835c7d32ca1433de8894", url="https://pypi.org/packages/51/dd/23c61e58980df8b44ac06c4781643c3e22de92d3b7ab78e0b4aa91fa0da7/pydantic-1.9.0a2.tar.gz")
    version("1.9.0-alpha1", sha256="c51156e35b35dcaeb964cad89e0914d9468f2612bd2455898ac11b038aced03d", url="https://pypi.org/packages/6b/a2/f088f5018b88b4ba83679040115aa2a931ab92527f32192ff4444b3bf833/pydantic-1.9.0a1.tar.gz")
    version("1.8.2", sha256="26464e57ccaafe72b7ad156fdaa4e9b9ef051f69e175dbbb463283000c05ab7b", url="https://pypi.org/packages/b9/d2/12a808613937a6b98cd50d6467352f01322dc0d8ca9fb5b94441625d6684/pydantic-1.8.2.tar.gz")
    version("1.7.4", sha256="0a1abcbd525fbb52da58c813d54c2ec706c31a91afdb75411a73dd1dec036595", url="https://pypi.org/packages/2f/91/c0829599e8281492e40ff69a0d88340713a37fb0facd187fabfab53d6915/pydantic-1.7.4.tar.gz")

    variant("dotenv", default=False)

    with default_args(type="run"):
        depends_on("py-annotated-types@0.4:", when="@2:")
        depends_on("py-pydantic-core@2.16.3:2.16", when="@2.6.2:")
        depends_on("py-pydantic-core@2.16.2", when="@2.6.1")
        depends_on("py-pydantic-core@2.16.1", when="@2.6:2.6.0")
        depends_on("py-pydantic-core@2.14.6:2.14", when="@2.5.3:2.5")
        depends_on("py-pydantic-core@2.14.5", when="@2.5.2")
        depends_on("py-pydantic-core@2.14.3", when="@2.5:2.5.1")
        depends_on("py-pydantic-core@2.4", when="@2.1")
        depends_on("py-pydantic-core@2.3:2.3.0", when="@2.0.3:2.0")
        depends_on("py-pydantic-core@2.1:2.1.2", when="@2.0.2")
        depends_on("py-pydantic-core@2.0.2:2.0", when="@2.0.1")
        depends_on("py-pydantic-core@2.0.1", when="@2.0:2.0.0")
        depends_on("py-pydantic-core@0.25", when="@2.0-alpha3")
        depends_on("py-typing-extensions@4.6.1:", when="@2.0-beta1:")
        depends_on("py-typing-extensions@4.2:", when="@2:2.0-alpha3")

