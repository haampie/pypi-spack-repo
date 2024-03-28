# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMsrest(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.7.1", sha256="21120a810e1233e5e6cc7fe40b474eeb4ec6f757a15d7cf86702c369f9567c32", url="https://pypi.org/packages/15/cf/f2966a2638144491f8696c27320d5219f48a072715075d168b31d3237720/msrest-0.7.1-py3-none-any.whl")
    version("0.7.0", sha256="59b06d168ea11448b79921be0760f488347e140d69fb2c2b9f37000615ca4a39", url="https://pypi.org/packages/88/08/fea1a9f515e0ce7bc86560485efaec1b16d7f066441a52fa8670b76e62d4/msrest-0.7.0-py2.py3-none-any.whl")
    version("0.6.21", sha256="c840511c845330e96886011a236440fafc2c9aff7b2df9c0a92041ee2dee3782", url="https://pypi.org/packages/e8/cc/6c96bfb3d3cf4c3bdedfa6b46503223f4c2a4fa388377697e0f8082a4fed/msrest-0.6.21-py2.py3-none-any.whl")
    version("0.6.20", sha256="114293965a9f62afb61fb7c3bd08a528f04245198fc10cfc21fe294deb272361", url="https://pypi.org/packages/b3/a8/6b9f658ae953382affca7ae252a353178f99fa17f796b344e7cf4a231365/msrest-0.6.20-py2.py3-none-any.whl")
    version("0.6.19", sha256="87aa64948c3ef3dbf6f6956d2240493e68d714e4621b92b65b3c4d5808297929", url="https://pypi.org/packages/fa/f5/9e315fe8cb985b0ce052b34bcb767883dc739f46fadb62f05a7e6d6eedbe/msrest-0.6.19-py2.py3-none-any.whl")
    version("0.6.18", sha256="4993023011663b4273f15432fab75cc747dfa0bca1816d8122a7d1f9fdd9288d", url="https://pypi.org/packages/d9/ed/8e1b75721ad983c1672cd968ad3ae374d2e94767edff6f0b72a15dfde933/msrest-0.6.18-py2.py3-none-any.whl")
    version("0.6.17", sha256="c51ac6ce2d151b47dd4b3eed0fb8596b6e7c2067eff6bb82e874beaf7bfec531", url="https://pypi.org/packages/b6/b4/a95380d5199c4785b318038db6d199a203f6970188876b473c00533bc17f/msrest-0.6.17-py2.py3-none-any.whl")
    version("0.6.16", sha256="88b31e937eba95bda5b9a910b28498fdc130718bb5f8dd98a6af0d333670c897", url="https://pypi.org/packages/34/68/fa7892bd8bb46eba90f7a2ffbc6725ee0b2e302444677377d0853a1c840f/msrest-0.6.16-py2.py3-none-any.whl")
    version("0.6.15", sha256="7cc9e565b8e8829062c4b93687b64318bfed64bc138597203af50649accf7146", url="https://pypi.org/packages/b9/6a/c0a64967c84e33e7a13eabcb792898fd8a5bca6b0495e8b0273103d73773/msrest-0.6.15-py2.py3-none-any.whl")
    version("0.6.14", sha256="f54a60084969656faa2755bfa5f614951b07a870e97dfc8f0b0b8ea94a63b5b5", url="https://pypi.org/packages/48/93/f610aa37a56a8bf5085c55483b34dacc13b5f23476736d6d18f3b4f9d45b/msrest-0.6.14-py2.py3-none-any.whl")
    version("0.6.13", sha256="22349c718f632e37beee0dd10f7ea41984ded136db2199a9d3c6f1f3942868e9", url="https://pypi.org/packages/56/f2/e2f9e4dc72884fff27e68ceaf027b9a3b80ba16f5757fc2916cb5d9117bd/msrest-0.6.13-py2.py3-none-any.whl")
    version("0.6.12", sha256="e17e98d0b8f1832047a2512e3b9f5d3daf33fa09abd5ad7bdf1e3c651d514034", url="https://pypi.org/packages/e9/ec/0f51a0f119df5b0cb208c19c30b31be4fab858708431ec5f07ee9b83c7b2/msrest-0.6.12-py2.py3-none-any.whl")
    version("0.5.5", sha256="a39aac0ce3fae5b388c457b6acfc247e708322b6cd567dbc3cc691a386ff88df", url="https://pypi.org/packages/ad/2a/37b2481fa1a7cd727c07d20cbcb0a3f9bf9dd994930f44dd9770df15c28d/msrest-0.5.5-py2.py3-none-any.whl")
    version("0.5.4", sha256="e343734cb4cd2468362cd17c4071a64a860bdc944e3774853ca5e4dcfb0ae36a", url="https://pypi.org/packages/ed/48/a378f4c33b21a75454f7da387dc528f5ef65cf0f6d3791324b0212014c38/msrest-0.5.4-py2.py3-none-any.whl")
    version("0.5.3", sha256="e8ea629a87da77661733a88523061dd7a71b93f0ede0612265d14c2c5be52dcf", url="https://pypi.org/packages/be/87/fd889efe10d821b16a9e7391cfe98f42af098fe232d62521fe98ed13c70e/msrest-0.5.3-py2.py3-none-any.whl")
    version("0.5.2", sha256="d31d956683ceb00184185d156214d3b21b6dd8e35f33f86aa9aedb6c5b48bac5", url="https://pypi.org/packages/7a/6e/b03d37c1b30b82d235de2b358839864986ae5721940e1ed5e45b4f550668/msrest-0.5.2-py2.py3-none-any.whl")
    version("0.5.1", sha256="c17405bd07c3c9e70aea002faa86f5ee2fab2e53050e0cfefda7c634fe661d53", url="https://pypi.org/packages/93/d4/e82b67cbfc117ba2d45d8c515f0650273c22a77c913fea220eb0ed4aa2bd/msrest-0.5.1-py2.py3-none-any.whl")
    version("0.5.0", sha256="42549175aa25d6243d0df6d77d9a3837fa2eda2c547713e882ef82ff0719ee6e", url="https://pypi.org/packages/63/40/20aa720915463bd4e4ea6c979c5501ddbee4e9dbbe0fb3267d18aca12ebd/msrest-0.5.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-core@1.24:", when="@0.7:")
        depends_on("py-certifi@2017.4:", when="@0.4.8:")
        depends_on("py-isodate@0.6:", when="@0.4.26:")
        depends_on("py-requests@2.16:", when="@0.5:")
        depends_on("py-requests-oauthlib@0.5:", when="@0.0.2:")
    # END DEPENDENCIES

