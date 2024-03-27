##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyKeyringsAlt(PythonPackage):
    version("5.0.0", sha256="4b3fd67bbcdd5aa137e1537cc47b694dda134e290740918750a6a73bcf665b87", url="https://pypi.org/packages/af/20/046671abb06ec38e37fbf1d5e068456d1ba215a1913337723b22f7df803e/keyrings.alt-5.0.0-py3-none-any.whl")
    version("4.2.0", sha256="3d25912ed71d6deec85d7e6e867963e1357cd56186a41c9295b86939a5ebf85c", url="https://pypi.org/packages/71/0c/32cf193861389487e062dc91683146f696d11ce0d4bc3fb6539f68aa0ada/keyrings.alt-4.2.0-py3-none-any.whl")
    version("4.1.2", sha256="f69dc2ce71568fc982872cd591cfaf3d8d002ed34f1673fee35ddb718e975d99", url="https://pypi.org/packages/3d/8d/8e3c078ccde08a36c1dfa1e193282fda1f1d7ebc1e683699d6da4b2c26a8/keyrings.alt-4.1.2-py3-none-any.whl")
    version("4.1.1", sha256="1ca0f48a981ef4f5b1a44259ab034bd39c26f09613885f80f5453baa604e2f1b", url="https://pypi.org/packages/a0/af/b7a63dc71f8b61d1a0128c285bce59fd8f80791dedca0bf7c1f1aa581171/keyrings.alt-4.1.1-py3-none-any.whl")
    version("4.1.0", sha256="7b051f13ffeb216ea9940995f91ea3eece7795d199631ea25a625fbf614d74b4", url="https://pypi.org/packages/e2/74/5f312f4713aa1836f1b8595318cac4ab770fc2278d12ac66fdabeafb2b67/keyrings.alt-4.1.0-py3-none-any.whl")
    version("4.0.2", sha256="49ab586d0610e5f73e874fb3dcfc6b94f222d30a8457ef324f4124c34b3ea2f5", url="https://pypi.org/packages/55/bd/36afd53fe86dc28c2f7280d4e1f5e1e58dc26c0272609af069818f575698/keyrings.alt-4.0.2-py3-none-any.whl")
    version("4.0.1", sha256="a96b3b6125242e4db4e7b0eb732e35aaacf736765cd9a593296b831945c891c5", url="https://pypi.org/packages/96/42/7e9c46e7ccf02e32095e42f369666958911464c20e6faf971f4a47dde8db/keyrings.alt-4.0.1-py3-none-any.whl")
    version("4.0.0", sha256="7119a9938c4132ac92f24d4ee41d57aef27a447c713d05f1fcccc556a5394aa8", url="https://pypi.org/packages/79/f4/597ffdd0a9f5066b970fef86fd0dae7e861ea508b5d5b1829d21cca4d5fa/keyrings.alt-4.0.0-py3-none-any.whl")
    version("3.5.2", sha256="a845da5feebdb009d6b683ec27e55ff71bc679ac3b4761bae97c2e635b98e575", url="https://pypi.org/packages/e5/68/215631100a970940532fbc4e49af4091aa14b0a090509bd88b20c685e959/keyrings.alt-3.5.2-py3-none-any.whl")
    version("3.5.1", sha256="860732a49b4a066af39bbde904e8e06f9ad8579145e618fe4fe70778620ffd3a", url="https://pypi.org/packages/2a/fe/5536953df41df63fd6685cb1bd236c95a0567caf9b92a9551bc44c70e8f6/keyrings.alt-3.5.1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-jaraco-classes", when="@4.1.2:")

