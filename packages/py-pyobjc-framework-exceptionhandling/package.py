# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkExceptionhandling(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="fd7dfc197c29ccf187718dbb0b1dcd966a8c04ee6549ee9472959912e76a0609", url="https://pypi.org/packages/b6/54/56f374b63da234f2ed1985bddcbd81a3a6acf3bc729c46814fe49d56ecba/pyobjc_framework_ExceptionHandling-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="b8eb9142f141361982e498610bfd33803acb4f471f80b5cd9df8d382142449e9", url="https://pypi.org/packages/8b/f8/da96001c29a8fab94d3cacb3ec9a3b29098ec2e6e75ec928514c76589aed/pyobjc_framework_ExceptionHandling-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="3c7669d6e93d4f4d472de8c7b8e3b5ecd42dda16161e24b3bf796713fc20eb1a", url="https://pypi.org/packages/51/f6/823e603746840452794d4edc16d106866d1cd14dff211a68d39831a9c337/pyobjc_framework_ExceptionHandling-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="85893d10c9bc9370a6e1a61cedf999179cb59258583bdc57a4efdd632c1e6869", url="https://pypi.org/packages/70/36/6e797e443b6f58388a0e69cebc18df0fb05a8091f49be0f656a0a37e31a7/pyobjc_framework_ExceptionHandling-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="2929e47510d53fd04241f2761ef0f5b7383404bfbf18dbb43edc20fe67274c35", url="https://pypi.org/packages/5d/fe/6d77b1b88bb9330c0b9773ffe13b966bdcfe4ae3c7b4fe31b04f5edcb13a/pyobjc_framework_ExceptionHandling-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="552ca105077b1719637200d0cfffa0833a8a88c1bbcb83d8b6df45457a904831", url="https://pypi.org/packages/7e/d0/491656e58588b82c3feff231e62dcc68dc5a92b2c026196acf9ff0597f77/pyobjc_framework_ExceptionHandling-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="2e853b20911dae4532ddc5655602b14ac7d60e4c24b784e07f7879db24b6f179", url="https://pypi.org/packages/f3/1e/7b0dcf774a0d0b894666783b52f7bc37e1e65cb58c24d08b4e342e8fcd98/pyobjc_framework_ExceptionHandling-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="860981a40642a3cc64c8035c6c9d55e09a3055b0deb1c8ae309f8e7d1c850d5d", url="https://pypi.org/packages/a0/99/f674eae6a5802714f06c31aab7d7a8bc89135061e763ef27e68221932771/pyobjc_framework_ExceptionHandling-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="cf33e421eb789010e88f641cbb0d93b2b6a4b89a024c5941eb71941f401a4f6a", url="https://pypi.org/packages/e5/da/25d5361808395bfc863ec21765d7b7208a5126a2288b4461c847244eaf54/pyobjc_framework_ExceptionHandling-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="c2014ccd1c78c4b4a8aeae7ba62cb86d1c9d46f523b1e8efd1d47bb4da99cc2d", url="https://pypi.org/packages/63/fa/c6c9bae0e68a9543516ce2490659327d4d15176c125110d15c3b74aaca90/pyobjc_framework_ExceptionHandling-8.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-core@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-core@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-core@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-core@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-core@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-core@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-core@8.5:", when="@8.5:8.5.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-cocoa@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-cocoa@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-cocoa@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-cocoa@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-cocoa@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-cocoa@8.5:", when="@8.5:8.5.0")
    # END DEPENDENCIES

