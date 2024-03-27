##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTypesRequests(PythonPackage):
    version("2.31.0.20240311", sha256="47872893d65a38e282ee9f277a4ee50d1b28bd592040df7d1fdaffdf3779937d", url="https://pypi.org/packages/05/22/21c7918c9bb842faa92fd26108e9f669c3dee9b6b239e8f45dd5f673e6cf/types_requests-2.31.0.20240311-py3-none-any.whl")
    version("2.31.0.20240310", sha256="a4ba49353e3f6b3fdb481ba6f8455917e8bc2a0b62b775d80833ec000508e5dc", url="https://pypi.org/packages/7c/96/a651898995c25e8e1b5b8a87ed8b0bccc2895f0db051c534a75741387d40/types_requests-2.31.0.20240310-py3-none-any.whl")
    version("2.31.0.20240218", sha256="a82807ec6ddce8f00fe0e949da6d6bc1fbf1715420218a9640d695f70a9e5a9b", url="https://pypi.org/packages/ce/ca/82c7f75616c524856488cece6b37e459de626cad49b2a24a0b571c20be06/types_requests-2.31.0.20240218-py3-none-any.whl")
    version("2.31.0.20240125", sha256="9592a9a4cb92d6d75d9b491a41477272b710e021011a2a3061157e2fb1f1a5d1", url="https://pypi.org/packages/ae/29/3290a0d17865b9ec3d54fbb17faa265d9de7e856b6a3b52dfdf3507efd7c/types_requests-2.31.0.20240125-py3-none-any.whl")
    version("2.31.0.20240106", sha256="da997b3b6a72cc08d09f4dba9802fdbabc89104b35fe24ee588e674037689354", url="https://pypi.org/packages/69/be/af3ec284a5dd21cffc84fa0088211adf896b6e5e862ce9b1ead212e51b0e/types_requests-2.31.0.20240106-py3-none-any.whl")
    version("2.31.0.20231231", sha256="2e2230c7bc8dd63fa3153c1c0ae335f8a368447f0582fc332f17d54f88e69027", url="https://pypi.org/packages/1b/23/126ffd0c885926fbd95eac1148093a4d87e9698a1f938be16d109e63ca64/types_requests-2.31.0.20231231-py3-none-any.whl")
    version("2.31.0.10", sha256="b32b9a86beffa876c0c3ac99a4cd3b8b51e973fb8e3bd4e0a6bb32c7efad80fc", url="https://pypi.org/packages/1d/d6/1281c1d7b03a127562d6644ebff081e85045f0025b1fe26dcdd82811ad1a/types_requests-2.31.0.10-py3-none-any.whl")
    version("2.31.0.9", sha256="140e323da742a0cd0ff0a5a83669da9ffcebfaeb855d367186b2ec3985ba2742", url="https://pypi.org/packages/95/b1/805141aa0c0024c633828375918838841481c8b977de8636ae2b80fdcad9/types_requests-2.31.0.9-py3-none-any.whl")
    version("2.31.0.8", sha256="39894cbca3fb3d032ed8bdd02275b4273471aa5668564617cc1734b0a65ffdf8", url="https://pypi.org/packages/1e/50/fb7eed30eace72d2eb6cf71059f896e7b4a0c031b654b99f37146a68d60b/types_requests-2.31.0.8-py3-none-any.whl")
    version("2.31.0.7", sha256="39844effefca88f4f824dcdc4127b813d3b86a56b2248d3d1afa58832040d979", url="https://pypi.org/packages/38/89/12bdcc3709cbc95120c1a4234becb8a94c7271806c36ee90bcf792df1f30/types_requests-2.31.0.7-py3-none-any.whl")
    version("2.31.0.2", sha256="56d181c85b5925cbc59f4489a57e72a8b2166f18273fd8ba7b6fe0c0b986f12a", url="https://pypi.org/packages/06/9b/04bb62f11a6824df5d4568439cf0715118c265d0ffbebeb7cf4b8c9caa15/types_requests-2.31.0.2-py3-none-any.whl")
    version("2.28.10", sha256="45b485725ed58752f2b23461252f1c1ad9205b884a1e35f786bb295525a3e16a", url="https://pypi.org/packages/07/41/5c0bf629bb4abdda40a5c6966deb36a7435c634e710381c8ad7398e13839/types_requests-2.28.10-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-types-urllib3", when="@2.27.3:2.31.0.6")
        depends_on("py-urllib3@2.0.0:", when="@2.31.0.7:")

