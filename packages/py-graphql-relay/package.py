##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGraphqlRelay(PythonPackage):
    version("3.2.0", sha256="c9b22bd28b170ba1fe674c74384a8ff30a76c8e26f88ac3aa1584dd3179953e5", url="https://pypi.org/packages/74/16/a4cf06adbc711bd364a73ce043b0b08d8fa5aae3df11b6ee4248bcdad2e0/graphql_relay-3.2.0-py3-none-any.whl")
    version("3.1.5", sha256="d1455316182e1017d06f0b4d4a2ce8bafad38253a6c7c5666fc80d5d516ee5c8", url="https://pypi.org/packages/f0/dc/d6c9a32cbc3f44a390c23720873e9a4a448e48f812261d12eb53c9318f86/graphql_relay-3.1.5-py3-none-any.whl")
    version("3.1.4", sha256="24ae4e97f781d0bd6c981b50031676d675c8e086519e5bb2cccd238feb470120", url="https://pypi.org/packages/00/a7/aeb3913c323d288233ce83b215b3e7fd169e4262ab21bc39aa6a5971e482/graphql_relay-3.1.4-py3-none-any.whl")
    version("3.1.3", sha256="78e3525a69ecb933e4108256333e6200c59933c02d44988421e4e3df9ccb0ab9", url="https://pypi.org/packages/d2/9e/374bb8829e626e2a6671424338110302fe78b2061b9d1b455854bbbe7115/graphql_relay-3.1.3-py3-none-any.whl")
    version("3.1.2", sha256="3a6900f4eae0072dda548b21b6f743afaeb7be859fcc9332e0da3e9dff108835", url="https://pypi.org/packages/dc/58/b37accb5f0aed96d98e3f500dd444afbed0d822840f666f7cf2d0c2dd1df/graphql_relay-3.1.2-py3-none-any.whl")
    version("3.1.1", sha256="066ab3ffc1ee34faae1236e141b05efa4cc3d7d9e6eb80f132b1ac9d3f1364c1", url="https://pypi.org/packages/33/6f/400baf3cb11a792599db5bd3ea7191aad33521fc04b6157075093a452b0c/graphql_relay-3.1.1-py3-none-any.whl")
    version("3.1.0", sha256="2cda0ac0199dd56c28ca4f6e0381cdcf5787809c06d1507df3c2a738f9ad846f", url="https://pypi.org/packages/d3/d5/82f3300ae42faa1b3249d56d6d5a37ae1550e11f2bf489dc6c9ef63b8bc4/graphql_relay-3.1.0-py3-none-any.whl")
    version("3.0.0", sha256="b05ca0547557874f3bb1f34e4a6dce20bc60359fe6e73daaa63bb90df85f7ba9", url="https://pypi.org/packages/45/94/aa6ca63f7218c344879ba50a21d839efe732cf30c2cd3412f933edb25f48/graphql_relay-3.0.0-py3-none-any.whl")
    version("2.0.1", sha256="ac514cb86db9a43014d7e73511d521137ac12cf0101b2eaa5f0a3da2e10d913d", url="https://pypi.org/packages/94/48/6022ea2e89cb936c3b933a0409c6e29bf8a68c050fe87d97f98aff6e5e9e/graphql_relay-2.0.1-py3-none-any.whl")
    version("2.0.0", sha256="7fa74661246e826ef939ee92e768f698df167a7617361ab399901eaebf80dce6", url="https://pypi.org/packages/a0/83/bea0cd12b51e1459d6702b0975d2f42ae4607021f22ec90c50b03c397fcc/graphql-relay-2.0.0.tar.gz")
    version("0.5.0", sha256="67b35f036325b625c717b24930bfa87229181e5cdbf4b07713b845dacb8fed14", url="https://pypi.org/packages/b9/fc/026a69a0b20d9e0a06f6141d77cd1b5bee316b18a7878d1914c7bfdaa36f/graphql_relay-0.5.0-py3-none-any.whl")
    version("0.4.5", sha256="2716b7245d97091af21abf096fabafac576905096d21ba7118fba722596f65db", url="https://pypi.org/packages/5e/b0/b91fadc180544fc9e3c156d7049561fd5f1e2211d26fd29033548fd50934/graphql-relay-0.4.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-graphql-core@3.2.0:3.2", when="@3.2:")
        depends_on("py-graphql-core@3.1.0:3.1", when="@3.1.1:3.1")
        depends_on("py-graphql-core@3.1.0:", when="@3.1:3.1.0")
        depends_on("py-graphql-core@3:", when="@3.0.0-alpha2:3.0")
        depends_on("py-graphql-core@2.2:2", when="@2")
        depends_on("py-graphql-core@0.5:1", when="@0.5:0")
        depends_on("py-promise@2.2:", when="@2")
        depends_on("py-promise@0.4:", when="@0.5:0")
        depends_on("py-six@1.12:", when="@2")
        depends_on("py-six@1.10:", when="@0.5:0")

