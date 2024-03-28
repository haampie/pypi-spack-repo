# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyExecnet(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.0.2", sha256="88256416ae766bc9e8895c76a87928c0012183da3cc4fc18016e6f050e025f41", url="https://pypi.org/packages/e8/9c/a079946da30fac4924d92dbc617e5367d454954494cf1e71567bcc4e00ee/execnet-2.0.2-py3-none-any.whl")
    version("2.0.1", sha256="eb9d131005116496240eabb9682a580c11e46071b7e873fdc30e4251d5e7945c", url="https://pypi.org/packages/38/39/b999208ba22a6ede2254e2f91808641aaebcc0ceb876cb7fd79380b3800b/execnet-2.0.1-py3-none-any.whl")
    version("2.0.0", sha256="9e30983ff42c20bac5b18807910512058b12a79f6bccddd9ce813bf22b079a9c", url="https://pypi.org/packages/c0/6f/a42c78f48715a1462d557a460a8647c90023b20d06d981fd547b8525f799/execnet-2.0.0-py3-none-any.whl")
    version("1.9.0", sha256="a295f7cc774947aac58dde7fdc85f4aa00c42adf5d8f5468fc630c1acf30a142", url="https://pypi.org/packages/81/c0/3072ecc23f4c5e0a1af35e3a222855cfd9c80a1a105ca67be3b6172637dd/execnet-1.9.0-py2.py3-none-any.whl")
    version("1.8.1", sha256="e840ce25562e414ee5684864d510dbeeb0bce016bc89b22a6e5ce323b5e6552f", url="https://pypi.org/packages/41/85/0cd8c8670ea330150be3427f9d279143e766839e83545f77572749b6d8c3/execnet-1.8.1-py2.py3-none-any.whl")
    version("1.8.0", sha256="7a13113028b1e1cc4c6492b28098b3c6576c9dccc7973bfe47b342afadafb2ac", url="https://pypi.org/packages/8f/e6/116ccf9ab0177a2381c3ccd42c049fcdcf40c9b7993dcd0c593859e5ae75/execnet-1.8.0-py2.py3-none-any.whl")
    version("1.7.1", sha256="d4efd397930c46415f62f8a31388d6be4f27a91d7550eb79bc64a756e0056547", url="https://pypi.org/packages/d3/2e/c63af07fa471e0a02d05793c7a56a9f7d274a8489442a5dc4fb3b2b3c705/execnet-1.7.1-py2.py3-none-any.whl")
    version("1.7.0", sha256="0dd40ad3b960aae93bdad7fe1c3f049bbcc8fba47094655a4301f5b33e906816", url="https://pypi.org/packages/9b/8d/ca1daa8fcff5e1c37f2de7463321a53cf8c456de77f43c07175ef57113bb/execnet-1.7.0-py2.py3-none-any.whl")
    version("1.6.1", sha256="64dcdc248d007060f6f6500e7c79a4f87ee692063e3ec51e9bebf30ef2ea21d7", url="https://pypi.org/packages/9a/73/5be9d235327b3770c330bed707766c8885e8157577db85f11b874b26da34/execnet-1.6.1-py2.py3-none-any.whl")
    version("1.6.0", sha256="027ee5d961afa01e97b90d6ccc34b4ed976702bc58e7f092b3c513ea288cb6d2", url="https://pypi.org/packages/77/1a/f69e1f73bc36f55d3273afd1c52936def71ac67d9c5215be3a4ca3a45577/execnet-1.6.0-py2.py3-none-any.whl")
    version("1.4.1", sha256="d2b909c7945832e1c19cfacd96e78da68bdadc656440cfc7dfe59b766744eb8c", url="https://pypi.org/packages/07/16/51d99ff02e7b03dfdf407b05c157b8d578e23fb0404a640c0ef57ce708e9/execnet-1.4.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-apipkg@1.4:", when="@1.4:1.8")
    # END DEPENDENCIES

