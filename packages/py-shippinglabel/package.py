# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyShippinglabel(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.7.1", sha256="ffe6e95c1c190f0b4c073ed919e3a253ba3038af07ba920e7e335c365af2def0", url="https://pypi.org/packages/54/2f/b4543bdd448639821f3ee3d5b46a14581365c67b0f1b59ecff62d0d53731/shippinglabel-1.7.1-py3-none-any.whl")
    version("1.7.0", sha256="c61b9bfd447437a553f6b8121cd21c353d42eae408ffa451506fb7d9fad35688", url="https://pypi.org/packages/92/3e/bca0bdb4d86589a3d1623c4b9d9edcaec890d6b3b5bb66ffa8f5bb596ad0/shippinglabel-1.7.0-py3-none-any.whl")
    version("1.6.0", sha256="6032b077c4fd17189c44646757423f061d47656b95022d6a7755591a60587523", url="https://pypi.org/packages/f1/69/4cdb502b7696a002fa921f7d87adf05e7fbb5a18245811837118528ba2db/shippinglabel-1.6.0-py3-none-any.whl")
    version("1.5.0", sha256="5d4fed80499c00250d5e660296e7d6d0607ee4f2543b2d4bca72958f2b710241", url="https://pypi.org/packages/07/86/cc4be0164a335dea582be2bfb3d72fdacfbfa534b9791c580a3f5f5b3768/shippinglabel-1.5.0-py3-none-any.whl")
    version("1.4.1", sha256="dec30a73115ef96a6f54bbf11a367eb3c131197be4b26b4ed4077513ad883117", url="https://pypi.org/packages/b5/3a/b0c4c3918d4d2957a2d12dab85ae38076c1c200c269a0cfe063342926876/shippinglabel-1.4.1-py3-none-any.whl")
    version("1.3.1", sha256="9f385f428436464ee6a52278f4c94083d8542f04aeb5393f80e2a44666e17356", url="https://pypi.org/packages/a6/65/23183ee42bbe01ca50c37bce3ac4322d7a2e9b689e268a16b7bda31ee94a/shippinglabel-1.3.1-py3-none-any.whl")
    version("1.3.0", sha256="906a5b93f69291cb29d16c57007c672fdeb0dd1cb6a5a1f4d2a85c90d542ee1c", url="https://pypi.org/packages/c4/39/10defbcd285ad81a7758c953dcdcaf70d786a3908033854da4c7641fed05/shippinglabel-1.3.0-py3-none-any.whl")
    version("1.2.1", sha256="cbe805d14f66532bff0fcff683562384984f64e71e4b755dc66b08d2873209d1", url="https://pypi.org/packages/b7/df/507fe24340b0e210634f2c293ebb05d7b7f8fd15ed5dfb01182095d997f8/shippinglabel-1.2.1-py3-none-any.whl")
    version("1.2.0", sha256="8fa9eed4c4658a909a94868a1b8ea267e1d0223130b0cda07ba903fe3118a404", url="https://pypi.org/packages/df/e6/1f14228049967c562a815c1eff58f5f0e58f079949b142b3b6ca2b4b3d86/shippinglabel-1.2.0-py3-none-any.whl")
    version("1.1.1", sha256="d6f869846b05b5918a23dd8bf8106027dff9f7b347dcc5c64a8dfe9b2d6dd3f4", url="https://pypi.org/packages/1e/e5/5ea2e4f69604eaa890da77f3de8f6474ca61359a0fbeb542ddbfe53fcf3e/shippinglabel-1.1.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-apeye@1:", when="@1:")
        depends_on("py-appdirs@1.4.4:", when="@0.7:1.1")
        depends_on("py-deprecation-alias@0.3.2:", when="@1.6:")
        depends_on("py-dist-meta@0.1.2:", when="@1:")
        depends_on("py-dom-toml@0.2.2:", when="@0.13:")
        depends_on("py-domdf-python-tools@3.1:", when="@1:")
        depends_on("py-packaging@20.9:", when="@0.16:")
        depends_on("py-platformdirs@2.3:", when="@1.2:")
        depends_on("py-typing-extensions@3.7.4.3:", when="@0.2.3:")
    # END DEPENDENCIES

