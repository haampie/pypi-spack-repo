##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyEtelemetry(PythonPackage):
    version("0.3.1", sha256="a64f09bcd55cbfa5684e4d9fb6d1d6a018ab99d2ea28e638435c4c26e6814a6b", url="https://pypi.org/packages/83/27/f997c9da0e179986fadd6c8474d16743f1b3697c129c2fcd1e739cd038c2/etelemetry-0.3.1-py3-none-any.whl")
    version("0.3.0", sha256="78febd59a22eb53d052d731f10f24139eb2854fd237348fba683dd8616fb4a67", url="https://pypi.org/packages/8b/1b/a13fd41742cf2ed2498e90e5cdb27239e1115a788114aed0625dbf16737c/etelemetry-0.3.0-py3-none-any.whl")
    version("0.2.2", sha256="3e304ea9070902e6367282369cb8eaae05f4beef9313820053cc03f611bd1e29", url="https://pypi.org/packages/13/f9/e8e8cd04bdc44dfba28a3b2cc4d0b1efe8cbf3afc1bf12b11f1c9d697f1e/etelemetry-0.2.2-py3-none-any.whl")
    version("0.2.1", sha256="b2b459c986c482fa6aaae87e891904751af21728ccd4e1346396c684a7a4eb6f", url="https://pypi.org/packages/50/fe/7b4a4d7bd2756884ba2af5445ac538bff20ca8e6c89e24b253cc51845f1b/etelemetry-0.2.1-py3-none-any.whl")
    version("0.2.0", sha256="26775eb28bbf4ca8380fd443d49b327088ecb6bdee6996c46804737f462e72a2", url="https://pypi.org/packages/2b/57/51b587e91b37a11dff9d00d624d858637f129dfb5f2388548af941eda5df/etelemetry-0.2.0-py3-none-any.whl")
    version("0.1.2", sha256="75e133a23f81472a2cd01275224afc5374e8acaada96c01525623d7b1515ee64", url="https://pypi.org/packages/c0/e4/d11d33fe6b0c357776e2b36e76eea5948db2060a155b2862d0d6612730da/etelemetry-0.1.2-py3-none-any.whl")
    version("0.1.1", sha256="a2e7baf9f88beff450d39a84fb6cccc8a80a30515743fc2c48f18aff6726e1ea", url="https://pypi.org/packages/db/c9/b3cf01936afbc42d1d5bd72a27a71fff37863b716959958ed228ac801700/etelemetry-0.1.1-py3-none-any.whl")
    version("0.1", sha256="7a101b8c4e9f97c1d095f8c0dc9eb77e2bdef7ed1d504afc836c0f113cb5c8e9", url="https://pypi.org/packages/d7/d2/2cceec7c4523e9c33a60697c79d730a47aea9f588c8f006e5cbcc4a5d94d/etelemetry-0.1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-ci-info@0.2:", when="@0.2.1:")
        depends_on("py-ci-info", when="@0.2:0.2.0")
        depends_on("py-packaging", when="@0.3.1:")
        depends_on("py-requests")

