##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyprojectParser(PythonPackage):
    version("0.9.1", sha256="800dbf9f24ec1d55bbdb703cf0c49c5a3f02570b13424157c9adab947b1bc899", url="https://pypi.org/packages/ff/5e/91d23fa308a7ee93513b9ca84580eafb57fe1bd1deb8609116e202225dbd/pyproject_parser-0.9.1-py3-none-any.whl")
    version("0.9.0", sha256="7f52e84cb368dcdcc63f5f48641639c5fbc46f668fbdccdc91610d1eceec062e", url="https://pypi.org/packages/27/47/5bf2bdabf1862ffe6df918beef05fcf3d91dbe1154fff40cb8518edd0bf2/pyproject_parser-0.9.0-py3-none-any.whl")
    version("0.9.0-beta2", sha256="4ba20134f2551c880e0afc760e1d248a7f8d0ebf8b0aa1125190bcdbd9c78f23", url="https://pypi.org/packages/25/7d/2911feade1ee37b7e68bf0ae15d6e0867877644984afce03b5ae6091280a/pyproject_parser-0.9.0b2-py3-none-any.whl")
    version("0.9.0-beta1", sha256="b94b03228098027c5dd05917195c015e8caf8765df67f139b75a4e4b29a56dfc", url="https://pypi.org/packages/24/ac/05cff58fa54d5296fd48b3d2c4bb736fdc4af34e585c235e003374f189fa/pyproject_parser-0.9.0b1-py3-none-any.whl")
    version("0.8.0", sha256="582cdbf7f3e4698fdc6a007f22226da5bc82f13cc0a6c37912feaeedfa0e6cb5", url="https://pypi.org/packages/29/1b/43f759028199438bd541060e64bc6233407d2b8adbfda67c50a80b4e4cec/pyproject_parser-0.8.0-py3-none-any.whl")
    version("0.7.0", sha256="a0aac7930f5429737b44f2bd7825980a46f312c7352e2a7a99d7196721665c2c", url="https://pypi.org/packages/d6/8a/28e5fda16891b7a2f230c398d7cacd27a5e4816faaf738b795c25eaba9fa/pyproject_parser-0.7.0-py3-none-any.whl")
    version("0.7.0-beta1", sha256="42ffc69bb5101288de2577312f4cdf43ad1c9e581da37a37cfdd5051c1c09218", url="https://pypi.org/packages/35/fa/c327054b812ce0137970df4fb1ebd82118e132927fee3f44579ebf57af86/pyproject_parser-0.7.0b1-py3-none-any.whl")
    version("0.6.1", sha256="a9366926121ead369add06c97b12958342ce30971eddbd54f035e4505960281e", url="https://pypi.org/packages/69/15/e20be9b8be99653bfc9b73fa731b9c6faea859536be558f8123fa9e88cf5/pyproject_parser-0.6.1-py3-none-any.whl")
    version("0.6.0", sha256="d8ac6817a44bef2c38074ae552d472d7df5849a77b943428b769bfe310edb40e", url="https://pypi.org/packages/25/ce/feb0d62eb7e83fe59f60db123f2f3b19608610e1ecd25ff18b99f7eff91b/pyproject_parser-0.6.0-py3-none-any.whl")
    version("0.5.0", sha256="8c17efe2c03bff9759db048a2d8c1190664ef2ae62dfc1d3edf44d8fd5d021e5", url="https://pypi.org/packages/18/ba/377d17ad6fe2eabe2ebc530ac511d038991c63ca99cf0fec108fa7254f83/pyproject_parser-0.5.0-py3-none-any.whl")
    version("0.4.3", sha256="60d9bb9cf411250a1c071788f90202e6fdb6d02954e30cd8fb854433877e0de0", url="https://pypi.org/packages/c2/96/7a463cf58657553e6e05cf7e2e991ddf648b7f3899b5467576a9a8329b53/pyproject_parser-0.4.3-py3-none-any.whl")
    version("0.4.2", sha256="aa92513c3f6990a0c413a555205d83f13d76b9d7b956c6075f8157c9bf32d7f9", url="https://pypi.org/packages/9d/55/9b79ca94f32f55adc1fd9c2e6db5cb718d5dc1964662c858b25b720b3e2d/pyproject_parser-0.4.2-py3-none-any.whl")
    version("0.4.1", sha256="4ba0e7b17f5cdba564163a37eb3d9f2700b845ee6d8ff8f9ed4397a926c023f2", url="https://pypi.org/packages/75/bf/d75c51463608dcd8bd88ef059bef2c3b5dbd643fa9ae4e7a0031227ac874/pyproject_parser-0.4.1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-apeye@1:", when="@0.3:0.6")
        depends_on("py-apeye-core@1.0.0:", when="@0.7:")
        depends_on("py-attrs@20.3:")
        depends_on("py-dom-toml@0.4:")
        depends_on("py-domdf-python-tools@2.8:", when="@0.4:")
        depends_on("py-natsort@7.1.1:")
        depends_on("py-packaging@20.9:")
        depends_on("py-shippinglabel@1:", when="@0.4:")
        depends_on("py-toml@0.10.2:")
        depends_on("py-tomli@1.2.3:", when="@0.9: ^python@:3.10")
        depends_on("py-typing-extensions@3.7.4.3:4.7.0-rc1,4.7.1:", when="@0.9.1:")
        depends_on("py-typing-extensions@3.7.4.3:", when="@:0.9.0")

